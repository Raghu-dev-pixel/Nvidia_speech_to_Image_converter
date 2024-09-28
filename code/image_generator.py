#This Python code is used to convert text to image using Nvidia's API
import requests
from PIL import Image
from io import BytesIO
import base64
from IPython.display import display

# API URL and headers

def image_creation(text):
    invoke_url = "https://ai.api.nvidia.com/v1/genai/stabilityai/stable-diffusion-xl"

    headers = {
        "Authorization": "Bearer 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", #Replace with your Nvidia API
        "Accept": "application/json",
    }

    # Payload with text prompts
    payload = {
        "text_prompts": [
            {
                "text": text,
                "weight": 1
            }
        ],
        "cfg_scale": 5,
        "sampler": "K_DPM_2_ANCESTRAL",
        "seed": 0,
        "steps": 25
    }

    # Send the request
    response = requests.post(invoke_url, headers=headers, json=payload)
    response.raise_for_status()

    # Get the JSON response
    response_body = response.json()

    # Extract the base64 image data
    image_data_base64 = response_body['artifacts'][0]['base64']

    # Decode the base64 image to binary
    image_data = base64.b64decode(image_data_base64)

    # Open the image using PIL
    image = Image.open(BytesIO(image_data))
    return(image)