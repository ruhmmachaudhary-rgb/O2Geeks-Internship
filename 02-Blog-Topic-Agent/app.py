import streamlit as st
import requests
from prompts import topic_prompt

st.set_page_config(page_title="AI Blog Topic Agent")

st.title("🤖 AI Blog Topic Agent")

company = st.text_input("Enter Company Name")

if st.button("Generate Topics"):

    if company.strip() == "":
        st.warning("Please enter a company name.")
        st.stop()

    prompt = topic_prompt(company)

    with st.spinner("Generating Trending Topics..."):

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": prompt,
                "stream": False,
                "options": {
                    "temperature": 0.5,
                    "num_predict": 250
                }
            },
            timeout=120
        )

    if response.status_code == 200:

        result = response.json()

        st.success("Top 5 Trending Blog Topics")

        st.write(result["response"])

    else:

        st.error("Something went wrong!")
        st.write(response.text)