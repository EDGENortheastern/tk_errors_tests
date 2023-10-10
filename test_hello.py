import unittest # 🔴 importing unittest
from test_start import HelloName # 🔴 importing the class to be Tested

class SmokeTest(unittest.TestCase):
    def test_ut_works(self):
        self.assertEqual(2+2,4)
    
class TestHelloName(unittest.TestCase):
    # Tests for display_output function
    def test_display_output_valid(self):
        app = HelloName()  # Create an instance of the HelloName class
        response = app.display_output("John")  # Call display_output with a valid name
        self.assertEqual(response, "OK")  # Expect the response to be "OK" for a valid name
        self.assertIn("Hello,", app.decorate_name("John"))  # Ensure the decorated name starts with "Hello,"

    # Tests for decorate_name function
    def test_decorate_name_valid(self):
        app = HelloName()  # Create an instance of the HelloName class
        decorated = app.decorate_name("John")  # Call decorate_name to get the decorated name
        self.assertEqual(decorated, "Hello, 🌿🌼 John 🌼🌿!")  # Ensure the decorated name matches the expected format
        self.assertTrue(decorated.startswith("Hello,"))  # Check that the decorated name starts with "Hello,"

    # Tests for presence_check function
    def test_presence_check_valid(self):
        app = HelloName()  # Create an instance of the HelloName class
        self.assertTrue(app.presence_check("John"))  # Ensure that the presence check returns True for a valid name
        self.assertIsNotNone(app.presence_check("John"))  # Ensure the presence check doesn't return None for a valid name

    def test_presence_check_invalid(self):
        app = HelloName()  # Create an instance of the HelloName class
        self.assertFalse(app.presence_check(""))  # Ensure that the presence check returns False for an empty name
        self.assertIs(app.presence_check(""), False)  # Ensure the presence check explicitly returns False for an empty name

    # Tests for length_check function
    def test_length_check_valid(self):
        app = HelloName()  # Create an instance of the HelloName class
        self.assertTrue(app.length_check("Johnathan"))  # Ensure the length check returns True for a name of valid length
        self.assertNotEqual(len("Johnathan"), 2)  # Ensure the name's length is not 2

    # Tests for pattern_check function
    def test_pattern_check_valid(self):
        app = HelloName()  # Create an instance of the HelloName class
        self.assertTrue(app.pattern_check("John-Doe"))  # Ensure the pattern check returns True for a name with valid characters
        self.assertFalse(not app.pattern_check("Maria Angelica"))  # Double-check that the pattern check doesn't return False for a valid name

if __name__ == "__main__":
    unittest.main(verbosity=3)
