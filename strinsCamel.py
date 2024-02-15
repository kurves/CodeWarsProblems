def stringToCamel(text):
    words= text.replace('-', '_').split("_")
    return words[text] + ''.join(word.capitalize()) for words in words[1:]