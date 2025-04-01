import streamlit as st
import google.generativeai as genai
import re  # Import the regular expression module

# Set up Gemini API key
GEMINI_API_KEY = "AIzaSyBvLxH_CL8nm17Ake-Cr0KMdC8FFYoKmiU"  # Replace with your actual API key
genai.configure(api_key=GEMINI_API_KEY)

# Function to generate a formal Job Description using Gemini
def generate_formal_jd(role_title, seniority, location, responsibilities):
    prompt = f"""
    Write a formal job description for the role of {role_title}, which is {seniority} level. The job is located in {location}.
    The responsibilities are: {responsibilities}. Include company overview, required skills, job benefits, and other important details.
    """
    response = genai.GenerativeModel("models/gemini-1.5-flash-001").generate_content(prompt)
    return response.text.strip()

# Function to generate a funky Job Description using Gemini
def generate_fun_jd(role_title, seniority, location, responsibilities):
    prompt = f"""
    Write a fun and funky job description for the role of {role_title}, which is {seniority} level. The job is located in {location}.
    The responsibilities are: {responsibilities}. Make it creative, humorous, and engaging while still conveying the job requirements and skills.
    """
    response = genai.GenerativeModel("models/gemini-1.5-flash-001").generate_content(prompt)
    return response.text.strip()

# CSS Styles for the Streamlit app
css = """
<style>
    .stApp {
        background: linear-gradient(to right, #3a7bd5, #3a6073);
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }

    .stButton>button {
        background-color: #218838;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        transition: 0.3s;
    }

    .stButton>button:hover {
        background-color: #E9F1FA;
    }

    .stTextInput>div>input, .stTextArea>div>textarea {
        border-radius: 8px;
        padding: 10px;
        border: 1px solid #ccc;
    }
</style>
"""

st.markdown(css, unsafe_allow_html=True)

# App Title
st.title("\u2708\ufe0f AI Job Description Generator")

# User Inputs
role_title = st.text_input("Enter the role title:")
seniority = st.selectbox("Select seniority level:", ["Junior", "Mid-level", "Senior", "Lead", "Executive"])
location = st.text_input("Enter the job location:")
responsibilities = st.text_area("Enter responsibilities (comma-separated):")

# Generate Formal Job Description Button
if st.button("Generate Formal JD"):
    if role_title and seniority and location:
        st.success("Generating your formal job description...")

        # Generate Formal JD using Gemini
        jd_text = generate_formal_jd(role_title, seniority, location, responsibilities)

        # Display Formal JD in rich text editor
        st.text_area("Your Formal Job Description:", jd_text, height=400)
    else:
        st.error("Please fill in all required details.")

# Generate Funky Job Description Button
if st.button("Generate Funky JD"):
    if role_title and seniority and location:
        st.success("Generating your funky job description...")

        # Generate Funky JD using Gemini
        jd_text = generate_fun_jd(role_title, seniority, location, responsibilities)

        # Display Funky JD in rich text editor
        st.text_area("Your Funky Job Description:", jd_text, height=400)
    else:
        st.error("Please fill in all required details.")


