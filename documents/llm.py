
import json
from urllib.request import Request, urlopen

BASE_URL = "http://127.0.0.1:1234/v1"
MODEL = "gemma-3-12b-it-qat"


def chat(prompt, system_prompt="You are a helpful assistant."):
    data = json.dumps({
        "model": MODEL,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.3,
        "max_tokens": 2048,
        "chat_template_kwargs": {"enable_thinking": False},
    }).encode("utf-8")

    request = Request(
        f"{BASE_URL}/chat/completions",
        data=data,
        headers={"Content-Type": "application/json"},
    )

    with urlopen(request, timeout=180) as response:
        result = json.loads(response.read())

    content = result["choices"][0]["message"].get("content")

    if not isinstance(content, str) or not content.strip():
        raise RuntimeError("LLM returned empty content.")

    return content.strip()
