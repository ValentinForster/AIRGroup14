import json

def transform_data(input_data):
    transformed_data = []
    data = input_data.get('data')

    for item in data:
        paragraphs = item.get('paragraphs')

        for paragraph in paragraphs:
            qas = paragraph.get('qas')
            context = paragraph.get('context')
            document_id = paragraph.get('document_id')

            # Extract the title from the context (first part of the text)
            title, rest_of_context = context.split('\n', 1)

            for qa in qas:
                entry = {
                    "dataset": "German Wikipedia Articles",
                    "question": qa.get('question'),
                    "answers": [ans['text'] for ans in qa.get('answers')],
                    "positive_ctxs": [],
                    "negative_ctxs": [],
                    "hard_negative_ctxs": []
                }

                positive_ctx = {
                    "title": title.strip(),  # Use extracted title and remove leading/trailing spaces
                    "text": rest_of_context.strip(),  # Use the rest of the context without the title
                    "score": 10,  # Arbitrary score for now
                    "title_score": 8,  # Arbitrary score for now
                    "passage_id": str(document_id)
                }

                entry["positive_ctxs"].append(positive_ctx)
                transformed_data.append(entry)

    return transformed_data

# Read the JSON data from file
with open('GermanQuAD_test.json', 'r', encoding='utf-8') as file:
    input_json = json.load(file)

# Transform the data
transformed = transform_data(input_json)

# Save the transformed data to a new JSON file
output_file_name = 'GermanQuAD_test_neue_conversion.json'
with open(output_file_name, 'w', encoding='utf-8') as output_file:
    json.dump(transformed, output_file, indent=4)  # Indent for readability
