import setuptools


def long_description():
    with open("README.md", "r") as file:
        return file.read()


setuptools.setup(
    name="tuning_metrics",
    version="0.1.2",
    author="Alessio Sclocco",
    author_email="alessio@sclocco.eu",
    license="Apache 2.0",
    description="Library to compute auto-tuning and performance metrics.",
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/isazi/tuning_metrics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
    ],
    python_requires='>=3.7',
    install_requires=[
        "numpy>=1.19.2",
    ],
)
