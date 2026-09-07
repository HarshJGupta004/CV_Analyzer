import streamlit as st
from groq import Groq
import os
from PyPDF2 import PdfReader
from dotenv import load_dotenv
import re
import pandas as pd
import json

# Load env
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

st.set_page_config(page_title="Intelligent CV Scoring Engine", layout="wide")
st.title("Intelligent CV Scoring Engine")
st.markdown("Upload your CV (PDF)")

uploaded_file = st.file_uploader("Drop it here", type=["pdf"])

if uploaded_file:
    pdf = PdfReader(uploaded_file)
    text = ""

    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"

    # Clean text
    text_clean = re.sub(r"\n+", "\n", text)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("CV Preview")
        st.text_area("Extracted CV Text", value=text_clean, height=400)

    with col2:
        st.subheader("AI Analysis")

        if st.button("Analyze CV"):
            with st.spinner("Analyzing CV..."):

                prompt = f"""
                You are a professional CV reviewer.

                Analyze the CV below and return:
                1. Name and contact details (phone + email)
                2. Professional summary
                3. Key skills (bullet points)
                4. Score out of 100 based on:
                   - Skills match (30)
                   - Experience & achievements (30)
                   - Clarity & formatting (20)
                   - Overall impression (20)

                Return the scores STRICTLY in valid JSON format like this:
                {{
                  "Skills Match": 25,
                  "Experience & Achievements": 22,
                  "Clarity & Formatting": 18,
                  "Overall Impression": 15
                }}

                CV:
                {text_clean}
                """

                response = client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.3,
                    max_tokens=700
                )

                result = response.choices[0].message.content
                st.write(result)

                # Extract JSON safely
                try:
                    json_text = re.search(r"\{.*\}", result, re.S).group()
                    score_data = json.loads(json_text)

                    st.subheader("Score Breakdown")

                    df = pd.DataFrame(
                        list(score_data.items()),
                        columns=["Category", "Score"]
                    )

                    st.bar_chart(df.set_index("Category"))

                    total_score = sum(score_data.values())
                    st.subheader(f"Overall Score: {total_score}/100")
                    st.progress(total_score / 100)

                except Exception as e:
                    st.warning("Score JSON could not be parsed.")
