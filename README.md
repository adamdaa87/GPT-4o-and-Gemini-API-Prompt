# GPT-4o-and-Gemini-API-Prompt
Gemini_API_Prompting.py: This script interacts with the Gemini 1.5 Pro API, sending prompts and extracting responses, specifically focusing on code solutions. It processes input files, extracts Python and SQL code from responses, and saves the outputs into designated files.

GPT-4-API-Prompt.py: Similar to the Gemini script, this file communicates with the GPT-4 API, processing multiple prompts, extracting code (Python and SQL) from the responses, and saving the results. It includes asynchronous functions to handle multiple file inputs and manage the output storage efficiently. 

dynamic_loader.py: This script defines a class DynamicTestLoader that dynamically loads Python code from a file, executes it in a temporary module, and handles the file lookup process. It includes utility functions for managing file paths and extracting code blocks, which are useful for testing or loading algorithmic solutions for evaluation.

Framwork_Testing.py: This script is designed for testing and evaluation of coding models like GPT-4 and Gemini 1.5. It handles input processing, evaluating solutions through unit tests, and measures the execution time for solutions. The script likely integrates with external APIs or local files for testing.

The execution_times.py script is designed to analyze the execution times of coding solutions generated by GPT-4o, Gemini 1.5 Pro, and human programmers. It processes execution time data stored in text files, calculates averages for each problem, and determines the shortest execution time (best time) among the models and humans.
The script also computes the efficiency distance for each model relative to the best time and provides a comparative analysis. Results are saved in a tab-delimited text file, and a visual representation of the data is generated using Matplotlib, displaying execution times for all problems and models. This comprehensive approach helps evaluate the efficiency of solutions across models and humans.

### Steps to Execute the Provided Scripts Locally on a Windows Machine

1. **Set Up the Environment**:
   - Ensure Python (preferably 3.10 or higher) is installed on your system.
   - Open Command Prompt (cmd) or PowerShell and install the required libraries using the following command:
     ```cmd
     pip install openai vertexai google-api-core pandas matplotlib numpy
     ```

2. **Set API Keys**:
   - Obtain API keys for both OpenAI (for GPT-4o) and Vertex AI (for Gemini 1.5 Pro).
   - Set them as environment variables in the Command Prompt:
     ```cmd
     set OPENAI_API_KEY=<your-openai-api-key>  # For GPT-4o, the API keys are set through the Windows system environment settings.
     set GOOGLE_APPLICATION_CREDENTIALS=<path-to-your-service-account-json>  # For Gemini, this line doesn't exist in my code because the API keys are set through the Windows system environment settings.
     ```
   - Replace `<your-openai-api-key>` with your actual OpenAI key and `<path-to-your-service-account-json>` with the path to your Google credentials file. or you can set the API keys through the Windows sitting environment

3. **Organize Input and Output Directories**:
   - Create an `input` folder containing the problem descriptions in text files.
   - Ensure `output` directories are prepared for each script to store results:
     - Example paths:
       - For Gemini: `C:\Users\Asus\Desktop\Gemini_API_Test\output_Gemini`
       - For GPT-4: `C:\Users\Asus\Desktop\GPT-4-API-Prompt\output_GPT-4o

4. **Run the Prompting Scripts**:
   - For Gemini 1.5 Pro:
     ```cmd
     python Gemini_API_Prompting.py
     ```
   - For GPT-4o:
     ```cmd
     python GPT-4-API-Prompt.py
     ```
   - These scripts will process the prompts in the `input` folder and save the solutions in their respective `output` folders.

5. **Load Solutions Dynamically**:
   - This script will be called automatically by the `Framwork_Testing.by` script to load and execute the saved solutions dynamically 
     Don't forget to choose the right ASE_SOLUTION_PATH and FILE_EXTENSION based on LLM model by commenting out the unwanted directories and uncommenting the current model.

     ```cmd   
     #BASE_SOLUTION_PATH = r'C:\Users\Asus\Desktop\GPT-4o-and-Gemini-API-Prompt\output_Gemini'  # Set this to the appropriate path
     #FILE_EXTENSION = '_Gemini_output'  # Base part of the file extension to match

     BASE_SOLUTION_PATH = r'C:\Users\Asus\Desktop\GPT-4o-and-Gemini-API-Prompt\output_GPT-4o'  # Set this to the appropriate path
     FILE_EXTENSION = '_GPT-4_output'  # Base part of the file extension to match

     #BASE_SOLUTION_PATH = r'C:\Users\Asus\Desktop\GPT-4o-and-Gemini-API-Prompt\human_output'  # Set this to the appropriate path
     #FILE_EXTENSION = '_Human'  # Base part of the file extension to match
     ```
7. **Evaluate with Framework Testing**:
   - Run `Framwork_Testing.py` to evaluate the solutions by performing unit tests, calculating the `pass@1` metric, and recording execution times:
     ```cmd
     python Framwork_Testing.py
     ```
   - The results will include pass/fail statuses and execution times for each solution.

8. **Analyze Execution Times**:
   - Execute the `execution_times.py` script to process and visualize the execution time data:
     ```cmd
     python execution_times.py
     ```
   - This script computes averages, identifies the best execution times, and generates comparative plots using Matplotlib.

9. **Review the Results**:
   - Inspect the generated output files and visualizations:
     - Execution times: `execution_time_results.txt`
     - Comparison plots: Displayed as Matplotlib charts.
---

### Notes:
- Replace all placeholders (e.g., `<your-openai-api-key>`) with actual values before running the scripts.
- Ensure all required files are in the correct directories as referenced by the scripts.

This guide should provide a straightforward process to run the provided scripts on a Windows machine. Let me know if further clarification is needed!



