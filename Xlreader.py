import pylightxl as px
import string
import Util


def readXl(path, sheet, firstrow, firstcol):
    abc = list(string.ascii_uppercase)
    formulas = []
    dictionary = {}
    source = px.readxl(fn=path).ws(
        ws=sheet
    )  # this shit read file and define source as a current sheet :>
    for i in range(len(abc)):

        formcell = source.address(address=abc[i] + str(firstrow + 2), output="f")
        if formcell != "=" and formcell != "":
            formulas.append(str(formcell))

        idcell = str(abc[i] + str(firstrow + 2))

        namecell = str(source.address(address=abc[i] + str(firstrow + 1)))

        valuecell = Util.roundstr(
            str(source.address(address=abc[i] + str(firstrow + 2)))
        )

        if valuecell:
            templist = [namecell, valuecell, formcell]
            dictionary.update({idcell: templist})
    return [dictionary, formulas]
