from Xlreader import Xlreader
from Rephraser import Rephraser
import Wrdwriter


def main():
    reader = Xlreader("C:\\Users\\kubik\\Downloads\\LCHI.xlsx", "H", 0, 0)
    reader.readXl()
    rephrase = Rephraser(reader.formulas, reader.dict)
    rephrase.rewriteCE()
    print(rephrase.finalformulas)


if __name__ == main():
    main()
