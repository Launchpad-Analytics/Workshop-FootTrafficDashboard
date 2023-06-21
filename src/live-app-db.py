import streamlit as st
import time
import numpy as np
import pandas as pd
from sqlalchemy import create_engine, text

st.title("Foot Traffic Dashboard")

def load_data():
    
    engine = create_engine("sqlite:///data.db", echo=False)
    with engine.connect() as conn:
        stores = pd.read_sql("stores", conn).astype({"store_id": "string"})
        customers = pd.read_sql("customers", conn).astype({"customer_id": "string"})
        visits = pd.read_sql("visits", conn).astype({"customer_id":"string", "store_id":"string"})\
        .merge(customers, on="customer_id", how="left")\
        .merge(stores, on="store_id", how="left")
    visits["visit_date"] = pd.to_datetime(visits["visit_date"])
    
    return stores, customers, visits


stores, customers, visits = load_data()


show_data = st.checkbox("Show data")
if show_data:
    st.write(visits.head(25))

col1, col2, col3 = st.columns(3)



col1.metric("Active Customers", customers.shape[0])
col2.metric("Total Visits", visits.shape[0])
col3.metric("Total Revenue", f"${round(visits.order_total.sum() / 1000000, 1)}M")

st.subheader("Visits by Day")
# visits_by_day = visits.groupby("visit_date").size()
visits_by_day = visits.set_index("visit_date").resample("2W").size()
st.line_chart(visits_by_day)

st.subheader("Store Locations")
st.map(stores)

st.subheader("Most Stores by State")
st.bar_chart(stores["state"].value_counts().head())

st.subheader("Highest Foot Traffic by State")
st.bar_chart(visits["state"].value_counts().head(5))

time.sleep(10)
st.experimental_rerun()