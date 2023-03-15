from setuptools import find_packages, setup
from typing import List

hyphen_e_dot = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''this fun will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        reuirements = [req.replace('\n','') for req in requirements]
    if hyphen_e_dot in requirements:
        requirements.remove(hyphen_e_dot)

setup(
    name = "ML Model",
    version = '0.0.1',
    author = "Ashutosh Yadav",
    author_email = 'yashu8115@gmail.com',
    packages = find_packages(),  
    install_requires = get_requirements('requirements.txt')
)