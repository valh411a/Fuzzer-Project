
def createFile():
    names = open("site_names.txt")
    extensions = open("site_extensions.txt")
    output = open("common_words.txt", "w")
    nameArray = list(names)
    extArray = list(extensions)
    for i in nameArray:
        for j in extArray:
            concat = i.strip() + "." + j
            output.write(concat)
        output.write("\n")
