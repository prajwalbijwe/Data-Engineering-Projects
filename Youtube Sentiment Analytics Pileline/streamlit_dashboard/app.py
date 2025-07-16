import streamlit as st
import pandas as pd

import sys
import os

# Add parent directory (StreamLitDashboard) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_loader import read_gold_data


account_name = "practicestorageacc0"
container = "projectfiles"
sas_token = "sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2027-12-30T19:08:17Z&st=2025-07-11T11:08:17Z&spr=https&sig=GkUTZNv5%2FaAaKvmzNdHqLmUSOtaoetpgettSjbxVy9U%3D"
date_ = st.date_input("Select Date", pd.to_datetime("today")).strftime("%Y-%m-%d")
folder = f"commentsentiment/gold/{date_}/"

# Load Data
df = read_gold_data(container, folder, account_name, sas_token)

# Dashboard
st.title("🎥 YouTube Comments Sentiment Dashboard")

if df.empty:
    st.warning("No Data Available for this date.")
else:
    st.metric("Total Comments", len(df))
    st.metric("Positive Comments", df[df["sentiment"] == "POSITIVE"].shape[0])
    st.metric("Negative Comments", df[df["sentiment"] == "NEGATIVE"].shape[0])

    st.subheader("📋 Sample Comments")
    st.dataframe(df[["video_id", "text", "sentiment", "published_at"]].sample(10))

    st.subheader("📊 Sentiment Distribution")
    st.bar_chart(df["sentiment"].value_counts())


