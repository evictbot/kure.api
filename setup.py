from setuptools import setup 

with open("requirements.txt") as f: 
    requirements = f.read().splitlines()

setup(
    name="kure-api",
    version="1.0.0",
    description="A Python API wrapper for kure api",
    author="Resent",
    url="https://github.com/evictbot/kure.api",
    install_requires=requirements,
    python_requires='>=3.8.0',
    project_urls = {
        "Documentation": "https://kure.pl/docs"
    }
)
