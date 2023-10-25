# pytest-exercise
sample exercise of pytest concepts

python file should begin with test_*.py or end with *_test.py in pytest framework and 
the test case validation performed inside the function definition such function name should begin with "test" followed by testcase name in pytest framework. 

git clone this repo.
go to the cloned codebase path 

Run the command for pytest fixture function usage related file run
C:\Users\user\PycharmProjects\pytest-exercise>python -m pytest -v -s -k "test_addition.py"

Run the command for pytest fixture parametrization related file run
C:\Users\user\PycharmProjects\pytest-exercise\SamplePyTest>pytest -v -s test_fixtureparam_addition.py


GENERAL NOTE (SETUP):
**************************

I have tried these experiment on windows 10 OS based PC.
1. Install the PyCharm 2023.2.3 (Community Edition) package.
2. Install the python3.12 package.
3. Install the pip python package.
4. Install the ini plugin using PyCharm utility.
5. Install git version control system for windows PC using PyCharm utility.

EXE file required for Windows PC:
**************************************

pycharm-community-2023.2.3.exe
python-3.12.0-amd64.exe

pip python package installation procedure on windows PC:
**************************************************************

C:\Users\user\PycharmProjects\pytest-exercise>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
C:\Users\user\PycharmProjects\pytest-exercise>python -m get-pip
Successfully installed pip-23.3.1


Ensure the below specified package version is installed or not.
***************************************************************

C:\Users\user\PycharmProjects\pytest-exercise>python --version
Python 3.12.0

C:\Users\user\PycharmProjects\pytest-exercise>python -m pytest --version
pytest 7.4.2

C:\Users\user\PycharmProjects\pytest-exercise>pip3 list
Package    Version
---------- -------
colorama   0.4.6
iniconfig  2.0.0
packaging  23.2
pip        23.3.1
pluggy     1.3.0
pytest     7.4.2
setuptools 68.2.2
wheel      0.41.2







