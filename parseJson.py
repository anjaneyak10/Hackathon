import json

# Load the JSON data
with open('contracts.json', 'r') as file:
    parsed_data = json.load(file)

for parsed_data_each_page in parsed_data:
    for agency,contracts in parsed_data_each_page.items():
        print(f"Agency: {agency}")
        for contract in contracts:
            print(f"Contract: {contract}")
