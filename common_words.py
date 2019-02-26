
def createFile():
    names = open("site_names.txt")
    extensions = open("site_extensions.txt")
    output = open("common_words.txt", "w")
    for i in names:
        for j in extensions:
            concat = i.strip() + "." + j
            output.write(concat)
    # for each in output:
    #     print(each)
