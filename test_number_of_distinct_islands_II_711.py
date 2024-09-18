import unittest
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION
import time

class TestNumberOfDistinctIslands(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the solution file name using the FILE_EXTENSION variable
        solution_file = f'711. Number of Distinct Islands II{FILE_EXTENSION}.txt'
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
            (
                [[1, 1, 0, 0, 0], [1, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 1]],
                1
            ),
            (
                [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]],
                1
            )
        ]

        # Iterate through each test case
        for i, (grid, expected) in enumerate(test_cases, 1):
            try:
                start_time = time.perf_counter()  # Start timing the execution
                result = self.solution.numDistinctIslands2(grid)  # Call the solution method with the input data
                end_time = time.perf_counter()  # End timing the execution

                # Calculate the time taken for this test case in milliseconds
                execution_time = (end_time - start_time) * 1000
                total_time += execution_time  # Accumulate the total time

                # Print the test case details
                print(f"Test case {i}:")
                print(f"Input: grid = {grid}")
                print(f"Output: {result}")
                print(f"Expected: {expected}")
                print(f"Execution time: {execution_time:.3f} ms\n")

                # Check if the result matches the expected output
                if result != expected:
                    all_passed = False  # Set flag to False if the test case fails
                    print(f"✘ Test case {i} failed")
            except TypeError as e:
                all_passed = False
                print(f"✘ Test case {i} failed due to a runtime error: {str(e)}")

        # Calculate the average execution time
        average_time = total_time / len(test_cases)
        print(f"Average execution time: {average_time:.3f} ms")

        # Return the average time and whether all tests passed
        return average_time, all_passed

    def test_num_distinct_islands(self):
        # Run the tests and get the average time and all_passed status
        average_time, all_passed = self.run_tests()
        # Assert that all tests passed
        self.assertTrue(all_passed)

if __name__ == '__main__':
    # Run the unit tests with verbosity level 1
    unittest.main(verbosity=1)
