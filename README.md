# Intuit AI Specialist Finder

An AI-powered semantic search tool that uses vector embeddings to match customer inquiries with the most appropriate Intuit customer service specialist.

## Overview

This application leverages **Qdrant vector database** and **sentence transformers** to perform semantic search across 125+ specialized customer service agents. Instead of relying on exact keyword matching, it understands the meaning and context of customer inquiries to find the best specialist match.

## Features

- 🔍 **Semantic Search**: Understands the meaning behind customer queries, not just keywords
- 🎯 **Smart Matching**: Finds the most relevant specialist even with different wording
- 📊 **Confidence Scoring**: Provides confidence percentages for each match
- ⚡ **Fast Performance**: In-memory vector database for instant results
- 🎨 **Beautiful UI**: Intuit-branded Streamlit interface
- 🧠 **125+ Specialists**: Covers Tax, QuickBooks, Payroll, Technical Support, and more

## Technology Stack

- **Streamlit**: Web application framework
- **Qdrant**: High-performance vector database
- **Sentence Transformers**: State-of-the-art embedding model (`all-MiniLM-L6-v2`)
- **Python**: Core programming language

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd intuit-demo
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Running the Web App

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

### Using the Vector Database Programmatically

```python
from vector_db import get_vector_db

# Initialize the database
db = get_vector_db()

# Search for specialists
results = db.search(
    query="I need help reconciling my bank account in QuickBooks",
    top_k=5,
    score_threshold=0.3
)

# Display results
for result in results:
    print(f"{result['name']}: {result['confidence_percentage']}%")
```

### Testing the Vector Database

Run the test script to see example searches:

```bash
python vector_db.py
```

## Specialist Categories

The system includes specialists in the following categories:

- **TAX**: Tax filing, deductions, credits, audits, IRS notices
- **QB**: QuickBooks setup, features, industry-specific solutions
- **PAY**: Payroll processing, tax filing, benefits, corrections
- **ACCT**: Bookkeeping, financial statements, reconciliation
- **TECH**: Software installation, troubleshooting, updates
- **SUB**: Subscription management, billing, licensing
- **PROD**: Specialized products (TurboTax Live, Mint, Credit Karma, Mailchimp)
- **COMP**: Compliance and regulatory (GDPR, SOX, PCI, security)
- **ADV**: Advanced features (API integration, custom reports, automation)
- **CS**: Customer success, training, onboarding

## How It Works

### 1. Embedding Generation
Each specialist's name and description is converted into a 384-dimensional vector using a pre-trained language model.

### 2. Vector Database Storage
All embeddings are stored in Qdrant with metadata (ID, name, description).

### 3. Semantic Search
When a user enters a query:
1. The query is converted to a vector embedding
2. Qdrant performs cosine similarity search
3. The most similar specialists are returned with confidence scores
4. Results are ranked and displayed

### 4. Confidence Scoring
- **High Confidence (70%+)**: Excellent match
- **Medium Confidence (50-70%)**: Good match
- **Low Confidence (<50%)**: Possible match

## Example Queries

Try these example queries to see the semantic search in action:

- "I need help filing my individual tax return"
- "How do I reconcile my bank account in QuickBooks?"
- "I'm having trouble with payroll taxes"
- "Need help with inventory tracking"
- "I got a notice from the IRS"
- "Customer wants to set up automated invoicing"
- "Issue with multi-currency transactions"
- "Need help with retirement account distributions"

## Configuration

### Vector Database Settings

Edit `vector_db.py` to customize:

```python
# Change embedding model (default: all-MiniLM-L6-v2)
self.model = SentenceTransformer('your-model-name')

# Use persistent storage instead of in-memory
self.client = QdrantClient(url="http://localhost:6333")

# Adjust distance metric (default: COSINE)
distance=Distance.DOT  # or Distance.EUCLID
```

### Search Parameters

In the Streamlit app or programmatically:

- `top_k`: Number of results to return (default: 5)
- `score_threshold`: Minimum similarity score 0-1 (default: 0.3)

## Project Structure

```
intuit-demo/
├── streamlit_app.py           # Main Streamlit web application
├── vector_db.py               # Vector database module
├── specialists_dictionary.py  # Specialist definitions
├── requirements.txt           # Python dependencies
└── README.md                  # This file
```

## Dependencies

- `streamlit`: Web UI framework
- `qdrant-client`: Vector database client
- `sentence-transformers`: Embedding generation

## Performance

- **Indexing Time**: ~30 seconds for 125 specialists (first run)
- **Search Time**: <100ms per query
- **Memory Usage**: ~500MB (includes embedding model)
- **Vector Dimensions**: 384 (all-MiniLM-L6-v2)

## Development

### Adding New Specialists

1. Edit `specialists_dictionary.py`
2. Add new specialist to the `SPECIALISTS` list:
```python
{
    "id": "YOUR-001",
    "name": "Your Specialist Name",
    "description": "Detailed description of what this specialist handles..."
}
```
3. Restart the app or call `db.reindex()` to update embeddings

### Changing the Embedding Model

Different models offer tradeoffs between speed and accuracy:

- `all-MiniLM-L6-v2`: Fast, lightweight (384 dim) - **Current**
- `all-mpnet-base-v2`: More accurate, slower (768 dim)
- `paraphrase-multilingual-MiniLM-L12-v2`: Multilingual support

## Production Deployment

For production use:

1. **Use Persistent Storage**:
```python
self.client = QdrantClient(url="http://your-qdrant-server:6333")
```

2. **Add Caching**: The app already uses `@st.cache_resource` for the database

3. **Monitor Performance**: Add logging and metrics

4. **Scale Qdrant**: Use Qdrant Cloud or deploy your own cluster

## Troubleshooting

### Issue: Slow first load
**Solution**: First run downloads the embedding model (~80MB). Subsequent runs are instant.

### Issue: Low confidence scores
**Solution**: Lower the confidence threshold or rephrase the query with more context.

### Issue: No results found
**Solution**: Reduce the `score_threshold` parameter.

## License

See LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
