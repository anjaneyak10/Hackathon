import requests
from bs4 import BeautifulSoup
import json

# Check if the request was successful (status code 200)
def get_contracts_from_single_page(url):
    response = requests.get(url)
    contracts_data = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        sections = soup.find_all("p", style="text-align: center;")
        for section in sections:
            title = section.find("strong").text.strip()
            section_contracts = []
            contracts = section.find_next_siblings("p")
            i = 0
            while i <len(contracts):
                if contracts[i].find("strong"):
                    contracts_data[title] = section_contracts
                    title = contracts[i].find("strong").text.strip()
                    section_contracts=[]
                else:
                    contract_data = contracts[i].text.strip()
                    if not contract_data.startswith("*Small Business"):
                        section_contracts.append(contract_data)
                i += 1
            contracts_data[title] = section_contracts


    else:
        print("Failed to retrieve webpage:", response.status_code)
    print(contracts_data)
    with open("contracts.json", "a") as json_file:
        json.dump(contracts_data, json_file, indent=4)
        json_file.write(", ")

def get_urls_from_main_page():
    for i in range(12,20):
        url = f"https://www.defense.gov/News/Contracts/?Page={i}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            article_urls = []
            for tag in soup.find_all('listing-titles-only'):
                article_url = tag.get('article-url')
                article_urls.append(article_url)
                get_contracts_from_single_page(article_url)
        print(article_urls)

get_urls_from_main_page()
