
sudo = [
    [1, 0, 0, 2, 0, 0, 3, 0, 0],
    [0, 1, 0, 0, 2, 0, 0, 3, 0],
    [0, 4, 0, 0, 0, 0, 0, 0, 0],
    [4, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
erreur = 0

# Afficher la grille
def affichage(sudo) :
    for i in range(len(sudo)):
        print(sudo[i])

# Vérifie s'il n'y a pas 2 fois le même chiffre dans une ligne, (hormis 0)
def lignes(sudo, erreur):
    faux = []
    for i in range(9) :
        bon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9) :
            if sudo[i][j] in bon :
                bon.remove(sudo[i][j])
            elif sudo[i][j] != 0 :
                faux.append((i, j))
                erreur += 1
    if len(faux) != 0 :
        print(f'Il y a des erreurs aux coordonnées: {faux}')
    print(f'erreur : {erreur}')
    return erreur
    
# Vérifie s'il n'y a pas 2 fois le même chiffre dans une colonne (hormis 0)
def colonnes(sudo, erreur) :
    faux = []
    for i in range(9) :
        bon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for j in range(9) :
            if sudo[j][i] in bon :
                bon.remove(sudo[j][i])
            elif sudo[j][i] != 0 :
                faux.append((i, j))
                erreur += 1
    if len(faux) != 0 :
        print(f'Il y a des erreurs aux coordonnées: {faux}')
    print(f'erreur : {erreur}')
    return erreur

# Vérifie les carrés de 3 par 3
def carres(sudo, erreur) :
    erreur_c = []

    for y in range(0,7,3) :
        for x in range(0,7,3) : 
            bon = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for i in range(y , y+3) :
                for j in range(x, x+3) :
                    if sudo[i][j] in bon :
                        bon.remove(sudo[i][j])
                    elif sudo[i][j] != 0 :
                        erreur_c.append((int(x/3), int(y/3)))
                        erreur += 1
    if len(erreur_c) != 0 :
        print(f'Il y a des erreurs dans les carrés de coordonnées suivantes: {erreur_c}')
    print(f'erreur : {erreur}')
    return erreur

# Vérifie s'il n'y a aucune incohérence 
def incoherances(sudo, erreur) :
    incoherances = []
    bon = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(9) :
        for j in range(9) :
            if sudo[i][j] not in bon :
                incoherances.append((i , j))
                erreur += 1
    if len(incoherances) != 0 :
        print(f'Il y a des incohérances au coordonnées suivantes: {incoherances}')
    print(f'erreur : {erreur}')
    return erreur




# Dicte les cases n'ayant pas de valeur 
def cases_vides(sudo) :
    coo_cases_vides = []
    DETAIL = 'n'
    nb_0 = 0
    for i in range(9) :
        if DETAIL == 'y' :
            for j in range(9) :
                if sudo[j][i] == 0 :
                    coo_cases_vides.append((i+1, j+1))
                    nb_0 += 1
        elif DETAIL == 'n' :
            for j in range(9) :
                if sudo[j][i] == 0 :
                    nb_0 += 1
    if DETAIL == 'n' :
        print(f"Il y a {nb_0} cases vides dans votre sudoku")
    if DETAIL == 'y' :
        print(f'Les cases de coordonnées suivantes sont vides: {coo_cases_vides}')
    return nb_0

# Vérifie si le sudoku est bon
def correct(sudo, erreur, nb_0) :
    if (nb_0!=0) and (erreur != 0) :
        print("Attention ! Ce sudoku n'est pas complété")

    elif (nb_0 == 0) and (erreur != 0) :
        print(f"Quasiment ! Ce sudoku est rempli mais avec {erreur} erreur(s)")

    elif (nb_0 == 0) and (erreur == 0) :
        print("Bravo ! Ce sudoku est correct")
    return erreur


erreur = lignes(sudo, erreur)
erreur = colonnes(sudo, erreur)
erreur = carres(sudo, erreur)
erreur = incoherances(sudo,erreur)
nb_0 = cases_vides(sudo)
erreur = correct(sudo, erreur, nb_0)









