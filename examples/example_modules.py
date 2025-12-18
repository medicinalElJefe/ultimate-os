"""
Example 3: Custom Module Usage
Demonstrates using individual modules directly
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ultimate_os.modules import (
    GeometryModule,
    CoherentPossibilityCalculator,
    FrequencyProtocol,
    StateMatrixHandler
)


def custom_module_usage():
    """Custom module usage example"""
    print("Example 3: Custom Module Usage\n")
    
    # 1. Geometry Module
    print("1. Geometry Module:")
    geometry = GeometryModule()
    geometry.initialize_tetrahedron()
    courage_spark = geometry.compute_tetrahedron_courage_spark()
    print(f"   Courage Spark Intensity: {courage_spark['spark_intensity']:.4f}")
    print(f"   Geometric Stability: {courage_spark['geometric_stability']:.4f}")
    
    geometry.initialize_icosahedron()
    antenna = geometry.compute_icosahedron_antenna()
    print(f"   Antenna Reception: {antenna['reception_strength']:.4f}")
    
    # 2. State Matrix Handler
    print("\n2. State Matrix Handler:")
    state_handler = StateMatrixHandler()
    state_handler.initialize()
    
    # Map perception
    perception = state_handler.map_perception({
        'visual': 0.8,
        'auditory': 0.7,
        'tactile': 0.6
    })
    print(f"   Perception mapped: {perception['filtered_perception']:.4f}")
    
    # Map emotion
    emotion = state_handler.map_emotion({
        'valence': 0.5,
        'arousal': 0.7,
        'dominance': 0.6
    })
    print(f"   Emotion mapped: {emotion['filtered_emotion']:.4f}")
    
    # Calculate coherence
    coherence = state_handler.calculate_state_coherence()
    print(f"   State Coherence: {coherence:.4f}")
    
    # 3. Coherent Possibility Calculator
    print("\n3. Coherent Possibility Calculator:")
    coherence_calc = CoherentPossibilityCalculator()
    
    state = state_handler.get_current_state()
    coherence_score = coherence_calc.calculate_coherence(state)
    print(f"   Calculated Coherence: {coherence_score:.4f}")
    
    optimized = coherence_calc.optimize_coherence(state)
    new_coherence = coherence_calc.calculate_coherence(optimized)
    print(f"   Optimized Coherence: {new_coherence:.4f}")
    print(f"   Improvement: {(new_coherence - coherence_score):.4f}")
    
    # 4. Frequency Protocol
    print("\n4. Frequency Protocol:")
    frequency = FrequencyProtocol()
    
    # Set multiple frequencies
    frequency.set_frequency('coherence', 432.0)
    frequency.set_frequency('love', 528.0)
    frequency.set_frequency('awakening', 852.0)
    
    active = frequency.get_active_frequencies()
    print(f"   Active Frequencies: {list(active.keys())}")
    
    # Modulate state
    modulated_state = frequency.modulate_state('love', state)
    print(f"   State modulated with Love frequency (528 Hz)")
    
    # Get recommendations
    recommendations = frequency.get_frequency_recommendations(state)
    print(f"   Frequency Recommendations: {len(recommendations)} suggestions")
    for rec in recommendations[:2]:
        print(f"     - {rec['frequency']}: {rec['reason']}")


if __name__ == '__main__':
    custom_module_usage()
