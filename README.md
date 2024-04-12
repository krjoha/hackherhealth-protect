# chatbot

The PROTECT team

## Pre-requisites

* Python

## Installation

``` bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## OpenAI

Add openai api_key to .secrets.toml or set as environment variable HACKHER_OPENAI_KEY:

``` bash
echo 'openai_key = "your_key_here"' >  src/.secrets.toml
```

## Running a chatbot

``` bash
python src/chatbot_test.py
```
