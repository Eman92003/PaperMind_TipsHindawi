# 📄 PaperMind
**An NLP-based system for analyzing and understanding research papers**

---

## 🔍 Overview
**PaperMind** is an NLP graduation project that focuses on extracting meaningful insights from research papers using Transformer-based language models.
The project is implemented using Jupyter notebooks and provides three core features:
- Question Answering
- Automatic Multi-level Summarization
- Information Feature Extraction

The system is designed to handle long academic papers and present structured, explainable outputs grounded in the original paper content.

---

## 🧠 Core Features

### ❓ Question Answering
This feature allows users to ask natural language questions about a research paper and receive:
- A clear answer
- Supporting evidence extracted from the paper
- The exact citation location (page number) where the answer was found

#### Technical Details
- Built using the **Mistral** language model
- Implemented through a **LangChain pipeline**
- Uses a **Structured Output Parser** to ensure the output follows a predefined and well-formatted structure
- The final output includes:
  - Answer
  - Evidence text
  - Citation page number

This approach improves transparency and trustworthiness by grounding each answer in the paper itself.

---

### 📝 Automatic Multi-level Summarization
This feature generates a comprehensive summary of long research papers using a **multi-level summarization strategy**.

#### Why Multi-level Summarization?
Research papers are typically very long, which makes single-pass summarization ineffective.
To address this, the paper is summarized in multiple stages:
1. The paper is split into smaller sections
2. Each section is summarized individually
3. Partial summaries are then combined into a higher-level summary

#### Technical Details
- Implemented using **BART-Large**
- Designed to handle large documents efficiently
- Preserves the main ideas, methods, and conclusions of the paper

---

### 🔎 Information Feature Extraction
This feature extracts structured information from research papers to highlight their core components.

#### Extracted Information
- Problem Statement
- Dataset(s) used
- Models / Methods
- Results and Findings

#### Technical Details
- Implemented using **LangChain Chains**
- Uses prompt-driven extraction to convert unstructured academic text into structured outputs
- Helps users quickly understand the essence of a paper without reading it entirely

---

## 🗂️ Project Structure
The project is organized into Jupyter notebooks, each representing a core feature:

- `graduation-project-qa.ipynb`  
  → Question Answering using Mistral + LangChain + Structured information extraction using LangChain Chains

- `graduation-project-summary.ipynb`  
  → Multi-level Automatic Summarization using BART-Large  

---

## 🛠️ Technologies Used
- Python
- Hugging Face Transformers
- LangChain
- Mistral Language Model
- BART-Large
- Structured Output Parsers
- Jupyter Notebook
- Streamlit
- Ngrok

---

## 🚀 Deployment
The project was deployed as an interactive web application using:
- **Streamlit** for the user interface
- **Ngrok** to expose the local application to the internet

This setup allows users to:
- Upload papers
- Ask questions
- Generate summaries
- View extracted information interactively

---
## 🎥 Demo Video
[Watch the demo video](https://youtu.be/-djmNwb-8tA)

---

## 📌 Project Context
This project was developed as an **Tips_Hindawi intern graduation project** focusing on practical NLP applications using modern Transformer models and LangChain pipelines.
