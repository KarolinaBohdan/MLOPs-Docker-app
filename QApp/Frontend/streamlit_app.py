import streamlit as st
import sys
from pathlib import Path
 
# Add repo root so sibling package `backend` can be imported by Streamlit.
ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))
 
from backend.qa_service import answer_question
 
 
st.title("QApp - Simple Docker Demo")
question = st.text_input("Ask a question")
if st.button("Ask") and question.strip():
    st.success(answer_question(question))
 