import sys
import os
import google.generativeai as genai

def arguments_to_text(*args) -> str:

        text = ""

        for arg in args:
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
        prompt = arguments_to_text(*args)
        genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(prompt)
        print(response.text)

        with open("output", "a") as file:
                file.write(prompt)
                file.write(response.text)

if __name__ == "__main__":
        if len(sys.argv) < 2:
                print("Usage: python wtt.py <file_path_or_string> [<file_path_or_string> ...]")
                sys.exit(1)

        prompt_list = sys.argv[1:]
        wtt(*prompt_list)
