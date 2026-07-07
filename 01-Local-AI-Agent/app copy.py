import streamlit as st
import requests

st.set_page_config(page_title="My Local AI Agent")

st.title("🤖 My Local AI Agent")

prompt = st.text_input("Ask something")

if st.button("Send"):

    if prompt.strip() == "":
        st.warning("Please enter a question.")
        st.stop()

    with st.spinner("Thinking..."):

        response = requests.post(
            "http://127.0.0.1:11434/api/generate",
            json={
                "model": "gemma3:1b",
                "prompt": f"Answer in one short sentence only.\n\nQuestion: {prompt}",
                "stream": False,
                "options": {
                    "num_predict": 30,
                    "temperature": 0
                }
            },
            timeout=60
        )

    if response.status_code == 200:
        result = response.json()
        st.success("Done!")
        st.write(result["response"])
    else:
        st.error(response.text)