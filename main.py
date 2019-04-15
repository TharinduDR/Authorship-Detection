import os

from ml.w2v import build_model, save_model, print_model, get_words
from preprocessing.reading import filereader
from preprocessing.sentence_splitter import sentence_splitter


def main():
    text = ""
    author = "Fofi"
    data_folder = "Data"
    for filename in os.listdir(os.path.join(data_folder, author)):
        text = text + filereader(os.path.join(data_folder, author, filename))

    sentences = sentence_splitter(text)

    model = build_model(sentences)
    print_model(model)
    print(get_words(model))
    save_model(model, os.path.join("Models", author + ".bin"))


if __name__ == "__main__":
    main()
