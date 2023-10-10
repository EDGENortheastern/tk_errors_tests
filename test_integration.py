# 🌸 Importing the unittest library for creating unit tests
import unittest 

# 🌼 Importing the 'patch' function from unittest.mock for mocking purposes
from unittest.mock import patch 

# 🌻 Importing the 'HelloName' class from 'test_start' module which will be tested
from test_start import HelloName 

# 🌷 Creating a test class that inherits from unittest.TestCase to define our test cases
class TestHelloNameSimple(unittest.TestCase): 

    # 🌺 A special method that sets up before each test. It's called before every test method
    def setUp(self): 
        # 🌹 Creating an instance of the 'HelloName' class to be used in the tests
        self.app = HelloName() 

    # 🌾 Test case for a valid name input
    def test_valid_name(self): 
        # 🌼 Calling the 'display_output' method of 'HelloName' with a valid name
        result = self.app.display_output('John') 
        # 🌻 Asserting that the method returns the expected output "OK"
        self.assertEqual(result, "OK") 

    # 🌷 Patching (mocking) the 'showerror' function of 'tkinter.messagebox' for this test
    @patch('tkinter.messagebox.showerror') 
    def test_invalid_names(self, mock_showerror): 
        # 🌺 Testing for an invalid name (empty name)
        self.app.display_output('') 
        # 🌹 Checking if the mocked 'showerror' function was called with the expected arguments
        mock_showerror.assert_called_with("Error", "Name cannot be left blank") 

        # 🌾 Testing for another invalid name (name containing numbers)
        self.app.display_output('John123') 
        # 🌼 Checking if the mocked 'showerror' function was called with the expected arguments
        mock_showerror.assert_called_with("Error", "The name can only contain letters") 

# 🌻 If this script is run as the main program, the tests are executed with increased verbosity
if __name__ == "__main__": 
    unittest.main(verbosity=3)

