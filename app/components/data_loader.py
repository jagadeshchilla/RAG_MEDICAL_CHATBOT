import os
from app.components.pdf_loader import load_pdf_files, create_text_chunks
from app.components.vector_store import save_vector_store
from app.config.config import DB_FAISS_PATH

from app.common.logger import get_logger
from app.common.custom_exception import CustomException

logger = get_logger(__name__)

def process_and_store_pdfs():
    try:
        logger.info("Processing and storing PDFs")
        documents=load_pdf_files()
        text_chunks=create_text_chunks(documents)
        vector_store=save_vector_store(text_chunks)
        logger.info("Vector store created successfully")
        return vector_store
    except Exception as e:
        error_message=CustomException("Error creating vector store",e)
        logger.error(str(error_message))
        return None
    
if __name__ == "__main__":
    process_and_store_pdfs()
    
    
    
