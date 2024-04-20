from openai import OpenAI
client = OpenAI(api_key="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")
# Set your OpenAI API key

# Define the text to analyze
text = "Honeywell International Inc., Clearwater, Florida, has been awarded a maximum $70,000,000 firm-fixed-price, indefinite-delivery/indefinite-quantity contract to produce spare parts in support of the Radar Altimeter Common Core APN-209 receiver transmitters and indicator receiver transmitters spares and repairs. This was a sole-source acquisition using 10 U.S. Code 3204 (a)(1), as stated in Federal Acquisition Regulation 6.302-1 (a)(1). This is a five-year base contract with three one-year option periods. The performance completion date is Oct. 29, 2029. Using military service is Army. Type of appropriation is fiscal 2024 through 2029 Army working capital funds. The contracting activity is the Defense Logistics Agency Land and Maritime, Aberdeen Proving Ground, Maryland (SPRBL1-24-D-0007)."
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "The following is a contract summary:"},
        {"role": "user", "content": text+"give me json format who is the contractor? what is the location? what is the cost? what is the purpose? WHhen will the work be completed? where will the work be performed? What is the contract number?"},
    ],
    )

code = response.choices[0].message.content
print(code)
#
# # Send a request to the OpenAI API for named entity recognition
#
#
# # Parse the response to extract the data values
# organization = ""
# location = ""
# cost = ""
# purpose = ""
#
# # Extract entities from the response
# for entity in response['choices'][0]['document']['entities']:
#     if entity['type'] == 'Organization':
#         organization = entity['text']
#     elif entity['type'] == 'Location':
#         location = entity['text']
#     elif entity['type'] == 'Money':
#         cost = entity['value']
#
# # Extract the purpose from the text
# # Assuming the purpose follows the format "for the [purpose]"
# purpose_start_index = text.find("for the") + len("for the")
# purpose = text[purpose_start_index:].strip()
#
# # Print the extracted information
# print("Contractor Name:", organization)
# print("Location:", location)
# print("Cost:", cost)
# print("Purpose:", purpose)
