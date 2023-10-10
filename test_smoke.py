import unittest # 🔴 importing unittest

class SmokeTest(unittest.TestCase):
    def test_ut_works(self):
        # Assert that 2 + 2 is equal to 4
        self.assertEqual(2+2,4)
        
        # Assert that the value is True (truthy)
        self.assertTrue(True)
        
        # Assert that the value is False (falsy)
        self.assertFalse(0)
    
    def test_ut_works_with_more(self):
        # Assert that 5 is greater than 4
        self.assertGreater(5,4)
        
        # Assert that "Me" is an instance of the str (string) class
        self.assertIsInstance("Me", str)
        
        # Assert that the letter "c" is not present in the word "lion"
        self.assertNotIn("c", "lion")

if __name__ == "__main__":
    unittest.main(verbosity=3)
