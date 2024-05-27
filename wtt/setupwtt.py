import os
import sys
import subprocess

def setup():
        # Set up virtual environment
        os.system('python -m venv venv')
        os.system('. venv/bin/activate')
        os.system('pip install google.generativeai')
        os.system('export GOOGLE_API_KEY = "$(cat ~/.api-gemini)"') 
        subprocess.call('. venv/bin/activate', shell=True)
