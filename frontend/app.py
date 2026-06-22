import streamlit as st
import requests

st.title("EnterpriseDoc AI")

question = st.text_input(
    "Ask a question about your document"
)

if st.button("Submit"):

    response = requests.post(
        "http://127.0.0.1:8000/query",
        params={
            "question": question
        }
    )

    result = response.json()

    st.subheader("Answer")

    st.write(result["answer"])