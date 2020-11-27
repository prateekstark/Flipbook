from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.readlines()

long_description = "Flipbook is a basic implementation of real-world like book. We can generate various cool gifs and pdfs using this package!"

setup(
    name="Flipbook",
    version="1.0.0",
    author="Prateek Garg",
    author_email="prateekgarg.iitd@gmail.com",
    url="https://github.com/prateekstark/Flipbook",
    description="Small Package for Hasura recruitment.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=find_packages(),
    entry_points={"console_scripts": ["flipc = run:main"]},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords="Flipbook pdf python gif",
    install_requires=requirements,
    zip_safe=False,
)
