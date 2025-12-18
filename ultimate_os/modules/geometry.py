"""
Geometric Framework Module
Implements geometric computation based on platonic solids and sacred geometry
"""

import numpy as np
from typing import Dict, Any, List, Tuple


class GeometryModule:
    """
    Handles geometric computations using platonic solids
    - Tetrahedron: Courage sparks, foundational stability
    - Icosahedron: Antenna effects, reception and transmission
    - Octahedron: Balance and equilibrium
    - Dodecahedron: Universal connection
    - Cube: Material manifestation
    """
    
    def __init__(self):
        self.active_geometry = None
        self.vertices = {}
        self.edges = {}
        self.faces = {}
        
    def initialize_tetrahedron(self) -> Dict[str, Any]:
        """Initialize tetrahedron geometry for courage spark generation"""
        # Tetrahedron vertices (4 points forming a pyramid)
        self.vertices['tetrahedron'] = np.array([
            [1, 1, 1],
            [1, -1, -1],
            [-1, 1, -1],
            [-1, -1, 1]
        ], dtype=float)
        
        # Normalize to unit sphere
        self.vertices['tetrahedron'] /= np.linalg.norm(self.vertices['tetrahedron'][0])
        
        self.active_geometry = 'tetrahedron'
        return {'geometry': 'tetrahedron', 'vertices': 4, 'edges': 6, 'faces': 4}
    
    def initialize_icosahedron(self) -> Dict[str, Any]:
        """Initialize icosahedron geometry for antenna effects"""
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        # Icosahedron vertices (12 points)
        self.vertices['icosahedron'] = np.array([
            [0, 1, phi],
            [0, 1, -phi],
            [0, -1, phi],
            [0, -1, -phi],
            [1, phi, 0],
            [1, -phi, 0],
            [-1, phi, 0],
            [-1, -phi, 0],
            [phi, 0, 1],
            [phi, 0, -1],
            [-phi, 0, 1],
            [-phi, 0, -1]
        ], dtype=float)
        
        # Normalize
        for i in range(len(self.vertices['icosahedron'])):
            self.vertices['icosahedron'][i] /= np.linalg.norm(self.vertices['icosahedron'][i])
        
        self.active_geometry = 'icosahedron'
        return {'geometry': 'icosahedron', 'vertices': 12, 'edges': 30, 'faces': 20}
    
    def compute_tetrahedron_courage_spark(self) -> Dict[str, Any]:
        """
        Compute courage spark using tetrahedron geometry
        Represents foundational courage and willpower activation
        """
        if 'tetrahedron' not in self.vertices:
            self.initialize_tetrahedron()
        
        vertices = self.vertices['tetrahedron']
        
        # Calculate centroid (center of mass)
        centroid = np.mean(vertices, axis=0)
        
        # Calculate outward vectors from centroid
        courage_vectors = vertices - centroid
        
        # Compute spark intensity (magnitude of expansion)
        spark_intensity = np.linalg.norm(courage_vectors, axis=1).mean()
        
        # Calculate resonance frequency (based on geometry)
        resonance = 396.0  # Root chakra frequency Hz
        
        return {
            'spark_intensity': float(spark_intensity),
            'centroid': centroid.tolist(),
            'courage_vectors': courage_vectors.tolist(),
            'resonance_frequency': resonance,
            'geometric_stability': 1.0  # Tetrahedron is most stable
        }
    
    def compute_icosahedron_antenna(self) -> Dict[str, Any]:
        """
        Compute icosahedron antenna effects
        Represents reception and transmission capabilities
        """
        if 'icosahedron' not in self.vertices:
            self.initialize_icosahedron()
        
        vertices = self.vertices['icosahedron']
        
        # Calculate spherical harmonic properties
        reception_strength = np.std(vertices)  # Variance indicates reception diversity
        
        # Calculate transmission vectors (from center to vertices)
        transmission_vectors = vertices / np.linalg.norm(vertices, axis=1, keepdims=True)
        
        # Antenna gain (based on surface area)
        phi = (1 + np.sqrt(5)) / 2
        edge_length = 2 / np.sqrt(phi * np.sqrt(5))
        surface_area = 5 * np.sqrt(3) * edge_length**2
        
        return {
            'reception_strength': float(reception_strength),
            'transmission_vectors': transmission_vectors.tolist(),
            'antenna_gain': float(surface_area),
            'resonance_frequency': 528.0,  # Love/DNA repair frequency Hz
            'vertex_count': 12,
            'coverage': 'omnidirectional'
        }
    
    def compute_general_geometry(self, geometry_type: str) -> Dict[str, Any]:
        """Compute general geometric properties"""
        if geometry_type == 'octahedron':
            return self._compute_octahedron()
        elif geometry_type == 'dodecahedron':
            return self._compute_dodecahedron()
        elif geometry_type == 'cube':
            return self._compute_cube()
        else:
            return {'error': f'Unknown geometry type: {geometry_type}'}
    
    def _compute_octahedron(self) -> Dict[str, Any]:
        """Octahedron: Balance and equilibrium"""
        vertices = np.array([
            [1, 0, 0], [-1, 0, 0],
            [0, 1, 0], [0, -1, 0],
            [0, 0, 1], [0, 0, -1]
        ], dtype=float)
        
        return {
            'geometry': 'octahedron',
            'balance_coefficient': 1.0,
            'vertices': vertices.tolist(),
            'property': 'equilibrium'
        }
    
    def _compute_dodecahedron(self) -> Dict[str, Any]:
        """Dodecahedron: Universal connection"""
        phi = (1 + np.sqrt(5)) / 2
        
        vertices = []
        # Add cube vertices
        for i in [-1, 1]:
            for j in [-1, 1]:
                for k in [-1, 1]:
                    vertices.append([i, j, k])
        
        # Add rectangular face vertices
        for i in [0]:
            for j in [-1/phi, 1/phi]:
                for k in [-phi, phi]:
                    vertices.append([i, j, k])
                    vertices.append([j, k, i])
                    vertices.append([k, i, j])
        
        vertices = np.array(vertices, dtype=float)
        
        return {
            'geometry': 'dodecahedron',
            'connection_strength': phi,
            'vertices': vertices.tolist(),
            'property': 'universal_connection'
        }
    
    def _compute_cube(self) -> Dict[str, Any]:
        """Cube: Material manifestation"""
        vertices = np.array([
            [1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
            [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]
        ], dtype=float)
        
        return {
            'geometry': 'cube',
            'manifestation_strength': 1.0,
            'vertices': vertices.tolist(),
            'property': 'material_stability'
        }
    
    def get_geometric_coherence(self) -> float:
        """Calculate coherence based on active geometry"""
        if self.active_geometry is None:
            return 0.0
        
        vertices = self.vertices.get(self.active_geometry, np.array([]))
        if len(vertices) == 0:
            return 0.0
        
        # Coherence is based on how uniformly distributed vertices are
        centroid = np.mean(vertices, axis=0)
        distances = np.linalg.norm(vertices - centroid, axis=1)
        coherence = 1.0 - (np.std(distances) / (np.mean(distances) + 1e-10))
        
        return float(coherence)
