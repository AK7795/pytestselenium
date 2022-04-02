'''import pytest
import assessment4

@pytest.fixture()
def setUp():
    print("start test case")
    yield
    print("end test case")


def test_sqroot1(setUp):
    r1 = assessment4.sqroot(49)
    assert 7 == r1


@pytest.mark.skip(reason="something")
@pytest.mark.parametrize("a, b", [(64, 8), (49, 7), (81, 9)])
def test_sqroot2(a, b):
    r1 = assessment4.sqroot(a)
    assert b == r1


@pytest.mark.parametrize("a, b", [(64, 8), (49, 7), (81, 9)])
def test_sqroot3(a, b):
    r1 = assessment4.sqroot(a)
    assert b == r1


@pytest.mark.parametrize("a,b,c,d", [(1, 7, 6, [-1.0, -6.0]), (1, -11, 28, [7.0, 4.0])])
def test_quadratic(a, b, c, d):
    r2 = assessment4.quadratic(a, b, c)
    assert d == r2


@pytest.mark.xfail
@pytest.mark.parametrize("a, b", [(4, 39.2), (2, 35.6), (6, 42.8)])
def test_celfah(a, b):
    r3 = assessment4.celfah(a)
    assert b == r3


@pytest.mark.parametrize("a, b", [(40, "positive"), (0, "Zero"), (-5, "negative")])
def test_number(a, b):
    r4 = assessment4.number(a)
    assert b == r4


@pytest.mark.parametrize("a, b", [(4, 10), (5, 15), (6, 21)])
def test_recur(a, b):
    r5 = assessment4.recur(a)
    assert b == r5
'''