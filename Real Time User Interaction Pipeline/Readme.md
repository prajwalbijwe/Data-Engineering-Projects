Pipeline Flow
User interaction logs (messages, viewers, joins, exits) are simulated using a local Kafka producer and streamed to a topic in Confluent Kafka.

Databricks notebooks read from Kafka and store the raw logs to the Bronze layer in Azure Data Lake using Delta format.

The logs are parsed and cleaned in the Silver layer, standardizing time and event format.

In the Gold layer, data is aggregated to calculate:

Active users per hour

Peak viewers

Event type distribution

Session duration and frequency

A Streamlit dashboard visualizes this data using real-time queries against Azure Blob (via SAS token).


Spark Streaming on Databricks
Run these in Databricks notebook jobs (or .py scripts):

bronze_layer.py → Ingests raw JSON from Kafka

silver_layer.py → Parses, filters, and standardizes logs

gold_layer.py → Aggregates by time, user, session

Sample Schema (Bronze Parsed)
{
  "timestamp": "2025-07-13T12:30:20Z",
  "event": "message",
  "user_id": "user_33",
  "video_id": "video_42",
  "payload": "awesome stream!"
}

Auth & Connectivity
Azure Blob (ADLS)	--> SAS Token (secure URI)
Kafka (Confluent)	--> SASL_SSL with API key/secret
Databricks	      --> Workspace notebooks


Features
✅ Structured Bronze → Silver → Gold pipeline
✅ Real-time streaming via Spark
✅ Modular Python + notebook-based development
✅ Live dashboard, powered by cloud-native storage
✅ Clean GitHub-friendly structure for deployment/showcase


Next Steps
 Add GitHub Actions CI for Streamlit lint/test
 Package dashboard as a Docker container
 Enable alerts via Slack (Airflow or Prometheus integration)
