import os
import re
import unittest
import datetime
import numpy as np  # Ensure numpy is installed or available
import matplotlib.pyplot as plt  # Import Matplotlib for plotting
from dynamic_loader import DynamicTestLoader, BASE_SOLUTION_PATH, FILE_EXTENSION

# Import all unit test classes with the new naming convention
from test_permutations_46 import TestPermutations
from test_candy_135 import TestCandy
from test_sort_list_148 import TestSortList
from test_reconstruct_queue_406 import TestReconstructQueue
from test_strong_password_checker_420 import TestStrongPasswordChecker
from test_concatenated_words_472 import TestFindAllConcatenatedWordsInADict
from test_big_countries_595 import TestBigCountries
from test_number_of_distinct_islands_II_711 import TestNumberOfDistinctIslands
from test_peak_index_in_mountain_array_852 import TestPeakIndexInMountainArray
from test_min_falling_path_sum_931 import TestMinFallingPathSum
from test_shuffle_the_array_1470 import TestShuffleTheArray
from test_check_if_pangram_1832 import TestCheckIfPangram
from test_count_rectangles_2250 import TestCountRectangles
from test_length_of_lis_2407 import TestLengthOfLIS
from test_score_of_string_3110 import TestScoreOfString
from test_median_of_uniqueness_array_3134 import TestMedianOfUniquenessArray
from test_min_cost_to_equalize_array_3139 import TestMinCostToEqualizeArray
from test_minimum_substrings_in_partition_3144 import TestMinimumSubstringsInPartition

def normalize_sql(sql):
    """
    Normalize SQL by converting to lowercase and removing extra whitespace.
    """
    return re.sub(r'\s+', ' ', sql).strip().lower()

def pass_at_k(n, c, k):
    if n - c < k:
        return 1.0
    return 1.0 - np.prod(1.0 - k / np.arange(n - c + 1, n + 1))

def run_all_tests(solution_dir):
    # List all solution files in the solution directory
    solution_files = [f for f in os.listdir(solution_dir) if f.endswith(FILE_EXTENSION + '.txt')]
    
    # Mapping of problem numbers to test classes
    test_class_mapping = {
        '46': TestPermutations,
        '135': TestCandy,
        '148': TestSortList,
        '406': TestReconstructQueue,
        '420': TestStrongPasswordChecker,
        '472': TestFindAllConcatenatedWordsInADict,
        '595': TestBigCountries,
        '711': TestNumberOfDistinctIslands,
        '852': TestPeakIndexInMountainArray,
        '931': TestMinFallingPathSum,
        '1470': TestShuffleTheArray,
        '1832': TestCheckIfPangram,
        '2250': TestCountRectangles,
        '2407': TestLengthOfLIS,
        '3110': TestScoreOfString,
        '3134': TestMedianOfUniquenessArray,
        '3139': TestMinCostToEqualizeArray,
        '3144': TestMinimumSubstringsInPartition
    }
    
    total_tests = len(test_class_mapping)
    passed_tests = 0
    total_time = 0
    pass_1_scores = []
    failed_problems = []  # List to store failed problems

    # Iterate over each solution file
    for solution_file in solution_files:
        # Construct the full path to the solution file
        solution_path = os.path.join(solution_dir, solution_file)
        
        # Extract the problem number from the file name
        problem_number = solution_file.split('.')[0].strip()
        
        if problem_number == '595':  # Special handling for SQL-based solution
            with open(solution_path, 'r') as file:
                sql_query = file.read().strip()
            
            # Expected SQL query (adjust as necessary)
            expected_sql_query = "SELECT name, population, area FROM World WHERE area >= 3000000 OR population >= 25000000;"
            
            # Normalize and compare the SQL output
            if normalize_sql(sql_query) == normalize_sql(expected_sql_query):
                passed_tests += 1
                print(f"Results for problem number {problem_number}:")
                print("  All Tests Passed: Yes")
            else:
                failed_problems.append((problem_number, "Big Countries"))
                print(f"Results for problem number {problem_number}:")
                print("  All Tests Passed: No")
            print('-' * 40)
            continue

        # Dynamically load the solution class for non-SQL problems
        loader = DynamicTestLoader(solution_path)
        
        try:
            loader.load()
            solution_class = loader.get_class('Solution')  # Assuming the main class in the solution is named 'Solution'
        except SyntaxError as e:
            print(f"Syntax error in solution file {solution_file}: {e}")
            failed_problems.append((problem_number, "Syntax Error"))
            continue
        
        if solution_class is None:
            print(f"Could not find 'Solution' class in {solution_file}")
            failed_problems.append((problem_number, "No Solution Class Found"))
            continue
        
        # Get the corresponding test class from the mapping
        test_class = test_class_mapping.get(problem_number)
        if test_class is None:
            print(f"No test class found for problem number {problem_number}")
            continue
        
        # Create an instance of the test class
        test_instance = test_class()
        test_instance.solution = solution_class()  # Assign the loaded solution class to the test instance
        
        # Run the tests and capture average_time and all_passed
        try:
            average_time, all_passed = test_instance.run_tests()
            # Print the results
            print(f"Results for problem number {problem_number}:")
            print(f"  Average Time: {average_time:.3f} ms")
            print(f"  All Tests Passed: {'Yes' if all_passed else 'No'}")
            print('-' * 40)
            if all_passed:
                passed_tests += 1
                total_time += average_time
                pass_1_scores.append(1)
            else:
                pass_1_scores.append(0)
                failed_problems.append((problem_number, test_class.__name__))
        except Exception as e:
            print(f"Error running tests for problem number {problem_number}: {e}")
            failed_problems.append((problem_number, str(e)))

    # Calculate pass@1
    pass_1_score = pass_at_k(total_tests, passed_tests, 1)

    # Calculate average time for passed tests (excluding SQL test)
    avg_time = total_time / passed_tests if passed_tests > 0 else 0

    # Get the current date and time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Print the summary with a timestamp
    #model_name = "gemini-1.5-pro-001"
    model_name = "gpt-4o-2024-08-06"
    #model_name = "Human Solutions"   
    print(f"Summary (Generated on {current_time}):")
    print(f"  Model: {model_name}")
    print(f"  Passed Tests: {passed_tests}/{total_tests}")
    print(f"  pass@1: {pass_1_score:.3f}")
    print(f"  Average Time for Passed Tests: {avg_time:.3f} ms")
    #print(f"  Temperature = 1")

    # Print the list of failed problems
    if failed_problems:
        print("\nFailed Problems:")
        for problem_number, problem_name in failed_problems:
            print(f"  Problem {problem_number} ({problem_name})")


if __name__ == "__main__":
    solution_dir = BASE_SOLUTION_PATH  # Set to your solutions directory path
    run_all_tests(solution_dir)