import streamlit as st
from src.agents import Coordinator
import random  # <- add this

# Initialize coordinator
coordinator = Coordinator()

# Page setup
st.set_page_config(page_title="FloatChat 🌊", layout="wide")

# Custom CSS (Ancient Blue)
st.markdown("""
    <style>
    body {
        background-color: #F7F9FB;
        color: #0D1B2A;
        font-family: 'Inter', sans-serif;
    }
    .block-container {
        padding-top: 2rem;
    }
    .title {
        font-size: 2rem;
        color: #0A4D68;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }
    .subtext {
        color: #1B263B;
        font-size: 1rem;
        margin-bottom: 2rem;
    }
    .stTextArea textarea {
        background-color: #E3F2FD;
        color: #0D1B2A;
        border-radius: 10px;
        border: 1px solid #90CAF9;
        padding: 10px;
    }
    .response-box {
        background-color: #E8F1F5;
        border-radius: 12px;
        padding: 1rem 1.5rem;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    .user-box {
        background-color: #D0E8FF;
        border-radius: 10px;
        padding: 0.8rem 1rem;
        margin-bottom: 0.8rem;
        font-weight: 500;
        color: #0D1B2A;
    }
    </style>
""", unsafe_allow_html=True)

# Title section
st.markdown("<div class='title'>FloatChat 🌊</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>Explore ocean temperature & salinity data interactively</div>", unsafe_allow_html=True)

# ------------------ Add Animated Metrics ------------------
col1, col2, col3 = st.columns(3)
col1.metric("🌡️ Avg Temperature", f"{random.uniform(10, 25):.2f} °C")
col2.metric("💧 Avg Salinity", f"{random.uniform(33, 36):.2f} PSU")
col3.metric("📅 Last Update", "2025-10-17")
# ----------------------------------------------------------

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []  # list of (query, response_dict)

# Split layout: left = chatbot response, right = user query
left_col, right_col = st.columns([2, 1])

with right_col:
    st.markdown("### 💬 Ask FloatChat")
    query = st.text_area("Your question:", placeholder="e.g. What is the temperature and salinity of the Arabian Sea?")
    submit = st.button("Ask")

    if submit and query.strip():
        with st.spinner("Analyzing your query..."):
            result = coordinator.handle(query)
        st.session_state.chat_history.append((query, result))

with left_col:
    st.markdown("### 🤖 FloatChat Response")

    if not st.session_state.chat_history:
        st.info("Ask your first question on the right → to get started!")
    else:
        for query, result in reversed(st.session_state.chat_history):
            st.markdown(f"<div class='user-box'>🧭 You: {query}</div>", unsafe_allow_html=True)
            st.markdown("<div class='response-box'>", unsafe_allow_html=True)
            st.markdown(f"**Intent:** {result['intent']}")
            st.markdown("#### Data Results:")
            for item in result["data"]:
                st.write(f"- {item}")

            if result["visualization"]:
                st.image(result["visualization"], caption="Generated Visualization", use_container_width=True)
            st.markdown("</div>", unsafe_allow_html=True)
