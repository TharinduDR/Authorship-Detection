import spacy

nlp = spacy.load('it_core_news_sm')


def tokenizer(text):
    tokenized_text = ""
    doc = nlp(text)
    for token in doc:
        tokenized_text += (" " + token.text)

    return tokenized_text
