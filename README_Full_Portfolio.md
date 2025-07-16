# 🧪 Real-Time Data Engineering Portfolio (Azure + Kafka + Databricks)

This repository contains 4 real-time data engineering projects demonstrating expertise in Kafka streaming, Spark Structured Streaming, cloud data lakes, and dashboarding with Streamlit. All projects are built on **Azure**, using **Delta Lake**, **Confluent Kafka**, and **Databricks** for processing.

---

## 🚀 Projects Overview

| Project | Description |
|--------|-------------|
| [01. Real-Time User Interaction Pipeline](./01-user-interaction-pipeline/) | Simulates user activity in live video platforms and computes session-based analytics (viewers, chat, durations). |
| [02. YouTube Comments Sentiment Pipeline](./02-youtube-sentiment-pipeline/) | Streams YouTube comments, applies Spark NLP sentiment detection, and visualizes trends. |
| [03. Clickstream Recommender System](./03-clickstream-recommender/) | Builds a product recommender using ALS trained on real-time clickstream data (sessions + items). |
| [04. Streaming Log Analytics](./04-streaming-log-analytics/) | Ingests GitHub public event logs to detect activity, errors, and top repositories in real-time. |

---

## ⚙️ Unified Tech Stack

- **Messaging**: Apache Kafka (Confluent Cloud)
- **Compute**: Spark Structured Streaming on Databricks
- **Storage**: Azure Data Lake Gen2 (Delta format)
- **Visualization**: Streamlit (Python dashboard)
- **Authentication**: SAS Token (Azure), SASL_SSL (Kafka)

---

## 📂 Directory Structure

```
faang-de-projects/
├── 01-user-interaction-pipeline/
├── 02-youtube-sentiment-pipeline/
├── 03-clickstream-recommender/
├── 04-streaming-log-analytics/
├── shared/ (optional utils or modules)
├── LICENSE
├── .gitignore
└── README.md  ← (this file)
```

Each project has:
- A Kafka producer written in Python (`producer/`)
- A set of Databricks notebooks/scripts (`databricks/`) for ETL
- A local dashboard app (`streamlit_dashboard/`)
- Architecture diagram and pipeline flow (`architecture/`)
- Sample data for testing or previewing logs (`sample_data/`)

---

## 📊 Live Dashboards

Each project contains a Streamlit app that can be launched locally and reads from Azure Blob using SAS tokens.

```bash
cd 01-user-interaction-pipeline/streamlit_dashboard/
streamlit run app.py
```

Repeat for other projects similarly.

---

## 🧪 Skills Demonstrated

- Structured Streaming (Spark)
- Delta Lake table design: Bronze → Silver → Gold
- Kafka ingestion (JSON events)
- Time-windowed aggregations, Watermarking
- Real-time dashboards with Python/Streamlit
- CI/CD ready project layout

---

## 📌 Notes

- All projects have **realistic, reproducible datasets**
- Streamlit apps are lightweight and local (no deployment needed)
- Clean modular codebases ready for resume/GitHub showcase

---

## 👤 Author

Built by [Your Name](https://linkedin.com/in/your-profile) · MIT License

---

## 🧭 Future Extensions

- Add CI with GitHub Actions for lint/test
- Deploy dashboards using Streamlit Cloud or Azure App Service
- Integrate ML alerting (anomaly detection on streaming metrics)