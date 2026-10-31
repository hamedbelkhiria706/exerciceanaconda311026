import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, RateLimitError, APIError

env_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=env_path)

api_key = os.getenv("OPENAI_API_KEY")

if not api_key or not api_key.strip() or api_key.strip() == "your_actual_api_key_here":
    sys.exit("Error: OPENAI_API_KEY is missing. Please set it in your .env file.")

client = OpenAI(api_key=api_key)

SYSTEM_PROMPT = (
    "You are a helpful and concise learning assistant. "
    "Explain concepts simply and clearly. "
    "If you are unsure or do not know the answer, state that honestly and avoid inventing facts."
)

MODEL_NAME = "gpt-4o-mini"

print("AI Learning Assistant initialized.")
print("Type 'exit' or 'quit' to end the session.")

while True:
    try:
        user_input = input("\nYou: ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Assistant: Goodbye!")
            break

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input},
            ],
        )

        answer = response.choices[0].message.content
        model_used = response.model

        print(f"\nAssistant: {answer}")
        print(f"\n[Model: {model_used}]")

        if response.usage:
            prompt_tokens = response.usage.prompt_tokens
            completion_tokens = response.usage.completion_tokens
            total_tokens = response.usage.total_tokens
            print(f"[Tokens: prompt={prompt_tokens}, completion={completion_tokens}, total={total_tokens}]")

    except AuthenticationError:
        print("\nError: Authentication failed. Please check your API key.")
    except RateLimitError:
        print("\nError: Rate limit reached or quota exceeded. Please try again later.")
    except APIError as e:
        print(f"\nAPI Error: {e.message}")
    except KeyboardInterrupt:
        print("\n\nAssistant: Goodbye!")
        break
    except Exception as e:
        print(f"\nUnexpected error: {e}")