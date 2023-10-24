#tesst_addition.py file has 2 test cases.
def testadditionoftwonum():
    """testcase: function for adding two hardcoded values and sum it.  \
    assert the sum value is equal to hardcoded sum value or not """
    a=5
    b=10
    sum=a+b
    assert sum == 15

def testadditionofthreenum():
    """testcase: function for adding three hardcoded values and sum it.  \
    assert the sum value is equal to hardcoded sum value or not """
    a=5
    b=10
    c=20
    sum=a+b+c
    assert sum == 35