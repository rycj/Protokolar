import Util
import random

CE_phrases = [
    "Nejprve spocteme ",
    "Pote pocitame ",
    "Dale spocteme ",
    "Jako dalsi pocitame ",
    "Pokracujeme vypoctem ",
    "Nakonec zbyva jeste vypocitat ",
]


# def makeLateX(forms):
#     file="plchldr"
#     writeintro(file)
#     writeFL(file,forms)
#     writeCE(file,forms)
#     # writeSL(file)


# def writeintro(file)->None:
#     file.write('\documentclass{article}\n'+
#                '\usepackage[czech]{babel}\n'+
#                '\usepackage{amsmath}\n'+
#                '\usepackage{graphicx}\n'+
#                '\usepackage[colorlinks=true, allcolors=blue]{hyperref}\n'+
#                'begin{document}')


# def writeFL(file,FLforms)->None:
#     FL='\n\section{Seznam vztahů}'
#     for formula in FLforms:
#         FL+='\n'+formula
#     file.write(FL)


# def writeCE(file,FLforms)->None:
#     FL='\n\section{Seznam vztahů}'
#     for formula in FLforms:
#         FL+='\n'+formula
#     file.write(FL)

# def writeSL(): ...
# not sure if possible...


# ____________________________________________________________________________________________________________________________________
# obsolete, keeping it to see if it can be useful later
def WriteWrdOLD(dictionary: dict, dblvl: int):
    transferfile = open("transferfile.txt", "w")
    Util.inform(
        dblvl,
        "Wrdwriter outputting results to .docx\n",
        f"Wrdwriter outputting results to .docx through {transferfile.name}\n",
    )
    for i in range(len(dictionary)):
        form = dictionary.get(list(dictionary.keys())[i])[2]
        if form != None:
            if i == 0:
                transferfile.write(f"{CE_phrases[i]+form}\n")
            elif i == len(dictionary) - 1:
                transferfile.write(f"{CE_phrases[len(CE_phrases)-1]+form}\n")
            else:
                transferfile.write(
                    f"{CE_phrases[random.randint(1,len(CE_phrases)-2)]+form}\n"
                )
    transferfile.close()
