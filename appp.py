import streamlit as st
import google.generativeai as genai

# Configure your API key
google_gemini_api_key = "AIzaSyDSw5Gz4gwI2PW36JzuYBgZRrJTBZAwemk"  # Replace with your actual key
genai.configure(api_key=google_gemini_api_key)

# Set up the model
generation_config = {
    "temperature": 1.05,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",
    generation_config=generation_config,
)

st.set_page_config(layout="wide")
st.title('Blogcraft: Your AI Writing Companion')
st.subheader("Craft the perfect blog effortlessly!")

with st.sidebar:
    st.title("Input Blog Details")
    blog_title = st.text_input("Blog Title")
    keywords = st.text_area("Keywords (comma-separated)")
    num_words = st.slider("Number of words", min_value=250, max_value=1000, step=100)
    num_images = st.number_input("Number of images", min_value=1, max_value=5, step=1)
    submit_button = st.button("Generate Blog")

if submit_button:
    chat_session = model.start_chat(
        history=[
            {
                "role": "user",
                "parts": [f"Generate a blog with the title '{blog_title}' using these keywords: {keywords}. Limit it to {num_words} words."],
            },
        ]
    )
    response = chat_session.send_message("Please write the blog content.")
    st.write(response.text)
