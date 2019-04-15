import numpy as np
import spacy

from preprocessing.tokenizing import tokenizer

nlp = spacy.load('it_core_news_sm')


def sentence_splitter(text):
    sentences = list()
    text_sentences = nlp(text)
    for sentence in text_sentences.sents:
        sentences.append(tokenizer(sentence.text))

    return sentences
