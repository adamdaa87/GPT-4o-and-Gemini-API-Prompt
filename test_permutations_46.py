import unittest
from tick_cross import CustomTestRunner  # Import the custom test runner
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION  # Import the DynamicTestLoader class and FILE_EXTENSION
from typing import List  # Ensure the List type hint is available
import time

class TestPermutations(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the solution file name dynamically using the FILE_EXTENSION variable
        solution_file = f'46. Permutations{FILE_EXTENSION}.txt'
        solution_path = f'{BASE_SOLUTION_PATH}\\{solution_file}'
        
        # Load the solution class from the file using DynamicTestLoader
        loader = DynamicTestLoader(solution_path)
        loader.load()
        Solution = loader.get_class('Solution')  # Get the Solution class
        cls.solution = Solution()  # Initialize the Solution object

    def run_tests(self):
        total_time = 0  # To store the total execution time for all test cases
        all_passed = True  # Flag to track if all test cases pass

        # Define the test cases with inputs and expected outputs
        test_cases = [
            ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
            ([0, 1], [[0, 1], [1, 0]]),
            ([1], [[1]])
        ]

        # Iterate through each test case
        for i, (input_data, expected_output) in enumerate(test_cases, 1):
            start_time = time.perf_counter()  # Start timing the execution
            result = self.solution.permute(input_data)  # Call the permute method with the input data
            end_time = time.perf_counter()  # End timing the execution
            test_time = (end_time - start_time) * 1000  # Calculate the time taken in milliseconds
            total_time += test_time  # Accumulate the total time
            print(f"Test case {i}:")
            print(f"Input: {input_data}")
            print(f"Output: {result}")
            print(f"Expected: {expected_output}")
            print(f"Execution time: {test_time:.3f} ms\n")  # Corrected line

            # Check if the result matches the expected output, disregarding the order
            try:
                self.assertEqual(sorted(result), sorted(expected_output))
            except AssertionError:
                all_passed = False  # Set flag to False if the test case fails

        # Calculate the average execution time
        average_time = total_time / len(test_cases)
        print(f"Average execution time: {average_time:.3f} ms")  # Print the average execution time
        return average_time, all_passed  # Return the average time and pass status

    def test_permutations(self):
        # Run the tests and get the average time and all_passed status
        average_time, all_passed = self.run_tests()
        # Assert that all tests passed
        self.assertTrue(all_passed)

if __name__ == '__main__':
    # Run the unit tests with the custom test runner and verbosity level 1
    unittest.main(testRunner=CustomTestRunner(verbosity=1))
