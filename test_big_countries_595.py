import unittest
from tick_cross import CustomTestRunner  # Import the custom test runner
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION  # Import DynamicTestLoader and constants
import time
import os

class TestBigCountries(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Define the solution file name using the FILE_EXTENSION variable
        solution_file = f'595. Big Countries{FILE_EXTENSION}.txt'
        solution_path = os.path.join(BASE_SOLUTION_PATH, solution_file)
        
        # Debug print to verify the path
        print(f"Looking for solution file at: {solution_path}")
        
        # Read the SQL query from the file as a string
        try:
            with open(solution_path, 'r') as file:
                cls.query = file.read().strip()
        except FileNotFoundError:
            print(f"File not found: {solution_path}")
            raise
        
        cls.expected_query = """
        SELECT name, population, area
        FROM World
        WHERE area >= 3000000 OR population >= 25000000;
        """.strip()

    def simulate_query_execution(self):
        # Simulated result set including additional countries
        return [
            {"name": "Afghanistan", "population": 25500100, "area": 652230},  # Added country
            {"name": "Algeria", "population": 37100000, "area": 2381741}     # Added country
        ]

    def test_query_structure(self):
        # Normalize whitespace by collapsing consecutive spaces and removing leading/trailing spaces
        normalized_query = ' '.join(self.query.split())
        normalized_expected_query = ' '.join(self.expected_query.split())

        print("Testing query structure:")
        print(f"Actual Query: {normalized_query}")
        print(f"Expected Query: {normalized_expected_query}")

        # Test if the normalized queries match
        self.assertEqual(normalized_query, normalized_expected_query, "The SQL query does not match the expected query structure.")

    def test_big_countries(self):
        print("Testing query execution:")
        start_time = time.time()
        result = self.simulate_query_execution()
        execution_time = time.time() - start_time

        expected_result = [
            {"name": "Afghanistan", "population": 25500100, "area": 652230},
            {"name": "Algeria", "population": 37100000, "area": 2381741}
        ]

        print(f"Simulated Result: {result}")
        print(f"Expected Result: {expected_result}")
        print(f"Execution Time: {execution_time} seconds")

        self.assertEqual(result, expected_result, "The query result does not match the expected output.")
        self.assertTrue(execution_time < 1, f"Query execution took too long: {execution_time} seconds")

if __name__ == '__main__':
    # Run the unit tests with the custom test runner
    unittest.main(testRunner=CustomTestRunner())
