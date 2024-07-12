### wtt walkthetalk

wtt is a simple command line interface to the google.generativeai API
that accepts variable number of string and/or file path arguments.

It concatenates them into a prompt and passes it to the 
google API, which returns a textual response.

Both prompt and textual response get appended to a file.

# Installation and Usage 
1. Download the file or clone the repository 
```sh
git clone https://github.com/kolewttd/wtt
```
2. Install the API and export the API key
```sh
cd wtt
python -m venv venv
source venv/bin/activate
pip install google-generativeai
export GOOGLE_API_KEY="your-api-key-here"
export PATH=$PATH:.
```
3. Run
```bash
wtt hello
```
