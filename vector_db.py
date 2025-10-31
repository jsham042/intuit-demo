"""
Vector Database Module using Qdrant
Handles embedding and semantic search for specialist matching
"""

from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from sentence_transformers import SentenceTransformer
from specialists_dictionary import SPECIALISTS
import os


class SpecialistVectorDB:
    def __init__(self, collection_name="intuit_specialists"):
        """
        Initialize the vector database with Qdrant.
        Uses in-memory storage for development.
        """
        self.collection_name = collection_name
        
        # Initialize Qdrant client (in-memory for development)
        # For production, you can use: QdrantClient(url="http://localhost:6333")
        self.client = QdrantClient(":memory:")
        
        # Initialize the embedding model
        # Using a lightweight but effective model
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        
        # Get vector dimension from the model
        self.vector_dim = self.model.get_sentence_embedding_dimension()
        
        # Initialize the collection
        self._initialize_collection()
    
    def _initialize_collection(self):
        """
        Create the Qdrant collection with appropriate configuration.
        """
        # Check if collection exists
        collections = self.client.get_collections().collections
        collection_exists = any(c.name == self.collection_name for c in collections)
        
        if not collection_exists:
            # Create collection with cosine similarity
            self.client.create_collection(
                collection_name=self.collection_name,
                vectors_config=VectorParams(
                    size=self.vector_dim,
                    distance=Distance.COSINE
                )
            )
            print(f"Created collection: {self.collection_name}")
            
            # Embed and index all specialists
            self._index_specialists()
        else:
            print(f"Collection {self.collection_name} already exists")
    
    def _create_searchable_text(self, specialist):
        """
        Create a comprehensive text representation for embedding.
        Combines name and description for better search results.
        """
        return f"{specialist['name']}. {specialist['description']}"
    
    def _index_specialists(self):
        """
        Embed all specialists and add them to the vector database.
        """
        points = []
        
        for idx, specialist in enumerate(SPECIALISTS):
            # Create searchable text
            text = self._create_searchable_text(specialist)
            
            # Generate embedding
            embedding = self.model.encode(text).tolist()
            
            # Create point with metadata
            point = PointStruct(
                id=idx,
                vector=embedding,
                payload={
                    "specialist_id": specialist["id"],
                    "name": specialist["name"],
                    "description": specialist["description"],
                    "searchable_text": text
                }
            )
            points.append(point)
        
        # Upload all points to Qdrant
        self.client.upsert(
            collection_name=self.collection_name,
            points=points
        )
        print(f"Indexed {len(points)} specialists")
    
    def search(self, query, top_k=5, score_threshold=0.3):
        """
        Search for the most relevant specialists based on a query.
        
        Args:
            query (str): User's search query
            top_k (int): Number of results to return
            score_threshold (float): Minimum similarity score (0-1)
        
        Returns:
            list: List of dictionaries containing specialist info and scores
        """
        # Generate query embedding
        query_embedding = self.model.encode(query).tolist()
        
        # Search in Qdrant using the new API
        from qdrant_client.models import QueryRequest
        
        results = self.client.query_points(
            collection_name=self.collection_name,
            query=query_embedding,
            limit=top_k,
            score_threshold=score_threshold
        ).points
        
        # Format results
        formatted_results = []
        for result in results:
            formatted_results.append({
                "specialist_id": result.payload["specialist_id"],
                "name": result.payload["name"],
                "description": result.payload["description"],
                "score": result.score,
                "confidence_percentage": round(result.score * 100, 1)
            })
        
        return formatted_results
    
    def get_specialist_count(self):
        """
        Get the total number of specialists in the database.
        """
        collection_info = self.client.get_collection(self.collection_name)
        return collection_info.points_count
    
    def reindex(self):
        """
        Re-index all specialists (useful after updates to the dictionary).
        """
        # Delete existing collection
        self.client.delete_collection(self.collection_name)
        
        # Reinitialize
        self._initialize_collection()


# Singleton instance for the app
_vector_db_instance = None


def get_vector_db():
    """
    Get or create the singleton vector database instance.
    """
    global _vector_db_instance
    if _vector_db_instance is None:
        _vector_db_instance = SpecialistVectorDB()
    return _vector_db_instance


if __name__ == "__main__":
    # Test the vector database
    print("Initializing vector database...")
    db = SpecialistVectorDB()
    
    print(f"\nTotal specialists indexed: {db.get_specialist_count()}")
    
    # Test searches
    test_queries = [
        "I need help filing my individual tax return",
        "How do I reconcile my bank account in QuickBooks?",
        "I'm having trouble with payroll taxes",
        "Need help with inventory tracking",
        "I got a notice from the IRS"
    ]
    
    print("\n" + "="*80)
    print("Testing semantic search:")
    print("="*80)
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        results = db.search(query, top_k=3)
        
        for i, result in enumerate(results, 1):
            print(f"\n  {i}. {result['name']} ({result['specialist_id']})")
            print(f"     Confidence: {result['confidence_percentage']}%")
            print(f"     Description: {result['description'][:80]}...")

