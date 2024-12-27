from langchain.text_spitter import RecursiveCharacTextSplitter # type: ignore
from langchain.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.prompts import PromtTemplate
from langchain.chains.question_answering import load_qa_chain
import os
import google.genrativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from utlis import 

genai.configure(api_key="AIzaSyDFVSB5kLpqut7GDee-WqSHPGuXTd4GF3E")
os.environ["GOOGLE_API_KEY"]="AIzaSyDFVSB5kLpqut7GDee-WqSHPGuXTd4GF3E"

def get_model_response(file,query):

    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=200)
    context ="\n\n".join(str(p.page_content)for p in file)

    data =text_splitter.split_text(context)

    embeddings=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    searcher = Chroma.from_texts(data,embeddings).as_retriever()

    q="which employer has maximum salary"
    records= searcher.get_relevant_documents(q)
    print(records)

    prompt_tempalte=""""""

     You ,,,have to answer the question from the previous context and make sure that you provide all the details
       context:{context}?\n
        question:{question}\n
        Answer:
    """"""

     prompt=PromtTemplate(template=prompt_tempalte,input_variables=["context","question"]
                          )
    model=ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.9)
    chain= load_qa_chain(model,chain_type="stuff",prompt=prompt)

    response=chain(
      {
        "input_documents":records,
        "question": query
      }
        return_only_outputs=True)
    return response["output_text"] 
    
       


     