'''
This setup.py file is an essential part of packaging and distributing python projects . 
It is used by setuptools (or distutils in older python version) to define the configuration 
of your project such as its metadata dependencis and more 
'''


from setuptools import find_packages,setup
from typing import List 


def get_requirements()->list[str]:
    """
    This function will return list of requirements 

    """
    requirement_lst:list[str]=[]
    try:
        with open("requirements.txt" , 'r') as file:
            #Read lines from the file 
            lines = file.readlines()
            #process each line
            for line in lines:
                requirement = line.strip()
                ## ignore the empty line and -e.
                if requirement and requirement != "-e .":
                    requirement_lst.append(requirement)

    except FileNotFoundError:
        print('requirements.txt file not found')

    return requirement_lst

setup(
    name="NetworkSecurity",
    versionn="0.0.1",
    author="Kawsar Ahmmed",
    author_email="kawsar07ahmmed0712@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
)