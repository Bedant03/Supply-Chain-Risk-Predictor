import streamlit as st
from event_extraction import event_extraction_llm
from risk_predictor import compute_risk
from mitigation import suggest_actions_llm

st.set_page_config(page_title="Supply Chain Predictor", layout="wide")

st.title("📦 Supply Chain Risk Predictor")

text = st.text_area("Enter news/event")

if st.button("Analyze"):

    if not text.strip():
        st.warning("Enter some text")
    else:
        with st.spinner("Analyzing..."):

            event = event_extraction_llm(text)
            risk = compute_risk(event)
            actions = suggest_actions_llm(event, risk)

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Event")
            st.json(event)

        with col2:
            st.subheader("⚠️ Risk Score")

            if risk >= 70:
                st.error(f"High Risk: {risk}/100")
            elif risk >= 40:
                st.warning(f"Medium Risk: {risk}/100")
            else:
                st.success(f"Low Risk: {risk}/100")

        st.subheader("🛠️ Suggested Actions")

        for i, action in enumerate(actions["actions"], 1):
            st.write(f"{i}. {action}")