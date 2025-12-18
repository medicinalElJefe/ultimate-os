"""
Coherent Possibility Calculator
Calculates and optimizes coherence across multiple dimensions
"""

import numpy as np
from typing import Dict, Any, List


class CoherentPossibilityCalculator:
    """
    Calculates coherence metrics and optimizes system states
    for maximum coherent possibility
    """
    
    def __init__(self):
        self.coherence_history = []
        self.axioms = self._initialize_axioms()
        
    def _initialize_axioms(self) -> List[str]:
        """Initialize universal axioms for computation"""
        return [
            "Unity: All is one, interconnected",
            "Resonance: Like attracts like",
            "Vibration: Everything vibrates at specific frequencies",
            "Polarity: Everything has opposites that are complementary",
            "Rhythm: Everything flows in cycles",
            "Causation: Every cause has an effect",
            "Correspondence: As above, so below"
        ]
    
    def calculate_coherence(self, state: Dict[str, Any]) -> float:
        """
        Calculate coherence level of a system state
        
        Args:
            state: System state dictionary
            
        Returns:
            Coherence score [0, 1]
        """
        if not state:
            return 0.0
        
        # Extract state components
        perception = state.get('perception', 0.5)
        emotion = state.get('emotion', 0.5)
        intention = state.get('intention', 0.5)
        
        # Calculate alignment (how well components align)
        alignment = 1.0 - np.std([perception, emotion, intention])
        
        # Calculate intensity (overall energy level)
        intensity = np.mean([perception, emotion, intention])
        
        # Calculate balance (proximity to golden ratio)
        phi = (1 + np.sqrt(5)) / 2
        balance = 1.0 / (1.0 + abs(intensity - 1.0/phi))
        
        # Coherence is weighted combination
        coherence = 0.4 * alignment + 0.3 * intensity + 0.3 * balance
        
        # Store in history
        self.coherence_history.append(coherence)
        
        return float(coherence)
    
    def optimize_coherence(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimize a state for maximum coherence
        
        Args:
            state: Current system state
            
        Returns:
            Optimized state
        """
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        # Extract current values
        perception = state.get('perception', 0.5)
        emotion = state.get('emotion', 0.5)
        intention = state.get('intention', 0.5)
        
        # Calculate optimal values using golden ratio
        current_mean = np.mean([perception, emotion, intention])
        
        # Move towards golden ratio proportion
        optimal_level = 1.0 / phi
        
        # Gentle adjustment (10% towards optimal)
        adjustment_rate = 0.1
        
        optimized_perception = perception + adjustment_rate * (optimal_level - perception)
        optimized_emotion = emotion + adjustment_rate * (optimal_level - emotion)
        optimized_intention = intention + adjustment_rate * (optimal_level - intention)
        
        # Ensure values are in valid range [0, 1]
        optimized_state = {
            'perception': np.clip(optimized_perception, 0, 1),
            'emotion': np.clip(optimized_emotion, 0, 1),
            'intention': np.clip(optimized_intention, 0, 1),
            'coherence_optimized': True,
            'optimization_factor': adjustment_rate
        }
        
        # Copy other state properties
        for key, value in state.items():
            if key not in optimized_state:
                optimized_state[key] = value
        
        return optimized_state
    
    def calculate_possibility_field(self, coherence: float, dimensions: int = 3) -> np.ndarray:
        """
        Calculate possibility field based on coherence
        Higher coherence = more possible futures
        
        Args:
            coherence: Coherence level [0, 1]
            dimensions: Number of dimensions for field
            
        Returns:
            Possibility field array
        """
        # Create possibility field with coherence-based variance
        field_size = 10
        
        # Higher coherence = more focused possibilities
        variance = (1.0 - coherence) * 5.0 + 0.1
        
        possibility_field = np.random.normal(
            loc=coherence,
            scale=variance,
            size=(field_size,) * dimensions
        )
        
        # Normalize to [0, 1]
        possibility_field = np.clip(possibility_field, 0, 1)
        
        return possibility_field
    
    def quantum_superposition(self, states: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Create quantum superposition of multiple states
        
        Args:
            states: List of possible states
            
        Returns:
            Superposed state
        """
        if not states:
            return {}
        
        # Calculate probability weights based on coherence
        weights = []
        for state in states:
            coherence = self.calculate_coherence(state)
            weights.append(coherence)
        
        # Normalize weights
        weights = np.array(weights)
        if weights.sum() > 0:
            weights /= weights.sum()
        else:
            weights = np.ones(len(states)) / len(states)
        
        # Create superposed state
        superposed = {}
        
        # Get all keys from all states
        all_keys = set()
        for state in states:
            all_keys.update(state.keys())
        
        # Weighted average for each key
        for key in all_keys:
            values = []
            for state in states:
                if key in state:
                    value = state[key]
                    if isinstance(value, (int, float)):
                        values.append(value)
            
            if values:
                superposed[key] = float(np.average(values, weights=weights[:len(values)]))
        
        superposed['superposition'] = True
        superposed['state_count'] = len(states)
        
        return superposed
    
    def coherence_resonance(self, freq_hz: float, base_coherence: float) -> float:
        """
        Calculate coherence resonance with a frequency
        
        Args:
            freq_hz: Frequency in Hz
            base_coherence: Base coherence level
            
        Returns:
            Resonant coherence
        """
        # Sacred frequencies and their resonance factors
        sacred_frequencies = {
            174: 0.8,   # Pain reduction
            285: 0.85,  # Energy field healing
            396: 0.9,   # Liberation from fear
            417: 0.92,  # Transformation
            432: 1.0,   # Universal harmony
            528: 0.95,  # DNA repair, love
            639: 0.93,  # Relationships
            741: 0.91,  # Awakening intuition
            852: 0.89,  # Spiritual order
            963: 0.88   # Divine consciousness
        }
        
        # Find closest sacred frequency
        closest_freq = min(sacred_frequencies.keys(), 
                          key=lambda x: abs(x - freq_hz))
        
        # Calculate resonance
        freq_diff = abs(freq_hz - closest_freq)
        resonance_factor = sacred_frequencies[closest_freq] * np.exp(-freq_diff / 100.0)
        
        # Apply resonance to base coherence
        resonant_coherence = base_coherence * resonance_factor
        
        return float(np.clip(resonant_coherence, 0, 1))
    
    def get_axiom_alignment(self, state: Dict[str, Any]) -> Dict[str, float]:
        """
        Calculate alignment with universal axioms
        
        Args:
            state: System state
            
        Returns:
            Alignment scores for each axiom
        """
        coherence = self.calculate_coherence(state)
        
        alignment = {}
        for i, axiom in enumerate(self.axioms):
            # Each axiom contributes to overall coherence
            # Add some variance based on state
            axiom_name = axiom.split(':')[0]
            alignment[axiom_name] = coherence * (0.9 + 0.2 * np.random.random())
        
        return alignment
    
    def get_coherence_statistics(self) -> Dict[str, Any]:
        """Get statistics about coherence history"""
        if not self.coherence_history:
            return {'message': 'No coherence history available'}
        
        history = np.array(self.coherence_history)
        
        return {
            'current': float(history[-1]),
            'mean': float(np.mean(history)),
            'std': float(np.std(history)),
            'min': float(np.min(history)),
            'max': float(np.max(history)),
            'trend': 'increasing' if len(history) > 1 and history[-1] > history[0] else 'stable',
            'samples': len(history)
        }
