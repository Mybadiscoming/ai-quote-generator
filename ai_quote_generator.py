from transformers import pipeline
import random

# Load the small GPT-2 model
generator = pipeline("text-generation", model="gpt2")

# Prompts for variety
prompts = [
    "Write a short motivational quote about consistency:",
    "Give a one-line quote about learning and progress:",
    "Say something inspiring about coding:",
    "Share a wise quote about patience and success:"
]

def generate_quote():
    prompt = random.choice(prompts)
    result = generator(
        prompt,
        max_new_tokens=30,
        truncation=True,
        pad_token_id=50256  # ensures no padding errors
    )
    quote = result[0]["generated_text"].replace(prompt, "").strip()
    print(f"💬 {quote}")

if __name__ == "__main__":
    print("✨ AI Quote Generator — Freelance Spirit Edition")
    generate_quote()