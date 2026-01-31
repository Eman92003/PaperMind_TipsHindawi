import streamlit as st
import requests
import base64
import json
import re

# ================= Page Config =================
st.set_page_config(
    page_title="PaperMind",
    layout="wide"
)

# ================= Session State =================
if "page" not in st.session_state:
    st.session_state.page = "home"

# ================= Sidebar =================
with st.sidebar:
    st.image(
        r"C:\Users\Eman Yaser\Documents\Tips Hindawi\Graduation project\graduation project logo.png",
        width=260
    )

    if st.button("🏠 Home", use_container_width=True):
        st.session_state.page = "home"

    if st.button("📄 Paper Summarization", use_container_width=True):
        st.session_state.page = "summary"

    if st.button("🧾 Information Extraction", use_container_width=True):
        st.session_state.page = "extract"

    if st.button("❓ Question Answering", use_container_width=True):
        st.session_state.page = "qa"

# ================= Constants =================
API_KEY = "secret123"

SUMMARY_API = "https://nonrationalized-unmercurially-finley.ngrok-free.dev/sammary"
QA_API = "https://pennie-sabulous-rheba.ngrok-free.dev/QA"
EXTRACT_API = "https://pennie-sabulous-rheba.ngrok-free.dev/info_Extractor"

HEADERS = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

page = st.session_state.page

# ================= Pages =================

# -------- Home --------
if page == "home":
    st.title("📘 PaperMind – AI Research Assistant")
    st.markdown("""
    **PaperMind** is an AI-powered system designed to help users
    understand academic research papers efficiently.

    ### 🔍 Features
    - Paper Summarization
    - Information Extraction
    - Question Answering (RAG)

    ### ⚙️ Tech Stack
    FastAPI • Streamlit • LangChain • LLMs
    """)

# -------- Summarization --------
elif page == "summary":
    st.title("📄 Research Paper Summarization")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )

    if st.button("Summarize Paper"):
        if uploaded_file is None:
            st.warning("Please upload a PDF.")
        else:
            pdf_bytes = uploaded_file.read()
            pdf_base64 = base64.b64encode(pdf_bytes).decode()
            payload = {"pdf_file": pdf_base64}

            with st.spinner("Summarizing..."):
                try:
                    res = requests.post(
                        SUMMARY_API,
                        headers=HEADERS,
                        json=payload,
                        timeout=300
                    )
                    res.raise_for_status()
                    summary = res.json().get("summary", "")
                    st.subheader("📝 Summary")
                    st.write(summary)
                except Exception as e:
                    st.error(f"Failed to summarize the paper: {e}")

# -------- Information Extraction --------
elif page == "extract":
    st.title("🧾 Information Extraction")

    uploaded_file = st.file_uploader(
        "Upload Research Paper (PDF)",
        type=["pdf"]
    )

    if st.button("Extract Information"):
        if uploaded_file is None:
            st.warning("Please upload a PDF file.")
        else:
            pdf_bytes = uploaded_file.read()
            pdf_base64 = base64.b64encode(pdf_bytes).decode()
            payload = {"pdf_file": pdf_base64}

            with st.spinner("Extracting information..."):
                try:
                    res = requests.post(
                        EXTRACT_API,
                        headers=HEADERS,
                        json=payload,
                        timeout=1000
                    )
                    res.raise_for_status()
                    data = res.json()

                    # Problem Statement
                    st.subheader("📌 Problem Statement")
                    st.write(data.get("problem_statement", ""))

                    # Datasets
                    st.subheader("📊 Datasets")
                    datasets_raw = data.get("datasets", "[]")
                    datasets = []
                    if isinstance(datasets_raw, str):
                        try:
                            datasets = json.loads(datasets_raw)
                        except Exception:
                            # لو string malformed، نجرب نفصل يدوي
                            pattern = r'\{.*?\}'
                            matches = re.findall(pattern, datasets_raw)
                            for m in matches:
                                try:
                                    datasets.append(json.loads(m))
                                except Exception:
                                    datasets.append({"name": m, "images": "", "classes": []})
                    elif isinstance(datasets_raw, list):
                        datasets = datasets_raw

                    if datasets:
                        with st.expander("View All Datasets"):
                            for d in datasets:
                                classes = d.get('classes', [])
                                if not isinstance(classes, list):
                                    classes = [str(classes)]
                                st.markdown(
                                    f"- **Name:** {d.get('name')}\n  - **Images:** {d.get('images')}\n  - **Classes:** {', '.join(classes)}"
                                )
                    else:
                        st.write("Datasets not available")

                    # Models
                    st.subheader("🧠 Models")
                    models_raw = data.get("models", "")
                    models = []

                    if isinstance(models_raw, str):
                        try:
                            models = json.loads(models_raw)
                        except Exception:
                            # نفصل الموديلات يدوياً لو string طويل
                            pattern = r'\{.*?\}'
                            matches = re.findall(pattern, models_raw)
                            for m in matches:
                                try:
                                    models.append(json.loads(m))
                                except Exception:
                                    models.append({"name": m, "type": "", "task": ""})
                    elif isinstance(models_raw, list):
                        models = models_raw

                    if models:
                        with st.expander("View All Models"):
                            for m in models:
                                if not isinstance(m, dict):
                                    m = {"name": str(m), "type": "", "task": ""}
                                st.markdown(
                                    f"- **Name:** {m.get('name','')}\n  - **Type:** {m.get('type','')}\n  - **Task:** {m.get('task','')}"
                                )
                    else:
                        st.write("Models not available")

                    # Results
                    st.subheader("📈 Results")
                    st.write(data.get("results", ""))

                except Exception as e:
                    st.error(f"Information extraction failed: {e}")

# -------- Question Answering --------
elif page == "qa":
    st.title("❓ Question Answering")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"]
    )
    question = st.text_input("Enter your question")

    if st.button("Get Answer"):
        if not uploaded_file or not question.strip():
            st.warning("Please upload a PDF and enter a question.")
        else:
            pdf_bytes = uploaded_file.read()
            pdf_base64 = base64.b64encode(pdf_bytes).decode()
            payload = {"pdf_file": pdf_base64, "question": question}

            with st.spinner("Finding answer..."):
                try:
                    res = requests.post(
                        QA_API,
                        headers=HEADERS,
                        json=payload,
                        timeout=1000
                    )
                    res.raise_for_status()
                    data = res.json().get("answer", {})

                    st.subheader("🧾 Question")
                    st.write(data.get("Question", ""))

                    st.subheader("✅ Answer")
                    st.write(data.get("Answer", ""))

                    st.subheader("📌 Evidence")
                    evidence = data.get("Evidence", [])
                    if evidence:
                        cleaned = [ev.strip().lstrip("•.- ") for ev in evidence]
                        st.markdown("\n".join([f"- {ev}" for ev in cleaned]))
                    else:
                        st.write("No evidence found.")

                    st.subheader("📄 Pages")
                    pages = data.get("Pages", [])
                    if pages:
                        st.write(", ".join(map(str, sorted(set(pages)))))
                    else:
                        st.write("Not available")

                except Exception as e:
                    st.error(f"Failed to get answer: {e}")
