import streamlit as st
import os
import zipfile
from ollama_helper import generate
from prompts import extract_topics_prompt, blog_prompt
from company_analyzer import analyze_company

# ---------------- Load CSS ---------------- #

def load_css():

    with open("styles.css") as file:

        st.markdown(
            f"<style>{file.read()}</style>",
            unsafe_allow_html=True
        )


# ---------------- Save Blog ---------------- #

def save_blog(filename, content):
    os.makedirs("outputs", exist_ok=True)

    filepath = os.path.join("outputs", filename)

    with open(filepath, "w", encoding="utf-8") as file:
        file.write(content)

    return filepath


# ---------------- Create ZIP ---------------- #

def create_zip():
    zip_path = "outputs/blogs.zip"

    with zipfile.ZipFile(zip_path, "w") as zipf:

        for file in os.listdir("outputs"):

            if file.endswith(".txt"):

                zipf.write(
                    os.path.join("outputs", file),
                    arcname=file
                )

    return zip_path


# ---------------- Page Config ---------------- #

st.set_page_config(
    page_title="AI Blog Generator Agent",
    page_icon="🤖",
    layout="wide"
)
load_css()

# ---------------- Header ---------------- #
# ---------------- Hero Section ---------------- #

st.markdown("""
<div class="hero">

    <h1>Local AI Blog Generator</h1>

    <p>
        Generate professional SEO blogs using local AI models.
        Fast, secure and completely private.
    </p>

</div>
""", unsafe_allow_html=True)
# ---------------- Company Input ---------------- #

st.markdown(
    '<h3 class="section-title">Company Name</h3>',
    unsafe_allow_html=True
)

company = st.text_input(
    label="",
    placeholder="Enter your company name...",
    label_visibility="collapsed"
)
# ---------------- Generate Blogs ---------------- #

generate_btn = st.button(
    "Generate Blogs",
    use_container_width=True
)

if generate_btn:

    if company.strip() == "":
        st.warning("⚠ Please enter a company name.")
        st.stop()
    # ---------------- Company Analysis ---------------- #

    with st.spinner("🔍 Analyzing Company..."):

        company_info = analyze_company(company)

    st.success("✅ Company Analysis Completed")

    with st.expander("🏢 Company Analysis", expanded=False):

        st.write(company_info)

    st.divider()
    # Generate Topics
    with st.spinner("🤖 Generating Trending Topics..."):
        topics = generate(extract_topics_prompt(company))

    topic_list = [topic.strip() for topic in topics.split("\n") if topic.strip()]

    st.success("✅ Topics Generated Successfully!")

    # ---------------- Dashboard Metrics ---------------- #

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="📚 Topics Generated",
            value=len(topic_list)
        )

    with col2:
        st.metric(
            label="📝 Blogs Generated",
            value=len(topic_list)
        )

    with col3:
        st.metric(
            label="🤖 AI Model",
            value="Gemma3:1b"
        )

    # ---------------- Topic Cards ---------------- #

    st.markdown(
    '<h2 class="section-heading">Suggested Topics</h2>',
    unsafe_allow_html=True
)

    for i, topic in enumerate(topic_list, start=1):

     st.markdown(
        f"""
        <div class="topic-card">
            <span>{i:02}</span>
            {topic}
        </div>
        """,
        unsafe_allow_html=True
    )
    st.divider()

    # ---------------- Blog Generation ---------------- #

    st.markdown(
    '<h2 class="section-heading">Generated Blogs</h2>',
    unsafe_allow_html=True
)

    count = 1

    for topic in topic_list:

        with st.spinner(f"✍ Writing blog for '{topic}'..."):

            blog = generate(blog_prompt(topic))

        filepath = save_blog(f"blog{count}.txt", blog)
        display_blog(
            title=topic,
            blog=blog,
            filepath=filepath,
            key=f"download_{count}"
            )

        count += 1

    st.success("🎉 All blogs generated and saved successfully!")

    # ---------------- Download ZIP ---------------- #

    zip_path = create_zip()

    with open(zip_path, "rb") as file:

        st.download_button(
            label="📦 Download All Blogs (ZIP)",
            data=file,
            file_name="AI_Blogs.zip",
            mime="application/zip",
            use_container_width=True
        )
def display_blog(title, blog, filepath, key):

    st.markdown(f"""
<div class="blog-card">

    <div class="blog-header">
        <h3>{title}</h3>
    </div>

</div>
""", unsafe_allow_html=True)

    st.markdown(blog)
    st.divider()

    with open(filepath, "rb") as file:
        st.download_button(
            "Download Blog",
            data=file,
            file_name=os.path.basename(filepath),
            mime="text/plain",
            key=key,
            use_container_width=True
        )