from data.employees import generate_employee_data
#from dotenv import load_dotenv
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
#from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
import logging
from assistant import Assistant
from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
from langchain_groq import ChatGroq
from gui import AssistantGUI
import os


def get_secret_key(key_name):
    """
    Retrieves key securely from Streamlit secrets (Cloud) or os.getenv (Local Dev).
    This function replaces direct reliance on the .env file.
    """
    if key_name in st.secrets:
        return st.secrets[key_name]
    return os.getenv(key_name)

def setup_environment():
    """
    Fetches necessary keys and sets environment variables for LangChain/Groq.
    This replaces load_dotenv().
    """

    groq_key = get_secret_key("GROQ_API_KEY")

    if not groq_key:
        st.error("Deployment Error: GROQ_API_KEY is missing from Streamlit Secrets. Please set it securely.")
        st.stop()
        

    os.environ["GROQ_API_KEY"] = groq_key
    

    langchain_key = get_secret_key("LANGCHAIN_API_KEY")
    if langchain_key:
        os.environ["LANGCHAIN_API_KEY"] = langchain_key
        os.environ["LANGCHAIN_TRACING_V2"] = get_secret_key("LANGCHAIN_TRACING_V2") or "true"
        os.environ["LANGCHAIN_PROJECT"] = get_secret_key("LANGCHAIN_PROJECT") or "RAG_PROJECT"
        logging.info("LangSmith Tracing Enabled.")



if __name__ == "__main__":

    setup_environment() 

    logging.basicConfig(level=logging.INFO)

    st.set_page_config(page_title="Personal Help", page_icon="🖥️", layout="wide")

    @st.cache_data(ttl=3600, show_spinner="Loading Employee Data....")
    def get_user_data():
        return generate_employee_data(1)[0]
    
    @st.cache_resource(ttl=3600, show_spinner="Loading Vector Store....")
    def init_vector_store(pdf_path):
        try:
            loader = PyPDFLoader(pdf_path)
            docs = loader.load()
            text_splitter = RecursiveCharacterTextSplitter(
                chunk_size=2000, chunk_overlap=200
            )
            splits = text_splitter.split_documents(docs)

            embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
            persistent_path = "./data/vectorstore"

            vectorstore = Chroma.from_documents(
                documents=splits,
                embedding=embedding_function,
                persist_directory=persistent_path
            )

            return vectorstore
        except Exception as e:
            logging.error(f"Error initializing vector store: {str(e)}")
            st.error(f"Failed to initialize vector store: {str(e)}")
            return None
        
    customer_data = get_user_data()

    vector_store = init_vector_store("data/portfolio1.pdf")

    if "customer" not in st.session_state:
        st.session_state.customer = customer_data
    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "ai", "content": WELCOME_MESSAGE}]

     

    llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=get_secret_key("GROQ_API_KEY"))
     

    assistant = Assistant(
        system_prompt=SYSTEM_PROMPT,
        llm=llm,
        message_history=st.session_state.messages,
        employee_information=st.session_state.customer,
        vector_store=vector_store,
    )

    gui = AssistantGUI(assistant)
    gui.render()










# from data.employees import generate_employee_data
# from dotenv import load_dotenv
# import streamlit as st
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter
# #from langchain_openai import OpenAIEmbeddings
# from langchain_huggingface import HuggingFaceEmbeddings
# from langchain_chroma import Chroma
# import logging
# from assistant import Assistant
# from prompts import SYSTEM_PROMPT, WELCOME_MESSAGE
# from langchain_groq import ChatGroq
# from gui import AssistantGUI
# import os


# if __name__ == "__main__":

#     load_dotenv()

#     logging.basicConfig(level=logging.INFO)

#     st.set_page_config(page_title="Personal Help", page_icon="🖥️", layout="wide")

#     @st.cache_data(ttl=3600, show_spinner="Loading Employee Data....")
#     def get_user_data():
#         return generate_employee_data(1)[0]
#     
#     @st.cache_resource(ttl=3600, show_spinner="Loading Vector Store....")
#     def init_vector_store(pdf_path):
#         try:
#             loader = PyPDFLoader(pdf_path)
#             docs = loader.load()
#             text_splitter = RecursiveCharacterTextSplitter(
#                 chunk_size=2000, chunk_overlap=200
#             )
#             splits = text_splitter.split_documents(docs)

#             #embedding_function = OpenAIEmbeddings()
#             embedding_function = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
#             persistent_path = "./data/vectorstore"

#             vectorstore = Chroma.from_documents(
#                 documents=splits,
#                 embedding=embedding_function,
#                 persist_directory=persistent_path
#             )

#             return vectorstore
#         except Exception as e:
#             logging.error(f"Error initializing vector store: {str(e)}")
#             st.error(f"Failed to initialize vector store: {str(e)}")
#             return None
#         
#     customer_data = get_user_data()
#     #vector_store = init_vector_store("data/portfolio.pdf")
#     vector_store = init_vector_store("data/portfolio1.pdf")

#     if "customer" not in st.session_state:
#         st.session_state.customer = customer_data
#     if "messages" not in st.session_state:
#         st.session_state.messages = [{"role": "ai", "content": WELCOME_MESSAGE}]

#      

#     #llm = ChatGroq(model="llama-3.1-8b-instant")
#     llm = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=os.getenv("GROQ_API_KEY"))
#      

#     assistant = Assistant(
#         system_prompt=SYSTEM_PROMPT,
#         llm=llm,
#         message_history=st.session_state.messages,
#         employee_information=st.session_state.customer,
#         vector_store=vector_store,
#     )

#     gui = AssistantGUI(assistant)
#     gui.render()
#  this is app.py now tell me the changes and answer here in chat only 



















