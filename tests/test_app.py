import sys

sys.path.append("/opt/app-root")

import app

def test_hello():
    assert "Hello Ryan" in app.hello()

def test_hello_bad():
    assert True

def test_one_eq_1():
    assert 1 == 1


def test_two_eq_2():
    assert 2 == 2

