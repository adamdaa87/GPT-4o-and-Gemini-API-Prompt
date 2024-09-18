import os
import re
import types
from typing import List, Optional  # Correctly import List and Optional from the typing module
from collections import defaultdict  # Ensure defaultdict is available

BASE_SOLUTION_PATH = 'C:\\Users\\Asus\\Desktop\\Gemini API Test\\output'  # Set this to the appropriate path
FILE_EXTENSION = '_Gemini_output'  # Base part of the file extension to match

#BASE_SOLUTION_PATH = 'C:\\Users\\Asus\\Desktop\\GPT-4-API-Prompt\\output_v2'  # Set this to the appropriate path
#FILE_EXTENSION = '_GPT-4_output'  # Base part of the file extension to match

#BASE_SOLUTION_PATH = 'C:\\Users\\Asus\\Desktop\\Gemini API Test\\human_output'  # Set this to the appropriate path
#FILE_EXTENSION = '_Human'  # Base part of the file extension to match

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class DynamicTestLoader:
    def __init__(self, filepath):
        self.filepath = filepath
        self.module = None

    def load(self):
        # Extract the base filename without the iteration number
        base_filename = re.sub(r'_\d+\.txt$', '.txt', self.filepath)
        
        # Check if the file with the base filename exists
        if not os.path.exists(base_filename):
            # If not, try to find the file with an iteration number
            base_filename = self.filepath
        
        if not os.path.exists(base_filename):
            print(f"File not found: {base_filename}")
            raise FileNotFoundError(f"No such file: '{base_filename}'")
        
        with open(base_filename, 'r') as file:
            code = file.read()
        
        # Create a temporary module to execute the code
        module_name = os.path.splitext(os.path.basename(base_filename))[0]
        self.module = types.ModuleType(module_name)
        exec_globals = {
            '__name__': module_name,
            '__file__': base_filename,
            '__builtins__': __builtins__,
            # Add any other necessary imports here
            'defaultdict': defaultdict,  # Ensure defaultdict is available
            'List': List,  # Correctly reference List from the typing module
            'Optional': Optional,  # Correctly reference Optional from the typing module
            'ListNode': ListNode,  # Add ListNode to the global context
        }
        exec(code, exec_globals)
        self.module.__dict__.update(exec_globals)

    def get_class(self, class_name):
        if self.module and hasattr(self.module, class_name):
            return getattr(self.module, class_name)
        return None
