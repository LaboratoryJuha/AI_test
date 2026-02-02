#! /bin/bash
. vllm-gpt-oss-20b-project/.env
curl http://localhost:4242/v1/chat/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "openai/gpt-oss-20b",
	"messages": [
            {"role": "system", "content": "너는 한국 전문가야"},
            {"role": "user", "content": "한국 최고의 건축물은 뭐야?"}
        ]
    }'
