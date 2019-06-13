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
        self.assertIn("Hello Ryan", app.hello())

    def test_hello_bad(self):
        #self.assertIn("Hello Jeb", app.hello())
        pass

if __name__ == "__main__":
    unittest.main()

