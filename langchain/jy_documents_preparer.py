from langchain_community.document_loaders import UnstructuredURLLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from jy_url_dictionary import URLS_DICTIONARY, COLLECTION_NAME

class UrlDocumentPreparer:
    """
    preparing documents from url_dictionary.py\n
    check your url_dictionary.py

    using pkg
        pip install -U langchain
        pip install -U langchain-community
        pip install -U unstructured
    """

    def __init__(self):
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=800,
                                                  chunk_overlap=150,
                                                  add_start_index=True,
                                                )
        self.loader = UnstructuredURLLoader(
            urls=list(URLS_DICTIONARY.values()),
            mode="single",              # "single" 또는 "elements"
            show_progress_bar=True,      # 진행 상황 표시 여부
        )
        self.documents = self.loader.load_and_split(text_splitter=self.text_splitter)

#   TODO: 필요하다면 여기서 형태소화 작업 추가 필요 특히 한국어

    def print_document(self, idx):
        print(self.documents[idx].metadata['source'])
        return self

if __name__ == "__main__":
    base_doc = UrlDocumentPreparer()
    base_doc.print_document(0)

    for doc in base_doc.documents:
        print(doc)
    print(len(base_doc.documents))
