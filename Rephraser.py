import Util


def formsubssym(dictionary: dict) -> list:
    formulas = []
    for i in dictionary:
        form = dictionary.get(i)[2]
        if form:
            for key in dictionary:
                if dictionary.get(key)[2] == form:
                    sym = dictionary.get(key)[0]
            form = form.replace("$", "")
            for key in dictionary:
                formula = formula.replace(key, sym)
        formulas.append(formula)
    return formulas


def formsubsval(dictionary: dict) -> list:
    formulas = []
    for i in dictionary:
        form = dictionary.get(i)[2]
        if form:
            for key in dictionary:
                if dictionary.get(key)[2] == form:
                    val = dictionary.get(key)[1]
            form = form.replace("$", "")
            for key in dictionary:
                formula = formula.replace(key, val)
        formulas.append(formula)
    return formulas


def FLformulas(dictionary: dict, dblvl: int) -> list:
    syms = formsubssym(dictionary)
    finalforms = []
    for i in range(len(syms)):
        key = dictionary.keys()[i]
        formula = dictionary.get(key)[0] + syms[i]
        finalforms.append(formula)
    return finalforms


def CEformulas(dictionary: dict, dblvl: int) -> list:
    syms = formsubssym(dictionary)
    vals = formsubsval(dictionary)
    finalforms = []
    for i in range(len(vals)):
        key = dictionary.keys()[i]
        formula = (
            dictionary.get(key)[0] + syms[i] + vals[i] + "=" + dictionary.get(key)[1]
        )
        finalforms.append(formula)
    return finalforms


def rewritefracs(formula: str) -> str:
    list = formula.split("/")

    # tohle bude mega hard
    ...


# ____________________________________________________________________________________________________________________________________
# obsolete, keeping it to see if it can be useful later
def CEformulasOLD(dictionary: dict, dblvl: int) -> dict:
    Util.inform(
        dblvl,
        f"Rephraser initiating translation of {len(dictionary)+1} formulas to calculation example\n",
        f"Rephraser initiating translation of {dictionary} \nto calculation example\n",
    )
    for i in dictionary:
        form = dictionary.get(i)[2]
        print(type(form))
        if form:
            for key in dictionary:
                if dictionary.get(key)[2] == form:
                    sym = dictionary.get(key)[0]
                    val = dictionary.get(key)[1]
            form = form.replace("$", "")
            formula = form
            for key in dictionary:
                formula = form.replace(key, dictionary.get(key)[0]) + form.replace(
                    key, dictionary.get(key)[1]
                )
            # formula = formula + form
            # for key in dictionary:
            #     formula = formula.replace(key, dictionary.get(key)[1])
            # for key in dictionary:
            #     formula = form.replace(key, dictionary.get(key)[0]) + form.replace(
            #         key, dictionary.get(key)[1]
            #     )
            formula = sym + formula + "=" + val
            templist = [dictionary.get(i)[0], dictionary.get(i)[1], formula]
            dictionary.update({i: templist})
    Util.inform(
        dblvl,
        "Rephraser completed translation to calculation example\n",
        f"Rephraser completed translation to calculation example:\n{dictionary}\n",
    )
    return dictionary
