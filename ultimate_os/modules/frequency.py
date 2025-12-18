"""
Frequency Protocol Module
Implements frequency-driven state modulation
"""

import numpy as np
from typing import Dict, Any, List, Optional


class FrequencyProtocol:
    """
    Manages frequency protocols for state modulation
    Implements sacred frequencies and their effects on system states
    """
    
    def __init__(self):
        self.active_frequencies = {}
        self.frequency_map = self._initialize_frequency_map()
        self.harmonic_series = []
        
    def _initialize_frequency_map(self) -> Dict[str, Dict[str, Any]]:
        """Initialize frequency map with effects"""
        return {
            'coherence': {
                'frequency': 432.0,
                'description': 'Universal harmony, A=432Hz tuning',
                'effects': ['harmony', 'balance', 'coherence'],
                'chakra': 'heart',
                'color': 'green'
            },
            'grounding': {
                'frequency': 396.0,
                'description': 'Liberation from fear and guilt',
                'effects': ['grounding', 'stability', 'liberation'],
                'chakra': 'root',
                'color': 'red'
            },
            'transformation': {
                'frequency': 417.0,
                'description': 'Transformation and change',
                'effects': ['change', 'transmutation', 'energy_clearing'],
                'chakra': 'sacral',
                'color': 'orange'
            },
            'love': {
                'frequency': 528.0,
                'description': 'Love, DNA repair, miracles',
                'effects': ['healing', 'love', 'DNA_repair', 'transformation'],
                'chakra': 'solar_plexus',
                'color': 'yellow'
            },
            'connection': {
                'frequency': 639.0,
                'description': 'Relationships and connection',
                'effects': ['relationships', 'connection', 'understanding'],
                'chakra': 'heart',
                'color': 'green'
            },
            'intuition': {
                'frequency': 741.0,
                'description': 'Awakening intuition',
                'effects': ['intuition', 'expression', 'solutions'],
                'chakra': 'throat',
                'color': 'blue'
            },
            'awakening': {
                'frequency': 852.0,
                'description': 'Spiritual awakening',
                'effects': ['spiritual_order', 'awakening', 'third_eye'],
                'chakra': 'third_eye',
                'color': 'indigo'
            },
            'unity': {
                'frequency': 963.0,
                'description': 'Divine consciousness and unity',
                'effects': ['unity', 'divine_connection', 'pineal_activation'],
                'chakra': 'crown',
                'color': 'violet'
            },
            'schumann': {
                'frequency': 7.83,
                'description': 'Earth resonance frequency',
                'effects': ['earth_connection', 'healing', 'balance'],
                'chakra': 'all',
                'color': 'white'
            },
            'gamma': {
                'frequency': 40.0,
                'description': 'Gamma brainwave, peak awareness',
                'effects': ['focus', 'peak_performance', 'consciousness'],
                'chakra': 'crown',
                'color': 'white'
            }
        }
    
    def set_frequency(self, freq_type: str, value: Optional[float] = None):
        """
        Set or activate a frequency
        
        Args:
            freq_type: Type of frequency
            value: Optional custom frequency value
        """
        if freq_type in self.frequency_map:
            if value is None:
                value = self.frequency_map[freq_type]['frequency']
            
            self.active_frequencies[freq_type] = {
                'value': value,
                'type': freq_type,
                'active': True,
                'timestamp': len(self.active_frequencies)
            }
        else:
            # Custom frequency
            self.active_frequencies[freq_type] = {
                'value': value if value else 432.0,
                'type': 'custom',
                'active': True,
                'timestamp': len(self.active_frequencies)
            }
    
    def get_frequency(self, freq_type: str) -> Optional[float]:
        """
        Get frequency value
        
        Args:
            freq_type: Type of frequency
            
        Returns:
            Frequency value in Hz
        """
        if freq_type in self.active_frequencies:
            return self.active_frequencies[freq_type]['value']
        elif freq_type in self.frequency_map:
            return self.frequency_map[freq_type]['frequency']
        return None
    
    def get_active_frequencies(self) -> Dict[str, float]:
        """Get all active frequencies"""
        return {
            name: info['value'] 
            for name, info in self.active_frequencies.items()
            if info.get('active', False)
        }
    
    def modulate_state(self, freq_type: str, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Modulate state using frequency
        
        Args:
            freq_type: Frequency type to apply
            state: Current state
            
        Returns:
            Modulated state
        """
        if freq_type not in self.frequency_map:
            return state
        
        freq_info = self.frequency_map[freq_type]
        freq_hz = freq_info['frequency']
        effects = freq_info['effects']
        
        modulated_state = state.copy()
        
        # Apply frequency effects
        modulation_factor = self._calculate_modulation_factor(freq_hz)
        
        # Enhance specific state dimensions based on effects
        if 'coherence' in effects or 'harmony' in effects:
            perception = modulated_state.get('perception', 0.5)
            emotion = modulated_state.get('emotion', 0.5)
            intention = modulated_state.get('intention', 0.5)
            
            # Move towards balance
            mean_val = np.mean([perception, emotion, intention])
            
            modulated_state['perception'] = perception + 0.1 * modulation_factor * (mean_val - perception)
            modulated_state['emotion'] = emotion + 0.1 * modulation_factor * (mean_val - emotion)
            modulated_state['intention'] = intention + 0.1 * modulation_factor * (mean_val - intention)
        
        if 'grounding' in effects or 'stability' in effects:
            modulated_state['grounded'] = True
            modulated_state['stability'] = modulated_state.get('stability', 0.5) * (1 + 0.2 * modulation_factor)
        
        if 'healing' in effects or 'love' in effects:
            modulated_state['healing_factor'] = modulation_factor
            # Boost all dimensions
            for key in ['perception', 'emotion', 'intention']:
                if key in modulated_state:
                    modulated_state[key] = min(1.0, modulated_state[key] * (1 + 0.1 * modulation_factor))
        
        modulated_state['frequency_applied'] = freq_type
        modulated_state['frequency_hz'] = freq_hz
        
        return modulated_state
    
    def _calculate_modulation_factor(self, freq_hz: float) -> float:
        """
        Calculate modulation factor for frequency
        
        Args:
            freq_hz: Frequency in Hz
            
        Returns:
            Modulation factor [0, 1]
        """
        # Base modulation on harmonic relationships
        # Higher sacred frequencies have stronger effects
        if freq_hz >= 432:
            factor = 0.8 + 0.2 * (freq_hz / 1000.0)
        else:
            factor = 0.6 + 0.2 * (freq_hz / 432.0)
        
        return min(1.0, factor)
    
    def generate_harmonic_series(self, fundamental: float, num_harmonics: int = 8) -> List[float]:
        """
        Generate harmonic series from fundamental frequency
        
        Args:
            fundamental: Fundamental frequency
            num_harmonics: Number of harmonics to generate
            
        Returns:
            List of harmonic frequencies
        """
        harmonics = [fundamental * (i + 1) for i in range(num_harmonics)]
        self.harmonic_series = harmonics
        return harmonics
    
    def calculate_resonance(self, freq_a: float, freq_b: float) -> Dict[str, Any]:
        """
        Calculate resonance between two frequencies
        
        Args:
            freq_a, freq_b: Frequencies to compare
            
        Returns:
            Resonance analysis
        """
        # Calculate frequency ratio
        ratio = freq_a / freq_b if freq_b != 0 else 1.0
        
        # Check for harmonic relationships
        # Perfect ratios: 1:1, 2:1, 3:2, 4:3, 5:4 (octave, fifth, fourth, major third)
        harmonic_ratios = {
            1.0: 'unison',
            2.0: 'octave',
            1.5: 'perfect_fifth',
            1.333: 'perfect_fourth',
            1.25: 'major_third',
            0.5: 'octave_down'
        }
        
        # Find closest harmonic ratio
        closest_ratio = min(harmonic_ratios.keys(), key=lambda x: abs(ratio - x))
        
        # Calculate consonance (how close to harmonic ratio)
        consonance = 1.0 / (1.0 + abs(ratio - closest_ratio))
        
        # Beat frequency (for close frequencies)
        beat_freq = abs(freq_a - freq_b)
        
        return {
            'frequency_ratio': ratio,
            'closest_harmonic': harmonic_ratios.get(closest_ratio, 'custom'),
            'consonance': float(consonance),
            'beat_frequency': beat_freq,
            'resonant': consonance > 0.9
        }
    
    def create_binaural_beat(self, base_freq: float, beat_freq: float) -> Dict[str, Any]:
        """
        Create binaural beat specification
        
        Args:
            base_freq: Base frequency (e.g., 432 Hz)
            beat_freq: Desired beat frequency (e.g., 7.83 Hz for Schumann)
            
        Returns:
            Binaural beat specification
        """
        left_freq = base_freq
        right_freq = base_freq + beat_freq
        
        # Determine brainwave state
        brainwave_states = {
            (0.5, 4): 'delta',      # Deep sleep
            (4, 8): 'theta',        # Meditation, creativity
            (8, 13): 'alpha',       # Relaxation, learning
            (13, 30): 'beta',       # Focus, alertness
            (30, 100): 'gamma'      # Peak awareness
        }
        
        state = 'unknown'
        for (low, high), name in brainwave_states.items():
            if low <= beat_freq < high:
                state = name
                break
        
        return {
            'left_ear_frequency': left_freq,
            'right_ear_frequency': right_freq,
            'beat_frequency': beat_freq,
            'brainwave_state': state,
            'base_frequency': base_freq
        }
    
    def systematic_reset(self, state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Perform systematic reset using frequency protocols
        
        Args:
            state: Current state
            
        Returns:
            Reset state
        """
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        # Reset to golden ratio proportions
        reset_state = {
            'perception': 1.0 / phi,
            'emotion': 1.0 / phi,
            'intention': 1.0 / phi,
            'reset': True,
            'reset_frequency': 432.0
        }
        
        # Apply coherence frequency
        reset_state = self.modulate_state('coherence', reset_state)
        
        # Copy non-dimensional properties
        for key, value in state.items():
            if key not in reset_state and key not in ['perception', 'emotion', 'intention']:
                reset_state[key] = value
        
        return reset_state
    
    def get_frequency_recommendations(self, state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Get frequency recommendations based on current state
        
        Args:
            state: Current state
            
        Returns:
            List of frequency recommendations
        """
        recommendations = []
        
        # Analyze state
        perception = state.get('perception', 0.5)
        emotion = state.get('emotion', 0.5)
        intention = state.get('intention', 0.5)
        
        balance = 1.0 - np.std([perception, emotion, intention])
        
        # Recommend based on needs
        if balance < 0.5:
            recommendations.append({
                'frequency': 'coherence',
                'reason': 'Low balance detected, coherence frequency recommended',
                'priority': 'high'
            })
        
        if emotion < 0.4:
            recommendations.append({
                'frequency': 'love',
                'reason': 'Low emotional state, love frequency recommended',
                'priority': 'medium'
            })
        
        if intention < 0.4:
            recommendations.append({
                'frequency': 'transformation',
                'reason': 'Low intention, transformation frequency recommended',
                'priority': 'medium'
            })
        
        if not recommendations:
            recommendations.append({
                'frequency': 'unity',
                'reason': 'State is balanced, unity frequency for enhancement',
                'priority': 'low'
            })
        
        return recommendations
