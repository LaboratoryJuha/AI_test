from documentsPreparer import DocumentPreparer
from langchain_huggingface import HuggingFaceEmbeddings

documentPreparer = DocumentPreparer()
documentList = documentPreparer.clean_documents().printDocument()


from langchain_text_splitters import RecursiveCharacterTextSplitter
textSplitter = RecursiveCharacterTextSplitter(chunk_size=800,
                                              chunk_overlap=150,
                                              add_start_index=True,
                                            )
chunkDocumentList = textSplitter.split_documents(documentPreparer.documents)
# print(len(chunkDocumentList))

huggingFace = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
embedding_list = huggingFace.embed_documents([chunk.page_content for chunk in chunkDocumentList])

print(len(embedding_list))
# print(embedding_list)

