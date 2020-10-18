from setuptools import setup, find_packages


setup(
    name='xlsAsData',
    version='0.0.1',
    description='a method of of useing xls as a datasource',
    long_description='',
    long_description_content_type="text/markdown",
    author='postitnotenija',
    url='https://github.com/MechaCoder/',
    py_modules=['xlsAsData'],
    packages=find_packages(),
    install_requires=['openpyxl'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
    ]
)