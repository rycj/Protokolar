# import pandas as pd
# test=pd.read_excel('C:\\Users\\Kuba\\Downloads\\LCHI.xlsx',keep_default_na=False)
# # print(test.loc[test.shape[0]-1])
import pylightxl as px
import string


class FormulaWriter:
    def __init__(self, path, sheet, firstrow, firstcol):
        self.path = path
        self.sheet = sheet
        self.firstrow = firstrow
        self.firstcol = firstcol
        self.abc = list(string.ascii_uppercase)
        self.formulas = []
        self.dict = {}

    def _round(self, value):
        decnum = 0
        decbool = False
        roundedvalue = str()
        for i in value:
            if i != "." and decbool == False:
                roundedvalue += i
                continue
            elif decbool == False:
                roundedvalue += i
                decbool = True
                continue
            if decnum < 3:
                if i == "0" and decnum == 0:
                    ...
                else:
                    decnum += 1
                roundedvalue += i
        value = roundedvalue
        return value

    def read(self):
        self.source = px.readxl(fn=self.path).ws(
            ws=self.sheet
        )  # this shit read file and define source as a current sheet :>
        for i in range((self.firstcol), len(self.abc)):

            self.formcell = self.source.address(
                address=self.abc[i] + str(self.firstrow + 2), output="f"
            )
            if self.formcell != "=" and self.formcell != "":
                self.formulas.append(str(self.formcell))

            self.idcell = str(self.abc[i] + str(self.firstrow + 2))

            self.namecell = str(
                self.source.address(address=self.abc[i] + str(self.firstrow + 1))
            )

            self.valuecell = self._round(
                str(self.source.address(address=self.abc[i] + str(self.firstrow + 2)))
            )

            if self.valuecell:
                self.templist = [self.namecell, self.valuecell, self.formcell]
                self.dict.update({self.idcell: self.templist})

    def rewrite(self):
        self.finalformulas = []
        for form in self.formulas:
            formula = str(form)
            for key in self.dict:
                if self.dict.get(key)[2] == formula:
                    sym = self.dict.get(key)[0]
                    val = self.dict.get(key)[1]
            formula = formula.replace("$", "")
            for key in self.dict:
                formula = formula.replace(key, self.dict.get(key)[0])
            formula = formula + str(form)
            formula = formula.replace("$", "")
            for key in self.dict:
                formula = formula.replace(key, self.dict.get(key)[1])
            formula = sym + formula + "=" + val
            print(formula)
            self.finalformulas.append(formula)


h = FormulaWriter("C:\\Users\\Kuba\\Downloads\\LCHI.xlsx", "Sheet1", 0, 0)
h.read()
h.rewrite()
