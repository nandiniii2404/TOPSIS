from setuptools import setup, find_packages
from pathlib import Path

base_directory = Path(__file__).parent
detailed_description = (base_directory / "README.md").read_text()

setup(
    name='topsis_utility_102203958',
    version='1.1.0',
    description='A Python utility to compute TOPSIS rankings for decision-making problems',
    long_description=detailed_description,  
    long_description_content_type='text/markdown',
    author='Nandini Shekhar',  
    author_email='nandinishekhar01@gmail.com', 
    packages=find_packages(),  
    py_modules=['topsis_calculator'],  
    install_requires=[
        'pandas>=1.1.5',  
        'numpy>=1.19.0',
    ],
    entry_points={
        'console_scripts': [
            'topsis_tool=topsis_calculator:run',  
        ],
    },
)
