# Can you write a python program to read parameters from a json file and generate an image using DALL-E model?
# The json has these parameters
# {
#   "api_key": "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",
#   "output_directory": "./generated_images",
#   "image_size": "1024x1024",
#   "default_prompt": "A beautiful landscape with mountains and a lake"
# }

import os
import requests
import secrets
import string
import json

# Can you update this proram to read the parameters from a json file and generate an image using DALL-E model?
# Load configuration from JSON file
def load_config(config_path="config.json"):
    try:
        with open(config_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: Configuration file '{config_path}' not found.")
        return None
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON file. {e}")
    
# Generate a random filename
def generate_random_filename(extension=".png", length=8):
    characters = string.ascii_letters + string.digits
    random_name = ''.join(secrets.choice(characters) for _ in range(length))
    return f"{random_name}{extension}"

# Generate an image using DALL-E API
def generate_image(prompt, config):
    if not config:
        print("Error: Configuration is missing.")
        return

    api_key = config.get("api_key")
    if not api_key:
        print("Error: API key is missing in the configuration.")
        return

    output_dir = config.get("output_directory", "./generated_images")
    image_size = config.get("image_size", "1024x1024")

    # API endpoint and headers
    endpoint = "https://api.openai.com/v1/images/generations"
    headers = {"Authorization": f"Bearer {api_key}"}

    # API payload
    payload = {
        "prompt": prompt,
        "size": image_size
    }

    # Make API call
    try:
        response = requests.post(endpoint, json=payload, headers=headers)
        response.raise_for_status()
        image_url = response.json()["data"][0]["url"]
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to call DALL-E API. {e}")
        return

    # Save the image
    os.makedirs(output_dir, exist_ok=True)

    random_filename = generate_random_filename()
    image_path = os.path.join(output_dir, random_filename)

    try:
        with open(image_path, "wb") as img_file:
            img_file.write(requests.get(image_url).content)
        print(f"Image saved at: {image_path}")
    except Exception as e:
        print(f"Error: Failed to save the image. {e}")

# Main function
def main():
    config_path="config.json"
    config = load_config(config_path)
    if not config:
        print("Error: Configuration is missing.")
        return
    prompt = input(f"Enter prompt (default: {config.get('default_prompt', 'A default prompt')}): ") or config.get("default_prompt", "A default prompt")
    generate_image(prompt, config)

if __name__ == "__main__":
    main()
