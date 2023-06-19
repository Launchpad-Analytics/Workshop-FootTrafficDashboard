import streamlit as st
st.set_page_config(layout="wide")
import pandas as pd
import numpy as np
import plotly.express as px
import time

# @st.cache
def load_data():
    stores = pd.read_csv("../data/db/stores.csv", dtype={"store_id": "string"})
    customers = pd.read_csv("../data/db/customers.csv", dtype={"customer_id": "string"})
    visits = pd.read_csv("../data/db/visits.csv", dtype={"customer_id":"string", "store_id":"string"})
    visits["visit_date"] = pd.to_datetime(visits["visit_date"])
    
    data = visits.merge(customers, on="customer_id", how="left").merge(stores, on="store_id", how="left")
    
    return data, stores, customers, visits

data, stores, customers, visits = load_data()

st.title("Foot Traffic Dashboard")

data_view = st.checkbox("show raw data")

if data_view:
    st.write(data.head(80))

@st.cache
def kpi_deltas():
    v = pd.read_csv("../data/db/visits.csv")
    num_visits = v.shape[0]
    revenue = v['order_total'].sum()
    
    return num_visits, revenue

num_visits, revenue = kpi_deltas()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Store Count", stores.shape[0])
col2.metric("Active Customers", customers.shape[0])
col3.metric("Total Visits", visits.shape[0], num_visits)
col4.metric("Revenue", f"${round(visits['order_total'].sum() / 1000000, 1)}M", round(revenue))

st.subheader("Store Map")
st.map(stores, zoom=2.5)

st.subheader("Visits By Day")
st.line_chart(data.groupby("visit_date").size().to_frame().resample('10D').sum())

st.subheader("Payment Methods")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Cash vs. Credit")
    cash_credit = data["payment_method"].value_counts().to_frame().reset_index()
    cash_credit.columns = ["payment_method", "count"]
    fig = px.pie(cash_credit, names='payment_method', hole=0.4)
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("Top Card Providers")
    card_types = data["card_on_file"].value_counts().to_frame().reset_index()
    card_types.columns = ["provider", "count"]
    # fig = px.pie(card_types, names="provider",  hole=0.4)
    # st.plotly_chart(fig, use_container_width=True)
    fig = px.bar(card_types, y='provider', x='count', orientation='h')
    st.plotly_chart(fig, use_container_width=True)

st.subheader("Members vs. Nonmembers")

x = data[['visit_date', 'order_total', 'is_member']].groupby(["visit_date", "is_member"]).sum().unstack()["order_total"]
x.columns = ["nonmember", "member"]
x.index = pd.to_datetime(x.index)
x = x.resample("W").sum()

st.line_chart(x)
st.area_chart(x)


# time.sleep(5)
# st.experimental_rerun()