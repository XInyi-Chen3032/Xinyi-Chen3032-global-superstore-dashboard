import streamlit as st
import pandas as pd

st.set_page_config(page_title="Global Superstore Dashboard", layout="wide")
st.title("Global Superstore Sales Dashboard by Xinyi Chen")
st.subheader("See more filters in the sidebar:")

df = pd.read_excel("Global Superstore.xls", sheet_name="Orders", engine="xlrd2")

st.sidebar.header("Filters")

region_options = sorted(df["Region"].unique())
select_region = st.sidebar.multiselect("Select Region", region_options, default=region_options)

cat_options = sorted(df["Category"].unique())
select_cat = st.sidebar.multiselect("Select Category", cat_options, default=cat_options)

min_sales = st.sidebar.slider(
    "Minimal Sales Value",
    min_value=float(df["Sales"].min()),
    max_value=float(df["Sales"].max()),
    value=float(df["Sales"].min())
)

df_filter = df[
    (df["Region"].isin(select_region)) &
    (df["Category"].isin(select_cat)) &
    (df["Sales"] >= min_sales)
]

st.markdown("### Filtered Order Table")
st.dataframe(df_filter, use_container_width=True)

st.markdown("### Total Sales by Sub-Category")
group_sales = df_filter.groupby("Sub-Category")["Sales"].sum().reset_index()
st.bar_chart(group_sales, x="Sub-Category", y="Sales")
