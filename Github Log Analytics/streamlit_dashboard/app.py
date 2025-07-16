import streamlit as st
import pandas as pd
import datetime
from deltalake import DeltaTable


import sys
import os

# Add parent directory (StreamLitDashboard) to the path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from utils.data_loader import read_gold_data


account_name = "practicestorageacc0"
container = "projectfiles"
sas_token = "sv=2024-11-04&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2027-12-30T19:08:17Z&st=2025-07-11T11:08:17Z&spr=https&sig=GkUTZNv5%2FaAaKvmzNdHqLmUSOtaoetpgettSjbxVy9U%3D"
date_ = st.date_input("Select Date", pd.to_datetime("today")).strftime("%Y-%m-%d")
print(date_)

events_folder = f"githublogs/gold/events/{date_}/"
users_folder = f"githublogs/gold/active_users/{date_}/"
repo_folder = f"githublogs/gold/repos_activity/{date_}/"

# Load Data
df_events = read_gold_data(container, events_folder, account_name, sas_token)
df_users = read_gold_data(container, users_folder, account_name, sas_token)
df_repos = read_gold_data(container, repo_folder, account_name, sas_token)

print(df_events)
print(df_users)
print(df_repos)

# Clean empty cases
if df_events.empty or df_repos.empty or df_users.empty:
    st.warning("Waiting for data to be generated....")
    st.stop()

# Fix for nested 'window' column
if "window" in df_events.columns:
    df_events[["window_start", "window_end"]] = df_events["window"].apply(lambda w: pd.Series([w["start"], w["end"]]))

# Events per type Panel
st.subheader("Events per Type (per minute)")
st.bar_chart(df_events.set_index("window_start")["event_count"])

# Active Users Panel
st.subheader("Active users per Org (per Hour)")
st.dataframe(df_users.sort_values("active_users", ascending=False))

# Top Repos Panel
st.subheader("Top Repositories by Activity")
top_n = st.slider("Top N", 5, 20, 10)
top_repos = df_repos.sort_values("activity_count", ascending=False).head(top_n)
st.table(top_repos)

# Footer
st.caption("Built with ❤️ using Spark, Delta Lake, Azure Blob and Streamlit")
