# Step 1: Install Required Libraries
!pip install streamlit pyngrok groq

# Step 2: Write the Streamlit App Code
import os
from pyngrok import ngrok
import streamlit as st
from groq import Groq

# Step 3: Configure the Groq API
client = Groq(
    api_key=os.environ.get("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"),  # Set your API key here
)

# Function to get feedback using the Groq API
def get_feedback(user_input, level="A1"):
    prompt = f"""
You are an expert in image classify with 40 years of experience in providing concise but effective feedback. 
Adjust the feedback based on the user's level ({level}) and improve their text according to proper English standards.
Here is the user input: "{user_input}"
    """
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input},
        ],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Step 4: Streamlit App UI
def main():
    st.title("Image Classify Writing Assistant")
    st.subheader("Practice and Improve Your Writing Skills with Expert Feedback")

    # Plan Selection
    st.sidebar.title("Choose Your Plan")
    plans = {
        "30 Days": "A concise 30-day plan with daily writing topics.",
        "45 Days": "A comprehensive 45-day plan with structured topics.",
        "60 Days": "An extensive 60-day plan for mastering your skills.",
    }
    plan = st.sidebar.radio("Select Your Plan:", list(plans.keys()))
    st.sidebar.write(plans[plan])

    # Current Day Indicator
    day = st.sidebar.slider("Select Day", 1, int(plan.split()[0]), 1)
    st.write(f"### Day {day}: Today's Writing Topic")
    st.write("Write about the importance of image classification in AI applications.")

    # User Input Section
    st.text_area("Your Writing:", key="writing_input", height=300, placeholder="Start writing here...")
    level = st.selectbox("Choose Your Proficiency Level:", ["A1", "A2", "A3", "B1", "B2", "C1"])

    # Submit Button
    if st.button("Get Feedback"):
        user_input = st.session_state.get("writing_input", "")
        if user_input.strip():
            feedback = get_feedback(user_input, level)
            st.subheader("Feedback on Your Writing:")
            st.write(feedback)
        else:
            st.error("Please enter your writing before submitting.")

# Step 5: Run the Streamlit App
if __name__ == "__main__":
    public_url = ngrok.connect(addr=8501)
    print(f"Streamlit app is live at: {public_url}")
    main()
