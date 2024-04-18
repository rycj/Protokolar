import pylightxl as px
import string
import Util


def XlToDict(path: str, sheet: str, firstrow: int, dblvl: int) -> dict:
    abc = list(string.ascii_uppercase)
    formulas = []
    dictionary = {}
    source = px.readxl(fn=path).ws(ws=sheet)
    Util.inform(
        dblvl,
        f"Xlreader reading Excel file '{path}'\n",
        f"Xlreader reading Excel file '{path}', sheet '{sheet}'\n",
    )
    for i in range(len(abc)):

        formcell = source.address(address=abc[i] + str(firstrow + 2), output="f")
        if formcell != "=" and formcell != "":
            formulas.append(str(formcell))

        idcell = str(abc[i] + str(firstrow + 2))

        namecell = str(source.address(address=abc[i] + str(firstrow + 1)))

        valuecell = Util.roundliza(
            str(source.address(address=abc[i] + str(firstrow + 2))), dblvl
        )

        if valuecell:
            if formcell != "=":
                templist = [namecell, valuecell, formcell]
            else:
                templist = [namecell, valuecell, None]
            dictionary.update({idcell: templist})
    Util.inform(
        dblvl,
        f"Xlreader found {len(dictionary)+1} columns and {len(formulas)+1} formulas\n",
        f"Xlreader found {len(dictionary)+1} columns,\ncreated list of formulas \n{formulas} \nand dictionary \n{dictionary}\n",
    )
    return dictionary
