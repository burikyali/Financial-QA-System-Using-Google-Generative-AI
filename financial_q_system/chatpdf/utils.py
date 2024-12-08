from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")


def get_pdf_text(pdf_files):
    text = ""
    for pdf in pdf_files:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    return splitter.split_text(text)


def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    store = FAISS.from_texts(text_chunks, embedding=embeddings)
    store.save_local("faiss_index")


def get_response(query):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    store = FAISS.load_local(
        "faiss_index", embeddings, allow_dangerous_deserialization=True
    )
    docs = store.similarity_search(query)

    prompt_template = """
    You are a highly knowledgeable financial advisor with expertise in financial systems, analysis, and decision-making. Based on the following context, provide a detailed and accurate answer to the question. Ensure the answer is relevant, clear, and professional. If the answer cannot be found in the provided context, respond with: 'Answer is not available in the context.'

    Context: {context}

    Question: {question}

    Answer:
    """
    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )
    model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt)

    result = chain(
        {"input_documents": docs, "question": query}, return_only_outputs=True
    )
    return result["output_text"]
