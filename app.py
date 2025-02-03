import streamlit as st
import ollama
import time

# Set Streamlit page configuration
st.set_page_config(page_title="CC Bot", page_icon="🤖", layout="wide")

# Sidebar with user details
st.sidebar.title("👤 About Me")
st.sidebar.markdown(""" """, unsafe_allow_html=True)

details = [
    "**Name:** Appalaneni Uday Kiran", 
    "**Job Role:** Responsible AI Engineer",
    "[🔗 LinkedIn](https://www.linkedin.com/in/uday-kiran-chowdary-4aa25b1b5/)"
]

# Display sidebar details with delay effect
for detail in details:
    st.sidebar.markdown(detail)
    time.sleep(1)

# Custom CSS for chat alignment
st.markdown(
    """
    <style>
        .user-msg { text-align: right; background-color: #ADD8E6; padding: 10px; border-radius: 10px; display: inline-block; }
        .bot-msg { text-align: left; background-color: #f1f0f0; padding: 10px; border-radius: 10px; display: inline-block; }
        .chat-container { display: flex; flex-direction: column; }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🤖 CC Chatbot")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f'<div class="chat-container" style="align-items: flex-end;"><div class="user-msg">{message["content"]}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-container" style="align-items: flex-start;"><div class="bot-msg">{message["content"]}</div></div>', unsafe_allow_html=True)

# User input
user_input = st.chat_input("Ask something...")
if user_input:
    # Append user message to chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Display user message immediately
    st.markdown(f'<div class="chat-container" style="align-items: flex-end;"><div class="user-msg">{user_input}</div></div>', unsafe_allow_html=True)

    # AI response processing with spinner
    with st.spinner("🧠 Thinking..."):
        time.sleep(1)  # Simulating delay
        response = ollama.chat(
            model="deepseek-r1:1.5b",
            messages=st.session_state.messages  # Maintain chat history
        )
        bot_reply = response["message"]["content"]

    # Append AI response to chat history
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})

    # Refresh UI without losing messages
    st.experimental_rerun()
