def afiseaza(tabla):
    print()
    for i in range(3):
        for j in range(3):
            print(tabla[i][j], end=" ")
        print()
    print()


def citeste_mutare(tabla, jucator):
    while True:
        try:
            linie = int(input(f"Jucatorul {jucator}, introdu linia (0-2): "))
            coloana = int(input(f"Jucatorul {jucator}, introdu coloana (0-2): "))

            if linie < 0 or linie > 2 or coloana < 0 or coloana > 2:
                print("Coordonate invalide!")
            elif tabla[linie][coloana] != ".":
                print("Pozitia este ocupata!")
            else:
                return linie, coloana
        except ValueError:
            print("Introdu numere intregi!")


def stare_joc(tabla):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] != ".":
            return tabla[i][0]

    for j in range(3):
        if tabla[0][j] == tabla[1][j] == tabla[2][j] != ".":
            return tabla[0][j]

    if tabla[0][0] == tabla[1][1] == tabla[2][2] != ".":
        return tabla[0][0]

    if tabla[0][2] == tabla[1][1] == tabla[2][0] != ".":
        return tabla[0][2]

    for i in range(3):
        for j in range(3):
            if tabla[i][j] == ".":
                return "CONTINUA"

    return "EGAL"


tabla = [
    [".", ".", "."],
    [".", ".", "."],
    [".", ".", "."]
]

jucator = "X"

while True:
    afiseaza(tabla)

    linie, coloana = citeste_mutare(tabla, jucator)
    tabla[linie][coloana] = jucator

    rezultat = stare_joc(tabla)
    if rezultat != "CONTINUA":
        break

    if jucator == "X":
        jucator = "O"
    else:
        jucator = "X"

afiseaza(tabla)

if rezultat == "EGAL":
    print("Joc egal!")
else:
    print("A castigat jucatorul", rezultat)


