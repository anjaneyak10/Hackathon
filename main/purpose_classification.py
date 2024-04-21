import pandas as pd
import google.generativeai as genai
import time
import os
from dotenv import load_dotenv

load_dotenv()
readData= pd.read_excel('data_clean.xlsx')
purpose = readData['purpose']
classifications= []
for i in purpose:
    your_api_key = os.getenv('API_KEY')
    genai.configure(api_key=your_api_key)
    try:
        model = genai.GenerativeModel('gemini-pro')
        query = "classify the work type in 1 to 3 words? Classify like modernization, construction, maintenance, manufactring"
        response = model.generate_content(i+query)
        generated_text= ""
        if response:
            generated_text = response.text
        classifications.append(generated_text)
        time.sleep(1)
    except:
        classifications.append("")
df = pd.DataFrame(classifications, columns=['dataClassification'])
df.to_excel('resources/data_classification.xlsx', index=False)
