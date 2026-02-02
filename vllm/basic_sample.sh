#! /bin/bash
. vllm-gpt-oss-20b-project/.env
curl http://localhost:4242/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "openai/gpt-oss-20b",
        "prompt": "안녕",
        "max_tokens": 7,
        "temperature": 0
    }'
