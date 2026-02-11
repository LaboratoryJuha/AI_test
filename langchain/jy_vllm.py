import os
from langchain_openai import ChatOpenAI


class VLLMCall:
    """
    vLLM 모델 호출 클래스
    OpenAI 호환 API를 통해 vLLM 모델과 통신
    """
    
    def __init__(
        self,
        model_name: str = "openai/gpt-oss-20b",
        base_url: str = "http://127.0.0.1:4242/v1",
        temperature: float = 0.7,
        max_tokens: int = 512
    ):
        """
        VLLMCall 초기화
        
        Args:
            model_name: 사용할 모델 이름
            base_url: vLLM 서버 엔드포인트
            temperature: 샘플링 온도
            max_tokens: 최대 토큰 수
        """
        os.environ["OPENAI_API_KEY"] = "EMPTY"
        
        self.model = ChatOpenAI(
            model_name=model_name,
            api_key="EMPTY",
            base_url=base_url,
            temperature=temperature,
            max_tokens=max_tokens
        )
    
    def call(self, message: str) -> str:
        """
        모델에 메시지를 전송하고 응답 받기
        
        Args:
            message: 전송할 메시지
        
        Returns:
            모델의 응답 전체
        """
        response = self.model.invoke(message)
        return response


if __name__ == "__main__":
    # 사용 예제
    vllm = VLLMCall()
    response = vllm.call("response test")
    print(response.content)