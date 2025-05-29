import streamlit as st
import requests
import os
import config
from decision_pipeline import make_decision

# Model response handler
st.set_page_config(page_title="AI Eligibility Chatbot", layout="centered")
st.title("🤖 Social Support Assistant")

if "step" not in st.session_state:
    st.session_state.step = 0
    st.session_state.answers = {}

questions = [
    ("monthly_income", "What is your monthly income in AED?"),
    ("employment_years", "How many years have you been employed?"),
    ("family_size", "How many family members live with you?"),
    ("total_assets", "What is your total assets value in AED?"),
    ("total_liabilities", "What is your total liabilities value in AED?"),
    ("credit_score", "What's your credit score?")
]

def ask_next_question():
    key, question = questions[st.session_state.step]
    return st.chat_input(question)

# Chat flow
if st.session_state.step < len(questions):
    user_answer = ask_next_question()
    if user_answer:
        key = questions[st.session_state.step][0]
        try:
            # Store as numeric
            st.session_state.answers[key] = float(user_answer)
            st.session_state.step += 1
        except ValueError:
            st.error("Please enter a valid number.")
else:
    # All data collected
    features = st.session_state.answers
    result = make_decision(features)
    st.success(f"✅ You are likely to be **{result['decision']}** (Confidence: {result['confidence']})")

    # Optional: recommendation logic
    if result["decision"] == "Soft Decline":
        st.info("💡 Consider applying for job training or resume help.")
    else:
        st.info("🎉 You may qualify for fast-track financial aid.")

    # Reset button
    if st.button("Start Over"):
        st.session_state.step = 0
        st.session_state.answers = {}
