"""
Diet Calculator Module
Calculates optimal diet with vectorial corrections aligned to coherence
"""

import numpy as np
from typing import Dict, Any, List, Tuple


class DietCalculator:
    """
    Calculates optimal diet plans with vectorial corrections
    based on coherence metrics and user data
    """
    
    def __init__(self):
        self.nutrient_database = self._initialize_nutrients()
        self.frequency_map = self._initialize_frequency_map()
        
    def _initialize_nutrients(self) -> Dict[str, Dict[str, Any]]:
        """Initialize nutrient database with vibrational properties"""
        return {
            'protein': {
                'frequency': 432.0,
                'coherence_factor': 0.8,
                'recommended_ratio': 0.25,
                'vector': np.array([1, 0, 0])
            },
            'carbohydrates': {
                'frequency': 528.0,
                'coherence_factor': 0.7,
                'recommended_ratio': 0.45,
                'vector': np.array([0, 1, 0])
            },
            'fats': {
                'frequency': 396.0,
                'coherence_factor': 0.75,
                'recommended_ratio': 0.30,
                'vector': np.array([0, 0, 1])
            },
            'vitamins': {
                'frequency': 741.0,
                'coherence_factor': 0.9,
                'recommended_ratio': 0.05,
                'vector': np.array([1, 1, 0])
            },
            'minerals': {
                'frequency': 639.0,
                'coherence_factor': 0.85,
                'recommended_ratio': 0.05,
                'vector': np.array([0, 1, 1])
            },
            'water': {
                'frequency': 528.0,
                'coherence_factor': 1.0,
                'recommended_ratio': 0.60,
                'vector': np.array([1, 1, 1])
            }
        }
    
    def _initialize_frequency_map(self) -> Dict[str, float]:
        """Map food types to frequencies"""
        return {
            'raw_vegetables': 528.0,  # Life force frequency
            'fruits': 528.0,
            'whole_grains': 432.0,
            'legumes': 396.0,
            'nuts_seeds': 639.0,
            'lean_proteins': 432.0,
            'fermented_foods': 741.0,
            'herbs_spices': 852.0,
            'processed_foods': 174.0,  # Low frequency
            'refined_sugar': 174.0
        }
    
    def calculate_optimal_diet(self, user_data: Dict[str, Any], coherence: float) -> Dict[str, Any]:
        """
        Calculate optimal diet plan for user
        
        Args:
            user_data: User information (age, weight, activity, etc.)
            coherence: Current coherence level
            
        Returns:
            Optimal diet plan
        """
        # Extract user parameters
        weight_kg = user_data.get('weight_kg', 70)
        activity_level = user_data.get('activity_level', 'moderate')
        goals = user_data.get('goals', ['health', 'energy'])
        
        # Calculate base caloric needs
        bmr = self._calculate_bmr(user_data)
        
        # Activity multipliers
        activity_multipliers = {
            'sedentary': 1.2,
            'light': 1.375,
            'moderate': 1.55,
            'active': 1.725,
            'very_active': 1.9
        }
        
        tdee = bmr * activity_multipliers.get(activity_level, 1.55)
        
        # Adjust based on coherence (higher coherence = better nutrient absorption)
        absorption_efficiency = 0.7 + 0.3 * coherence
        effective_calories = tdee / absorption_efficiency
        
        # Calculate macronutrient distribution
        macros = self._calculate_macros(effective_calories, coherence, goals)
        
        # Generate meal plan
        meal_plan = self._generate_meal_plan(macros, coherence)
        
        return {
            'caloric_needs': {
                'bmr': bmr,
                'tdee': tdee,
                'adjusted': effective_calories
            },
            'macronutrients': macros,
            'meal_plan': meal_plan,
            'coherence_factor': absorption_efficiency,
            'recommendations': self._generate_recommendations(coherence)
        }
    
    def _calculate_bmr(self, user_data: Dict[str, Any]) -> float:
        """Calculate Basal Metabolic Rate"""
        weight_kg = user_data.get('weight_kg', 70)
        height_cm = user_data.get('height_cm', 170)
        age = user_data.get('age', 30)
        gender = user_data.get('gender', 'male')
        
        # Mifflin-St Jeor Equation
        if gender == 'male':
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
        
        return bmr
    
    def _calculate_macros(self, calories: float, coherence: float, goals: List[str]) -> Dict[str, Any]:
        """Calculate macronutrient distribution"""
        # Base ratios from nutrient database
        base_protein_ratio = 0.25
        base_carb_ratio = 0.45
        base_fat_ratio = 0.30
        
        # Adjust based on goals
        if 'muscle_gain' in goals:
            base_protein_ratio += 0.05
            base_carb_ratio -= 0.05
        elif 'weight_loss' in goals:
            base_fat_ratio -= 0.05
            base_carb_ratio -= 0.05
            base_protein_ratio += 0.10
        
        # Coherence optimization (higher coherence = better balance)
        phi = (1 + np.sqrt(5)) / 2  # Golden ratio
        coherence_factor = 0.1 * coherence
        
        protein_ratio = base_protein_ratio + coherence_factor * (1/phi - base_protein_ratio)
        carb_ratio = base_carb_ratio + coherence_factor * (1/phi - base_carb_ratio)
        fat_ratio = 1.0 - protein_ratio - carb_ratio
        
        return {
            'protein': {
                'ratio': protein_ratio,
                'calories': calories * protein_ratio,
                'grams': (calories * protein_ratio) / 4.0
            },
            'carbohydrates': {
                'ratio': carb_ratio,
                'calories': calories * carb_ratio,
                'grams': (calories * carb_ratio) / 4.0
            },
            'fats': {
                'ratio': fat_ratio,
                'calories': calories * fat_ratio,
                'grams': (calories * fat_ratio) / 9.0
            }
        }
    
    def _generate_meal_plan(self, macros: Dict[str, Any], coherence: float) -> List[Dict[str, Any]]:
        """Generate sample meal plan"""
        meals = []
        
        # Breakfast
        meals.append({
            'name': 'Breakfast',
            'foods': ['oatmeal', 'berries', 'nuts', 'green_tea'],
            'frequency': 528.0,
            'coherence_boost': 0.1 * coherence
        })
        
        # Lunch
        meals.append({
            'name': 'Lunch',
            'foods': ['quinoa', 'vegetables', 'legumes', 'olive_oil'],
            'frequency': 432.0,
            'coherence_boost': 0.15 * coherence
        })
        
        # Dinner
        meals.append({
            'name': 'Dinner',
            'foods': ['lean_protein', 'sweet_potato', 'greens', 'herbs'],
            'frequency': 639.0,
            'coherence_boost': 0.12 * coherence
        })
        
        return meals
    
    def _generate_recommendations(self, coherence: float) -> List[str]:
        """Generate dietary recommendations based on coherence"""
        recommendations = [
            "Hydrate with structured water at 528 Hz",
            "Consume raw, living foods for maximum life force",
            "Practice mindful eating to increase absorption"
        ]
        
        if coherence < 0.5:
            recommendations.append("Increase fresh, organic vegetables")
            recommendations.append("Reduce processed foods and refined sugars")
            recommendations.append("Consider intermittent fasting for cellular reset")
        elif coherence > 0.8:
            recommendations.append("Maintain current high-vibrational diet")
            recommendations.append("Experiment with superfoods and adaptogens")
        
        return recommendations
    
    def calculate_vectorial_corrections(self, diet_plan: Dict[str, Any], coherence: float) -> Dict[str, Any]:
        """
        Calculate vectorial corrections to align diet with coherence
        
        Args:
            diet_plan: Current diet plan
            coherence: System coherence level
            
        Returns:
            Vectorial corrections
        """
        # Current diet vector (macronutrient distribution)
        macros = diet_plan.get('macronutrients', {})
        
        protein_ratio = macros.get('protein', {}).get('ratio', 0.25)
        carb_ratio = macros.get('carbohydrates', {}).get('ratio', 0.45)
        fat_ratio = macros.get('fats', {}).get('ratio', 0.30)
        
        current_vector = np.array([protein_ratio, carb_ratio, fat_ratio])
        
        # Optimal vector based on coherence and golden ratio
        phi = (1 + np.sqrt(5)) / 2
        optimal_ratio = 1.0 / phi
        
        # Calculate ideal distribution
        ideal_vector = np.array([
            optimal_ratio * 0.8,
            optimal_ratio * 1.2,
            optimal_ratio * 1.0
        ])
        ideal_vector /= ideal_vector.sum()  # Normalize
        
        # Calculate correction vector
        correction_vector = ideal_vector - current_vector
        
        # Scale correction by coherence (higher coherence = smaller corrections needed)
        correction_magnitude = np.linalg.norm(correction_vector)
        scaled_correction = correction_vector * (1.0 - coherence) * 0.5
        
        return {
            'current_vector': current_vector.tolist(),
            'ideal_vector': ideal_vector.tolist(),
            'correction_vector': scaled_correction.tolist(),
            'correction_magnitude': float(correction_magnitude),
            'suggested_adjustments': self._interpret_corrections(scaled_correction)
        }
    
    def _interpret_corrections(self, correction_vector: np.ndarray) -> List[str]:
        """Interpret correction vector into actionable suggestions"""
        suggestions = []
        
        labels = ['protein', 'carbohydrates', 'fats']
        
        for i, correction in enumerate(correction_vector):
            if abs(correction) > 0.02:  # Significant correction
                if correction > 0:
                    suggestions.append(f"Increase {labels[i]} by {abs(correction)*100:.1f}%")
                else:
                    suggestions.append(f"Decrease {labels[i]} by {abs(correction)*100:.1f}%")
        
        if not suggestions:
            suggestions.append("Diet is well-balanced, maintain current ratios")
        
        return suggestions
