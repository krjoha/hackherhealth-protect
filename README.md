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

## OpenAI credentials

Add openai api_key to .secrets.toml, or set as env-variable HACKHER_OPENAI_KEY:

``` bash
echo 'openai_key = "your_key_here"' >  src/.secrets.toml
```

## Running a chatbot

To try if your setup is working:

``` bash
python src/chatbot_test.py
```

To run the questionnaire bot. The bot will ask you three questions and if any answer is 'yes' or positive, it should give you information about organizations to contact for help:

``` bash
python src/chatbot_agent_with_memory.py
```
