from demo_02.demo_func import add_3


def test_addition():
    expected = 5
    actual = add_3(2, 3)
    assert actual == expected