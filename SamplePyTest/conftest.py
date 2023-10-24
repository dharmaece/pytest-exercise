import pytest

# keep the common pytest fixture function into conftest.py.
# so that we can use across the files available inside the package.

@pytest.fixture
def addition_setup():
    print("\n going to perform addition operation for int data type variables")

@pytest.fixture
def welcome_setup():
    print("\n saying welcome to user for pytest based codebase understanding")

