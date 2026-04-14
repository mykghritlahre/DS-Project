from setuptools import setup, find_packages

#(3)
# this '-e.' is required to defined and removed from requirements.txt
# if '-e .' is present in requirements.txt, setup.py is not required to be executed
# as we can directly run setup.py just with "pip install -r requirements.txt"
# this installs requirements along with executing setup.py
HYPHEN_E_DOT = "-e ."

#(2)
from typing import List
def get_requirements(file_path:str)-> List[str]:
    '''
    This function will return the list of requirements
    '''
    requirements = []

    with open(file_path) as file_object:
        requirements = file_object.readlines()
        requirements =[req.replace("\n", "") for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)

    return requirements



#(1)
setup(name='ds_project',
      version='0.1',
      author='Stellar',
      author_email='stellar@example.com',
      packages=find_packages(),
    #   install_requires=[
    #       "numpy",
    #       "pandas",
    #   ]    
    
    #  instead of listing down the libraries here, we can create a function to 
    # read the requirements.txt file and load the libraries dynamically.
      install_requires= get_requirements('requirements.txt')
      )
