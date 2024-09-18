import unittest
from tick_cross import CustomTestRunner  # Import the custom test runner
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION  # Import DynamicTestLoader and constants
import time
from typing import Optional

# Define ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class TestSortList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the solution file name using the FILE_EXTENSION variable
        solution_file = f'148. Sort List{FILE_EXTENSION}.txt'
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
            (self.create_linked_list([4, 2, 1, 3]), [1, 2, 3, 4]),
            (self.create_linked_list([-1, 5, 3, 4, 0]), [-1, 0, 3, 4, 5])
        ]

        # Iterate through each test case
        for i, (input_data, expected_output) in enumerate(test_cases, 1):
            start_time = time.perf_counter()  # Start timing
            result = self.solution.sortList(input_data)
            end_time = time.perf_counter()  # End timing

            # Calculate the time taken for this test case in milliseconds
            test_time = (end_time - start_time) * 1000
            total_time += test_time  # Accumulate the total time

            # Convert linked list results to lists for easier comparison
            result_list = self.linked_list_to_list(result)

            # Print the test case details
            input_list = self.linked_list_to_list(input_data)
            print(f"Test case {i}:")
            print(f"Input: {input_list}")
            print(f"Output: {result_list}")
            print(f"Expected: {expected_output}")
            print(f"Execution time: {test_time:.3f} ms\n")

            # Check if the result matches the expected output
            try:
                self.assertEqual(result_list, expected_output)
            except AssertionError:
                all_passed = False  # Set flag to False if the test case fails

        # Calculate the average execution time
        average_time = total_time / len(test_cases)
        print(f"Average execution time: {average_time:.3f} ms")

        # Return the average time and whether all tests passed
        return average_time, all_passed

    def create_linked_list(self, elements):
        # Helper method to create a linked list from a list of elements
        if not elements:
            return None
        head = ListNode(elements[0])
        current = head
        for element in elements[1:]:
            current.next = ListNode(element)
            current = current.next
        return head

    def linked_list_to_list(self, head):
        # Helper method to convert a linked list back to a Python list
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result

    def test_sort_list(self):
        # Run the tests and get the average time and all_passed status
        average_time, all_passed = self.run_tests()
        # Assert that all tests passed
        self.assertTrue(all_passed)

if __name__ == '__main__':
    # Run the unit tests with the custom test runner and verbosity level 1
    unittest.main(testRunner=CustomTestRunner(verbosity=1))
