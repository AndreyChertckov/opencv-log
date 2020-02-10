import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="andreychertckov", # Replace with your own username
    version="1.1.0",
    author="Andrey Chertkov",
    author_email="andreychertckov@gmail.com",
    description="Open CV log",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AndreyChertckov/opencv-log",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)