from setuptools import find_packages,setup
from typing import List
def get_requirements(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
    return requirements
setup(
    name='sensor fault',
    version='0.0.1',
    author='kranthi',
    author_mail='kranthinaik09@gmail.com',
    install_requirements=get_requirements("requirements.txt"),
    pakages=find_packages()
)