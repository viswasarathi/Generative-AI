import streamlit as st

st.title("Chatbot")

with st.form("form1"):
    query = st.text_area("Ask me anything.....")
    submit = st.form_submit_button("submit")
    if submit:
        st.info("I am chatbot")