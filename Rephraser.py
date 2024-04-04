class Rephraser:
    def __init__(self, formulas: list, dict: dict):
        self.formulas = formulas
        self.dict = dict

    def rewriteCE(self):
        self.finalformulas = []
        for form in self.formulas:
            form = str(form)
            form = form.replace("$", "")
            formula = form
            for key in self.dict:
                if self.dict.get(key)[2] == formula:
                    sym = self.dict.get(key)[0]
                    val = self.dict.get(key)[1]
            for key in self.dict:
                formula = formula.replace(key, self.dict.get(key)[0])
            formula = formula + form
            for key in self.dict:
                formula = formula.replace(key, self.dict.get(key)[1])
            formula = sym + formula + "=" + val
            print(formula)
            self.finalformulas.append(formula)
