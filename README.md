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
```sh
python wtt.py
```
## Testing and Development (Experiments)

It should run everywhere. 
### Linux
### Termux

### On Licence
I am not informed nor a lawyer.
TODO

# The APIs for large language models should be in the public domain

# GET INVOLVED

# FIND THE KEY
# change
# COMMIT

The key will be leaked.






Solve

Failed to build maturin                     ERROR: Could not build wheels for maturin, which is required to install pyproject.toml-based projecta
To fix this issue, you can try the following:

1. Make sure you have the latest version of `maturin` installed. You can do this by running the following command:

```
pip install --upgrade maturin
```

2. Try running the following command to build the maturin wheels:

```
maturin build
```

If this does not work, you can try the following:

1. Uninstall `maturin` and then reinstall it:

```
pip uninstall maturin
pip install maturin
```

2. Try running the following command to build the maturin wheels:

```
maturin build
```

3. If you are still having problems, you can try creating a new virtual environment and installing `maturin` in it. You can do this by running the following commands:

```
python3 -m venv venv
source venv/bin/activate
pip install maturin
```

Once you have `maturin` installed in the virtual environment, you can try running the following command to build the maturin wheels:

```
maturin build
```
