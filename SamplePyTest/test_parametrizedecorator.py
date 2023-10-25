import pytest

#this test case for explaining parametize decorator concept.

@pytest.mark.parametrize("a,b,final",[(2,4,6),(3,7,10),(4,8,12)])
def test_multiplecall_diffarg_fun(a,b,final):
    """ testcase: same function executed with different set of argument \
    in this example, used two variable with that performed sum and ensured the asserting the condition is True or False
    """
    assert a+b == final
