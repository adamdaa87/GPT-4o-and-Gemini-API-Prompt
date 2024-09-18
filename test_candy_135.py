import unittest
from tick_cross import CustomTestRunner  # Import the custom test runner
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION  # Import DynamicTestLoader and constants
import time

class TestCandy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the solution file name using the FILE_EXTENSION variable
        solution_file = f'135. Candy{FILE_EXTENSION}.txt'
        solution_path = f'{BASE_SOLUTION_PATH}\\{solution_file}'

        # Load the solution class from the file using DynamicTestLoader
        loader = DynamicTestLoader(solution_path)
        loader.load()
        Solution = loader.get_class('Solution')  # Get the Solution class

        # Initialize the Solution object
        cls.solution = Solution()

    def run_tests(self):
        total_time = 0  # To store the total execution time for all test cases
        all_passed = True  # Flag to track if all test cases pass

        # Define the test cases with inputs and expected outputs
        test_cases = [
            ([1, 0, 2], 5),  # Example input and expected output
            ([1, 2, 2], 4),
            ([1], 1)
        ]

        # Iterate through each test case
        for i, (input_data, expected) in enumerate(test_cases, 1):
            try:
                start_time = time.perf_counter()  # Use perf_counter for higher resolution timing
                result = self.solution.candy(input_data)
                end_time = time.perf_counter()  # End timing
                execution_time = (end_time - start_time) * 1000  # Convert to ms
                total_time += execution_time

                print(f"Test case {i}:")
                print(f"Input: {input_data}")
                print(f"Output: {result}")
                print(f"Expected: {expected}")
                print(f"Execution time: {execution_time:.3f} ms\n")

                if result != expected:
                    all_passed = False

            except Exception as e:
                print(f"✘ Test failed due to runtime error: {str(e)}")
                all_passed = False

        average_time = total_time / len(test_cases)
        print(f"\nAverage execution time: {average_time:.3f} ms")
        return average_time, all_passed

    def test_candy(self):
        # Run the tests and get the average time and all_passed status
        average_time, all_passed = self.run_tests()
        # Assert that all tests passed
        self.assertTrue(all_passed)

if __name__ == '__main__':
    # Run the unit tests with the custom test runner and verbosity level 1
    unittest.main(testRunner=CustomTestRunner(verbosity=1))
