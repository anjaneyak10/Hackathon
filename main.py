import pdfplumber
import tensorflow as tf
import re
from datetime import datetime

from transformers import AutoTokenizer, AutoModelForTokenClassification

# Load the TensorFlow model and tokenizer
model_name = "dslim/bert-base-NER"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForTokenClassification.from_pretrained(model_name)

# Define a function to preprocess text
def preprocess_text(text):
    # Remove unnecessary characters and split into sentences
    text = re.sub(r'[\(\)\[\]]', '', text)
    sentences = re.split(r'[.!?]', text)

    # Tokenize and pad each sentence
    tokenized_sentences = [tokenizer(sentence, return_tensors="tf", padding=True, truncation=True, max_length=512) for sentence in sentences]
    return tokenized_sentences

# Define a function to extract entities using NER
def extract_entities(tokenized_sentences):
    entities = []
    for tokens in tokenized_sentences:
        outputs = model(**tokens)
        predictions = tf.argmax(outputs.logits, axis=-1).numpy()
        input_ids = tf.squeeze(tokens.input_ids).numpy().tolist()
        tokens = tokenizer.convert_ids_to_tokens(input_ids)
        spans = get_entity_spans(predictions.squeeze(), tokens)
        entities.extend([tokenizer.convert_tokens_to_string(tokens[start:end]) for start, end in spans])
    return entities

def get_entity_spans(predictions, tokens):
    entity_spans = []
    current_entity = None
    for idx, (token, prediction) in enumerate(zip(tokens, predictions)):
        if prediction != 0 and current_entity is None:
            current_entity = idx
        elif prediction == 0 and current_entity is not None:
            entity_spans.append((current_entity, idx))
            current_entity = None
    if current_entity is not None:
        entity_spans.append((current_entity, len(tokens)))
    return entity_spans

# Define functions to extract relevant information from entities
def extract_company_names(entities):
    company_names = [entity for entity in entities if entity.endswith("Inc.") or entity.endswith("Corp.") or entity.endswith("LLC")]
    return company_names

def extract_locations(entities):
    locations = [entity for entity in entities if any(location_word in entity for location_word in ["Virginia", "Maryland", "District of Columbia"])]
    return locations

def extract_amounts(text):
    amount_pattern = r'\$\d+,?\d*,?\d+'
    amounts = re.findall(amount_pattern, text)
    return amounts

def extract_dates(text):
    date_pattern = r'(?:January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}'
    dates = re.findall(date_pattern, text)
    parsed_dates = [datetime.strptime(date_str, '%B %d, %Y').date() for date_str in dates]
    return parsed_dates

def extract_contracting_activities(entities):
    contracting_activities = [entity for entity in entities if "Command" in entity or "Army" in entity or "Contracting" in entity]
    return contracting_activities

# Extract data from the PDF
def extract_data_from_pdf(pdf_path):
    contracts = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if "CONTRACTS" in text:
                paragraphs = text.split("\n\n")
                for paragraph in paragraphs:
                    if paragraph.strip():
                        tokenized_sentences = preprocess_text(paragraph)
                        entities = extract_entities(tokenized_sentences)
                        company_names = extract_company_names(entities)
                        locations = extract_locations(entities)
                        amounts = extract_amounts(paragraph)
                        dates = extract_dates(paragraph)
                        contracting_activities = extract_contracting_activities(entities)

                        contract = {
                            "company_names": company_names,
                            "locations": locations,
                            "amounts": amounts,
                            "dates": dates,
                            "contracting_activities": contracting_activities
                        }
                        contracts.append(contract)
    return contracts

# Example usage
pdf_path = "C:/Users/anjan/Downloads/Contracts/9thApril.pdf"
contracts = extract_data_from_pdf(pdf_path)
for i, contract in enumerate(contracts, start=1):
    print(f"Contract {i}:")
    print("Company Names:", contract["company_names"])
    print("Locations:", contract["locations"])
    print("Amounts:", contract["amounts"])
    print("Dates:", contract["dates"])
    print("Contracting Activities:", contract["contracting_activities"])
    print()
