import requests
import json
import os

# https://openrouter.ai/models?max_price=0
model_list = ["bytedance-seed/seedream-4.5",
              "black-forest-labs/flux.2-klein-4b",
              "black-forest-labs/flux.2-max",
              "qwen/qwen3-next-80b-a3b-instruct:free",
              "openai/gpt-oss-120b:free",
              "moonshotai/kimi-k2:free",
              "z-ai/glm-4.5-air:free",
              "deepseek/deepseek-r1-0528:free",
              ]

OPENROUTER_API_KEY=os.environ.get("OPENROUTER_API_KEY")

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": "Bearer " + OPENROUTER_API_KEY,
    "Content-Type": "application/json",
    "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
    "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
  },
  data=json.dumps({
    # "model": "openrouter/auto",
    "model": "deepseek/deepseek-r1-0528:free",
    "messages": [
      {
        "role": "user",
        "content": "What is the meaning of life?"
      }
    ]
  })
)
print(response.json())
