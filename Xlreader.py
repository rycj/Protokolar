# import pandas as pd
# test=pd.read_excel('C:\\Users\\Kuba\\Downloads\\LCHI.xlsx',keep_default_na=False)
# # print(test.loc[test.shape[0]-1])
import pylightxl as px
import string
import Util


class Xlreader:
    def __init__(self, path, sheet, firstrow, firstcol):
        self.path = path
        self.sheet = sheet
        self.firstrow = firstrow
        self.firstcol = firstcol
        self.abc = list(string.ascii_uppercase)
        self.formulas = []
        self.dict = {}

    def readXl(self):
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

            self.valuecell = Util.roundstr(
                str(self.source.address(address=self.abc[i] + str(self.firstrow + 2)))
            )

            if self.valuecell:
                self.templist = [self.namecell, self.valuecell, self.formcell]
                self.dict.update({self.idcell: self.templist})
