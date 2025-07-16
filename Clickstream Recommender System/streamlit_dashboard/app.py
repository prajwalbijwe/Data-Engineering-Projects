import requests
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Recommender", layout="wide")
st.title("Personalized Recommendations")


# API Config
api_url = "http://127.0.0.1:8080/recommendations"

# USer Input

user_id = st.text_input("Enter user ID (e.g. user_101)", value="user_101")
top_k = st.slider("Top K Recommendations", min_value=1, max_value=10, value=5)

if st.button("Get Recommendations"):
    try:
        response = requests.get(api_url, params={"user_id": user_id, "topK":top_k})
        if response.status_code==200:
            recs = pd.DataFrame(response.json())
            st.success(f"Showing top {top_k} items for {user_id}")
            st.dataframe(recs)

            st.bar_chart(recs.set_index("item_id")["rating"])
        else:
            st.error(f"{response.status_code}: {response.json()['detail']}")
    except Exception as e:
        st.error(f"Failed to fetch recommendations: {str(e)}")
