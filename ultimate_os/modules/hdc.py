"""
Hyperdimensional Computing (HDC) Architecture
Implements brain-inspired high-dimensional vector computations
"""

import numpy as np
from typing import Dict, Any, List, Optional
import hashlib


class HDCArchitecture:
    """
    Hyperdimensional Computing using high-dimensional binary vectors
    Implements encoding, binding, bundling, and similarity operations
    """
    
    def __init__(self, dimensionality: int = 10000):
        """
        Initialize HDC architecture
        
        Args:
            dimensionality: Number of dimensions (typically 10,000)
        """
        self.dimensionality = dimensionality
        self.item_memory = {}  # Store encoded items
        self.associative_memory = {}  # Store associations
        
    def encode_item(self, item: Any, seed: Optional[int] = None) -> np.ndarray:
        """
        Encode an item as a high-dimensional vector
        
        Args:
            item: Item to encode (string, number, etc.)
            seed: Random seed for reproducibility
            
        Returns:
            High-dimensional binary vector {-1, 1}
        """
        # Use hash of item for consistent encoding
        item_str = str(item)
        if seed is None:
            seed = int(hashlib.md5(item_str.encode()).hexdigest(), 16) % (2**32)
        
        np.random.seed(seed)
        vector = np.random.choice([-1, 1], size=self.dimensionality)
        
        # Store in item memory
        self.item_memory[item_str] = vector
        
        return vector
    
    def encode_task(self, task: Dict[str, Any]) -> np.ndarray:
        """Encode a task dictionary as HDC vector"""
        task_str = str(sorted(task.items()))
        
        if task_str in self.item_memory:
            return self.item_memory[task_str]
        
        return self.encode_item(task_str)
    
    def bind(self, vector_a: np.ndarray, vector_b: np.ndarray) -> np.ndarray:
        """
        Bind two vectors using element-wise multiplication
        Creates a new vector that is dissimilar to both inputs
        
        Args:
            vector_a, vector_b: HDC vectors to bind
            
        Returns:
            Bound vector
        """
        return vector_a * vector_b
    
    def bundle(self, vectors: List[np.ndarray]) -> np.ndarray:
        """
        Bundle multiple vectors using element-wise addition and thresholding
        Creates a superposition that is similar to all inputs
        
        Args:
            vectors: List of HDC vectors to bundle
            
        Returns:
            Bundled vector
        """
        if len(vectors) == 0:
            return np.zeros(self.dimensionality)
        
        # Sum all vectors
        bundled = np.sum(vectors, axis=0)
        
        # Threshold to binary
        bundled = np.where(bundled >= 0, 1, -1)
        
        return bundled
    
    def permute(self, vector: np.ndarray, shift: int = 1) -> np.ndarray:
        """
        Permute (rotate) a vector for sequence encoding
        
        Args:
            vector: HDC vector to permute
            shift: Number of positions to shift
            
        Returns:
            Permuted vector
        """
        return np.roll(vector, shift)
    
    def similarity(self, vector_a: np.ndarray, vector_b: np.ndarray) -> float:
        """
        Calculate cosine similarity between two vectors
        
        Args:
            vector_a, vector_b: Vectors to compare
            
        Returns:
            Similarity score [-1, 1]
        """
        dot_product = np.dot(vector_a, vector_b)
        return dot_product / self.dimensionality
    
    def compute(self, task_vector: np.ndarray) -> Dict[str, Any]:
        """
        Perform HDC computation on a task vector
        
        Args:
            task_vector: Encoded task vector
            
        Returns:
            Computation result
        """
        # Find most similar stored pattern
        max_similarity = -1
        best_match = None
        
        for item_name, stored_vector in self.item_memory.items():
            sim = self.similarity(task_vector, stored_vector)
            if sim > max_similarity:
                max_similarity = sim
                best_match = item_name
        
        # Perform transformation
        result_vector = self.permute(task_vector, shift=1)
        
        return {
            'result_vector': result_vector,
            'best_match': best_match,
            'similarity': float(max_similarity),
            'dimensionality': self.dimensionality
        }
    
    def learn_association(self, key: Any, value: Any):
        """
        Learn an association between key and value
        
        Args:
            key: Key item
            value: Associated value
        """
        key_vector = self.encode_item(key)
        value_vector = self.encode_item(value)
        
        # Store bound association
        association = self.bind(key_vector, value_vector)
        self.associative_memory[str(key)] = association
    
    def recall(self, key: Any) -> Optional[str]:
        """
        Recall value associated with key
        
        Args:
            key: Key to recall
            
        Returns:
            Most similar associated value
        """
        key_vector = self.encode_item(key)
        
        if str(key) not in self.associative_memory:
            return None
        
        association = self.associative_memory[str(key)]
        
        # Unbind by binding with key again (since bind is invertible)
        value_vector = self.bind(association, key_vector)
        
        # Find closest match in item memory
        max_similarity = -1
        best_match = None
        
        for item_name, stored_vector in self.item_memory.items():
            sim = self.similarity(value_vector, stored_vector)
            if sim > max_similarity:
                max_similarity = sim
                best_match = item_name
        
        return best_match
    
    def encode_sequence(self, sequence: List[Any]) -> np.ndarray:
        """
        Encode a sequence using permutation
        
        Args:
            sequence: List of items in sequence
            
        Returns:
            Sequence vector
        """
        vectors = []
        for i, item in enumerate(sequence):
            item_vector = self.encode_item(item)
            # Permute based on position
            permuted = self.permute(item_vector, shift=i)
            vectors.append(permuted)
        
        # Bundle all permuted vectors
        return self.bundle(vectors)
    
    def cleanup(self, noisy_vector: np.ndarray, threshold: float = 0.5) -> Optional[str]:
        """
        Clean up a noisy vector by finding closest match
        
        Args:
            noisy_vector: Noisy or partial vector
            threshold: Minimum similarity threshold
            
        Returns:
            Name of closest matching item
        """
        max_similarity = -1
        best_match = None
        
        for item_name, stored_vector in self.item_memory.items():
            sim = self.similarity(noisy_vector, stored_vector)
            if sim > max_similarity:
                max_similarity = sim
                best_match = item_name
        
        if max_similarity >= threshold:
            return best_match
        return None
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get statistics about stored memories"""
        return {
            'dimensionality': self.dimensionality,
            'items_stored': len(self.item_memory),
            'associations_stored': len(self.associative_memory),
            'memory_capacity': 'theoretical: unbounded, practical: ~millions',
            'storage_efficiency': f'{len(self.item_memory) * self.dimensionality * 8 / 1024 / 1024:.2f} MB'
        }
