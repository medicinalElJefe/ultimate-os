"""
State Matrix Handler Module
Implements perception-emotion-intention mapping and state management
"""

import numpy as np
import tempfile
import logging
import os
from typing import Dict, Any, List, Optional
import json

logger = logging.getLogger(__name__)


class StateMatrixHandler:
    """
    Manages state matrices for perception, emotion, and intention tracking
    Implements multi-dimensional state representation and evolution
    """
    
    def __init__(self):
        self.current_state = {}
        self.state_history = []
        self.state_dimensions = ['perception', 'emotion', 'intention']
        self.transition_matrix = None
        self.initialized = False
        
    def initialize(self) -> Dict[str, Any]:
        """Initialize state matrix with default values"""
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        # Initialize state with golden ratio proportions
        self.current_state = {
            'perception': 1.0 / phi,
            'emotion': 1.0 / phi,
            'intention': 1.0 / phi,
            'coherence': 0.0,
            'timestamp': 0,
            'dimension': 3
        }
        
        # Initialize transition matrix (3x3 for P-E-I)
        # Defines how each dimension influences others
        self.transition_matrix = np.array([
            [0.7, 0.2, 0.1],  # Perception influences
            [0.2, 0.6, 0.2],  # Emotion influences
            [0.1, 0.3, 0.6]   # Intention influences
        ])
        
        self.state_history.append(self.current_state.copy())
        self.initialized = True
        
        return self.current_state
    
    def get_current_state(self) -> Dict[str, Any]:
        """Get current state"""
        if not self.initialized:
            self.initialize()
        return self.current_state.copy()
    
    def update_state(self, new_state: Dict[str, Any]):
        """
        Update current state
        
        Args:
            new_state: New state values
        """
        # Update timestamp
        new_state['timestamp'] = self.current_state.get('timestamp', 0) + 1
        
        # Store in history
        self.state_history.append(new_state.copy())
        
        # Update current
        self.current_state = new_state
        
        # Limit history size
        if len(self.state_history) > 1000:
            self.state_history = self.state_history[-1000:]
    
    def get_state_vector(self) -> np.ndarray:
        """
        Get current state as vector
        
        Returns:
            State vector [perception, emotion, intention]
        """
        return np.array([
            self.current_state.get('perception', 0.0),
            self.current_state.get('emotion', 0.0),
            self.current_state.get('intention', 0.0)
        ])
    
    def evolve_state(self, steps: int = 1) -> Dict[str, Any]:
        """
        Evolve state through transition matrix
        
        Args:
            steps: Number of evolution steps
            
        Returns:
            Evolved state
        """
        current_vector = self.get_state_vector()
        
        # Apply transition matrix multiple times
        for _ in range(steps):
            current_vector = self.transition_matrix @ current_vector
            # Normalize to maintain scale
            current_vector = current_vector / (np.sum(current_vector) + 1e-10)
        
        # Create new state
        evolved_state = {
            'perception': float(current_vector[0]),
            'emotion': float(current_vector[1]),
            'intention': float(current_vector[2]),
            'evolved': True,
            'evolution_steps': steps
        }
        
        return evolved_state
    
    def calculate_state_coherence(self) -> float:
        """
        Calculate coherence of current state
        
        Returns:
            Coherence value [0, 1]
        """
        vector = self.get_state_vector()
        
        # Coherence based on balance and alignment
        mean_val = np.mean(vector)
        std_val = np.std(vector)
        
        # Lower std = higher coherence
        coherence = 1.0 / (1.0 + std_val)
        
        # Factor in alignment with golden ratio
        phi = (1 + np.sqrt(5)) / 2
        ideal_val = 1.0 / phi
        
        alignment = 1.0 - abs(mean_val - ideal_val)
        
        total_coherence = 0.6 * coherence + 0.4 * alignment
        
        return float(np.clip(total_coherence, 0, 1))
    
    def map_perception(self, sensory_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map sensory input to perception state
        
        Args:
            sensory_input: Raw sensory data
            
        Returns:
            Perception mapping
        """
        # Extract sensory dimensions
        visual = sensory_input.get('visual', 0.5)
        auditory = sensory_input.get('auditory', 0.5)
        tactile = sensory_input.get('tactile', 0.5)
        
        # Combine into perception value
        perception = np.mean([visual, auditory, tactile])
        
        # Apply perceptual filters
        filtered_perception = self._apply_filters(perception, 'perception')
        
        return {
            'raw_perception': perception,
            'filtered_perception': filtered_perception,
            'sensory_components': {
                'visual': visual,
                'auditory': auditory,
                'tactile': tactile
            }
        }
    
    def map_emotion(self, emotional_input: Dict[str, Any]) -> Dict[str, Any]:
        """
        Map emotional input to emotion state
        
        Args:
            emotional_input: Emotional data
            
        Returns:
            Emotion mapping
        """
        # Extract emotional dimensions
        valence = emotional_input.get('valence', 0.0)  # Positive/negative
        arousal = emotional_input.get('arousal', 0.5)  # Intensity
        dominance = emotional_input.get('dominance', 0.5)  # Control
        
        # Map to emotion value
        emotion = (valence + 1.0) / 2.0 * arousal  # Normalize valence from [-1,1] to [0,1]
        
        # Apply emotional filters
        filtered_emotion = self._apply_filters(emotion, 'emotion')
        
        return {
            'raw_emotion': emotion,
            'filtered_emotion': filtered_emotion,
            'emotional_components': {
                'valence': valence,
                'arousal': arousal,
                'dominance': dominance
            }
        }
    
    def map_intention(self, goal: Any, motivation: float = 0.5) -> Dict[str, Any]:
        """
        Map goal and motivation to intention state
        
        Args:
            goal: Goal specification
            motivation: Motivation level [0, 1]
            
        Returns:
            Intention mapping
        """
        # Calculate intention strength
        goal_clarity = 1.0 if goal is not None else 0.0
        
        intention = goal_clarity * motivation
        
        # Apply intention filters
        filtered_intention = self._apply_filters(intention, 'intention')
        
        return {
            'raw_intention': intention,
            'filtered_intention': filtered_intention,
            'goal': str(goal),
            'motivation': motivation
        }
    
    def _apply_filters(self, value: float, filter_type: str) -> float:
        """
        Apply filters to state values
        
        Args:
            value: Input value
            filter_type: Type of filter
            
        Returns:
            Filtered value
        """
        # Apply smoothing based on history
        if len(self.state_history) > 0:
            historical_value = self.state_history[-1].get(filter_type, value)
            # Exponential moving average
            alpha = 0.3
            filtered = alpha * value + (1 - alpha) * historical_value
        else:
            filtered = value
        
        return float(np.clip(filtered, 0, 1))
    
    def create_state_snapshot(self) -> Dict[str, Any]:
        """
        Create comprehensive state snapshot
        
        Returns:
            State snapshot
        """
        return {
            'current_state': self.current_state.copy(),
            'state_vector': self.get_state_vector().tolist(),
            'coherence': self.calculate_state_coherence(),
            'history_length': len(self.state_history),
            'transition_matrix': self.transition_matrix.tolist() if self.transition_matrix is not None else None
        }
    
    def save_state(self, filepath: Optional[str] = None):
        """
        Save state to file
        
        Args:
            filepath: Path to save state (defaults to temp directory)
        """
        if filepath is None:
            filepath = os.path.join(tempfile.gettempdir(), 'ultimate_os_state_matrix.json')
        
        snapshot = self.create_state_snapshot()
        
        # Convert numpy arrays to lists for JSON serialization
        try:
            with open(filepath, 'w') as f:
                json.dump(snapshot, f, indent=2)
            return True
        except (IOError, PermissionError, OSError) as e:
            logger.error(f"Error saving state to {filepath}: {e}")
            return False
    
    def load_state(self, filepath: Optional[str] = None):
        """
        Load state from file
        
        Args:
            filepath: Path to load state from (defaults to temp directory)
        """
        if filepath is None:
            filepath = os.path.join(tempfile.gettempdir(), 'ultimate_os_state_matrix.json')
        
        try:
            with open(filepath, 'r') as f:
                snapshot = json.load(f)
            
            self.current_state = snapshot['current_state']
            if snapshot['transition_matrix']:
                self.transition_matrix = np.array(snapshot['transition_matrix'])
            
            return True
        except (IOError, PermissionError, OSError, FileNotFoundError) as e:
            logger.error(f"Error loading state from {filepath}: {e}")
            return False
    
    def analyze_state_trajectory(self, window: int = 10) -> Dict[str, Any]:
        """
        Analyze trajectory of state over time
        
        Args:
            window: Number of recent states to analyze
            
        Returns:
            Trajectory analysis
        """
        if len(self.state_history) < 2:
            return {'message': 'Insufficient history for trajectory analysis'}
        
        recent_states = self.state_history[-window:]
        
        # Extract time series for each dimension
        perception_series = [s.get('perception', 0) for s in recent_states]
        emotion_series = [s.get('emotion', 0) for s in recent_states]
        intention_series = [s.get('intention', 0) for s in recent_states]
        
        # Calculate trends
        def calculate_trend(series):
            if len(series) < 2:
                return 0.0
            return (series[-1] - series[0]) / len(series)
        
        return {
            'window_size': len(recent_states),
            'trends': {
                'perception': calculate_trend(perception_series),
                'emotion': calculate_trend(emotion_series),
                'intention': calculate_trend(intention_series)
            },
            'variance': {
                'perception': float(np.var(perception_series)),
                'emotion': float(np.var(emotion_series)),
                'intention': float(np.var(intention_series))
            },
            'stability': 1.0 / (1.0 + np.mean([
                np.var(perception_series),
                np.var(emotion_series),
                np.var(intention_series)
            ]))
        }
