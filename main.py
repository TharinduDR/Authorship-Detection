from preprocessing.reading import filereader
from preprocessing.tokenizing import tokenizer
from preprocessing.writing import filewriter


def main():
    text = filereader("Data/Fofi/prefazione.txt")
    tokenized_text = tokenizer(text)
    filewriter(tokenized_text, "Tokenized_Data/Fofi/prefazione.txt")


if __name__ == "__main__":
    main()
