# AI Learning Assistant

A lightweight command-line AI assistant configured with a small model for learning tasks.

## Setup Steps

1. Navigate to the project folder:
```bash
cd ai_assistant
```

2. Create and activate a virtual environment:

On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

On macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

3. Install the dependencies:
```bash
pip install -r requirements.txt
```

4. Configure your API key:
- Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
- Open `.env` and insert your real OpenAI API key:
```env
OPENAI_API_KEY=your_actual_api_key_here
```

## How to Run

Run the assistant with:
```bash
python main.py
```

Type your prompt and press Enter. To leave the session, type `exit` or `quit`.

## Example Interaction

```text
AI Learning Assistant initialized.
Type 'exit' or 'quit' to end the session.

You: What is an API in simple terms?

Assistant: Think of an API like a waiter at a restaurant. You are the customer, the kitchen is a system or database, and the waiter takes your order, brings it to the kitchen, and delivers your food back to you. An API allows two different computer programs to talk to each other and exchange information safely.

[Model: gpt-4o-mini-2024-07-18]
[Tokens: prompt=56, completion=64, total=120]

You: exit
Assistant: Goodbye!
```

