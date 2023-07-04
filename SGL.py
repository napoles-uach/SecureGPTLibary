import os
import openai
import toml
import re

class SGL:
    def __init__(self):
        self.config = self.load_config()
        self.api_key = self.config["api_key"]
        openai.api_key = self.api_key
        self.model = "gpt-3.5-turbo"  # Set the desired model

    def load_config(self):
        # Load configuration from a TOML file
        config_file = "config.toml"  # Update with your file path
        if not os.path.exists(config_file):
            raise ValueError("Configuration file not found.")
        return toml.load(config_file)

    def sanitize_input(self, prompt, forbidden_words=None):
        sanitized_prompt = prompt

        # Remove forbidden words from the prompt
        if forbidden_words:
            for word in forbidden_words:
                sanitized_prompt = re.sub(re.escape(word), '', sanitized_prompt)

        return sanitized_prompt

    def content_filter(self, response):
        # Implement content filtering logic to detect and block sensitive content
        filtered_response = response  # Placeholder for content filtering
        return filtered_response

    def generate_chat_answer(self, messages):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        response = completion#.choices[0].message
        return response

    def generate_text_answer(self, prompt, max_tokens=10, temperature=0.8):
        completion = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            max_tokens=max_tokens,
            temperature=temperature
        )
        response = completion#.choices[0].text
        return response


# Example usage for chat completion
sgl = SGL()

chat_messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
]

chat_answer = sgl.generate_chat_answer(chat_messages)
print(chat_answer.choices[0].message)


# Example usage for text completion
text_prompt = "Say this is a test"
text_max_tokens = 7
text_temperature = 0

text_answer = sgl.generate_text_answer(text_prompt, text_max_tokens, text_temperature)
print(text_answer.choices[0].text)


prompt = "Hello, this is a test."
forbidden_words = ["test", "hello"]
sanitized_prompt = sgl.sanitize_input(prompt, forbidden_words)

print("santitized ",sanitized_prompt)