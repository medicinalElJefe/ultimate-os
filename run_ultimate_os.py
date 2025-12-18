#!/usr/bin/env python3
"""
Wrapper script to run Ultimate OS main
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ultimate_os.main import main

if __name__ == '__main__':
    main()
