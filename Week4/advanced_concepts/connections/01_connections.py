import streamlit as st

conn = st.connection("my_database")
df = conn.query("select * from my_table")
st.dataframe(df)