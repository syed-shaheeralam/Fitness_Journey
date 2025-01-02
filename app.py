import os
import streamlit as st
from groq import Groq

# Set your Groq API key
os.environ["GROQ_API_KEY"] = "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"

# Initialize the Groq client
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

def get_fitness_advice(user_message):
    """Fetch fitness advice from the Groq API."""
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": user_message}
            ],
            model="llama-3.3-70b-versatile",
        )
        return chat_completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# Streamlit app UI
st.title("Advanced Fitness Chatbot")
st.subheader("Your personal fitness expert for all age groups!")

# User input
user_input = st.text_input("Ask me anything about fitness, goals, or diet:", placeholder="E.g., Suggest a workout plan for weight loss")

if user_input:
    with st.spinner("Fetching advice..."):
        response = get_fitness_advice(user_input)
    st.text_area("Chatbot Response:", value=response, height=200, max_chars=None)

# Footer
st.markdown("---")
st.markdown("Created with ❤️ using Groq API and Streamlit")
