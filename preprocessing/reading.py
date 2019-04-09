def filereader(filename):
    f = open(filename, "r", encoding='cp1250')
    contents = f.read()
    return contents
