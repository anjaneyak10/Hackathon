import requests
from bs4 import BeautifulSoup
import json

# This method will get the contracts from a single page. This will store json values in a contracts.json file.
#We get the data as agency names and their contracts
# We will then process the contracts to extract valuable information
def get_contracts_from_single_page(url):
    response = requests.get(url)
    contracts_data = {}
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        sections = soup.find_all("p", style="text-align: center;")
        for section in sections:
            # All the agency names are in bold, so we will separate them
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
    with open("resources/contracts.json", "a") as json_file:
        json.dump(contracts_data, json_file, indent=4)
        json_file.write(", ")

# This method will get the urls of the contracts from the main page
def get_urls_from_main_page():
    # We will go through all pages containing the links of the contracts
    for i in range(0,2):
        url = f"https://www.defense.gov/News/Contracts/?Page={i}"
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, "html.parser")
            article_urls = []
            # We will get all the links to the contracts in article_urls
            for tag in soup.find_all('listing-titles-only'):
                article_url = tag.get('article-url')
                article_urls.append(article_url)
                get_contracts_from_single_page(article_url)
get_urls_from_main_page()
