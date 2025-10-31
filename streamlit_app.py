import streamlit as st

# Configure page
st.set_page_config(
    page_title="Intuit Demo",
    page_icon="💙",
    layout="centered"
)

# Intuit brand styling
st.markdown("""
    <style>
    /* Import Intuit's preferred font family */
    @import url('https://fonts.googleapis.com/css2?family=Avenir+Next:wght@400;500;600;700&display=swap');
    
    /* Global styles */
    .stApp {
        background-color: #ffffff;
    }
    
    /* Main title styling */
    h1 {
        color: #0077C5 !important;
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-weight: 700 !important;
        padding-bottom: 1rem;
    }
    
    /* Dropdown styling */
    .stSelectbox label {
        color: #393A3D !important;
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    .stSelectbox > div > div {
        background-color: #ffffff;
        border: 2px solid #D9D9DC;
        border-radius: 4px;
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #0077C5;
    }
    
    .stSelectbox > div > div:focus-within {
        border-color: #0077C5;
        box-shadow: 0 0 0 1px #0077C5;
    }
    
    /* Text input styling */
    .stTextInput label {
        color: #393A3D !important;
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    .stTextInput > div > div > input {
        background-color: #ffffff;
        border: 2px solid #D9D9DC;
        border-radius: 4px;
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        color: #393A3D;
    }
    
    .stTextInput > div > div > input:hover {
        border-color: #0077C5;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #0077C5;
        box-shadow: 0 0 0 1px #0077C5;
    }
    
    /* Container styling */
    .element-container {
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
    }
    
    /* Intuit blue accent */
    .intuit-brand {
        border-left: 4px solid #0077C5;
        padding-left: 1rem;
        margin-bottom: 2rem;
    }
    
    /* Button styling */
    .stButton > button {
        background-color: #0077C5;
        color: #ffffff;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 2rem;
        font-family: 'Avenir Next', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        font-weight: 600;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.2s ease;
    }
    
    .stButton > button:hover {
        background-color: #005fa3;
    }
    
    .stButton > button:active {
        background-color: #004d82;
    }
    </style>
""", unsafe_allow_html=True)

# Header with Intuit branding
st.title("Intuit Demo")

# Create two columns for text input and dropdown
col1, col2 = st.columns(2)

with col1:
    user_input = st.text_input(
        "Describe customer situation in a few sentences",
        placeholder="Type here..."
    )

with col2:
    category = st.selectbox(
        "Select Category",
        options=["QuickBooks", "TurboTax", "Mint", "Credit Karma", "Mailchimp"],
        index=0
    )

# Enter button
submit_button = st.button("Enter")

# Display selection when button is clicked
if submit_button:
    st.markdown("<div class='intuit-brand'>", unsafe_allow_html=True)
    if category and user_input:
        st.write(f"**Selected:** {category} | **Details:** {user_input}")
    elif category:
        st.write(f"**Selected:** {category}")
    elif user_input:
        st.write(f"**Details:** {user_input}")
    st.markdown("</div>", unsafe_allow_html=True)
