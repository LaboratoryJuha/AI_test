from langchain_community.document_loaders import UnstructuredURLLoader
from url_dictionary import URLS_DICTIONARY, COLLECTION_NAME

class DocumentPreparer:
    """_summary_
    preparing documents from url_dictionary.py
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
        self.doc_id = 0

    def add_document_id(self):
        for doc in self.documents:
            doc.page_content = " ".join(doc.page_content.split())  # remove whitespace
            doc.metadata["id"] = self.doc_id
            print(doc.metadata)
            self.doc_id += 1
        return self

    def printDocument(self):
        print(self.documents[0])
        return self

if __name__ == "__main__":
    base_doc = DocumentPreparer()
    base_doc.add_document_id().printDocument()
