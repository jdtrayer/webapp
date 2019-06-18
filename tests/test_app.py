import sys

sys.path.append("/opt/app-root")

import app

def test_hello():
    assert "Hello Ryan" in app.hello()

def test_hello_bad():
    assert "Hello Jeb" in app.hello()
