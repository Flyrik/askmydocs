import re


def tokenize(chunks):
    list_tokens = []
    for chunk in chunks:
        
        tokens = re.findall(r'\w+', chunk["text"].lower())
        list_tokens.append(tokens)
    
    return list_tokens