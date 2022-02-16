# Afficher la grille sous une belle forme
def affichage(sudo) :
    for i in range(len(sudo)):      #parcourt les lignes du sudoku
        print(sudo[i])          #print les lignes en question

# Vérifie s'il n'y a pas 2 fois le même chiffre dans une ligne, (hormis 0)
def lignes(sudo, erreur):
    faux = []       #variable qui va contenir les coordonnées des chiffres qu'il y aura en trop
    for i in range(9) :     #parcourt les lignes du sudoku
        bon = [1, 2, 3, 4, 5, 6, 7, 8, 9]       #reset les possibilité des chiffres sur la ligne
        for j in range(9) :         #parcourt chaque éléments de la ligne
            if sudo[i][j] in bon :      #si le chiffre est dans la liste (donc qu'il n'est jamais encore apparu dans cette ligne) :
                bon.remove(sudo[i][j])      #enlever ce chiffre de la liste
            elif sudo[i][j] != 0 :      #si le chiffre n'y est pas (et que c'est pas 0(car ça represente une case vide)) (ça veux dire que le chiffre apparait déjà dans cette ligne)
                faux.append((i, j))     #mettre dans la liste créé pour ça, les coordonnée de l'erreur
                erreur += 1     #on ajoute 1 au nombre d'erreurs total
    if len(faux) != 0 :     #si il y a des erreurs
        print(f'Il y a des erreurs aux coordonnées : \n{faux}')        #print les coordonnée de toutes les erreurs    
    return erreur       #renvoie le nombre d'erreurs total pour le garder en mémoire

# Vérifie s'il n'y a pas 2 fois le même chiffre dans une colonne (hormis 0)
def colonnes(sudo, erreur) :
    faux = []       #variable qui va contenir les coordonnées des chiffres qu'il y aura en trop       
    for i in range(9) :     #parcourt les colones du sudoku
        bon = [1, 2, 3, 4, 5, 6, 7, 8, 9]         #reset les possibilité des chiffres sur la ligne 
        for j in range(9) :     #parcourt chaque éléments de la colone 
            if sudo[j][i] in bon :      #si le chiffre est dans la liste (donc qu'il n'est jamais encore apparu dans cette colone) :      
                bon.remove(sudo[j][i])      #enlever ce chiffre de la liste
            elif sudo[j][i] != 0 :      #si le chiffre n'y est pas (et que c'est pas 0(car ça represente une case vide)) (ça veux dire que le chiffre apparait déjà dans cette colone)
                faux.append((i, j))     #mettre dans la liste créé pour ça, les coordonnée de l'erreur
                erreur += 1     #on ajoute 1 au nombre d'erreurs total
    if len(faux) != 0 :     #si il y a des erreurs
        print(f'Il y a des erreurs aux coordonnées : \n{faux}')        #print les coordonnée de toutes les erreurs    
    return erreur       #renvoie le nombre d'erreurs total pour le garder en mémoire

# Vérifie les carrés de 3 par 3
def carres(sudo, erreur) :
    erreur_c = []       #variable qui stockera les coordonnée des CARRER qui seront faux
    for y in range(0,7,3) :     #parcour les carré dans l'axe des x
        for x in range(0,7,3) :     #parcour les carré dans l'axe des y
            bon = [1, 2, 3, 4, 5, 6, 7, 8, 9]         #reset les possibilité des chiffres dans ce carré   
            for i in range(x , x+3) :       #parcourt la ligne du carré en cour de vérification      
                for j in range(y, y+3) :        #parcourt chaque élément de la ligne sélectionnée (toujours dans le carré)
                    if sudo[i][j] in bon :      #si le chiffre n'apparais pas dans la liste, donc n'apparais pas 2 fois dans le carré selectionnée
                        bon.remove(sudo[i][j])      #enlevé cette possiblité de chiffre
                    elif sudo[i][j] != 0 :      #sinon, si c'est pas 0 :
                        erreur_c.append((int(x/3), int(y/3)))   #ajouter a la liste faite pour ça les coordonnée du carré dans lequel il y a l'erreur
                        erreur += 1     #on ajoute 1 au nombre d'erreurs total
    if len(erreur_c) != 0 :     #si il y a des erreurs
        print(f'Il y a des erreurs dans les carrés de coordonnées suivantes : \n {erreur_c}')        #print les coordonnée de tous les carrés avec des erreurs    
    return erreur       #renvoie le nombre d'erreurs total pour le garder en mémoire

