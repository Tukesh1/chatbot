import streamlit as st
import google.generativeai as genai

# Initialize Google GenAI client
genai.configure(api_key="YOUR_API_KEY")

# Function to get response from Gemini AI
def get_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

# Streamlit UI
st.set_page_config(page_title="Fintech Chatbot", page_icon="💰")

st.title("💰 Fintech Chatbot powered by Gemini AI")
st.write("Ask me about **loans, interest rates, credit reports,** and more!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
user_input = st.chat_input("Ask me anything about finance...")

if user_input:
    # Append user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate AI response
    prompt = f"As a FinTech expert, please provide a brief explanation in 3-4 sentences: {user_input}"
    response = get_response(prompt)

    # Append AI message
    st.session_state.messages.append({"role": "assistant", "content": response})

    # Display AI response
    with st.chat_message("assistant"):
        st.markdown(response)
