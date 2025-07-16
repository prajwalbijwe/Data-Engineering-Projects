from confluent_kafka import Producer
from faker import Faker
import json
import time
import random
import uuid
from datetime import datetime, timedelta

fake = Faker()
kafka_config = {
    'bootstrap.servers': 'pkc-56d1g.eastus.azure.confluent.cloud:9092',
    'security.protocol': 'SASL_SSL',
    'sasl.mechanisms': 'PLAIN',
    'sasl.username': 'LLPDTJOM6HZMVVEK',
    'sasl.password': 'M35bZlxNWayWwn8p8F/4nxbBrsdt3TOhSAM5BTCK48C4FZjiFeHckPhD2ZCOBWiF'
}
producer = Producer(kafka_config)
TOPIC = "advanced_clickstream"

# Sample Users and items
users = [f"user_{i}" for i in range(1, 101)]
items = [f"item_{i}" for i in range(1, 501)]
device_types = ['mobile', 'laptop', 'tablet']
referrers = ['search', 'homepage', 'email', 'ad']
ab_groups = ['A', 'B']
categories = ['fashion', 'electronics', 'books', 'home', 'fitness']
event_flow = [
    ("page_view", 1.0),
    ("item_view", 0.95),
    ("click", 0.8),
    ("add_to_cart", 0.4),
    ("purchase", 0.2)
]

session_duration_in_min = 5


def generate_session_event(user_id):
    session_id = str(uuid.uuid4())
    item_id = random.choice(items)
    item_cat = random.choice(categories)
    location = fake.location_on_land()
    device = random.choice(device_types)
    ab_group = random.choice(ab_groups)
    referrer = random.choice(referrers)

    base_time = datetime.utcnow()
    session_events = []

    for idx, (event_type, prob) in enumerate(event_flow):
        if random.random() > prob:
            break

        event_time = base_time + timedelta(seconds=int(5 * idx))

        event = {
            "user_id": user_id,
            "item_id": item_id,
            "item_category": item_cat,
            "event_type": event_type,
            "event_time": int(event_time.timestamp()),
            "session_id": session_id,
            "device_type": device,
            "referrer": referrer,
            "ab_group": ab_group,
            "location": {
                "country": location[3],
                "region": location[4],
                "city": location[2]
            }
        }
        session_events.append(event)
    return session_events


run_duration_min = 10
end_time = time.time() + run_duration_min * 60

while time.time() < end_time:
    user = random.choice(users)
    session = generate_session_event(user)
    for event in session:
        producer.produce(TOPIC, key=event["user_id"], value=json.dumps(event))
        producer.flush()
        print("sent:", event)
        time.sleep(0.1)
print("Finished the simulation!")
