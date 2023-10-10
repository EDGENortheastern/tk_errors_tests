import unittest # 🔴 importing unittest
from test_start import HelloName

class SmokeTest(unittest.TestCase):
    def test_ut_works(self):
        self.assertEqual(2+2,4)

class TestHelloName(unittest.TestCase):

    def setUp(self):
        self.app = HelloName(init_gui=False)

    # Tests for decorate_name function
    def test_decorate_name(self):
        app = HelloName()
        decorated = app.decorate_name("John")
        self.assertEqual(decorated, "Hello, 🌿🌼 John 🌼🌿!")
        self.assertTrue(decorated.startswith("Hello,"))
        self.assertIsInstance(app.decorate_name("alice"), str)

if __name__ == "__main__":
    unittest.main(verbosity=3)
