import streamlit as st
import requests
from prompts import topic_prompt

# ---------------- Page Configuration ---------------- #

st.set_page_config(
    page_title="AI Blog Generator Agent",
    page_icon="🤖",
    layout="wide"
)

# ---------------- Header ---------------- #

st.title("🤖 Local AI Blog Generator Agent")

st.markdown("""
Generate professional SEO blog topics using a local AI model **Gemma3:1b** powered by **Ollama**.

Enter a software company name and let AI generate professional blog ideas.
""")

st.divider()

# ---------------- Sidebar ---------------- #

with st.sidebar:

    st.header("📌 Project Information")

    st.markdown("""
### AI Blog Generator Agent

#### 🛠 Technology Stack

- 🐍 Python
- 🎨 Streamlit
- 🦙 Ollama
- 🤖 Gemma3:1b

---

### 🚀 Current Status

✅ Local AI Running

✅ Topic Generator Ready

⏳ Blog Generator Coming Next
""")

# ---------------- Company Input ---------------- #

company = st.text_input(
    "🏢 Enter Software Company Name",
    placeholder="Example: O2Geeks"
)

# ---------------- Generate Button ---------------- #

if st.button("🚀 Generate Topics", use_container_width=True):

    if company.strip() == "":
        st.warning("⚠ Please enter a company name.")
        st.stop()

    prompt = topic_prompt(company)

    with st.spinner("🤖 AI is generating blog topics..."):

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

        st.success("✅ Top 5 Blog Topics Generated Successfully")

        topics = result["response"].split("\n")

        st.subheader("📚 Suggested Blog Topics")

        count = 1

        for topic in topics:

            topic = topic.strip()

            if topic:

                st.markdown(
                    f"""
                    <div style="
                        background: linear-gradient(90deg, #4F46E5, #2563EB);
                        color:white;
                        padding:16px 20px;
                        border-radius:14px;
                        margin-bottom:15px;
                        font-size:18px;
                        font-weight:600;
                        box-shadow:0px 4px 12px rgba(0,0,0,0.18);
                    ">

                    <span style="
                        background:white;
                        color:#2563EB;
                        padding:6px 12px;
                        border-radius:25px;
                        font-weight:bold;
                        margin-right:12px;
                    ">
                    {count:02}
                    </span>

                    🚀 {topic}

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                count += 1

    else:

        st.error("❌ Something went wrong!")

        st.write(response.text)