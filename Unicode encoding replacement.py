def replace_unicode_chars(file_path):
    replacements = {
        '\\u00df': 'ß',
        '\\u00e4': 'ä',
        '\\u00f6': 'ö',
        '\\u00fc': 'ü'
    }

    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Perform the replacements
    for unicode_char, replacement in replacements.items():
        content = content.replace(unicode_char, replacement)

    # Write the updated content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

file_path = 'GermanQuAD_test_neue_conversion.json'
replace_unicode_chars(file_path)
