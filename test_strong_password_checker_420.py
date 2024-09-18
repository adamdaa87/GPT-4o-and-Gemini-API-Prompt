import unittest
from tick_cross import CustomTestRunner  # Import the custom test runner
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION  # Import DynamicTestLoader and constants
import time

class TestStrongPasswordChecker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the solution file name using the FILE_EXTENSION variable
        solution_file = f'420. Strong Password Checker{FILE_EXTENSION}.txt'
        solution_path = f'{BASE_SOLUTION_PATH}\\{solution_file}'

        # Load the solution class from the file using DynamicTestLoader
        loader = DynamicTestLoader(solution_path)
        loader.load()
        Solution = loader.get_class('Solution')  # Get the Solution class

        # Initialize the Solution object
        cls.solution = Solution()

    def run_tests(self):
        total_time = 0  # To store the total execution time
        all_passed = True  # Flag to track if all test cases pass

        # Define the test cases: input and expected output
        test_cases = [
            ("a", 5),
            ("aA1", 3),
            ("1337C0d3", 0)
        ]

        # Iterate through each test case
        for i, (input_data, expected_output) in enumerate(test_cases, 1):
            start_time = time.perf_counter()  # Start timing
            result = self.solution.strongPasswordChecker(input_data)
            end_time = time.perf_counter()  # End timing

            # Calculate the time taken for this test case in milliseconds
            test_time = (end_time - start_time) * 1000
            total_time += test_time  # Accumulate the total time

            # Print the test case details
            print(f"Test case {i}:")
            print(f"Input: {input_data}")
            print(f"Output: {result}")
            print(f"Expected: {expected_output}")
            print(f"Execution time: {test_time:.3f} ms\n")

            # Check if the result matches the expected output
            try:
                self.assertEqual(result, expected_output)
            except AssertionError:
                all_passed = False  # Set flag to False if the test case fails

        # Calculate the average execution time
        average_time = total_time / len(test_cases)
        print(f"Average execution time: {average_time:.3f} ms")

        # Return the average time and whether all tests passed
        return average_time, all_passed

    def test_strong_password_checker(self):
        # Run the tests and get the average time and all_passed status
        average_time, all_passed = self.run_tests()
        # Assert that all tests passed
        self.assertTrue(all_passed)

if __name__ == '__main__':
    # Run the unit tests with the custom test runner and verbosity level 1
    unittest.main(testRunner=CustomTestRunner(verbosity=1))