# Vérifie s'il n'y a aucune incohérence 
def incoherances(sudo, erreur) :
    incoherances = []       #variable qui repertorie toutes les incohérence
    bon = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]        #toutes les possibilité de nombre
    for i in range(9) :     #parcourt les lignes
        for j in range(9) :     #parcourt chaque élément de la ligne
            if sudo[i][j] not in bon :      #si l'élément selectionnée n'est pas dans les possibilité 
                incoherances.append((i , j))        #ajouter les coordonnée de se point a la variable fait pour ça
                erreur += 1         #ajouter 1 au nombree d'érreur totoal
    if len(incoherances) != 0 :     #si il y a des incohérence
        print(f'Il y a des incohérances au coordonnées suivantes : \n {incoherances}')      #print leurs coordonnées
    return erreur       #renvoie le nombre d'érreur total

# Dicte les cases n'ayant pas de valeur 
def cases_vides(sudo) :
    coo_cases_vides = []        #variable qui va stoquez les coordonnée des case vide
    DETAIL = 'n'    #si c'est 'n' ça va juste dire le nombre de case vide, si c'est 'y' ça va dire tous les emplacement (!! parametre 'n' extrement recommendé!!)
    nb_0 = 0        #variable qui décrit le nombre de case vide
    for i in range(9) :     #parcourt les lignes
        for j in range(9) :     #parcours les élément de la ligne
            if sudo[j][i] == 0 :        #si la case est un '0' alors :
                coo_cases_vides.append((i+1, j+1))      #ajouter les coordonnée a la variable crée pour ça
                nb_0 += 1       #rajoute 1 au nombre de '0'
    
    if DETAIL == 'n' :      #si l'utilisateur ne veux pas de détail :
        print(f"Il y a {nb_0} cases vides dans votre sudoku")       #écrire le nombre de case vide
    if DETAIL == 'y' :      #si l'utilisateur veux des détail
        print(f'Les cases de coordonnées suivantes sont vides : \n {coo_cases_vides}')      #écrit les coordonnée des case vides
    return nb_0     #renvoie le nombre de case vide (utile pour la prochaine fonction)

# Vérifie si le sudoku est bon
def correct(sudo, erreur, nb_0) :
    resultator = False      #set par défaut que le sudoku n'est pas bon
    if (nb_0 != 0) and (erreur != 0) :      #si le sudoku contiens des case vide et des erreurs alors :
        print("Attention ! Ce sudoku n'est pas complété et il y a des erreurs !")       #le dire
        return erreur, resultator       #renvoyer le nombre d'erreur et si le sudoku est bon ou pas
    elif (nb_0 != 0) and (erreur == 0) :      #si le sudoku n'est pas complété mais a aucune erreur alors :
        print("Attention ! Ce sudoku est bon mais il n'est pas complété")       #le dire
        return erreur, resultator       #renvoyer le nombre d'erreur et si le sudoku est bon ou pas
    elif (nb_0 == 0) and (erreur != 0) :   #si toutes les cases sont rempli mais qu'il y a des erreurs alors : 
        print(f"Quasiment ! Ce sudoku est rempli mais avec {erreur} erreur(s)")     #le dire
        return erreur, resultator       #renvoyer le nombre d'erreur et si le sudoku est bon ou pas
    elif (nb_0 == 0) and (erreur == 0) :        #si le sudoku a aucune erreur et qu'il est rempli (gg si c'est le cas) alors :
        print("Bravo ! Ce sudoku est correct")      #le dire
        resultator = True       #set le sudoku comme 'bon'
        return erreur, resultator       #renvoyer le nombre d'erreur et si le sudoku est bon ou pas

