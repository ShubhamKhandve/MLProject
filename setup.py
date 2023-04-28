from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    List of Requirements
    
    '''
    req=[]
    with open(file_path) as file_obj:
        req=file_obj.readlines()
        req=[requ.replace("/n","")for requ in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)

setup(
    name='MLProjrct',
    version='0.0.1',
    author='Shubham khandve',
    author_email='khandveshubham@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('Requirements.txt')
)