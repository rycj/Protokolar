import os


def WriteWrd(finalformulas):
    transferfile = open("transferfile.txt", "w")
    for i in finalformulas:
        transferfile.write(f"{i}\n")
    transferfile.close()
    os.system("docal transferfile.txt -o finaldoc.docx")
