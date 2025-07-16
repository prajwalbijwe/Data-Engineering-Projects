from confluent_kafka import Producer
from faker import Faker
import json
import random
import time
import cv2
kafka_config = {
    'bootstrap.servers': 'pkc-56d1g.eastus.azure.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'LLPDTJOM6HZMVVEK',
    'sasl.password': 'M35bZlxNWayWwn8p8F/4nxbBrsdt3TOhSAM5BTCK48C4FZjiFeHckPhD2ZCOBWiF'
}
producer = Producer(kafka_config)  # producer instance
faker = Faker()  # faker instance to generate fake user data

# Load Prerecorded stream video
video_path = '../Videos/match_stream.mp4' # Dummy or predownloaded video
cap = cv2.VideoCapture(video_path)

fps = cap.get(cv2.CAP_PROP_FPS)
# we will emit the data every second, so after every int(fps) th frame
frame_interval = int(fps)

frame_count = 0  # to track the processed frames count
video_id = faker.uuid4()  # fake video session id


# Function to generate fake user interaction event
def generate_event(frame_no):
    # Events type
    event_types = ['video_start', 'reaction', 'chat_message', 'viewers count']
    event_type = random.choice(event_types)

    # event structure
    message = None
    if event_type == "chat_message":
        message = faker.sentence()
    elif event_type == "viewers count":
        message = random.randint(100, 1000)
    event = {
        "user_id": faker.uuid4(),
        "event_type": event_type,
        "timestamp": int(time.time()),
        "video_id": str(video_id),
        "frame": frame_no,
        "message": message
    }
    return event


# Iterate through video frames

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break  # end of video

    # Every Nth Frame (once per second), emit an event
    if frame_count % frame_interval == 0:
        event = generate_event(frame_count) # generate the randon event
        event_json = json.dumps(event)  # Serialize to JSON string

        # send to kafka topic
        producer.produce(
            topic='discord_video_stream',
            value=event_json.encode('utf-8')
        )

        print(f"Sent event at frame {frame_count}: {event['event_type']}")

        producer.poll(1)  # Force the delivery of the event (handles async flushing)
        time.sleep(1)  # Wait to simular real time stream (1 event/sec)
    frame_count += 1
cap.release()
producer.flush()
print("Done streaming events.")
