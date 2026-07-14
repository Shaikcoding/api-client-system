from setuptools import setup, find_packages

setup(
    name="apiclient",
    version="1.0.0",
    description="API Client System",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "httpx>=0.27.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
    python_requires=">=3.9",
) 
