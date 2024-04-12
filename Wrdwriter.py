import Util


def WriteWrd(finalformulas, dblvl):
    transferfile = open("finaldoc.docx", "w")
    Util.inform(
        dblvl,
        "Wrdwriter outputting results to .docx\n",
        f"Wrdwriter outputting results to .docx through {transferfile.name}\n",
    )
    for i in finalformulas:
        transferfile.write(f"{i}\n")
    transferfile.close()
