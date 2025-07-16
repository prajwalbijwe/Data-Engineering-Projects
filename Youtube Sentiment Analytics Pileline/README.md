# 🎥 YouTube Comments Sentiment Pipeline

This project processes real-time YouTube comments using Kafka, Spark NLP pipelines, and Azure Databricks to generate sentiment analytics. It visualizes audience sentiment trends for content creators or platform teams.

---

## ⚙️ Tech Stack

| Layer         | Tool/Service                             |
|---------------|------------------------------------------|
| Ingestion     | YouTube API → Python Kafka Producer      |
| Processing    | Spark Structured Streaming + NLP (Databricks) |
| Storage       | Azure Data Lake Gen2 (Delta format)      |
| Visualization | Streamlit (local)                        |
| NLP Model     | Spark NLP SentimentDetector              |

---

## 🧱 Project Structure

```
02-youtube-sentiment-pipeline/
├── producer/
│   └── yt_comment_producer.py
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
│   └── sample_comments.json
├── requirements.txt
└── README.md
```

---

## 📊 Features

- Real-time ingestion of YouTube comments via API
- Sentiment classification using Spark NLP (positive, negative, neutral)
- Aggregated metrics per video, region, and time
- Streamlit dashboard with sentiment trends and volume

---

## 🧭 Architecture

![Architecture Diagram](architecture/architecture_diagram.png)

---

## 🔄 Pipeline Flow

1. Comments fetched from YouTube API using a Python Kafka producer.
2. Databricks reads raw JSON to Bronze.
3. Silver layer parses and applies Spark NLP model for sentiment tagging.
4. Gold aggregates sentiment per video over time windows.
5. Streamlit dashboard visualizes top videos, comment volumes, and sentiment ratio.

---

## 🔐 Authentication

| Component   | Access Method           |
|------------|--------------------------|
| YouTube API| OAuth or API key         |
| Azure Blob | SAS Token (URL based)    |
| Kafka      | SASL_SSL + API credentials |
| Databricks | Workspace notebook access |

---

## 🧪 How to Run

### 1. Start Kafka Producer

```bash
cd producer/
python yt_comment_producer.py
```

### 2. Run Databricks Notebooks

Execute the following in order:
- `bronze_layer.py`
- `silver_layer.py` (includes NLP transformation)
- `gold_layer.py`

### 3. Run Streamlit Dashboard

```bash
cd streamlit_dashboard/
streamlit run app.py
```

---

## 🧾 Sample Comment Log Format

```json
{
  "timestamp": "2025-07-13T16:12:45Z",
  "video_id": "abc123",
  "user_id": "user_58",
  "comment": "This video is amazing!",
  "language": "en"
}
```

---

## ✅ Output Metrics

| Table             | Metrics Included                          |
|------------------|---------------------------------------------|
| `sentiment_trends` | Sentiment distribution per video over time |
| `top_comments`     | Most engaged/commented videos              |
| `language_breakdown`| Language-wise comment counts              |

---

## 📈 Dashboard Panels

- Sentiment timeline chart
- Top 10 videos by engagement
- Pie chart: sentiment split
- Bar chart: comments per language

---

## 👤 Author

Built by [Prajwal Bijwe](https://linkedin.com/in/prajwalbijwe)

---

## 📁 Related Projects

- [01: Real-Time User Interaction Pipeline](https://github.com/prajwalbijwe/Data-Engineering-Projects/tree/main/Real%20Time%20User%20Interaction%20Pipeline)
- [03: Clickstream Recommender System](https://github.com/prajwalbijwe/Data-Engineering-Projects/tree/main/Clickstream%20Recommender%20System)
- [04: Streaming Log Analytics](https://github.com/prajwalbijwe/Data-Engineering-Projects/tree/main/Github%20Log%20Analytics)
