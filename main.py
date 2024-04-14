import Xlreader
import Rephraser
import Wrdwriter
import Util
import UImaker


def main():

    print("Create time\n")
    # settings = UImaker.Startsetup()
    # path = settings[0]
    # sheet = settings[1]
    # dblvl = settings[2]
    path = "TEST.xlsx"
    sheet = "Sheet1"
    dblvl = 1
    firstrow = 0
    [dictionary, formulas] = [
        Xlreader.readXl(path, sheet, firstrow, dblvl)[0],
        Xlreader.readXl(path, sheet, firstrow, 0)[1],
    ]
    finalformulas = Rephraser.rewriteCE(formulas, dictionary, dblvl=dblvl)
    Wrdwriter.WriteWrd(finalformulas, dblvl)


if __name__ == main():
    main()
