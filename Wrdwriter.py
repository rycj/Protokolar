import Util
import random

CE_phrases = [
    "Nejprve spočteme ",
    "Poté počítáme ",
    "Dále spočteme ",
    "Jako další počítáme ",
    "Pokračujeme výpočtem ",
    "Nakonec zbývá ještě vypočítat ",
]


def WriteWrd(finalformulas, dblvl):
    transferfile = open("transferfile.txt", "w")
    Util.inform(
        dblvl,
        "Wrdwriter outputting results to .docx\n",
        f"Wrdwriter outputting results to .docx through {transferfile.name}\n",
    )
    for i in range(len(finalformulas)):
        if i == 0:
            transferfile.write(f"{CE_phrases[i]+finalformulas[i]}\n")
        elif i == len(finalformulas) - 1:
            transferfile.write(f"{CE_phrases[len(CE_phrases)-1]+finalformulas[i]}\n")
        else:
            transferfile.write(
                f"{CE_phrases[random.randint(1,len(CE_phrases)-2)]+finalformulas[i]}\n"
            )
    transferfile.close()
