from gensim.models import Word2Vec


def build_model(documents):
    model = Word2Vec(documents, min_count=1)
    return model


def save_model(model, path):
    model.save(path)


def load_model(path):
    model = Word2Vec.load(path)
    return model


def print_model(model):
    print(model)


def get_words(model):
    return list(model.wv.vocab)
