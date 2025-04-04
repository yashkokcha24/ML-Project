## We use for building application as a package

from setuptools import find_packages, setup
## For returning list we have to import list package from typing module
from typing import List

HYPEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """
    This Function returns a list of package requirements.
    """
    requirements = []
    with open(file_path, "r", encoding="utf-8") as file_obj:  # Added encoding
        requirements = [req.strip() for req in file_obj.readlines()]  # Cleaner newline handling
        
        # Remove '-e .' if present
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Yash",
    author_email="yashkokcha@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  # Ensuring it's correctly read
)

