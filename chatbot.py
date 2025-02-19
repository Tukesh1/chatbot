import streamlit as st
from google import genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Retrieve API key from .env file
api_key = os.getenv("API_KEY")

# Initialize the client with your API key
client = genai.Client(api_key=api_key)

def get_response(prompt):
    try:
        # Generate content using the specified model
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )

        # Return the generated text
        return response.text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    st.title("Google GenAI-powered Fintech Chatbot")
    st.write("You can ask me about loans, interest rates, credit reports, and more.")

    user_input = st.text_input("You:", "")
    if st.button("Send"):
        if user_input:
            # Add context to the prompt to encourage concise responses
            prompt = f"As a FinTech expert, please provide a concise explanation: {user_input}"
            response = get_response(prompt)
            st.text_area("Chatbot:", value=response, height=200)

if __name__ == "__main__":
    main()
