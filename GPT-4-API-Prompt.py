import os
import asyncio
from openai import OpenAI, OpenAIError

# Attempt to import RateLimitError; if unavailable, fallback to a more general OpenAIError
try:
    from openai import RateLimitError
except ImportError:
    RateLimitError = OpenAIError  # Fallback to a more general error if RateLimitError is not available

client = OpenAI()

# Initialize the OpenAI client with your API key from an environment variable
OpenAI.api_key = os.getenv("OPENAI_API_KEY")

async def process_file(input_file_path, output_dir):
    try:
        # Read the content of the input file
        with open(input_file_path, 'r', encoding='utf-8') as file:
            text_prompt = file.read().strip()
    except PermissionError:
        print(f"Permission denied: {input_file_path}")
        return
    
    full_text = ''
    while True:
        try:
            # Send the prompt to the OpenAI API and receive the response
            response = client.chat.completions.create(
                model="gpt-4o-2024-08-06",
                temperature=1,  # Set the temperature to 1
                messages=[
                    {"role": "user", "content": text_prompt}
                ]    
            )
            # Append the response content to the full_text variable
            if response.choices and len(response.choices) > 0:
                full_text += response.choices[0].message.content
            break
        except RateLimitError:
            # Handle rate limit errors by retrying after a minute
            print("Rate limit exceeded, retrying after a minute...")
            await asyncio.sleep(60)
        except OpenAIError as e:
            # Handle general API errors
            print(f"API error: {e}")
            break
        except Exception as e:
            # Handle any other exceptions
            print(f"Failed to process {input_file_path}: {e}")
            break

    # Extract Python and SQL code blocks from the response
    extracted_code = extract_and_save_code(full_text)
    print(full_text)
    
    # Construct the output file path
    base_name, ext = os.path.splitext(os.path.basename(input_file_path))
    output_file_path = os.path.join(output_dir, f"{base_name}_GPT-4_output{ext}")

    # Write the extracted code to the output file with UTF-8 encoding
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        output_file.write(extracted_code)

    print(f"Successfully processed {input_file_path}")

async def generate_from_file(input_dir, output_dir):
    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a list of tasks for processing files asynchronously
    tasks = []
    for filename in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, filename)
        tasks.append(process_file(input_file_path, output_dir))
        await asyncio.sleep(10)  # Introduce a delay to ensure the system can handle the next prompt

    # Run all tasks concurrently
    await asyncio.gather(*tasks)

#---------------------------------------------------------------------
def extract_and_save_code(content):
    import re

    # Use regular expressions to find all Python code blocks in the response
    python_code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)

    # Use regular expressions to find all SQL code blocks in the response
    sql_code_blocks = re.findall(r'```sql(.*?)```', content, re.DOTALL)

    # Combine both Python and SQL code blocks into a single string
    extracted_code = '\n\n'.join(python_code_blocks + sql_code_blocks).strip()

    return extracted_code

#---------------------------------------------------------------------
# Specify the input and output directories for processing
input_dir = r'C:\Users\Asus\Desktop\Gemini API Test\input'
output_dir = r'C:\Users\Asus\Desktop\GPT-4-API-Prompt\output_v2'

# Run the asynchronous file processing function
asyncio.run(generate_from_file(input_dir, output_dir))
