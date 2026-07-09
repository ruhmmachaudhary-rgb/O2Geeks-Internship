import streamlit as st
from prompts import blog_prompt
from ollama_helper import generate

st.set_page_config(page_title="AI Blog Writer")

st.title("📝 AI Blog Writer")

topic = st.text_input("Enter Blog Topic")

if st.button("Generate Blog"):

    if topic.strip() == "":
        st.warning("Please enter a blog topic.")
        st.stop()

    prompt = blog_prompt(topic)

    with st.spinner("Writing Blog..."):

        blog = generate(prompt)

    st.success("Blog Generated Successfully!")

    st.write(blog)