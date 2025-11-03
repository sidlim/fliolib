from setuptools import setup, find_packages

setup(
    name="flimlib",
    version="2.2.6-DEV",
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "flimlib": ["libflimlib.so"],
    },
    python_requires=">=3.8",
)

