import Xlreader
import Rephraser
import Wrdwriter
import Util
import UImaker
import docal


def main():

    print("Create time\n")
    # settings = UImaker.Startsetup()
    # path = settings[0]
    # sheet = settings[1]
    # dblvl = settings[2]
    path = "TEST.xlsx"
    sheet = "Sheet1"
    dblvl = 2
    firstrow = 0
    dictionary = Xlreader.XlToDict(path, sheet, firstrow, dblvl)
    dictionary = Rephraser.CEformulasOLD(dictionary, dblvl=dblvl)
    Wrdwriter.WriteWrdOLD(dictionary, dblvl)


if __name__ == main():
    main()
