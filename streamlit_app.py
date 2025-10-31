import streamlit as st
from specialists_dictionary import SPECIALISTS
from vector_db import get_vector_db

# Configure page
st.set_page_config(
    page_title="Intuit Demo",
    page_icon="💙",
    layout="centered"
)

# Initialize vector database (cached for performance)
@st.cache_resource
def init_vector_db():
    """Initialize and cache the vector database"""
    return get_vector_db()

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
st.title("🔍 AI Specialist Finder")

st.markdown("""
<div style='color: #393A3D; font-family: "Avenir Next", sans-serif; margin-bottom: 2rem;'>
Use AI-powered semantic search to find the best specialist for your customer's needs.
</div>
""", unsafe_allow_html=True)

# Initialize the vector database
try:
    vector_db = init_vector_db()
    total_specialists = vector_db.get_specialist_count()
    st.info(f"🔍 Searching across {total_specialists} specialized agents")
except Exception as e:
    st.error(f"Error initializing vector database: {str(e)}")
    st.stop()

# User input
user_query = st.text_area(
    "Describe the customer's issue or question",
    placeholder="Example: Customer needs help reconciling their bank account in QuickBooks and is seeing discrepancies...",
    height=100
)

# Search parameters
col1, col2 = st.columns(2)
with col1:
    num_results = st.slider("Number of results", min_value=1, max_value=10, value=5)
with col2:
    confidence_threshold = st.slider("Minimum confidence %", min_value=0, max_value=100, value=30)

# Search button
search_button = st.button("🔍 Find Best Specialist", type="primary")

# Perform search
if search_button:
    if not user_query.strip():
        st.warning("⚠️ Please enter a description of the customer's issue.")
    else:
        with st.spinner("Searching for the best specialist..."):
            # Search the vector database
            results = vector_db.search(
                query=user_query,
                top_k=num_results,
                score_threshold=confidence_threshold / 100
            )
            
            if not results:
                st.warning(f"No specialists found with confidence above {confidence_threshold}%. Try lowering the confidence threshold.")
            else:
                st.markdown("<div class='intuit-brand'>", unsafe_allow_html=True)
                st.success(f"✅ Found {len(results)} matching specialist(s)")
                st.markdown("</div>", unsafe_allow_html=True)
                
                # Display results
                for i, result in enumerate(results, 1):
                    # Determine confidence level color
                    confidence = result['confidence_percentage']
                    if confidence >= 70:
                        confidence_color = "#28A745"  # Green
                        confidence_label = "High Confidence"
                    elif confidence >= 50:
                        confidence_color = "#FFC107"  # Yellow
                        confidence_label = "Medium Confidence"
                    else:
                        confidence_color = "#6C757D"  # Gray
                        confidence_label = "Low Confidence"
                    
                    # Create an expander for each result
                    with st.expander(
                        f"#{i} - {result['name']} ({result['specialist_id']}) - {confidence:.1f}% match",
                        expanded=(i == 1)  # Expand the first result by default
                    ):
                        # Confidence indicator
                        st.markdown(f"""
                        <div style='background-color: {confidence_color}; color: white; padding: 0.5rem; border-radius: 4px; margin-bottom: 1rem; text-align: center; font-weight: 600;'>
                            {confidence_label}: {confidence:.1f}%
                        </div>
                        """, unsafe_allow_html=True)
                        
                        # Specialist details
                        st.markdown(f"**Specialist ID:** `{result['specialist_id']}`")
                        st.markdown(f"**Name:** {result['name']}")
                        st.markdown(f"**Description:**")
                        st.markdown(f"<div style='background-color: #F8F9FA; padding: 1rem; border-radius: 4px; border-left: 4px solid #0077C5;'>{result['description']}</div>", unsafe_allow_html=True)
                        
                        # Action button
                        if st.button(f"Route to {result['name']}", key=f"route_{i}"):
                            st.success(f"✅ Routing customer to {result['name']} ({result['specialist_id']})")

# Add some spacing
st.markdown("<br><br>", unsafe_allow_html=True)

# Information section
with st.expander("ℹ️ How does this work?"):
    st.markdown("""
    ### AI-Powered Semantic Search
    
    This tool uses advanced natural language processing to match customer inquiries with the most appropriate specialist:
    
    1. **Vector Embeddings**: Each specialist's description is converted into a mathematical vector representation using a pre-trained language model
    2. **Semantic Understanding**: The system understands the meaning and context of queries, not just keywords
    3. **Similarity Matching**: Qdrant vector database finds specialists whose descriptions are semantically similar to the customer's issue
    4. **Confidence Scoring**: Results are ranked by relevance with confidence scores
    
    **Technology Stack:**
    - 🗄️ **Qdrant**: High-performance vector database
    - 🤖 **Sentence Transformers**: State-of-the-art embedding model
    - 🎯 **Cosine Similarity**: Measures semantic similarity between queries and specialists
    
    **Benefits:**
    - Finds relevant specialists even with different wording
    - Handles complex, multi-topic queries
    - Fast search across 90+ specialist types
    """)
