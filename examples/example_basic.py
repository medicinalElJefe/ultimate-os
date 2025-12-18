"""
Example 1: Basic OS Usage
Demonstrates basic initialization and task processing
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ultimate_os import UltimateOS


def basic_usage():
    """Basic usage example"""
    print("Example 1: Basic OS Usage\n")
    
    # Create and boot OS
    os = UltimateOS()
    os.boot()
    
    # Process a simple task
    task = {
        'type': 'geometric_computation',
        'geometry': 'tetrahedron'
    }
    
    result = os.process_task(task)
    print(f"Result: {result}")
    
    # Get system status
    status = os.get_system_status()
    print(f"\nSystem Coherence: {status['coherence']:.4f}")
    
    os.shutdown()


if __name__ == '__main__':
    basic_usage()
