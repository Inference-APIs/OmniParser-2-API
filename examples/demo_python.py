import requests
import base64
import json

# OmniParser API Configuration
API_URL = "https://omniparser.inferenceapis.com/parse"
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key

# Load and encode an image to Base64
image_path = "images/screenshot.png"  # Replace with your image file
with open(image_path, "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

# Prepare API request payload
payload = {
    "base64_image": base64_image,
    "box_threshold": 0.5,
    "iou_threshold": 0.3,
    "text_threshold": 0.7,
    "use_paddleocr": True
}

# Set request headers
headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json"
}

# Send request to OmniParser API
print("Sending request to OmniParser API...")
response = requests.post(API_URL, headers=headers, json=payload)

# Handle response
if response.status_code == 200:
    result = response.json()
    print(" Parsed UI Elements: ", json.dumps(result, indent=2))

    # Save processed image if available
    if "processed_image" in result:
        processed_image_data = base64.b64decode(result["processed_image"])
        output_image_path = "images/screenshot_processed.png"
        with open(output_image_path, "wb") as output_file:
            output_file.write(processed_image_data)
        print(f" Processed image saved as {output_image_path}")
    else:
        print(" No processed image found in response.")

else:
    print("Error:", response.status_code, response.text)

