from jy_documents_preparer import UrlDocumentPreparer
from jy_embedding import Embeddings

documents = UrlDocumentPreparer()
embedding_model = Embeddings("sentence-transformers/all-mpnet-base-v2")

embedding_list = embedding_model.start([doc.page_content for doc in documents.documents])
#print('차원', len(embedding_list[0]))
#print('chunk 개수', len(embedding_list))
