# Gemini Command-Line Chatbot

A simple, interactive command-line chatbot powered by Google's Gemini 1.5 Pro model. This chatbot is designed to be a friendly and helpful assistant for programming students, capable of answering questions about code, debugging, and tech career paths.

## Features

-   **Interactive Chat:** Have a continuous conversation in your terminal.
-   **Conversation History:** The chatbot remembers the context of the conversation.
-   **Custom Personality:** The AI's behavior is guided by a system instruction to be friendly, warm, and supportive.
-   **Special Commands:**
    -   `clear`: Clears the conversation history and refreshes the screen.
    -   `exit` or `quit`: Ends the chat session.
-   **Token Usage Display:** Shows the token count for each API call.

## System Requirements

-   Python 3.7+

## Setup and Installation

Follow these steps to get the chatbot running on your local machine.

**1. Clone the Repository (or Create the File)**

If you are using Git, clone the repository. Otherwise, create a folder and save the `chatbot.py` script inside it.

```bash
git clone https://your-repository-url.com/
cd your-repository-folder
```

**2. Install Dependencies**

This project requires the `google-generativeai` library. Install it using pip:

```bash
pip install google-generativeai
```

**3. Get a Google Gemini API Key**

You need an API key to use the Gemini model.

1.  Visit the [Google AI Studio](https://aistudio.google.com/app/apikey).
2.  Click "**Create API key**" and copy your new key.

**4. Add Your API Key**

Open the `chatbot.py` file and find the following line:

```python
client = genai.Client(api_key="GEMINI API KEY")
```

Replace `"GEMINI API KEY"` with your actual key.

> **⚠️ Security Warning:** Do not commit your API key directly to a public repository. For better security, use environment variables to store your key.

## How to Run

1.  Navigate to the project directory in your terminal.
2.  Run the script using the following command:

    ```bash
    python chatbot.py
    ```

3.  The chat will start, and you will see a `You:` prompt. Start typing your questions!

## Usage Example

```
You: what is a list in python?

Chatbot: Hey there! A list in Python is a collection of items that is ordered and changeable. You can think of it like a shopping list where you can add, remove, or change items. You create one using square brackets `[]`. For example: `fruits = ["apple", "banana", "cherry"]`. What else can I help you with? 😊
📊 Tokens used: 88

You: how do I add "orange" to it?

Chatbot: Great question! You can easily add an item to the end of a list using the `.append()` method. Like this: `fruits.append("orange")`. Your list would then be `["apple", "banana", "cherry", "orange"]`. Keep the great questions coming!
📊 Tokens used: 162

You: clear

Chatbot: History cleared and screen refreshed ✨

You: exit

Chatbot: Conversation ended! Catch you later 😄
```
