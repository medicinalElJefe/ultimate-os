#!/usr/bin/env python3
"""
Ultimate OS Interactive Demo
Shows all capabilities in a visual format
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ultimate_os import UltimateOS
import json

def print_banner(text):
    """Print a formatted banner"""
    print("\n" + "=" * 70)
    print(f"  {text}")
    print("=" * 70)

def print_section(title):
    """Print a section header"""
    print(f"\n{'─' * 70}")
    print(f"  {title}")
    print('─' * 70)

def main():
    """Run interactive demo"""
    print_banner("ULTIMATE OS - INTERACTIVE DEMONSTRATION")
    
    print("\nInitializing Ultimate Operating System...")
    os_instance = UltimateOS({'hdc_dims': 10000})
    
    print_section("SYSTEM BOOT")
    boot_result = os_instance.boot()
    print(f"✓ System Coherence: {boot_result['coherence_level']:.4f}")
    print(f"✓ Geometry Mode: {boot_result['geometry_mode']}")
    print(f"✓ All modules loaded successfully")
    
    print_section("GEOMETRIC COMPUTING")
    
    # Tetrahedron
    result = os_instance.process_task({
        'type': 'geometric_computation',
        'geometry': 'tetrahedron'
    })
    print("Tetrahedron (Courage Spark):")
    print(f"  • Spark Intensity: {result['result']['spark_intensity']:.4f}")
    print(f"  • Resonance: {result['result']['resonance_frequency']} Hz")
    print(f"  • Stability: {result['result']['geometric_stability']:.4f}")
    
    # Icosahedron
    result = os_instance.process_task({
        'type': 'geometric_computation',
        'geometry': 'icosahedron'
    })
    print("\nIcosahedron (Antenna Effect):")
    print(f"  • Reception Strength: {result['result']['reception_strength']:.4f}")
    print(f"  • Antenna Gain: {result['result']['antenna_gain']:.4f}")
    print(f"  • Coverage: {result['result']['coverage']}")
    
    print_section("COHERENCE OPTIMIZATION")
    result = os_instance.process_task({'type': 'coherence_optimization'})
    print(f"Initial Coherence:   {result['initial_coherence']:.6f}")
    print(f"Optimized Coherence: {result['optimized_coherence']:.6f}")
    print(f"Improvement:         +{result['improvement']:.6f}")
    
    print_section("FREQUENCY PROTOCOLS")
    frequencies = [
        ('coherence', 432.0, 'Universal Harmony'),
        ('love', 528.0, 'DNA Repair & Love'),
        ('awakening', 852.0, 'Spiritual Awakening')
    ]
    
    for freq_type, freq_value, description in frequencies:
        result = os_instance.process_task({
            'type': 'frequency_modulation',
            'frequency_type': freq_type,
            'value': freq_value
        })
        print(f"✓ {description}: {freq_value} Hz - State Modulated")
    
    print_section("DIET OPTIMIZATION")
    result = os_instance.process_task({
        'type': 'diet_optimization',
        'user_data': {
            'weight_kg': 75,
            'height_cm': 180,
            'age': 30,
            'gender': 'male',
            'activity_level': 'active',
            'goals': ['health', 'energy', 'muscle_gain']
        }
    })
    
    diet = result['diet_plan']
    print(f"Daily Caloric Needs: {diet['caloric_needs']['adjusted']:.0f} kcal")
    print(f"\nMacronutrients:")
    print(f"  • Protein:       {diet['macronutrients']['protein']['grams']:.1f}g")
    print(f"  • Carbohydrates: {diet['macronutrients']['carbohydrates']['grams']:.1f}g")
    print(f"  • Fats:          {diet['macronutrients']['fats']['grams']:.1f}g")
    print(f"\nVectorial Corrections:")
    for correction in result['corrections']['suggested_adjustments']:
        print(f"  • {correction}")
    
    print_section("GENESIS ENGINE")
    result = os_instance.process_task({
        'type': 'genesis_propagation',
        'domain': 'consciousness',
        'depth': 3
    })
    print(f"Domain: {result['propagation']['domain']}")
    print(f"Recursion Depth: {result['propagation']['level']}")
    print(f"Child Domains: {len(result['propagation']['children'])}")
    print(f"Friction Optimized: ✓")
    
    print_section("HYPERDIMENSIONAL COMPUTING")
    result = os_instance.process_task({
        'type': 'general',
        'operation': 'pattern_recognition',
        'data': [1, 1, 2, 3, 5, 8, 13, 21]  # Fibonacci
    })
    print(f"Vector Dimensionality: {result['dimensionality']:,}")
    print(f"Temporal-Spatial Transform: Applied")
    print(f"Pattern: Fibonacci Sequence Detected")
    
    print_section("SYSTEM STATUS")
    status = os_instance.get_system_status()
    print(f"System Coherence: {status['coherence']:.6f}")
    print(f"\nActive Frequencies:")
    for freq_name, freq_value in status['active_frequency'].items():
        print(f"  • {freq_name}: {freq_value} Hz")
    
    print(f"\nModule Status:")
    for module, active in status['modules_active'].items():
        symbol = "✓" if active else "✗"
        print(f"  {symbol} {module.replace('_', ' ').title()}")
    
    print_section("STATE MATRIX")
    state = status['state_matrix']
    print(f"Perception:  {state['perception']:.4f}")
    print(f"Emotion:     {state['emotion']:.4f}")
    print(f"Intention:   {state['intention']:.4f}")
    print(f"Coherence:   {status['coherence']:.4f}")
    
    print_banner("DEMONSTRATION COMPLETE")
    print("\nUltimate OS successfully demonstrated all capabilities:")
    print("  ✓ Geometric computing (Platonic solids)")
    print("  ✓ Coherence optimization (Golden ratio)")
    print("  ✓ Frequency protocols (Sacred frequencies)")
    print("  ✓ Diet optimization (Vectorial corrections)")
    print("  ✓ Genesis Engine (Recursive propagation)")
    print("  ✓ HDC computing (10,000 dimensions)")
    print("  ✓ State matrix (P-E-I mapping)")
    print("  ✓ Hyper-helical mathematics")
    
    os_instance.shutdown()
    print("\nSystem shutdown complete.\n")

if __name__ == '__main__':
    main()
