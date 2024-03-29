# Vocal Bot

## ToDo
- Add Chat History (one possibility is to have vocal bot access chat history to have 'memory' of previous prompts
- Fix voice input taking too long (either mic is stuck waiting for more input or it is a processing issue)

## About This Project
Vocal Bot is a chatbot application which utilises the OpenAI text generation and text-to-speech API to output chatbot responses through speaker audio.

## Setup

Ensure that you have the downloaded the following Software:
- [Python](https://www.python.org/downloads/) (Version 3.12.1 or higher)

As well as the following libraries:
- Tkinter
  
  ```
  $ pip install tk
  ```

- Pillow

  ```
  $ pip install pillow
  ```
- Speech Recognition

  ```
  $ pip install SpeechRecognition
  ```
  
- OpenAI
  
  ```
  $ pip install --upgrade openai
  ```

[**IMPORTANT**]

In order to make API calls using the openAI API you must have the following:
  - OpenAI API key
  - OpenAI API Tokens

To setup, visit the following link [here](https://platform.openai.com/docs/quickstart?context=python)

*Note that for first time users an initial fee of $6 must be deposited into your OpenAI account and will act as an initial balance for API calls. For the text generation (GPT-3.5-turbo) and tts API
each call costs <$0.01.
**The cost for each API call increases substantially with the gpt-4 models.***

## Usage

To run the project, ensure all files in the repository are locally downloaded and run the 'chatbot_app.py' file.

#### GPT-4.0

Currently, the program is using OpenAI's GPT-3.5-Turbo model. To use OpenAI's GPT-4.0 Model do the following:

- In the `chatbot_query` function in **chatbot_engine.py** change
  
  ```python
  model="gpt-3.5-turbo"
  ```
  
  to the following:
  ```python
  model="gpt-4"
  ```


## Progress
![Screenshot of Interface 10/03/2024](images/progress_10_03_2024.png)
(10/03/24)
