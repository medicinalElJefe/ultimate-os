"""
Test Suite for Ultimate OS
Tests all modules and integration
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import unittest
import numpy as np
from ultimate_os import UltimateOS
from ultimate_os.modules import (
    GeometryModule,
    HDCArchitecture,
    CoherentPossibilityCalculator,
    DietCalculator,
    GenesisEngine,
    HyperHelicalSphere,
    StateMatrixHandler,
    FrequencyProtocol
)


class TestGeometryModule(unittest.TestCase):
    """Test Geometry Module"""
    
    def setUp(self):
        self.geometry = GeometryModule()
    
    def test_tetrahedron_initialization(self):
        """Test tetrahedron initialization"""
        result = self.geometry.initialize_tetrahedron()
        self.assertEqual(result['vertices'], 4)
        self.assertEqual(result['edges'], 6)
        self.assertEqual(result['faces'], 4)
    
    def test_icosahedron_initialization(self):
        """Test icosahedron initialization"""
        result = self.geometry.initialize_icosahedron()
        self.assertEqual(result['vertices'], 12)
        self.assertEqual(result['edges'], 30)
        self.assertEqual(result['faces'], 20)
    
    def test_courage_spark(self):
        """Test courage spark computation"""
        result = self.geometry.compute_tetrahedron_courage_spark()
        self.assertIn('spark_intensity', result)
        self.assertIn('resonance_frequency', result)
        self.assertEqual(result['geometric_stability'], 1.0)
    
    def test_icosahedron_antenna(self):
        """Test icosahedron antenna effect"""
        result = self.geometry.compute_icosahedron_antenna()
        self.assertIn('reception_strength', result)
        self.assertIn('antenna_gain', result)
        self.assertEqual(result['coverage'], 'omnidirectional')


class TestHDCArchitecture(unittest.TestCase):
    """Test HDC Architecture"""
    
    def setUp(self):
        self.hdc = HDCArchitecture(dimensionality=1000)
    
    def test_encode_item(self):
        """Test item encoding"""
        vector = self.hdc.encode_item("test_item")
        self.assertEqual(len(vector), 1000)
        self.assertTrue(np.all((vector == 1) | (vector == -1)))
    
    def test_bind(self):
        """Test vector binding"""
        v1 = self.hdc.encode_item("item1")
        v2 = self.hdc.encode_item("item2")
        bound = self.hdc.bind(v1, v2)
        self.assertEqual(len(bound), 1000)
    
    def test_bundle(self):
        """Test vector bundling"""
        vectors = [
            self.hdc.encode_item("item1"),
            self.hdc.encode_item("item2"),
            self.hdc.encode_item("item3")
        ]
        bundled = self.hdc.bundle(vectors)
        self.assertEqual(len(bundled), 1000)
    
    def test_similarity(self):
        """Test similarity calculation"""
        v1 = self.hdc.encode_item("test")
        v2 = self.hdc.encode_item("test")  # Same item
        v3 = self.hdc.encode_item("different")
        
        sim_same = self.hdc.similarity(v1, v2)
        sim_diff = self.hdc.similarity(v1, v3)
        
        self.assertEqual(sim_same, 1.0)  # Same item should be identical
        self.assertLess(abs(sim_diff), 1.0)  # Different items should differ


class TestCoherentPossibilityCalculator(unittest.TestCase):
    """Test Coherent Possibility Calculator"""
    
    def setUp(self):
        self.calc = CoherentPossibilityCalculator()
    
    def test_calculate_coherence(self):
        """Test coherence calculation"""
        state = {
            'perception': 0.5,
            'emotion': 0.5,
            'intention': 0.5
        }
        coherence = self.calc.calculate_coherence(state)
        self.assertGreaterEqual(coherence, 0.0)
        self.assertLessEqual(coherence, 1.0)
    
    def test_optimize_coherence(self):
        """Test coherence optimization"""
        state = {
            'perception': 0.3,
            'emotion': 0.8,
            'intention': 0.4
        }
        optimized = self.calc.optimize_coherence(state)
        self.assertIn('perception', optimized)
        self.assertIn('emotion', optimized)
        self.assertIn('intention', optimized)
        self.assertTrue(optimized['coherence_optimized'])
    
    def test_quantum_superposition(self):
        """Test quantum superposition"""
        states = [
            {'perception': 0.5, 'emotion': 0.5, 'intention': 0.5},
            {'perception': 0.7, 'emotion': 0.6, 'intention': 0.8}
        ]
        superposed = self.calc.quantum_superposition(states)
        self.assertTrue(superposed['superposition'])
        self.assertEqual(superposed['state_count'], 2)


class TestDietCalculator(unittest.TestCase):
    """Test Diet Calculator"""
    
    def setUp(self):
        self.diet = DietCalculator()
    
    def test_calculate_optimal_diet(self):
        """Test diet calculation"""
        user_data = {
            'weight_kg': 70,
            'height_cm': 175,
            'age': 30,
            'gender': 'male',
            'activity_level': 'moderate'
        }
        result = self.diet.calculate_optimal_diet(user_data, 0.8)
        self.assertIn('caloric_needs', result)
        self.assertIn('macronutrients', result)
        self.assertIn('meal_plan', result)
    
    def test_vectorial_corrections(self):
        """Test vectorial corrections"""
        diet_plan = {
            'macronutrients': {
                'protein': {'ratio': 0.25},
                'carbohydrates': {'ratio': 0.45},
                'fats': {'ratio': 0.30}
            }
        }
        corrections = self.diet.calculate_vectorial_corrections(diet_plan, 0.8)
        self.assertIn('correction_vector', corrections)
        self.assertIn('suggested_adjustments', corrections)


class TestGenesisEngine(unittest.TestCase):
    """Test Genesis Engine"""
    
    def setUp(self):
        self.genesis = GenesisEngine()
    
    def test_recursive_propagate(self):
        """Test recursive propagation"""
        result = self.genesis.recursive_propagate('test_domain', 2)
        self.assertEqual(result['domain'], 'test_domain')
        self.assertEqual(result['level'], 2)
        self.assertIsInstance(result['children'], list)
    
    def test_optimize_friction(self):
        """Test friction optimization"""
        tree = self.genesis.recursive_propagate('domain', 2)
        optimized = self.genesis.optimize_friction(tree)
        self.assertIn('friction', optimized)
        self.assertTrue(optimized['friction_optimized'])
    
    def test_create_genesis_point(self):
        """Test genesis point creation"""
        genesis = self.genesis.create_genesis_point('origin', 1.0)
        self.assertEqual(genesis['name'], 'origin')
        self.assertEqual(genesis['type'], 'genesis_point')
        self.assertTrue(genesis['created'])


class TestHyperHelicalSphere(unittest.TestCase):
    """Test Hyper-Helical Sphere"""
    
    def setUp(self):
        self.sphere = HyperHelicalSphere()
    
    def test_temporal_spatial_transform(self):
        """Test temporal-spatial transformation"""
        data = np.array([1, 2, 3, 4, 5])
        result = self.sphere.temporal_spatial_transform(data)
        self.assertIn('transformed_vector', result)
    
    def test_fibonacci_sphere(self):
        """Test Fibonacci sphere generation"""
        points = self.sphere.fibonacci_sphere(100)
        self.assertEqual(len(points), 100)
        self.assertEqual(points.shape[1], 3)
    
    def test_interference_pattern(self):
        """Test interference pattern calculation"""
        wave_a = np.array([1, 2, 3, 4, 5])
        wave_b = np.array([2, 3, 4, 5, 6])
        result = self.sphere.interference_pattern(wave_a, wave_b)
        self.assertIn('coherence', result)
        self.assertIn('phase_difference', result)


class TestStateMatrixHandler(unittest.TestCase):
    """Test State Matrix Handler"""
    
    def setUp(self):
        self.handler = StateMatrixHandler()
    
    def test_initialize(self):
        """Test initialization"""
        result = self.handler.initialize()
        self.assertIn('perception', result)
        self.assertIn('emotion', result)
        self.assertIn('intention', result)
    
    def test_map_perception(self):
        """Test perception mapping"""
        sensory = {
            'visual': 0.7,
            'auditory': 0.6,
            'tactile': 0.5
        }
        result = self.handler.map_perception(sensory)
        self.assertIn('filtered_perception', result)
    
    def test_evolve_state(self):
        """Test state evolution"""
        self.handler.initialize()
        evolved = self.handler.evolve_state(steps=3)
        self.assertTrue(evolved['evolved'])
        self.assertEqual(evolved['evolution_steps'], 3)
    
    def test_calculate_coherence(self):
        """Test coherence calculation"""
        self.handler.initialize()
        coherence = self.handler.calculate_state_coherence()
        self.assertGreaterEqual(coherence, 0.0)
        self.assertLessEqual(coherence, 1.0)


class TestFrequencyProtocol(unittest.TestCase):
    """Test Frequency Protocol"""
    
    def setUp(self):
        self.protocol = FrequencyProtocol()
    
    def test_set_frequency(self):
        """Test frequency setting"""
        self.protocol.set_frequency('coherence', 432.0)
        freq = self.protocol.get_frequency('coherence')
        self.assertEqual(freq, 432.0)
    
    def test_modulate_state(self):
        """Test state modulation"""
        state = {
            'perception': 0.5,
            'emotion': 0.5,
            'intention': 0.5
        }
        modulated = self.protocol.modulate_state('love', state)
        self.assertIn('frequency_applied', modulated)
        self.assertEqual(modulated['frequency_hz'], 528.0)
    
    def test_create_binaural_beat(self):
        """Test binaural beat creation"""
        result = self.protocol.create_binaural_beat(432.0, 7.83)
        self.assertEqual(result['base_frequency'], 432.0)
        self.assertEqual(result['beat_frequency'], 7.83)
        self.assertIn('brainwave_state', result)


class TestUltimateOS(unittest.TestCase):
    """Test Ultimate OS Integration"""
    
    def setUp(self):
        self.os = UltimateOS()
    
    def test_boot(self):
        """Test OS boot"""
        result = self.os.boot()
        self.assertIn('coherence_level', result)
        self.assertIn('geometry_mode', result)
    
    def test_geometric_task(self):
        """Test geometric computation task"""
        task = {
            'type': 'geometric_computation',
            'geometry': 'tetrahedron'
        }
        result = self.os.process_task(task)
        self.assertEqual(result['status'], 'success')
        self.assertIn('result', result)
    
    def test_coherence_task(self):
        """Test coherence optimization task"""
        self.os.boot()
        task = {'type': 'coherence_optimization'}
        result = self.os.process_task(task)
        self.assertEqual(result['status'], 'success')
        self.assertIn('initial_coherence', result)
        self.assertIn('optimized_coherence', result)
    
    def test_diet_task(self):
        """Test diet optimization task"""
        self.os.boot()
        task = {
            'type': 'diet_optimization',
            'user_data': {
                'weight_kg': 70,
                'height_cm': 175,
                'age': 30,
                'gender': 'male',
                'activity_level': 'moderate'
            }
        }
        result = self.os.process_task(task)
        self.assertEqual(result['status'], 'success')
        self.assertIn('diet_plan', result)
    
    def test_genesis_task(self):
        """Test Genesis Engine task"""
        self.os.boot()
        task = {
            'type': 'genesis_propagation',
            'domain': 'test',
            'depth': 2
        }
        result = self.os.process_task(task)
        self.assertEqual(result['status'], 'success')
        self.assertIn('propagation', result)
    
    def test_frequency_task(self):
        """Test frequency modulation task"""
        self.os.boot()
        task = {
            'type': 'frequency_modulation',
            'frequency_type': 'love',
            'value': 528.0
        }
        result = self.os.process_task(task)
        self.assertEqual(result['status'], 'success')
        self.assertTrue(result['state_modulated'])
    
    def test_system_status(self):
        """Test system status"""
        self.os.boot()
        status = self.os.get_system_status()
        self.assertIn('coherence', status)
        self.assertIn('modules_active', status)
        self.assertTrue(all(status['modules_active'].values()))


def run_tests():
    """Run all tests"""
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestGeometryModule))
    suite.addTests(loader.loadTestsFromTestCase(TestHDCArchitecture))
    suite.addTests(loader.loadTestsFromTestCase(TestCoherentPossibilityCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestDietCalculator))
    suite.addTests(loader.loadTestsFromTestCase(TestGenesisEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestHyperHelicalSphere))
    suite.addTests(loader.loadTestsFromTestCase(TestStateMatrixHandler))
    suite.addTests(loader.loadTestsFromTestCase(TestFrequencyProtocol))
    suite.addTests(loader.loadTestsFromTestCase(TestUltimateOS))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    return result


if __name__ == '__main__':
    result = run_tests()
    sys.exit(0 if result.wasSuccessful() else 1)
