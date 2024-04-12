def Startsetup():
    print("Protokolar initiating...\n")
    print("Hello!\n")
    path = str(input("Please enter the full path to your Excel file:\n"))
    sheet = str(input("Please enter name of the sheet with your data:\n"))
    dblvl = int(
        input(
            "How much debug information should the program give you?\n0 = none\n1=normal\n2=full\n"
        )
    )
    return [path, sheet, dblvl]
