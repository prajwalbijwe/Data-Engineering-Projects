# 📊 Streaming Log Analytics Pipeline

This project implements a real-time log analytics system using GitHub public events as streaming data. It ingests, cleans, aggregates, and visualizes logs using Apache Spark, Databricks, and Azure Data Lake, ending in a live Streamlit dashboard.

---

## ⚙️ Tech Stack

| Layer         | Tool/Service                             |
|---------------|------------------------------------------|
| Ingestion     | Python Kafka Producer (GitHub API)       |
| Stream Engine | Spark Structured Streaming on Databricks |
| Storage       | Azure Data Lake Gen2 (Delta format)      |
| Dashboard     | Streamlit (local)                        |
| Kafka         | Confluent Cloud                          |

---

## 🧱 Project Structure

```
04-streaming-log-analytics/
├── producer/
│   └── github_log_producer.py
├── databricks/
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   └── gold_layer.py
├── streamlit_dashboard/
│   └── app.py
├── architecture/
│   ├── architecture_diagram.png
│   └── flow.md
├── requirements.txt
└── README.md
```

---

## 📊 Features Implemented

- Real-time streaming from GitHub Events API → Kafka → Spark
- Structured Bronze → Silver → Gold transformation
- Aggregations: active users, event types, top repos
- Visualized live using Streamlit dashboard (SAS-based access to blob)

---

## 🧭 Architecture

![Architecture Diagram](architecture/architecture_diagram.png)

---

## 🔄 Pipeline Flow

1. Python script polls GitHub Events API and pushes logs to Kafka topic `logs_raw`.
2. Spark reads from Kafka in Databricks and stores raw logs (Bronze).
3. Logs are parsed and transformed in Silver with timestamp casting.
4. Aggregations (Gold) include:
   - Events per type (minute)
   - Active users per org (hour)
   - Top repositories by event count
5. Streamlit loads Gold Delta tables from Azure Blob (via SAS token).

---

## 🧪 How to Run

### 1. GitHub Producer

```bash
cd producer/
python github_log_producer.py
```

### 2. Run Databricks ETL Jobs

Execute in order:
- `bronze_layer.py`
- `silver_layer.py`
- `gold_layer.py`

### 3. Launch Streamlit Dashboard

```bash
cd streamlit_dashboard/
streamlit run app.py
```

> Make sure to export your Azure Blob SAS token as an environment variable or include it in the URL config.

---

## 🔐 Authentication

| Component     | Access Method         |
|---------------|------------------------|
| GitHub API    | No auth needed (public) |
| Kafka (Confluent) | API key + SASL_SSL   |
| Azure Blob    | SAS Token URL access   |
| Databricks    | Notebook + workspace   |

---

## 📌 Sample Log Format

```json
{
  "timestamp": "2025-07-13T16:12:45Z",
  "event_type": "PushEvent",
  "actor": "octocat",
  "repo": "octo-org/octo-repo"
}
```

---

## 📈 Dashboard Metrics

- Bar chart: events per type per minute
- Table: active users by organization
- Top-N repositories by activity

---

## 👤 Author

Built by [Prajwal Bijwe](https://linkedin.com/in/prajwalbijwe)

---

## 📁 Related Projects

- [01: Real-Time User Interaction Pipeline](../01-user-interaction-pipeline/)
- [02: YouTube Comments Sentiment Pipeline](../02-youtube-sentiment-pipeline/)
- [03: Clickstream Recommender System](../03-clickstream-recommender/)
