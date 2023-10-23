import pytest

@pytest.mark.regression
def testmarkeraddoftwonum():
    """function for adding two hardcoded values"""
    a=5
    b=10
    sum=a+b
    assert sum == 15

@pytest.mark.sanity
def testmarkeraddofthreenum():
    """function for adding three hardcoded values"""
    a=5
    b=10
    c=20
    sum=a+b+c
    assert sum == 35

@pytest.mark.skip
def testmarkerwindowsplatform():
    """function for windowsplatform operation"""
    pass


def testmarkerlinuxplatform():
    """function for linuxplatform operation"""
    pass

@pytest.mark.xfail
def testmultiply():
    """function for multiplicaton operation, \
    need to add logic properly, currently kept it as xfail custom marker category"""
    pass
