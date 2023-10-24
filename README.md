# pytest-exercise
sample exercise of pytest concepts

python file should begin with test_*.py or end with *_test.py in pytest framework and 
the test case validation performed inside the function definition such function name should begin with "test" followed by testcase name in pytest framework. 

git clone this repo.
go to the cloned codebase path and run the command for pytest fixture function usage related file run
C:\Users\user\PycharmProjects\pytest-exercise>python -m pytest -v -s -k "test_addition.py"


general note:
I have tried these experiment on windows 10 OS based PC.
Install the PyCharm 2023.2.3 (Community Edition) package

pycharm-community-2023.2.3.exe
python-3.12.0-amd64.exe

C:\Users\user\PycharmProjects\pytest-exercise>curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
C:\Users\user\PycharmProjects\pytest-exercise>python -m get-pip
Defaulting to user installation because normal site-packages is not writeable
Collecting pip
  Using cached pip-23.3.1-py3-none-any.whl.metadata (3.5 kB)
Using cached pip-23.3.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.3.1
    Uninstalling pip-23.3.1:
      Successfully uninstalled pip-23.3.1
Successfully installed pip-23.3.1

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







