"""
Genesis Engine Module
Implements recursive domain propagation and friction optimization
"""

import numpy as np
from typing import Dict, Any, List, Optional


class GenesisEngine:
    """
    Genesis Engine for recursive domain propagation and friction optimization
    Implements creation, evolution, and optimization of computational domains
    """
    
    def __init__(self):
        self.domain_tree = {}
        self.friction_coefficients = {}
        self.propagation_history = []
        
    def recursive_propagate(self, domain: str, depth: int, parent: Optional[str] = None) -> Dict[str, Any]:
        """
        Recursively propagate a domain through multiple levels
        
        Args:
            domain: Domain identifier
            depth: Recursion depth
            parent: Parent domain (if any)
            
        Returns:
            Propagation result tree
        """
        if depth <= 0:
            return {'domain': domain, 'level': 0, 'children': []}
        
        # Create domain node
        node = {
            'domain': domain,
            'level': depth,
            'parent': parent,
            'children': [],
            'properties': self._calculate_domain_properties(domain, depth)
        }
        
        # Generate child domains
        num_children = min(depth, 3)  # Limit branching
        for i in range(num_children):
            child_domain = f"{domain}_child_{i}"
            child_node = self.recursive_propagate(child_domain, depth - 1, domain)
            node['children'].append(child_node)
        
        # Store in domain tree
        self.domain_tree[domain] = node
        
        # Record propagation
        self.propagation_history.append({
            'domain': domain,
            'depth': depth,
            'timestamp': len(self.propagation_history)
        })
        
        return node
    
    def _calculate_domain_properties(self, domain: str, depth: int) -> Dict[str, Any]:
        """Calculate properties for a domain"""
        # Use domain name to generate consistent properties
        seed = hash(domain) % (2**32)
        np.random.seed(seed)
        
        return {
            'energy': np.random.uniform(0.5, 1.0) * depth / 10.0,
            'coherence': np.random.uniform(0.6, 1.0),
            'stability': 1.0 / (1.0 + depth * 0.1),
            'frequency': 432.0 + np.random.normal(0, 50),
            'dimension': depth
        }
    
    def optimize_friction(self, propagation_tree: Dict[str, Any]) -> Dict[str, Any]:
        """
        Optimize friction in propagation tree
        Reduces resistance in domain transitions
        
        Args:
            propagation_tree: Tree from recursive_propagate
            
        Returns:
            Friction-optimized tree
        """
        optimized_tree = propagation_tree.copy()
        
        # Calculate friction at this node
        domain = propagation_tree['domain']
        level = propagation_tree['level']
        
        # Friction decreases with optimization
        base_friction = 1.0 / (1.0 + level)
        
        # Apply golden ratio optimization
        phi = (1 + np.sqrt(5)) / 2
        optimized_friction = base_friction / phi
        
        self.friction_coefficients[domain] = optimized_friction
        
        optimized_tree['friction'] = optimized_friction
        optimized_tree['friction_optimized'] = True
        
        # Recursively optimize children
        if 'children' in propagation_tree and propagation_tree['children']:
            optimized_children = []
            for child in propagation_tree['children']:
                optimized_child = self.optimize_friction(child)
                optimized_children.append(optimized_child)
            optimized_tree['children'] = optimized_children
        
        return optimized_tree
    
    def calculate_domain_coherence(self, domain_tree: Dict[str, Any]) -> float:
        """
        Calculate overall coherence of domain tree
        
        Args:
            domain_tree: Domain tree structure
            
        Returns:
            Coherence score
        """
        if not domain_tree:
            return 0.0
        
        # Get properties
        props = domain_tree.get('properties', {})
        node_coherence = props.get('coherence', 0.5)
        
        # Factor in friction
        friction = domain_tree.get('friction', 1.0)
        friction_factor = 1.0 - friction * 0.2
        
        # Calculate children coherence
        children = domain_tree.get('children', [])
        if children:
            child_coherences = [self.calculate_domain_coherence(child) for child in children]
            child_avg = np.mean(child_coherences)
            # Weighted average with children
            total_coherence = 0.6 * node_coherence + 0.4 * child_avg
        else:
            total_coherence = node_coherence
        
        # Apply friction factor
        total_coherence *= friction_factor
        
        return float(total_coherence)
    
    def merge_domains(self, domain_a: str, domain_b: str) -> Dict[str, Any]:
        """
        Merge two domains into a unified domain
        
        Args:
            domain_a, domain_b: Domains to merge
            
        Returns:
            Merged domain
        """
        merged_name = f"{domain_a}+{domain_b}"
        
        # Get properties of both domains
        props_a = self.domain_tree.get(domain_a, {}).get('properties', {})
        props_b = self.domain_tree.get(domain_b, {}).get('properties', {})
        
        # Merge properties (average values)
        merged_props = {}
        all_keys = set(props_a.keys()) | set(props_b.keys())
        
        for key in all_keys:
            val_a = props_a.get(key, 0)
            val_b = props_b.get(key, 0)
            merged_props[key] = (val_a + val_b) / 2.0
        
        # Merged domain has higher coherence due to integration
        merged_props['coherence'] = min(1.0, merged_props.get('coherence', 0.5) * 1.2)
        
        merged_domain = {
            'domain': merged_name,
            'level': max(
                self.domain_tree.get(domain_a, {}).get('level', 0),
                self.domain_tree.get(domain_b, {}).get('level', 0)
            ),
            'properties': merged_props,
            'merged_from': [domain_a, domain_b],
            'children': []
        }
        
        self.domain_tree[merged_name] = merged_domain
        
        return merged_domain
    
    def evolve_domain(self, domain: str, generations: int = 10) -> Dict[str, Any]:
        """
        Evolve a domain over multiple generations
        
        Args:
            domain: Domain to evolve
            generations: Number of evolution cycles
            
        Returns:
            Evolution history
        """
        if domain not in self.domain_tree:
            return {'error': 'Domain not found'}
        
        evolution_history = []
        current_props = self.domain_tree[domain]['properties'].copy()
        
        for gen in range(generations):
            # Evolution improves properties over time
            improvement_rate = 0.05
            
            for key in current_props:
                if isinstance(current_props[key], (int, float)):
                    # Positive evolution with diminishing returns
                    current_val = current_props[key]
                    target = 1.0
                    current_props[key] = current_val + improvement_rate * (target - current_val)
            
            evolution_history.append({
                'generation': gen,
                'properties': current_props.copy(),
                'fitness': current_props.get('coherence', 0.5) * current_props.get('stability', 0.5)
            })
        
        # Update domain with evolved properties
        self.domain_tree[domain]['properties'] = current_props
        self.domain_tree[domain]['evolved'] = True
        self.domain_tree[domain]['generations'] = generations
        
        return {
            'domain': domain,
            'generations': generations,
            'history': evolution_history,
            'final_properties': current_props
        }
    
    def create_genesis_point(self, name: str, initial_energy: float = 1.0) -> Dict[str, Any]:
        """
        Create a genesis point - the origin of a new domain
        
        Args:
            name: Name of genesis point
            initial_energy: Starting energy level
            
        Returns:
            Genesis point specification
        """
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        
        genesis = {
            'name': name,
            'type': 'genesis_point',
            'initial_energy': initial_energy,
            'properties': {
                'energy': initial_energy,
                'coherence': 1.0,  # Perfect coherence at origin
                'stability': 1.0,
                'frequency': 432.0,  # Universal frequency
                'dimension': 0,  # Origin point
                'expansion_rate': 1.0 / phi  # Golden ratio expansion
            },
            'created': True
        }
        
        self.domain_tree[name] = genesis
        
        return genesis
    
    def calculate_friction_gradient(self, domain_tree: Dict[str, Any]) -> List[float]:
        """
        Calculate friction gradient across domain tree
        
        Args:
            domain_tree: Domain tree
            
        Returns:
            List of friction values at each level
        """
        gradient = []
        
        def traverse(node, gradient_list):
            if 'friction' in node:
                gradient_list.append(node['friction'])
            
            for child in node.get('children', []):
                traverse(child, gradient_list)
        
        traverse(domain_tree, gradient)
        
        return gradient
    
    def get_propagation_statistics(self) -> Dict[str, Any]:
        """Get statistics about propagation history"""
        if not self.propagation_history:
            return {'message': 'No propagation history'}
        
        total_domains = len(self.domain_tree)
        avg_friction = np.mean(list(self.friction_coefficients.values())) if self.friction_coefficients else 0.0
        
        return {
            'total_domains': total_domains,
            'propagation_events': len(self.propagation_history),
            'average_friction': float(avg_friction),
            'friction_optimized_domains': len(self.friction_coefficients),
            'domain_types': list(self.domain_tree.keys())[:10]  # First 10
        }
