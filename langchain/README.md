# Langchain

## step 1. vllm 호출 준비
ex) vllm.py


## step 2. 문서준비
ex) prepare_documents.py


## step 3. 텍스트 분할 (chunk 단위로 벡터화, overlap 크기 설정)
ex) local_rag.py

# Reference
```python
from konlpy.tag import Mecab # 대용량 처리와 속도가 중요하므로 한국어 형태소 분석은 이 모델로
    # 예 ) mecab = Mecab() 
    #     print(mecab.pos("한글 품사 태깅을 테스트합니다.")) 
    # 불용어를 제거하여 벡터를 더 정교하게 작성합니다.
#     예)
#     • 	조사: 은, 는, 이, 가, 을, 를, 에, 의
#     • 	접속사: 그리고, 그러나, 하지만
#     • 	부사: 매우, 정말, 그냥
#     • 	기타: 저는, 우리는, 이것, 저것
```
