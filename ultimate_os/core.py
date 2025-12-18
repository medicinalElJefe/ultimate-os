"""
Core OS Engine
Integrates all modules into a cohesive operating system
"""

import numpy as np
import logging
from typing import Dict, Any, List, Optional
from .modules import (
    GeometryModule,
    HDCArchitecture,
    CoherentPossibilityCalculator,
    DietCalculator,
    GenesisEngine,
    HyperHelicalSphere,
    StateMatrixHandler,
    FrequencyProtocol
)

logger = logging.getLogger(__name__)


class UltimateOS:
    """
    Main operating system class integrating all advanced computational modules
    """
    
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        """Initialize the Ultimate OS with all modules"""
        self.config = config or {}
        
        # Initialize core modules
        self.geometry = GeometryModule()
        self.hdc = HDCArchitecture(dimensionality=self.config.get('hdc_dims', 10000))
        self.coherence = CoherentPossibilityCalculator()
        self.diet = DietCalculator()
        self.genesis = GenesisEngine()
        self.hyper_helical = HyperHelicalSphere()
        self.state_matrix = StateMatrixHandler()
        self.frequency = FrequencyProtocol()
        
        # System state
        self.system_state = {
            'coherence_level': 0.0,
            'dimensional_state': None,
            'active_frequency': None,
            'geometry_mode': 'tetrahedron'
        }
        
        logger.info("Ultimate OS initialized successfully")
    
    def boot(self) -> Dict[str, Any]:
        """Boot the operating system"""
        logger.info("Booting Ultimate OS...")
        
        # Initialize geometric framework
        self.geometry.initialize_tetrahedron()
        
        # Set baseline frequency
        self.frequency.set_frequency('coherence', 432.0)
        
        # Initialize state matrix
        self.state_matrix.initialize()
        
        # Calculate initial coherence
        coherence = self.coherence.calculate_coherence(
            self.state_matrix.get_current_state()
        )
        self.system_state['coherence_level'] = coherence
        
        logger.info(f"Boot complete. System coherence: {coherence:.4f}")
        return self.system_state
    
    def process_task(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """
        Process a task through the OS modules
        
        Args:
            task: Task specification with type and parameters
            
        Returns:
            Result dictionary with computed values
        """
        task_type = task.get('type', 'general')
        
        if task_type == 'geometric_computation':
            return self._process_geometric(task)
        elif task_type == 'coherence_optimization':
            return self._process_coherence(task)
        elif task_type == 'diet_optimization':
            return self._process_diet(task)
        elif task_type == 'genesis_propagation':
            return self._process_genesis(task)
        elif task_type == 'frequency_modulation':
            return self._process_frequency(task)
        else:
            return self._process_general(task)
    
    def _process_geometric(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process geometric computation tasks"""
        geometry_type = task.get('geometry', 'tetrahedron')
        
        if geometry_type == 'tetrahedron':
            result = self.geometry.compute_tetrahedron_courage_spark()
        elif geometry_type == 'icosahedron':
            result = self.geometry.compute_icosahedron_antenna()
        else:
            result = self.geometry.compute_general_geometry(geometry_type)
        
        return {'status': 'success', 'result': result, 'coherence': self.system_state['coherence_level']}
    
    def _process_coherence(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process coherence optimization"""
        current_state = self.state_matrix.get_current_state()
        coherence = self.coherence.calculate_coherence(current_state)
        
        # Apply coherence optimization
        optimized_state = self.coherence.optimize_coherence(current_state)
        self.state_matrix.update_state(optimized_state)
        
        new_coherence = self.coherence.calculate_coherence(optimized_state)
        self.system_state['coherence_level'] = new_coherence
        
        return {
            'status': 'success',
            'initial_coherence': coherence,
            'optimized_coherence': new_coherence,
            'improvement': new_coherence - coherence
        }
    
    def _process_diet(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process diet optimization with vectorial corrections"""
        user_data = task.get('user_data', {})
        coherence = self.system_state['coherence_level']
        
        diet_plan = self.diet.calculate_optimal_diet(user_data, coherence)
        corrections = self.diet.calculate_vectorial_corrections(diet_plan, coherence)
        
        return {
            'status': 'success',
            'diet_plan': diet_plan,
            'corrections': corrections,
            'aligned_coherence': coherence
        }
    
    def _process_genesis(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process Genesis Engine recursive propagation"""
        domain = task.get('domain', 'default')
        depth = task.get('depth', 3)
        
        propagation_result = self.genesis.recursive_propagate(domain, depth)
        friction_optimized = self.genesis.optimize_friction(propagation_result)
        
        return {
            'status': 'success',
            'propagation': propagation_result,
            'friction_optimized': friction_optimized
        }
    
    def _process_frequency(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process frequency modulation"""
        freq_type = task.get('frequency_type', 'coherence')
        value = task.get('value', None)
        
        if value:
            self.frequency.set_frequency(freq_type, value)
        
        current_freq = self.frequency.get_frequency(freq_type)
        state_modulation = self.frequency.modulate_state(freq_type, self.state_matrix.get_current_state())
        
        self.state_matrix.update_state(state_modulation)
        
        return {
            'status': 'success',
            'frequency_type': freq_type,
            'frequency_value': current_freq,
            'state_modulated': True
        }
    
    def _process_general(self, task: Dict[str, Any]) -> Dict[str, Any]:
        """Process general computation tasks"""
        # Use HDC architecture for general tasks
        task_vector = self.hdc.encode_task(task)
        result = self.hdc.compute(task_vector)
        
        # Apply hyper-helical temporal-spatial interfacing
        temporal_result = self.hyper_helical.temporal_spatial_transform(result)
        
        return {
            'status': 'success',
            'computation': temporal_result,
            'dimensionality': self.hdc.dimensionality
        }
    
    def get_system_status(self) -> Dict[str, Any]:
        """Get current system status"""
        return {
            'coherence': self.system_state['coherence_level'],
            'active_frequency': self.frequency.get_active_frequencies(),
            'state_matrix': self.state_matrix.get_current_state(),
            'geometry_mode': self.system_state['geometry_mode'],
            'modules_active': {
                'geometry': True,
                'hdc': True,
                'coherence': True,
                'diet': True,
                'genesis': True,
                'hyper_helical': True,
                'state_matrix': True,
                'frequency': True
            }
        }
    
    def shutdown(self):
        """Gracefully shutdown the operating system"""
        logger.info("Shutting down Ultimate OS...")
        self.state_matrix.save_state()
        logger.info("Shutdown complete")