#affiche le détail des erreurs
def detail_erreur(list_error) : 
    for i in range(len(list_error)) :   #parcour la liste des différente possibilité d'erreur
        print(list_error[i])      #print les erreurs possible

def possibilite(sudo, good) :
    if good == False :      #si le sudoku est dit comme 'pas bon'
        DETAIL = 'n'        #si l'utilisateur ne veux pas de detail (!! recommendé de le mettre a 'n'!!)
        MIN = 'y'       #si l'utilisateur veux vraiment le moins de detail possible 
        nb_time = [[1, 0], [2, 0],[3, 0],[4, 0],[5, 0],[6, 0],[7, 0],[8, 0],[9, 0]]     #liste qui est utile (j'arrive pas a comprendre comment j'ai fais)
        recap = []
        if DETAIL == 'y' :      #si l'utilisateur veux des détails :
            for i in range(9) :     #parcourt les lignes
                for j in range(9) :     #parcourt chaque éléments
                    if sudo[i][j] == 0 :        #si la case est vide
                        poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]      #reset les possiblilité
                        for k in range(9) :     #boucle qui va permettre de parcourir la ligne et la colone de la case selectionnée 
                            if sudo[i][k] in poss :     #la c'est pour vérifier la ligne
                                poss.remove(sudo[i][k])     #si c'est dedans alors ça l'enlève
                            if sudo[k][j] in poss :     #la c'est pour vérifier la colone
                                poss.remove(sudo[k][j])     #si c'est dedans alors ça l'enlève
                        
                        #permet de récupérer les coordonnée du carrée dans lequel ce situe la case selectionnée (ça sert a rien de détaillée plus que ça)

                        if 0 <= i < 3 :
                            cox = 0
                        if 3 <= i < 6 :
                            cox = 3
                        if 6 <= i < 9 :
                            cox = 6
                        if 0 <= j < 3 :
                            coy = 0
                        if 3 <= j < 6 :
                            coy = 3
                        if 6 <= j < 9 :
                            coy = 6
                        for w in range(3) :     #parcour les lignes de ce carré
                            for h in range(3) :     #parcour chaque élément de la ligne selectionnée
                                if  sudo[w+cox][h+coy] in poss :        #si l'élément selectionné est dans la liste des possibilité alors :
                                    poss.remove(sudo[w+cox][h+coy])     #l'enlevé
                        print(f'la case de position {i} : {j} peut prendre comme valeur {poss}')        #écrire de façon belle les possinilité 

        if DETAIL == 'n' :
            for i in range(9) :     #parcourt les lignes
                for j in range(9) :     #parcourt chaque éléments
                    if sudo[i][j] == 0 :        #si la case est vide
                        poss = [1, 2, 3, 4, 5, 6, 7, 8, 9]      #reset les possiblilité
                        for k in range(9) :     #boucle qui va permettre de parcourir la ligne et la colone de la case selectionnée 
                            if sudo[i][k] in poss :     #la c'est pour vérifier la ligne
                                poss.remove(sudo[i][k])     #si c'est dedans alors ça l'enlève
                            if sudo[k][j] in poss :     #la c'est pour vérifier la colone
                                poss.remove(sudo[k][j])     #si c'est dedans alors ça l'enlève
                        
                        #permet de récupérer les coordonnée du carrée dans lequel ce situe la case selectionnée (ça sert a rien de détaillée plus que ça)

                        if 0 <= i < 3 :
                            cox = 0
                        if 3 <= i < 6 :
                            cox = 3
                        if 6 <= i < 9 :
                            cox = 6
                        if 0 <= j < 3 :
                            coy = 0
                        if 3 <= j < 6 :
                            coy = 3
                        if 6 <= j < 9 :
                            coy = 6
                        for w in range(3) :     #parcour les lignes de ce carré
                            for h in range(3) :     #parcour chaque élément de la ligne selectionnée
                                if  sudo[w+cox][h+coy] in poss :        #si l'élément selectionné est dans la liste des possibilité alors :
                                    poss.remove(sudo[w+cox][h+coy])     #l'enlevé
                        recap.append(f'{i} : {j} -> {poss}')        #entrée dans la liste la position et les possibilité de la case 
                        if MIN == 'y' :     #si l'utilisateur veux vraiment très peu de détail
                            for w in range(len(nb_time)) :  #parcourt la liste des possibilité 
                                if nb_time[w][0] in poss :      #si la possibilité est dans la liste
                                    nb_time[w][1]  += 1     #réjouté 1 au nombre de case qui peuvent prendre cette valeur
            if MIN == 'n' :     #si l'utilisateur veux un peu de détail
                for y in range(len(recap)) :    #parcourt recap
                    print(recap[y])     #print la version un peu détaillée
            if MIN == 'y' :     #si l'utilisateur veux le moins de détail possible 
                for z in range(len(nb_time)) :      #parcourir la liste des possibilité
                    print(f'{nb_time[z][0]} peu être mis {nb_time[z][1]} fois')     #print les possibilté mais sans aucun détail
    if good == True :       #si le sudoku est bon :
        print("Ce sudoku est entièrement rempli et vrai donc il n'y a plus aucune possibilité")     #ne rien vérif 

