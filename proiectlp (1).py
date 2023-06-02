import random

def afiseaza_tabla(tabla):
    for rand in tabla:
        for element in rand:
            print(element, end=" ")
        print()

def creaza_tabla():
    tabla = []
    for i in range(3):
        rand = []
        for j in range(3):
            rand.append('-')
        tabla.append(rand)
    return tabla

def get_random_first_player():
    return random.choice(['X', 'O'])

def ocupa_loc(tabla, rand, coloana, jucator):
    if tabla[rand][coloana] == '-':
        tabla[rand][coloana] = jucator
        return True
    return False

def castiga_jucatorul(tabla, jucator):
    for i in range(3):
        if tabla[i][0] == tabla[i][1] == tabla[i][2] == jucator:
            return True
        if tabla[0][i] == tabla[1][i] == tabla[2][i] == jucator:
            return True
    if tabla[0][0] == tabla[1][1] == tabla[2][2] == jucator:
        return True
    if tabla[0][2] == tabla[1][1] == tabla[2][0] == jucator:
        return True
    return False

def tabla_plina(tabla):
    for rand in tabla:
        for element in rand:
            if element == '-':
                return False
    return True

def schimba_jucatorul(jucator):
    return 'X' if jucator == 'O' else 'O'

def start():
    tabla = creaza_tabla()

    jucator = get_random_first_player()
    while True:
        print(f"Este randul jucatorului {jucator}")

        afiseaza_tabla(tabla)

        # Preluam input-ul de la utilizator
        rand, coloana = list(map(int, input("Introduceti numarul randului si coloanei pentru a ocupa un loc: ").split()))
        rand -= 1
        coloana -= 1

        # Ocupam locul daca este valid
        if ocupa_loc(tabla, rand, coloana, jucator):
            # Verificam daca jucatorul curent a castigat
            if castiga_jucatorul(tabla, jucator):
                print(f"Jucatorul {jucator} a castigat jocul!")
                break

            # Verificam daca jocul s-a incheiat cu remiza
            if tabla_plina(tabla):
                print("Jocul s-a incheiat cu remiza!")
                break

            # Schimbam jucatorul
            jucator = schimba_jucatorul(jucator)
        else:
            print("Locul este deja ocupat. Selectati un alt loc.")

# Incepem jocul
start()