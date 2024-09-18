# GPT-4o-and-Gemini-API-Prompt
dynamic_loader.py: This script defines a class DynamicTestLoader that dynamically loads Python code from a file, executes it in a temporary module, and handles the file lookup process. It includes utility functions for managing file paths and extracting code blocks, which are useful for testing or loading algorithmic solutions for evaluation.

Framwork_Testing.py: This script is designed for testing and evaluation of coding models like GPT-4 and Gemini 1.5. It handles input processing, evaluating solutions through unit tests, and measures the execution time for solutions. The script likely integrates with external APIs or local files for testing.

Gemini_API_Prompting.py: This script interacts with the Gemini 1.5 Pro API, sending prompts and extracting responses, specifically focusing on code solutions. It processes input files, extracts Python and SQL code from responses, and saves the outputs into designated files.

GPT-4-API-Prompt.py: Similar to the Gemini script, this file communicates with the GPT-4 API, processing multiple prompts, extracting code (Python and SQL) from the responses, and saving the results. It includes asynchronous functions to handle multiple file inputs and manage the output storage efficiently. 
