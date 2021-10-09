import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acfc",
    version="1.0",
    author="Aziz Ben Ali",
    author_email="ba.taahaziz@gmail.com",
    description="Alacritty Colors to Foot Colors (Converter)",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/grtcdr/acfc",
    project_urls={
        "Bug Tracker": "https://github.com/grtcdr/acfc/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
