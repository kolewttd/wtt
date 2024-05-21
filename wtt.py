import sys
import os
import google.generativeai as genai

def arguments_to_text(*args) -> str:
    """
    Collects text data from files and/or direct string inputs.

    Args:
        *args: Variable number of arguments containing file paths and/or direct strings.

    Returns:
        str: Concatenated text data from the provided files and strings.

    Raises:
        FileNotFoundError: If a file path provided in *args does not exist.
        PermissionError: If the program does not have permission to read the file.
        TypeError: If any argument provided is not a valid file path or string.
    """
    text = ""

    for arg in args:
        # Check if the argument is a file. If not, assume it is a string
        if isinstance(arg, str):
            if os.path.isfile(arg):
                with open(arg, 'r') as file:
                    text += file.read()
            else:
                text += arg + '\n'
        else:
            raise TypeError("Arguments must be file paths or strings.")

    return text

def wtt(*args) -> None:
    """
    Collects input from files and/or strings, generates content using a generative AI model,
    and writes the generated content along with the input to an output file.

    Args:
        *args: Variable number of arguments containing file paths and/or direct strings.

    Returns:
        None

    The function performs the following steps:
    1. Collects and concatenates text data from the provided files and strings.
    2. Configures the generative AI model with an API key from the environment variable.
    3. Generates content using the collected text as a prompt.
    4. Prints the generated content to the console.
    5. Appends the prompt and the generated content to "output.txt".
    """
    prompt = arguments_to_text(*args)

    # Configure the generative AI model with the API key
    genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

    # Initialize the model
    model = genai.GenerativeModel('gemini-pro')

    # Generate content using the prompt
    response = model.generate_content(prompt)

    # Print the response text
    print(response.text)

    # Write the prompt and response to output.txt
    with open("output.txt", "a") as file:
        file.write(prompt)
        file.write(response.text)

    print("Text has been written to output.txt")

if __name__ == "__main__":
    """
    Main entry point of the script. It collects command-line arguments, processes them,
    and calls the wtt function with these arguments.

    Usage:
        python wtt.py <file_path_or_string> [<file_path_or_string> ...]

    The script expects at least one argument, which can be a file path or a direct string.
    If no arguments are provided, it prints usage instructions and exits.
    """
    if len(sys.argv) < 2:
        print("Usage: python wtt.py <file_path_or_string> [<file_path_or_string> ...]")
        sys.exit(1)

    prompt_list = sys.argv[1:]
    wtt(*prompt_list)
