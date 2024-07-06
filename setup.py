#With the help of setup.py, the project will be as a package, and can also be deployed in PyPI

from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements



setup(
name="ML project",
version='0.0.1',
author='Sai',
author_email='kodithyalasaiuday1234@gmail.com',
packegs=find_packages(),
install_requires=get_requirements('requirements.txt'),
)
