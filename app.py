import requests
from bs4 import BeautifulSoup
import streamlit as st
import os
import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()



# genai.configure(api_key=os.environ["GOOGLE_API_KEY"])
genai.configure(api_key="AIzaSyBMyOdPEJwgGdjyingwrEAqCLxaBLecWSg")


extracted_filename = "extracted_data.txt"



def create_vector_db(urls):
    with open(extracted_filename, "w", encoding="utf-8") as file:
        for url in urls:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            extracted_text = soup.get_text().replace('\n', ' ').replace('\t', ' ')
            file.write(extracted_text + " ")

    print(f"Data extracted and saved to '{extracted_filename}'.")



def get_answer(query):
    try:
        with open(extracted_filename, "r", encoding="utf-8") as file:
            data = file.read()

        prompt = f"""
        Based on the following context, please provide a detailed answer to the question posed. Use information only from the context provided and do not include any external knowledge or assumptions.

        CONTEXT:
        {data}

        QUESTION:
        {query}

        Answer:
        """

        model = genai.GenerativeModel(model_name="gemini-1.5-flash")
        response = model.generate_content(prompt)
        
        return response.text.strip()



    except FileNotFoundError:
        return "Error: The extracted data file does not exist. Please process the URLs first."
    except Exception as e:
        return f"An error occurred: {str(e)}"



st.title("Pangle")
st.sidebar.title("News Article URLs")




test_urls = ["https://www.moneycontrol.com/news/business/markets/wall-street-rises-as-tesla-soars-on-ai-optimism-11351111.html",
             "https://saikumaradapa.netlify.app/"]



urls = []
for i in range(2):
    url = st.sidebar.text_input(f"URL {i+1}", test_urls[i])
    if url:
        urls.append(url)



process_url_clicked = st.sidebar.button("Process URLs")
if process_url_clicked:
    create_vector_db(urls)
    st.sidebar.write("URLs processed successfully!")



query = st.text_input("Enter your query:", "What are Sai Kumar's qualifications, certifications, and projects?")



get_answer_clicked = st.button("Get Answer")
if get_answer_clicked:
    if query:
        answer = get_answer(query)
        st.write(answer)
    else:
        st.write("Please enter a query to get an answer.")
