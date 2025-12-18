from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="ultimate-os",
    version="1.0.0",
    author="Ultimate OS Team",
    author_email="",
    description="Advanced Multi-Dimensional Operating System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/medicinalElJefe/ultimate-os",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[
        "numpy>=1.21.0",
    ],
    include_package_data=True,
    package_data={
        'ultimate_os': ['data/*.csv', 'data/*.txt'],
    },
    entry_points={
        'console_scripts': [
            'ultimate-os=ultimate_os.main:main',
        ],
    },
)
