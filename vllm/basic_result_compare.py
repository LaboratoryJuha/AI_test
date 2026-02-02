from openai import OpenAI

# 환경 변수 대신 코드 안에 직접 정의
LATEST_VLLM_VERSION = "25.12-py3"
MODEL_NAME = "openai/gpt-oss-20b"
MAX_MODEL_LEN = 8192
GPU_MEM_UTIL = 0.85

# vLLM 서버 설정
openai_api_key = "EMPTY"  # vLLM은 키 검증 안 함
openai_api_base = "http://localhost:4242/v1"

client = OpenAI(
    api_key=openai_api_key,
    base_url=openai_api_base,
)

completion = client.completions.create(
    model=MODEL_NAME,
    prompt="안녕",
    max_tokens=1024,
    temperature=0,
    stop=["\n\n"]   # 두 줄 띄면 멈추도록 설정
)

print("\n=====Completion result=====:", completion)
print("\n=====Completion.choices[0] result=====:", completion.choices[0])
print("\n=====Completion.choices[0].text result=====:", completion.choices[0].text)
