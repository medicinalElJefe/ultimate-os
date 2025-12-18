"""
Hyper-Helical Sphere Mathematics Module
Implements temporal-spatial interfacing and interference management
"""

import numpy as np
from typing import Dict, Any, List, Tuple, Optional


class HyperHelicalSphere:
    """
    Hyper-Helical Sphere mathematics for temporal-spatial transformations
    Implements helical geometry on spherical manifolds for multi-dimensional interfacing
    """
    
    def __init__(self, base_frequency: float = 432.0):
        self.base_frequency = base_frequency
        self.phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        self.temporal_cache = {}
        
    def temporal_spatial_transform(self, data: Any) -> Dict[str, Any]:
        """
        Transform data through temporal-spatial interface
        
        Args:
            data: Input data (vector, scalar, or dict)
            
        Returns:
            Transformed result
        """
        if isinstance(data, dict):
            # Transform dictionary result
            if 'result_vector' in data:
                vector = np.array(data['result_vector'])
                transformed = self._helix_transform(vector)
                data['temporal_transformed'] = transformed.tolist()
            return data
        elif isinstance(data, np.ndarray):
            # Transform vector directly
            transformed = self._helix_transform(data)
            return {'transformed_vector': transformed.tolist()}
        else:
            # Transform scalar
            return {'transformed_value': self._scalar_helix_transform(float(data))}
    
    def _helix_transform(self, vector: np.ndarray) -> np.ndarray:
        """
        Apply helical transformation to vector
        
        Args:
            vector: Input vector
            
        Returns:
            Helically transformed vector
        """
        # Create helical rotation matrix
        t = np.linspace(0, 2*np.pi, len(vector))
        
        # Helical parameters based on golden ratio
        pitch = self.phi
        radius = 1.0
        
        # Transform each component with helical rotation
        transformed = np.zeros_like(vector)
        for i in range(len(vector)):
            angle = t[i]
            helix_factor = np.cos(angle * pitch) + 1j * np.sin(angle * pitch)
            transformed[i] = vector[i] * np.abs(helix_factor)
        
        return transformed
    
    def _scalar_helix_transform(self, value: float) -> float:
        """Transform scalar value through helix"""
        # Apply spiral transformation
        spiral_factor = np.exp(value / self.phi)
        transformed = value * np.cos(spiral_factor) / self.phi
        return float(transformed)
    
    def create_hyper_sphere(self, dimensions: int, radius: float = 1.0) -> np.ndarray:
        """
        Create hypersphere in n-dimensional space
        
        Args:
            dimensions: Number of dimensions
            radius: Sphere radius
            
        Returns:
            Points on hypersphere surface
        """
        # Generate points on n-sphere using normalized Gaussian
        num_points = 100 * dimensions
        points = np.random.randn(num_points, dimensions)
        
        # Normalize to unit sphere
        norms = np.linalg.norm(points, axis=1, keepdims=True)
        points = points / norms * radius
        
        return points
    
    def helical_projection(self, point: np.ndarray, time: float) -> np.ndarray:
        """
        Project point through helical time-space
        
        Args:
            point: Spatial point
            time: Time parameter
            
        Returns:
            Time-evolved point
        """
        # Helical time evolution
        omega = 2 * np.pi * self.base_frequency / 1000.0  # Angular frequency
        
        # Create rotation in time
        theta = omega * time
        
        # Apply helical rotation with pitch
        pitch = self.phi
        z_offset = pitch * theta / (2 * np.pi)
        
        # 3D helical transformation
        if len(point) >= 3:
            rotation_matrix = self._rotation_matrix_3d(theta)
            rotated = rotation_matrix @ point[:3]
            rotated[2] += z_offset
            
            if len(point) > 3:
                result = np.concatenate([rotated, point[3:]])
            else:
                result = rotated
        else:
            # 2D rotation
            rotation_matrix = self._rotation_matrix_2d(theta)
            result = rotation_matrix @ point
        
        return result
    
    def _rotation_matrix_3d(self, theta: float) -> np.ndarray:
        """Create 3D rotation matrix around z-axis"""
        return np.array([
            [np.cos(theta), -np.sin(theta), 0],
            [np.sin(theta), np.cos(theta), 0],
            [0, 0, 1]
        ])
    
    def _rotation_matrix_2d(self, theta: float) -> np.ndarray:
        """Create 2D rotation matrix"""
        return np.array([
            [np.cos(theta), -np.sin(theta)],
            [np.sin(theta), np.cos(theta)]
        ])
    
    def interference_pattern(self, wave_a: np.ndarray, wave_b: np.ndarray) -> Dict[str, Any]:
        """
        Calculate interference pattern between two waves
        
        Args:
            wave_a, wave_b: Wave vectors
            
        Returns:
            Interference pattern analysis
        """
        # Ensure same length
        min_len = min(len(wave_a), len(wave_b))
        wave_a = wave_a[:min_len]
        wave_b = wave_b[:min_len]
        
        # Constructive and destructive interference
        constructive = wave_a + wave_b
        destructive = wave_a - wave_b
        
        # Calculate interference metrics
        coherence = np.abs(np.correlate(wave_a, wave_b, mode='valid')[0]) / (
            np.linalg.norm(wave_a) * np.linalg.norm(wave_b) + 1e-10
        )
        
        # Phase difference
        phase_diff = np.angle(np.sum(wave_a * np.conj(wave_b)))
        
        return {
            'constructive': constructive.tolist(),
            'destructive': destructive.tolist(),
            'coherence': float(coherence),
            'phase_difference': float(phase_diff),
            'interference_type': 'constructive' if phase_diff < np.pi/2 else 'destructive'
        }
    
    def fibonacci_sphere(self, num_points: int) -> np.ndarray:
        """
        Generate points on sphere using Fibonacci spiral
        Provides optimal uniform distribution
        
        Args:
            num_points: Number of points to generate
            
        Returns:
            Points on unit sphere
        """
        points = []
        phi_const = np.pi * (3.0 - np.sqrt(5.0))  # Golden angle
        
        for i in range(num_points):
            y = 1 - (i / float(num_points - 1)) * 2  # y from 1 to -1
            radius = np.sqrt(1 - y * y)  # radius at y
            
            theta = phi_const * i
            
            x = np.cos(theta) * radius
            z = np.sin(theta) * radius
            
            points.append([x, y, z])
        
        return np.array(points)
    
    def toroidal_mapping(self, point: np.ndarray, major_radius: float = 2.0, 
                         minor_radius: float = 1.0) -> np.ndarray:
        """
        Map point to toroidal (donut) geometry
        
        Args:
            point: Input point
            major_radius: Major radius of torus
            minor_radius: Minor radius of torus
            
        Returns:
            Point on torus surface
        """
        # Convert to toroidal coordinates
        if len(point) >= 2:
            theta = np.arctan2(point[1], point[0])
            r = np.linalg.norm(point[:2])
            
            phi = np.arctan2(r - major_radius, point[2] if len(point) > 2 else 0)
            
            # Map to torus
            x = (major_radius + minor_radius * np.cos(phi)) * np.cos(theta)
            y = (major_radius + minor_radius * np.cos(phi)) * np.sin(theta)
            z = minor_radius * np.sin(phi)
            
            return np.array([x, y, z])
        else:
            return point
    
    def calculate_curvature(self, points: np.ndarray) -> Dict[str, Any]:
        """
        Calculate curvature of point set
        
        Args:
            points: Array of points
            
        Returns:
            Curvature metrics
        """
        if len(points) < 3:
            return {'curvature': 0.0, 'type': 'insufficient_points'}
        
        # Calculate discrete curvature using finite differences
        # First derivatives (velocities)
        velocities = np.diff(points, axis=0)
        
        # Second derivatives (accelerations)
        if len(velocities) > 1:
            accelerations = np.diff(velocities, axis=0)
            
            # Curvature magnitude
            v_norms = np.linalg.norm(velocities[:-1], axis=1)
            a_norms = np.linalg.norm(accelerations, axis=1)
            
            # Prevent division by zero
            v_norms = np.maximum(v_norms, 1e-10)
            
            curvatures = a_norms / (v_norms ** 2)
            mean_curvature = np.mean(curvatures)
        else:
            mean_curvature = 0.0
        
        return {
            'mean_curvature': float(mean_curvature),
            'type': 'helical_sphere',
            'smoothness': 1.0 / (1.0 + mean_curvature)
        }
    
    def vortex_field(self, center: np.ndarray, strength: float, 
                     grid_size: int = 10) -> np.ndarray:
        """
        Generate vortex field around center point
        
        Args:
            center: Vortex center
            strength: Vortex strength
            grid_size: Size of field grid
            
        Returns:
            Vector field
        """
        # Create grid
        x = np.linspace(-5, 5, grid_size)
        y = np.linspace(-5, 5, grid_size)
        X, Y = np.meshgrid(x, y)
        
        # Calculate vortex field
        dx = X - center[0]
        dy = Y - center[1]
        
        r = np.sqrt(dx**2 + dy**2) + 1e-10
        
        # Tangential velocity field (circular vortex)
        vx = -strength * dy / r
        vy = strength * dx / r
        
        field = np.stack([vx, vy], axis=-1)
        
        return field
    
    def spiral_energy(self, radius: float, angle: float, pitch: Optional[float] = None) -> float:
        """
        Calculate energy along spiral path
        
        Args:
            radius: Current radius
            angle: Current angle
            pitch: Spiral pitch (default: golden ratio)
            
        Returns:
            Energy value
        """
        if pitch is None:
            pitch = self.phi
        
        # Energy increases with spiral length
        z = pitch * angle / (2 * np.pi)
        spiral_length = np.sqrt(radius**2 + z**2)
        
        # Energy proportional to position along spiral
        energy = spiral_length / self.phi
        
        return float(energy)
