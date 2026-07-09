import streamlit as st
from ollama_helper import generate
from prompts import extract_topics_prompt, blog_prompt

st.set_page_config(page_title="AI Blog Generator")

st.title("🤖 AI Blog Generator")

company = st.text_input("Enter Company Name")
if st.button("Generate Blogs"):

    if company.strip() == "":
        st.warning("Please enter a company name.")
        st.stop()

    with st.spinner("Generating Topics..."):

        topics = generate(extract_topics_prompt(company))

    topic_list = topics.split("\n")

    st.success("Topics Generated Successfully!")

    for topic in topic_list:

        topic = topic.strip()

        if topic == "":
            continue

        st.subheader(topic)

        with st.spinner(f"Writing blog for: {topic}"):

            blog = generate(blog_prompt(topic))

        st.write(blog)

        st.markdown("---")