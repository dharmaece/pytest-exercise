import pytest

# keep the common pytest fixture function into conftest.py.
# so that we can use across the files available inside the package.

@pytest.fixture(autouse=True,scope="session")
def general_setup():
    print("\n general_setup fixture function will be applicable across all the file, since the scope is defined for session and autouse as True...")

@pytest.fixture()
def addition_setup():
    print("\n going to perform addition operation for int data type variables")

@pytest.fixture()
def welcome_setup():
    print("\n saying welcome to user for pytest based codebase understanding")

#fixtureparametrizing example
@pytest.fixture(params=["a","b"])
def test_alphabet(request):
    print("\n fixture function call counting using alphabet variable:",request.param,"\n")


