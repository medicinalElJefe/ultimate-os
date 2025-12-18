"""
Modules package for Ultimate OS
Contains all specialized computational modules
"""

from .geometry import GeometryModule
from .hdc import HDCArchitecture
from .coherence import CoherentPossibilityCalculator
from .diet import DietCalculator
from .genesis import GenesisEngine
from .hyper_helical import HyperHelicalSphere
from .state_matrix import StateMatrixHandler
from .frequency import FrequencyProtocol

__all__ = [
    'GeometryModule',
    'HDCArchitecture',
    'CoherentPossibilityCalculator',
    'DietCalculator',
    'GenesisEngine',
    'HyperHelicalSphere',
    'StateMatrixHandler',
    'FrequencyProtocol'
]
