from confluent_kafka import Producer
import requests, time, json


kafka_config = {
    'bootstrap.servers': 'pkc-56d1g.eastus.azure.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'LLPDTJOM6HZMVVEK',
    'sasl.password': 'M35bZlxNWayWwn8p8F/4nxbBrsdt3TOhSAM5BTCK48C4FZjiFeHckPhD2ZCOBWiF'
}

topic = 'github_logs'
producer = Producer(kafka_config)


def fetch_github_events():
    url = 'https://api.github.com/events'
    headers = {"Accept": "application/vnd.github+json"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Failed to fetch Gthub events: {e}")
        return []

def delivery_message(err, msg):
    if err is not None:
        print(f"Message Delivery Failed: {err}")
    else:
        print(f"Sent to Kafka: {msg.topic()} [{msg.partition()}]")

if __name__ == "__main__":
    print("Starting Github log producer _____")

    start = time.time()
    duration_min = 10
    while time.time() < start + duration_min*60:
        events = fetch_github_events()
        for event in events:
            log_entry = {
                "timestamp": event.get("created_at"),
                "event_type": event.get("type"),
                "repo": event.get("repo", {}).get("name"),
                "actor": event.get("actor", {}).get("login"),
                "raw": json.dumps(event) # full event reference
            }
            log_json = json.dumps(log_entry)

            producer.produce(topic, key=log_entry["actor"], value=log_json, callback=delivery_message)
        producer.flush()
        time.sleep(5)
