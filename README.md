### WALK THE TALK

wtt.py

wtt is a simple command line "ChatGPT". It is a wrapper around google.generativeai that accepts variable number of string and/or file path arguments.

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
python -m venv venv
source venv/bin/activate
pip install google-generativeai
export GOOGLE_API_KEY="your-api-key-here"
```
3. Run
```bash
wtt hello
```

Note: wtt command must be called from the wtt directory.
## Testing and Development (Experiments)
