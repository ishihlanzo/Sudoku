sudo = [
    [1,0,0,2,0,0,3,0,0],
    [0,1,0,0,2,0,0,3,0],
    [0,4,0,0,0,0,0,0,0],
    [4,0,0,0,0,0,0,0,0],
    [0,0,4,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]
erreur = 0

#afficher la grille

for i in range(len(sudo)) :
    print(sudo[i])

#vérifie si il y a pas 2 fois le même chiffre dans une ligne, (hors mis 0)

for i in range(9) :
    bon = [1,2,3,4,5,6,7,8,9]
    for j in range(9) :
        if sudo[i][j] in bon :
            bon.remove(sudo[i][j])
        elif sudo[i][j] != 0 :
            print(f"Il y a une erreur aux coordonné {i} : {j}")
            erreur += 1
    
#vérifie si il y a pas 2 fois le même chiffre dans une collone, (hors mis 0)

for i in range(9) :
    bon = [1,2,3,4,5,6,7,8,9]
    for j in range(9) :
        if sudo[j][i] in bon :
            bon.remove(sudo[j][i])
        elif sudo[j][i] != 0 :
            print(f"Il y a une erreur aux coordonné {i} : {j}")
            erreur += 1

#vérifie les carré de 3 par 3

erreur_c = []

for y in range(0,7,3) :
    for x in range(0,7,3) : 
        bon = [1,2,3,4,5,6,7,8,9]
        for i in range(y , y+3) :
            for j in range(x, x+3) :
                if sudo[i][j] in bon :
                    bon.remove(sudo[i][j])
                elif sudo[i][j] != 0 :
                    erreur_c.append((int(x/3), int(y/3)))
                    erreur += 1
if len(erreur_c) != 0 :
    print("Il y a des erreur dans les carrés de coordonnées suivante : ")
    print(erreur_c)

#verifie si il y a aucune icohérence 

bon = [0,1,2,3,4,5,6,7,8,9]
for i in range(9) :
    for j in range(9) :
        if sudo[i][j] not in bon :
            print(f"Ce sudoku n'est pas cohérent, il y a un nombre qui n'est pas censé être la aux coordonné {i} : {j}")
            erreur += 1

#vérifie si le sudoku est bon

if (0 in sudo[i]) and (erreur != 0) :
    print("Attention ! Ce sudoku n'est pas complété")

elif (0 not in sudo[i]) and (erreur != 0) :
    print(f"Quasiment ! Ce sudoku est remplie mais avec {erreur} erreur(s)")

elif (0 not in sudo[i]) and (erreur == 0) :
    print("Bravo ! ce sudoku est correct")

#Dicte les cases nayant pas de valeur 

void = []
longue = 'y'
nb_0 = 0
for i in range(9) :
    if longue == 'y' :
        for j in range(9) :
            if sudo[j][i] == 0 :
                void.append((i+1, j+1))
    elif longue == 'n' :
        for j in range(9) :
            if sudo[j][i] == 0 :
                nb_0 += 1
if nb_0 != 0 :
    print(f"Il y a {nb_0} cases vide dans votre sudoku")

if void != 0 :
    print("Les cases de coordonnées suivante sont vides : \n", void)





