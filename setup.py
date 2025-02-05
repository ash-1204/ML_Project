from setuptools import find_packages, setup

def get_requirements(file_path: str) -> list[str]:
    """This function will return a list of requirements."""
    requirements = []
    file = "-e ."
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]

        if file in requirements:
            requirements.remove(file)

    return requirements

setup(
    name="mlproject",
    version="0.0.1",
    author="Mak",
    author_email="114122005@nitt.edu",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Fixed argument name
)

