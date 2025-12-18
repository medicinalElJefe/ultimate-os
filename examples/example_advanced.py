"""
Example 2: Advanced Multi-Module Integration
Demonstrates integration of multiple modules for complex tasks
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ultimate_os import UltimateOS
import json


def advanced_integration():
    """Advanced integration example"""
    print("Example 2: Advanced Multi-Module Integration\n")
    
    # Initialize OS with custom config
    config = {
        'hdc_dims': 10000,
        'optimization_level': 'high'
    }
    
    os = UltimateOS(config)
    os.boot()
    
    # 1. Optimize coherence
    print("Step 1: Optimizing system coherence...")
    coherence_result = os.process_task({'type': 'coherence_optimization'})
    print(f"  Coherence improved from {coherence_result['initial_coherence']:.4f} "
          f"to {coherence_result['optimized_coherence']:.4f}")
    
    # 2. Apply frequency modulation
    print("\nStep 2: Applying 528 Hz love frequency...")
    freq_result = os.process_task({
        'type': 'frequency_modulation',
        'frequency_type': 'love',
        'value': 528.0
    })
    print(f"  Frequency modulation complete: {freq_result['state_modulated']}")
    
    # 3. Generate diet plan with optimized coherence
    print("\nStep 3: Generating personalized diet plan...")
    diet_result = os.process_task({
        'type': 'diet_optimization',
        'user_data': {
            'weight_kg': 75,
            'height_cm': 180,
            'age': 35,
            'gender': 'male',
            'activity_level': 'active',
            'goals': ['energy', 'muscle_gain']
        }
    })
    print(f"  Diet plan generated with coherence factor: "
          f"{diet_result['diet_plan']['coherence_factor']:.4f}")
    print(f"  Macronutrient adjustments: {diet_result['corrections']['suggested_adjustments']}")
    
    # 4. Run Genesis Engine propagation
    print("\nStep 4: Running Genesis Engine propagation...")
    genesis_result = os.process_task({
        'type': 'genesis_propagation',
        'domain': 'wellness',
        'depth': 4
    })
    print(f"  Propagated {len(genesis_result['propagation']['children'])} child domains")
    print(f"  Friction optimization applied")
    
    # 5. Compute geometric patterns
    print("\nStep 5: Computing geometric patterns...")
    for geometry in ['tetrahedron', 'icosahedron', 'octahedron']:
        result = os.process_task({
            'type': 'geometric_computation',
            'geometry': geometry
        })
        print(f"  {geometry.capitalize()}: computed successfully")
    
    # Final status
    print("\nFinal System Status:")
    status = os.get_system_status()
    print(json.dumps({
        'coherence': round(status['coherence'], 4),
        'active_modules': sum(status['modules_active'].values()),
        'geometry_mode': status['geometry_mode']
    }, indent=2))
    
    os.shutdown()


if __name__ == '__main__':
    advanced_integration()
