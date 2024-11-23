import unittest

# Sample functions to test
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Define the test class
class TestMathOperations(unittest.TestCase):
    
    def setUp(self):
        print("Setting up before test")

    def tearDown(self):
        print("Cleaning up after test")
    
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        
    def test_subtract(self):
        self.assertEqual(subtract(5, 3), 2)

# Create the test suite
def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestMathOperations('test_add'))
    suite.addTest(TestMathOperations('test_subtract'))
    return suite

# Run the test suite
if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
