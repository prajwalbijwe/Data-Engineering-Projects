# 🧠 Clickstream Recommender System (Session-Based)

This project builds a streaming recommendation system using simulated clickstream data. It processes real-time product interaction events and trains a collaborative filtering model to recommend products based on session behavior.

---

## ⚙️ Tech Stack

| Layer         | Tool/Service                             |
|---------------|------------------------------------------|
| Ingestion     | Kafka (Confluent Cloud) + Python Producer |
| Processing    | Spark Structured Streaming on Databricks |
| Storage       | Azure Data Lake Gen2 (Delta format)      |
| Recommendation| ALS (Spark MLlib)                        |
| Dashboard     | Streamlit (local)                        |

---

## 🧱 Project Structure

```
03-clickstream-recommender/
├── producer/
│   └── clickstream_producer.py
├── databricks/
│   ├── bronze_layer.py
│   ├── silver_layer.py
│   └── gold_layer_modeling.py
├── streamlit_dashboard/
│   └── app.py
├── architecture/
│   ├── architecture_diagram.png
│   └── flow.md
├── sample_data/
│   └── sample_clicks.json
├── requirements.txt
└── README.md
```

---

## 📊 Features Implemented

- Real-time ingestion of clickstream data via Kafka
- Structured Bronze → Silver pipeline with timestamped events
- Gold layer with session aggregations (duration, event counts)
- ALS model trained using session-item matrix
- Local Streamlit app to show top recommendations by session

---

## 🧭 Architecture

![Architecture Diagram](architecture/architecture_diagram.png)

---

## 🔄 Pipeline Flow

1. User click events (views, add to cart, purchase) are simulated using a Kafka producer.
2. Spark reads and stores them in Bronze Delta Lake on Azure.
3. Silver layer cleans data, extracts sessions and events.
4. Gold layer builds user-item interaction matrix, trains ALS model.
5. Streamlit shows top-N product recommendations per user session.

---

## 🧪 How to Run

### 1. Kafka Producer (Local)

```bash
cd producer/
python clickstream_producer.py
```

### 2. Databricks ETL Pipeline

Run notebooks in order:
- `bronze_layer.py`
- `silver_layer.py`
- `gold_layer_modeling.py` (includes ALS model)

### 3. Streamlit Recommendation Dashboard

```bash
cd streamlit_dashboard/
streamlit run app.py
```

---

## 🔐 Authentication

| Component   | Access Method           |
|------------|--------------------------|
| Kafka       | SASL_SSL + API key/secret |
| Azure Blob  | SAS Token (read access)  |
| Databricks  | Workspace-connected notebooks |

---

## 📌 Sample Click Event

```json
{
  "timestamp": "2025-07-13T18:42:10Z",
  "session_id": "sess_102",
  "user_id": "user_12",
  "item_id": "prod_88",
  "event_type": "view"
}
```

---

## 📈 Dashboard Outputs

- Recommended products per session
- Most viewed products
- Top active sessions
- Session engagement metrics

---

## 👤 Author

Built by [Your Name](https://linkedin.com/in/your-profile)

---

## 📁 Related Projects

- [01: Real-Time User Interaction Pipeline](../01-user-interaction-pipeline/)
- [02: YouTube Sentiment Pipeline](../02-youtube-sentiment-pipeline/)
- [04: Streaming Log Analytics](../04-streaming-log-analytics/)