def filewriter(text, filename):
    f = open(filename, "wb+")
    f.write(text.encode('cp1250'))
    f.close()
