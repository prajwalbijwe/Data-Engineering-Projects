# 📡 Real-Time User Interaction Pipeline

This project demonstrates a real-time data engineering pipeline that captures user interactions during live streams and processes them using Kafka, Spark Structured Streaming, and Azure Data Lake. The pipeline ends with a dashboard powered by Streamlit.

---

## ⚙️ Tech Stack

| Layer         | Tool/Service                             |
|---------------|------------------------------------------|
| Ingestion     | Python Producer → Kafka (Confluent Cloud)|
| Processing    | Spark Structured Streaming on Databricks |
| Storage       | Azure Data Lake Gen2 (Delta format)      |
| Visualization | Streamlit (local)                        |

---

## 🧱 Project Structure

```
01-user-interaction-pipeline/
├── producer/
│   └── user_interaction_producer.py
├── databricks/
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   └── gold_layer.py
├── streamlit_dashboard/
│   └── app.py
├── architecture/
│   ├── architecture_diagram.png
│   └── flow.md
├── sample_data/
│   └── sample_logs.json
├── requirements.txt
└── README.md
```

---

## 📊 Features

- Real-time ingestion using Kafka
- Structured ETL layers: Bronze → Silver → Gold
- Aggregated metrics: session duration, viewer count, event type
- Live dashboard using Streamlit
- Secure data access via Azure SAS token

---

## 🧭 Architecture

![Architecture Diagram](architecture/architecture_diagram.png)

---

## 🔄 Pipeline Flow

1. Python script produces user event logs to Kafka
2. Databricks reads Kafka → Bronze (Delta)
3. Parsed and cleaned data stored in Silver
4. Aggregated metrics written to Gold
5. Streamlit queries Azure Blob to render real-time dashboard

---

## 🔐 Authentication

| Component   | Access Method           |
|------------|--------------------------|
| Kafka       | SASL_SSL + API key/secret |
| Azure Blob  | SAS Token URL-based auth |
| Databricks  | Workspace-connected notebooks |

---

## 🧪 How to Run

### 1. Start Kafka Producer

```bash
cd producer/
python user_interaction_producer.py
```

### 2. Run Databricks Notebooks

Execute:
- `bronze_layer.py`
- `silver_layer.py`
- `gold_layer.py`

### 3. Run Streamlit App

```bash
cd streamlit_dashboard/
streamlit run app.py
```

---

## 📌 Example Log Format

```json
{
  "timestamp": "2025-07-13T12:30:20Z",
  "event": "message",
  "user_id": "user_33",
  "video_id": "video_42",
  "payload": "awesome stream!"
}
```

---

## ✅ Output Metrics

| Table             | Metrics Included                            |
|------------------|---------------------------------------------|
| `events_by_type` | Count of each event type per time window    |
| `user_sessions`  | Session length and event volume per user    |
| `video_activity` | Active viewers and peak message counts      |

---

## 👤 Author

Built by [Prajwal Bijwe](https://linkedin.com/in/prajwalbijwe)

---

## 📁 Other Projects

- [02: YouTube Comments Sentiment Pipeline](https://github.com/prajwalbijwe/Data-Engineering-Projects/tree/main/Youtube%20Sentiment%20Analytics%20Pileline)
- [03: Clickstream Recommender System](https://github.com/prajwalbijwe/Data-Engineering-Projects/tree/main/Clickstream%20Recommender%20System)
- [04: Streaming Log Analytics](https://github.com/prajwalbijwe/Data-Engineering-Projects/tree/main/Github%20Log%20Analytics)
