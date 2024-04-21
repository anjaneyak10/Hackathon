import google.generativeai as genai
import json
import util
import os
from dotenv import load_dotenv

load_dotenv()
def gemini_data_extraction(text):
    your_api_key = os.getenv('API_KEY')
    genai.configure(api_key=your_api_key)
    model = genai.GenerativeModel('gemini-pro')
    query = "give me json format - do not generate new data- who is the contractor? what is the location? what is the cost? what is the purpose? WHhen will the work be completed? where will the work be performed? What is the contract number? Give me the contracting activity?"
    response = model.generate_content(text+query)
    generated_text= ""
    if response :
        generated_text = response.text
    return generated_text

# Load the JSON data
with open('resources/contracts.json', 'r') as file:
    parsed_data = json.load(file)

def generate_csv():
    for parsed_data_each_page in parsed_data:
        for agency,contracts in parsed_data_each_page.items():
            for contract in contracts:
                data = gemini_data_extraction(contract)
                data = util.clean_data(data)
                util.extract_and_convert_to_csv(agency, data, "resources/data.csv")
# generate_csv()
