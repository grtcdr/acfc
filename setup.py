import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="acfc",
    version="2.0.1",
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
        "Topic :: Terminals :: Terminal Emulators/X Terminals",
        "Topic :: Utilities",
        "Development Status :: 5 - Production/Stable",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        "configparser", "PyYAML"
    ],
    python_requires=">=3.6",
)
