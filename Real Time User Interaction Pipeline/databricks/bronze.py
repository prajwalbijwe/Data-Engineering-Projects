from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, LongType
import time


# Define Kafka topic and schema
KAFKA_BOOTSTRAP = "pkc-56d1g.eastus.azure.confluent.cloud:9092"
KAFKA_TOPIC = "discord_video_stream"
API_KEY = "LLPDTJOM6HZMVVEK"
API_SECRET = "M35bZlxNWayWwn8p8F/4nxbBrsdt3TOhSAM5BTCK48C4FZjiFeHckPhD2ZCOBWiF"


schema = StructType() \
    .add("user_id", StringType()) \
    .add("event_type", StringType()) \
    .add("timestamp", LongType()) \
    .add("video_id", StringType()) \
    .add("frame", LongType()) \
    .add("message", StringType())

# connect to kafka
df_raw = spark.readStream.format('kafka')\
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP)\
        .option("subscribe", KAFKA_TOPIC)\
        .option("startingOffsets", "earliest")\
        .option("kafka.security.protocol", "SASL_SSL")\
        .option("kafka.sasl.mechanism", "PLAIN")\
        .option("kafka.sasl.jaas.config", f"kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required username=\"{API_KEY}\" password=\"{API_SECRET}\";") \
        .load()

df_parsed = df_raw.selectExpr("CAST(value AS STRING) AS json")\
                 .select(from_json(col("json"), schema).alias("data"))\
                    .select("data.*")

time_ = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
date_ = time.strftime("%Y-%m-%d", time.gmtime())
output_path = f"abfss://projectfiles@practicestorageacc0.dfs.core.windows.net/videostream/bronze/{date_}"
checkpoint_path = f"/tmp/checkpoints/{date_}/{time_}"

# dbutils.fs.rm("/tmp/checkpoints/", True)
# files = dbutils.fs.ls(f"/tmp/checkpoints/{folder_name}")
# print(files)
query = df_parsed.writeStream \
    .format("parquet") \
    .option("checkpointLocation", checkpoint_path) \
    .option("path", output_path) \
    .outputMode("append") \
    .trigger(availableNow=True) \
    .start()
query.awaitTermination()
