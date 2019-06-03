import unittest
import sys

sys.path.append("/opt/app-root")

import app

class TestApp(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello(self):
        self.assertContains("Hello Ryan", app.hello())

    def test_hello_bad(self):
        self.assertContains("Hello Jeb", app.hello())

if __name__ == "__main__":
    unittest.main()