#grille du sudoku 

sudo = [
    [2, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 8, 3, 0, 0, 0],
    [0, 5, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 4, 0, 1, 5, 0],
    [6, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 2, 0, 0, 7],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 5, 0, 9, 0, 4, 3],
    [0, 0, 3, 2, 0, 0, 0, 0, 9]
]

#varible qui servent tout au long du programme

erreur = 0
list_error = []

#lancement du programme (je vais pas détailler car c'est assez peu utile)

affichage(sudo)
erreur = lignes(sudo, erreur)
list_error.append(f'Lignes       : {erreur} erreur(s)')
erreur = colonnes(sudo, erreur)
list_error.append(f'Colonnes     : {erreur} erreur(s)')
erreur = carres(sudo, erreur)
list_error.append(f'Carrés       : {erreur} erreur(s)')
erreur = incoherances(sudo,erreur)
list_error.append(f'Incoherances : {erreur} erreur(s)')
detail_erreur(list_error)
nb_0 = cases_vides(sudo)
erreur, good = correct(sudo, erreur, nb_0)
possibilite(sudo, good)

#le sudoku totalement rempli

'''
sudo = [
    [8, 3, 9, 7, 5, 6, 4, 2, 1],
    [1, 2, 4, 9, 8, 3, 7, 6, 5],
    [7, 5, 6, 4, 2, 1, 3, 9, 8],
    [3, 9, 2, 8, 4, 7, 1, 5, 6],
    [6, 8, 7, 1, 9, 5, 2, 3, 4],
    [4, 1, 5, 6, 3, 2, 9, 8, 7],
    [9, 6, 8, 3, 1, 4, 5, 7, 2],
    [2, 7, 1, 5, 6, 9, 8, 4, 3],
    [5, 4, 3, 2, 7, 8, 6, 1, 9]
]

#le sudoku de base

sudo = [
    [0, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 8, 3, 0, 0, 0],
    [0, 5, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 8, 4, 0, 1, 5, 0],
    [6, 0, 0, 0, 9, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 2, 0, 0, 7],
    [0, 6, 0, 0, 0, 0, 0, 7, 0],
    [0, 0, 0, 5, 0, 9, 0, 4, 3],
    [0, 0, 3, 2, 0, 0, 0, 0, 9]
]
'''




