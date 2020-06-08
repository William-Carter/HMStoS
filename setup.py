import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="HMStoS",
    version="1.0.7",
    author="William Carter",
    author_email="williamcarter808@gmail.com",
    description="Converts HH:MM:SS to seconds",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/William-Carter/HMStoS",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
