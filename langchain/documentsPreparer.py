from langchain_community.document_loaders import UnstructuredURLLoader
from url_dictionary import URLS_DICTIONARY, COLLECTION_NAME

class DocumentPreparer:
    """
    preparing documents from url_dictionary.py\n
    check your url_dictionary.py

    using pkg
        pip install -U langchain
        pip install -U langchain-community
        pip install -U unstructured
    """

    def __init__(self):
        self.loader = UnstructuredURLLoader(
            urls=list(URLS_DICTIONARY.values()),
            mode="single",              # "single" 또는 "elements"
            show_progress_bar=True,      # 진행 상황 표시 여부
        )
        self.documents = self.loader.load()

    def clean_documents(self):
        for doc in self.documents:
            doc.page_content = " ".join(doc.page_content.split()) 
            print(doc.metadata)
        return self

# 필요하다면 여기서 형태소화 작업 추가 필요
    def printDocument(self):
        print(self.documents[0])
        return self

if __name__ == "__main__":
    base_doc = DocumentPreparer()
    base_doc.clean_documents().printDocument()
