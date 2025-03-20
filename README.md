# OmniParser 2 API


📄 [OmniParser API](https://inferenceapis.com/models/omniparser-v2-api) | 🌐 [Web Demo](https://inferenceapis.com/models/omniparser-v2-web-demo) | 🛠 [Official GitHub](https://github.com/microsoft/OmniParser) | 📑 [Model Paper](https://arxiv.org/abs/2408.00203)


## Overview
OmniParser 2 is a powerful screen parsing tool that extracts structured data from user interface screenshots. It enhances AI models, such as GPT-4V, by grounding actions in the correct UI regions.

## API Usage
This API uses [Inference APIs](https://inferenceapis.com/). You will need to get your API key from your [profile page](https://inferenceapis.com/profile).

### Base URL
```
https://api.aiapi.com/v1/models/omniparser
```

### Parse Screenshot
- **Endpoint**: `POST /parse`
- **Description**: Analyzes a screenshot to extract UI elements.
- **Headers**:
  - `Authorization: Bearer YOUR_API_KEY`
  - `Content-Type: application/json`
- **Request Body**:
```json
{
  "base64_image": "ENCODED_IMAGE_STRING",
  "box_threshold": 0.5,
  "iou_threshold": 0.3,
  "text_threshold": 0.7,
  "use_paddleocr": true
}
```

### Response
```json
{
  "elements": [
    { "type": "button", "text": "Submit", "coordinates": [100, 200, 300, 400] }
  ]
}
```

## Code Examples
You can also see full working demos in `examples/` directory.

See full Python Demo in : ([examples/demo_python.py](examples/demo_python.py))
```python
import requests
import base64

# Convert image to Base64
with open('screenshot.png', 'rb') as image_file:
    image_data = base64.b64encode(image_file.read()).decode('utf-8')

headers = {
    'Authorization': 'Bearer YOUR_API_KEY',
    'Content-Type': 'application/json'
}

response = requests.post(
    'https://omniparser.inferenceapis.com/parse',
    json={'base64_image': image_data},
    headers=headers
)

print(response.json())
```

### JavaScript 
See full html/js demo in : ([examples/demo_web.html](examples/demo_web.html))

```javascript
const fileInput = document.createElement('input');
fileInput.type = 'file';
fileInput.accept = 'image/*';
fileInput.addEventListener('change', function(event) {
    const file = event.target.files[0];
    if (!file) return;

    const reader = new FileReader();
    reader.readAsDataURL(file);
    reader.onload = async function() {
        const base64Image = reader.result.split(",")[1];

        const response = await fetch('https://omniparser.inferenceapis.com/parse', {
            method: 'POST',
            headers: {
                'Authorization': 'Bearer YOUR_API_KEY',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ base64_image: base64Image })
        });

        const result = await response.json();
        console.log(result);
    };
});
fileInput.click();
```

### cURL 
```bash
curl -X POST \
  https://omniparser.inferenceapis.com/parse \
  -H 'Authorization: Bearer YOUR_API_KEY' \
  -H 'Content-Type: application/json' \
  -d '{
    "base64_image": "ENCODED_IMAGE_STRING"
  }'
```

### PHP 
```php
<?php
$api_url = 'https://omniparser.inferenceapis.com/parse';
$api_key = 'YOUR_API_KEY';
$image_path = 'screenshot.png';

$image_data = base64_encode(file_get_contents($image_path));

$data = json_encode([
    "base64_image" => $image_data
]);

$options = [
    'http' => [
        'header'  => "Content-Type: application/json\r\nAuthorization: Bearer $api_key\r\n",
        'method'  => 'POST',
        'content' => $data
    ]
];

$context  = stream_context_create($options);
$response = file_get_contents($api_url, false, $context);
echo $response;
?>
```

