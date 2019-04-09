def filewriter(text, filename):
    f = open(filename, "w+")
    f.write(text)
    f.close()
