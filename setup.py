from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='Web-Convert-App',
    version='1.0.0',
    install_requires=requirements,
    author="Alexey Voevoda",
    author_email="AVayavoda@gomel.iba.by",
    description="Web App for convert temperature values between celsius and fahrenheit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
    ],
    python_requires=">=3.9")
