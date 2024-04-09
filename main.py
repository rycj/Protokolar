import Xlreader
import Rephraser
import Wrdwriter


def main():
    firstcol = 2
    firstrow = 0
    dictionary = Xlreader.readXl(
        "C:\\Users\\kubik\\Downloads\\LCHI.xlsx", "H", firstrow, firstcol
    )[0]
    formulas = Xlreader.readXl(
        "C:\\Users\\kubik\\Downloads\\LCHI.xlsx", "H", firstrow, firstcol
    )[1]
    finalformulas = Rephraser.rewriteCE(formulas, dictionary)
    Wrdwriter.WriteWrd(finalformulas)


if __name__ == main():
    main()
