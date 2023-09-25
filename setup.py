from setuptools import setup,find_packages
from typing import List

hypen_e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        
    return requirements
setup(
    name= 'credit_card_default_02',
    author='ayan',
    email='ayanchowdhury00@gmail.com',
    version='0.0.2',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)
