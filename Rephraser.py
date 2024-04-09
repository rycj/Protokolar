def rewriteCE(formulas: list[str], dictionary: dict):
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
        formula = sym + formula + "=" + val
        finalformulas.append(formula)
    return finalformulas
