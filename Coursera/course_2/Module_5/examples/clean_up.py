import unittest
import os
import shutil

# Function to test
def simple_addition(a, b):
	return a + b

# Paths for file operations
ORIGINAL_FILE_PATH = "/tmp/original_test_file.txt"
COPIED_FILE_PATH = "/mnt/data/copied_test_file.txt"

# Global counter
COUNTER = 0

# This method will be run once before any tests or test classes
def setUpModule():
	global COUNTER
	COUNTER = 0
    
	# Create a file in /tmp
	with open(ORIGINAL_FILE_PATH, 'w') as file:
    	file.write("Test Results:\n")

# This method will be run once after all tests and test classes
def tearDownModule():
	# Copy the file to another directory
	shutil.copy2(ORIGINAL_FILE_PATH, COPIED_FILE_PATH)
    
	# Remove the original file
	os.remove(ORIGINAL_FILE_PATH)

class TestSimpleAddition(unittest.TestCase):

	# This method will be run before each individual test
	def setUp(self):
    	global COUNTER
    	COUNTER += 1

	# This method will be run after each individual test
	def tearDown(self):
    	# Append the test result to the file
    	with open(ORIGINAL_FILE_PATH, 'a') as file:
        	result = "PASSED" if self._outcome.success else "FAILED"
        	file.write(f"Test {COUNTER}: {result}\n")

	def test_add_positive_numbers(self):
    	self.assertEqual(simple_addition(3, 4), 7)

	def test_add_negative_numbers(self):
    	self.assertEqual(simple_addition(-3, -4), -7)

# Running the tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestSimpleAddition)
runner = unittest.TextTestRunner()
runner.run(suite)

# Read the copied file to show the results
with open(COPIED_FILE_PATH, 'r') as result_file:
	test_results = result_file.read()

print(test_results)