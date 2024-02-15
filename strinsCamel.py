def stringToCamel(text):
    words= text.replace('-', '_').split("_")
    return words[text] + ''.join(word.capitalize())