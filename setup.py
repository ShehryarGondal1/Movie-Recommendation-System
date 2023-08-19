from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .' ## Ignoring 

def get_requirements(file_path:str)->List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

        return requirements


setup(
    name='Movie Recommendation System',
    version='0.0.1',
    author='Shehryar Gondal',
    author_email='gondalshehryar23@gmail.com',
    install_requires=get_requirements('requirements.txt'),
    ## Aternative way or bad way is : install_requires=['pandas','numpy']  
    packages=find_packages()
    
)
