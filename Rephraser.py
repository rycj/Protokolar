import Util


def rewriteCE(formulas: list[str], dictionary: dict, dblvl) -> list:
    Util.inform(
        dblvl,
        f"Rephraser initiating translation of {len(formulas)+1} formulas to calculation example\n",
        f"Rephraser initiating translation of {formulas} \nto calculation example\n",
    )
    finalformulas = []
    for form in formulas:
        for key in dictionary:
            if dictionary.get(key)[2] == form:
                sym = dictionary.get(key)[0]
                val = dictionary.get(key)[1]
        form = form.replace("$", "")
        formula = form
        for key in dictionary:
            formula = formula.replace(key, dictionary.get(key)[0])
        formula = formula + form
        for key in dictionary:
            formula = formula.replace(key, dictionary.get(key)[1])
        # for key in dictionary:
        #     formula = form.replace(key, dictionary.get(key)[0]) + form.replace(
        #         key, dictionary.get(key)[1]
        #     )
        formula = sym + formula + "=" + val
        finalformulas.append(formula)
    Util.inform(
        dblvl,
        "Rephraser completed translation to calculation example\n",
        f"Rephraser completed translation to calculation example:\n{finalformulas}\n",
    )
    return finalformulas
