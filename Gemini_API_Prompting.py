import os
import time
import asyncio
import vertexai
from vertexai.preview.generative_models import GenerativeModel
import vertexai.preview.generative_models as generative_models
from google.api_core.exceptions import ResourceExhausted

async def process_file(model, input_file_path, output_file_path):
    try:
        # Read the content of the input file
        with open(input_file_path, 'r') as file:
            text_prompt = file.read().strip()
    except PermissionError:
        print(f"Permission denied: {input_file_path}")
        return    

    while True:
        try:
            # Send the prompt to the Gemini model and receive the response
            responses = model.generate_content(
                [text_prompt],
                generation_config={
                    "max_output_tokens": 8192,  # Set maximum token limit for the output
                    "temperature": 1,  # Set the temperature to 1 to enhance creativity
                    "top_p": 1  # Use top-p sampling
                },
                safety_settings={
                    generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                    generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                },
                stream=True  # Stream responses to handle large outputs
            )

            full_text = ''
            for response in responses:
                if hasattr(response, 'candidates'):
                    for candidate in response.candidates:
                        if hasattr(candidate, 'content'):
                            for part in candidate.content.parts:
                                if hasattr(part, 'text'):
                                    # Accumulate text ensuring proper line breaks and structure
                                    full_text += part.text

            # Handle the response and extract code blocks
            print(full_text)
            extracted_code = extract_and_save_code(full_text)

            # Write the extracted code to the output file
            with open(output_file_path, 'w') as output_file:
                output_file.write(extracted_code)

            print(f"Successfully processed {input_file_path}")
            break

        except ResourceExhausted:
            # Handle quota exhaustion by retrying after a minute
            print("Quota exceeded, retrying after a minute...")
            await asyncio.sleep(60)
        except AttributeError as e:
            # Handle any attribute-related errors
            print(f"Failed to process {input_file_path}: {e}")
            break
#--------------------------------Vertex AI Initialization-------------------------------------
async def generate_from_file(input_dir, output_dir):
    # Initialize Vertex AI with the project name and location
    vertexai.init(project="gimini-api-test-416821", location="europe-north1")
    # Instantiate the generative model with a specific model ID
    model = GenerativeModel("gemini-1.5-pro-001")

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Create a list of tasks for processing files asynchronously
    tasks = []
    for filename in os.listdir(input_dir):
        input_file_path = os.path.join(input_dir, filename)
        base_name, ext = os.path.splitext(filename)
        output_file_path = os.path.join(output_dir, f"{base_name}_Gemini_output{ext}")
        tasks.append(process_file(model, input_file_path, output_file_path))
        await asyncio.sleep(10)  # Introduce a delay to ensure Gemini has enough time to handle the next prompt

    # Run all tasks concurrently
    await asyncio.gather(*tasks)
#---------------------------------extract_and_save_code------------------------------------
def extract_and_save_code(content):
    import re

    # Use regular expressions to find all Python code blocks in the response
    python_code_blocks = re.findall(r'```python(.*?)```', content, re.DOTALL)

    # Use regular expressions to find all SQL code blocks in the response
    sql_code_blocks = re.findall(r'```sql(.*?)```', content, re.DOTALL)

    # Combine both Python and SQL code blocks into a single string
    extracted_code = '\n\n'.join(python_code_blocks + sql_code_blocks).strip()

    return extracted_code
#------------------------------------------------------------------------------------------
# Specify the input and output directories for processing
input_dir = r'C:\Users\Asus\Desktop\Gemini API Test\input'
output_dir = r'C:\Users\Asus\Desktop\Gemini API Test\output_Gemini'

# Run the asynchronous file processing function
asyncio.run(generate_from_file(input_dir, output_dir))
