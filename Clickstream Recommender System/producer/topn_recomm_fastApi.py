from fastapi import FastAPI, HTTPException
import pandas as pd
from datetime import datetime
import sys
import os
# Add parent directory (StreamLitDashboard) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from utils.data_load_from_azure import read_gold_data

app = FastAPI()


account_name = "practicestorageacc0"
container = "projectfiles"
sas_token = "sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2027-12-30T19:08:17Z&st=2025-07-11T11:08:17Z&spr=https&sig=GkUTZNv5%2FaAaKvmzNdHqLmUSOtaoetpgettSjbxVy9U%3D"
date_ = datetime.utcnow().strftime("%Y-%m-%d")
folder = f"clickstream/gold/recommendations/{date_}/"

df = read_gold_data(container, folder, account_name, sas_token)

@app.get("/")
def root():
    return {"message": "API is Live!."}

@app.get("/recommendations")
def get_recommendations(user_id:str, topK: int = 5):
    user_recs = df[df["user_id"] == user_id].sort_values(by='rating', ascending=False)
    if user_recs.empty:
        raise HTTPException(status_code=404, detail="User not found or no recommendations available.")
    return user_recs.head(topK).to_dict(orient="records")




