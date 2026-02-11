from langchain_huggingface import HuggingFaceEmbeddings

class Embeddings:
  def __init__(self, model_name):
    self.hugging_face = HuggingFaceEmbeddings(model_name=model_name)

  def start(self, document_list):
    """
    document_list = {
      "documents": ["문서1", "문서2", ...],
      "metadatas": [{"source": "url1"}, {"source": "url2"}, ...],
    }
    """
    embedding_document = self.hugging_face.embed_documents(document_list)
    return embedding_document


if __name__ == "__main__":
  from jy_documents_preparer import UrlDocumentPreparer
  document_preparer = UrlDocumentPreparer()
  embed_documents = Embeddings("sentence-transformers/all-mpnet-base-v2")
  print(len(embed_documents.start(
        [doc.page_content for doc in document_preparer.documents]
    )))