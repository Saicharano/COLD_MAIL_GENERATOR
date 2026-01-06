import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chain import chain
from Portfolio import Portfolio
from utils import clean_text
def create_streamlit_app(llm,Portfolio,clean_text):
    st.title("Cold Email generator")
    url_input = st.text_input("Enter a url: ", value="https://careers.nike.com/nike-inc-product-graphics-design-intern/job/R-71649")
    submit_button = st.button("Generate cold email")

    if submit_button:
        try:
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            jobs = llm.extract_jobs(data)
            for job in jobs:
                skills = job.get('skills',[])
                links = Portfolio.query_links(skills)
                email = llm.write_mail(job,links)
                st.code(email,language='markdown')
        except Exception as e:
            st.error(f"An error occured: {e}")

if __name__ =="__main__":
    chain = chain()
    Portfolio = Portfolio()
    st.set_page_config(layout="wide",page_title="Cold Email Generator")
    create_streamlit_app(chain,Portfolio,clean_text)