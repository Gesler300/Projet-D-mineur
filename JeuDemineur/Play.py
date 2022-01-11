#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[1]:
import random
import ModuleInterfaceGraphique as MI

def magrille(l,c):
    """Cette fonction crée une liste imbriquée de l lignes et c colonnes qui nous servira à crée la grille contenant de base.
    """
    grille = []
    for i in range (l):
        grille.append([0]*c)
    return grille

def genPos(l,c):
    """Cette fonction crée un liste contenant les positions des cases au sein d'une grille de l lignes et c colonnes.
    """
    pos=[]
    for i in range(l):
        for j in range (c):
            pos.append((i,j))
    return pos

def printgrille(magrille):
    """Cette fonction crée un premier rendu visuel sous forme de grille de le liste imbriquée mise en paramètre.
    """
    nbligne = len(magrille)
    nbcol = len(magrille[0])
    for i in range(nbligne):
        lignetexte = "|"
        for j in range(nbcol):
            lignetexte += "{0}|".format(magrille[i][j])
        print(lignetexte)    
              
def putBomb(grille, nbBomb):
    """Cette fonction séectionne aléatoirement un nombre de cases donné au sein d'une grile donnée et change le contenu de ces positions en "B".
    """
    nbligne = len(grille)
    nbcol = len(grille[0])
    pos = genPos(nbligne, nbcol)
    posBomb = random.sample(pos, nbBomb) 
    for Bomb in (posBomb):
        grille[Bomb[0]][Bomb[1]] = "B"
    return grille

def checkbomb2(mgB,l,c):
    """Cette fonction donne le nombre de bombes dans les cases adjacentes à la case sélectionnée (l = ligne de la case, c = colonne de la case) (utile uniquement dans mgB) (fonctionne dans tout les cas).
    """
    lcheck = l
    ccheck = c
    if l == 0 and c == 0:
        for i in range (2):
            for j in range (2):
                if mgB[lcheck][ccheck] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck == l and ccheck == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-2
    elif l == 0 and c == len(mgB[0])-1:
        for i in range (2):
            for j in range (2):
                if mgB[lcheck][ccheck-1] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck == l and ccheck-1 == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-2
    elif l == len(mgB)-1 and c == 0:
        for i in range (2):
            for j in range (2):
                if mgB[lcheck-1][ccheck] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck-1 == l and ccheck == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-2
    elif l == len(mgB)-1 and c == len(mgB[0])-1:
        for i in range (2):
            for j in range (2):
                if mgB[lcheck-1][ccheck-1] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck-1 == l and ccheck-1 == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-2
    elif l == 0:
        for i in range (2):
            for j in range (3):
                if mgB[lcheck][ccheck-1] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck == l and ccheck-1 == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-3
    elif l == len(mgB)-1:
        for i in range (2):
            for j in range (3):
                if mgB[lcheck-1][ccheck-1] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck-1 == l and ccheck-1 == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-3
    elif c == 0:
        for i in range (3):
            for j in range (2):
                if mgB[lcheck-1][ccheck] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck-1 == l and ccheck == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-2
    elif c == len(mgB[0])-1:
        for i in range (3):
            for j in range (2):
                if mgB[lcheck-1][ccheck-1] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck-1 == l and ccheck-1 == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-2
    else:
        for i in range (3):
            for j in range (3):
                if mgB[lcheck-1][ccheck-1] == "B":
                    mgB[l][c] += 1
                    ccheck = ccheck+1
                elif lcheck-1 == l and ccheck-1 == c:
                    ccheck = ccheck+1
                else:
                    ccheck = ccheck+1
            lcheck = lcheck+1
            ccheck = ccheck-3
            
def checkbombgrille(mgB):
    """Cette fonction donne le nombre de bombes dans les cases adjacentes à la case en cours de vérification (utile uniquement dans mgB) (fonctionne pour toute la grilee et non pour une case sélectionnée).
    """
    for i in range(len(mgB)):
        for j in range(len(mgB[0])):
            if mgB[i][j] == "B":
                continue
            else:
                checkbomb2(mgB,i,j)

def grille_joueur(l,c):
    """Cette fonction crée une liste imbriquée de l lignes et c colonnes qui nous servira à crée la grille du joueur.
    """
    grille_joueur = []
    for i in range (l):
        grille_joueur.append(["?"]*c)
    return grille_joueur

def grille_controle(l,c):
    """Cette fonction crée une liste imbriquée de l lignes et c colonnes qui nous servira à crée la grille qui serivira à éviter une boucle infine lorsque le joueur réveler les cases.
    """
    grille_joueur = []
    for i in range (l):
        grille_joueur.append([0]*c)
    return grille_joueur

def action_joueur(l,c):
    """Cette fonction permet au joueur de réveler les cases. Elle définit ce qui se passe si le joueur sélectionne une case piégée et ce qui ce passe lorsque la case est révelée. C'est aussi elle qui permet aux zéros de se répendrent. (l = ligne de la case, c = colonne de la case)
    """
    ma = MI.m
    if mgB[l][c] == 0 and pg[l][c] == "F":
        print("Vous ne pouvez pas révéler cette case tant qu'elle est marquée.")
    elif mgB[l][c] == "B":
        if pg[l][c] == "F":
            print("Vous ne pouvez pas révéler cette case tant qu'elle est marquée.")
        else:
            for i in range(len(mgB)):
                for j in range(len(mgB[0])):
                    if mgB[i][j] == "B":
                        if pg[i][j] == "F":
                            pg[i][j] = "B"
                        else:
                            pg[i][j] = "b"
            pg[l][c] = "a"
    elif mgB[l][c] == 0:
        lcheck = l
        ccheck = c
        check =[]
        if l == 0 and c == 0:
            for i in range (2):
                for j in range (2):
                    if pg[lcheck][ccheck] == "F":
                        ccheck = ccheck+1
                    elif lcheck == l and ccheck == c:
                        pg[lcheck][ccheck] = mgB[lcheck][ccheck]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck][ccheck] == 0:
                            if gc[lcheck][ccheck] == 0:
                                gc[lcheck][ccheck] = 1
                                check.append(lcheck)
                                check.append(ccheck)
                                pg[lcheck][ccheck] = mgB[lcheck][ccheck]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck][ccheck] = mgB[lcheck][ccheck]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-2
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif l == 0 and c == len(mgB[0])-1:
            for i in range (2):
                for j in range (2):
                    if pg[lcheck][ccheck-1] == "F":
                        ccheck = ccheck+1
                    elif lcheck == l and ccheck-1 == c:
                        pg[lcheck][ccheck-1] = mgB[lcheck][ccheck-1]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck][ccheck-1] == 0:
                            if gc[lcheck][ccheck-1] == 0:
                                gc[lcheck][ccheck-1] = 1
                                check.append(lcheck)
                                check.append(ccheck-1)
                                pg[lcheck][ccheck-1] = mgB[lcheck][ccheck-1]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck][ccheck-1] = mgB[lcheck][ccheck-1]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-2
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif l == len(mgB)-1 and c == 0:
            for i in range (2):
                for j in range (2):
                    if pg[lcheck-1][ccheck] == "F":
                        ccheck = ccheck+1
                    elif lcheck-1 == l and ccheck == c:
                        pg[lcheck-1][ccheck] = mgB[lcheck-1][ccheck]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck-1][ccheck] == 0:
                            if gc[lcheck-1][ccheck] == 0:
                                gc[lcheck-1][ccheck] = 1
                                check.append(lcheck-1)
                                check.append(ccheck)
                                pg[lcheck-1][ccheck] = mgB[lcheck-1][ccheck]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck-1][ccheck] = mgB[lcheck-1][ccheck]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-2
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif l == len(mgB)-1 and c == len(mgB[0])-1:
            for i in range (2):
                for j in range (2):
                    if pg[lcheck-1][ccheck-1] == "F":
                        ccheck = ccheck+1
                    elif lcheck-1 == l and ccheck-1 == c:
                        pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck-1][ccheck-1] == 0:
                            if gc[lcheck-1][ccheck-1] == 0:
                                gc[lcheck-1][ccheck-1] = 1
                                check.append(lcheck-1)
                                check.append(ccheck-1)
                                pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-2
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif l == 0:
            for i in range (2):
                for j in range (3):
                    if pg[lcheck][ccheck-1] == "F":
                        ccheck = ccheck+1
                    elif lcheck == l and ccheck-1 == c:
                        pg[lcheck][ccheck-1] = mgB[lcheck][ccheck-1]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck][ccheck-1] == 0:
                            if gc[lcheck][ccheck-1] == 0:
                                gc[lcheck][ccheck-1] = 1
                                check.append(lcheck)
                                check.append(ccheck-1)
                                pg[lcheck][ccheck-1] = mgB[lcheck][ccheck-1]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck][ccheck-1] = mgB[lcheck][ccheck-1]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-3
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif l == len(mgB)-1:
            for i in range (2):
                for j in range (3):
                    if pg[lcheck-1][ccheck-1] == "F":
                        ccheck = ccheck+1
                    elif mgB[lcheck-1][ccheck-1] == 0:
                        if gc[lcheck-1][ccheck-1] == 0:
                            gc[lcheck-1][ccheck-1] = 1
                            check.append(lcheck-1)
                            check.append(ccheck-1)
                            pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                            ccheck = ccheck+1
                        else:
                            ccheck = ccheck +1
                    else:
                        pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                        ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-3
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif c == 0:
            for i in range (3):
                for j in range (2):
                    if pg[lcheck-1][ccheck] == "F":
                        ccheck = ccheck+1
                    elif lcheck-1 == l and ccheck == c:
                        pg[lcheck-1][ccheck] = mgB[lcheck-1][ccheck]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck-1][ccheck] == 0:
                            if gc[lcheck-1][ccheck] == 0:
                                gc[lcheck-1][ccheck] = 1
                                check.append(lcheck-1)
                                check.append(ccheck)
                                pg[lcheck-1][ccheck] = mgB[lcheck-1][ccheck]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck-1][ccheck] = mgB[lcheck-1][ccheck]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-2
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        elif c == len(mgB[0])-1:
            for i in range (3):
                for j in range (2):
                    if pg[lcheck-1][ccheck-1] == "F":
                        ccheck = ccheck+1
                    elif lcheck-1 == l and ccheck-1 == c:
                        pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck-1][ccheck-1] == 0:
                            if gc[lcheck-1][ccheck-1] == 0:
                                gc[lcheck-1][ccheck-1] = 1
                                check.append(lcheck-1)
                                check.append(ccheck-1)
                                pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-2
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
        else:
            for i in range (3):
                for j in range (3):
                    if pg[lcheck-1][ccheck-1] == "F":
                        ccheck = ccheck+1
                    elif lcheck-1 == l and ccheck-1 == c:
                        pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                        ccheck = ccheck+1
                        gc[l][c] = 1
                    else:
                        if mgB[lcheck-1][ccheck-1] == 0:
                            if gc[lcheck-1][ccheck-1] == 0:
                                gc[lcheck-1][ccheck-1] = 1
                                check.append(lcheck-1)
                                check.append(ccheck-1)
                                pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                                ccheck = ccheck+1
                            else:
                                ccheck = ccheck +1
                        else:
                            pg[lcheck-1][ccheck-1] = mgB[lcheck-1][ccheck-1]
                            ccheck = ccheck+1
                lcheck = lcheck+1
                ccheck = ccheck-3
            for i in range(int(len(check)/2)):
                l = check[0]
                c = check[1]
                del check[1]
                del check[0]
                action_joueur(l,c)
    else:
        if pg[l][c] == "F":
            print("Vous ne pouvez pas révéler cette case tant qu'elle est marquée.")
        else:
            pg[l][c] = mgB[l][c]
    return ma

def action_joueur2(m,l,c):
    """Cette fonction permet au joueur de marquer et démarquer les cases. Elle définit ce qui se passe lorsque le joueur pose un drapeau, qu'il en retire un et que plus aucun drapeau est disponible.( l = ligne de la case, c = colonne de la case)
    """
    ma = MI.m
    if pg[l][c] == "F":
        print("Drapeau retiré.")
        ma = ma+1
        pg[l][c] = "?"
    elif pg[l][c] == "?":
        if ma > 0:
            pg[l][c] = "F"
            ma = ma-1
    return ma

def VerifBombe():
	"""Cette fonction vérifie si on a cliqué sur une bombe pour ensuite enclencher le mécanisme de défaite si c'est le cas.
    """
    VerificationB = 0
    for i in range(len(pg)):
        if VerificationB == 1:
            break
        else:
            for j in range (len(pg[i])):
                if pg[i][j] == "b" or pg[i][j] == "B" or pg[i][j] == "a":
                    VerificationB = VerificationB + 1
                    break
                else:
                    continue
    return VerificationB

def CheckWin ():
	"""Cette fonction vérifie si on a révélé toute les cases sauf les bombes pour ensuite enclencher le mécanisme de victoire si c'est le cas.
    """
    for i in range(len(pg)):
        for j in range (len(pg[i])):
            if MI.GrilleCheckWin[i][j] == 1:
                continue
            else:
                if pg[i][j] != "?" and pg[i][j] != "F" and pg[i][j] != "B" and pg[i][j] != "b":
                    MI.GrilleCheckWin[i][j] += 1
                    MI.Victoire += 1

def f(c,l):
	"""Cette fonction permet de placer ou retirer un drapeau.
    """
    if MI.GrilleCheckDrapeau[l][c] == 1:
        MI.m = action_joueur2(MI.m,l,c)
        MI.EnleverDrapeau(l,c)
        MI.BombesRestantes(MI.m)
        MI.GrilleCheckDrapeau[l][c] -= 1
    elif MI.m == 0:
        print("Tous les drapeaux sont placés, vous devez d'abord en retirer un.")
    else:
        if pg[l][c] != "?":
            print("Vous ne pouvez pas marquer une case déjà révélée.")
        else:
            MI.m = action_joueur2(MI.m,l,c)
            MI.AfficherUnDrapeau(pg)
            MI.BombesRestantes(MI.m)
            MI.GrilleCheckDrapeau[l][c] += 1

def r(c,l):
	"""Cette fonction permet de révéler une case.
    """
    if pg[l][c] != "?" and pg[l][c] != "F":
        print("Vous ne pouvez pas révéler une case déjà révélée.")
    else: 
        MI.m = action_joueur(l,c)
        VerificationB = VerifBombe()
        if VerificationB == 1:
            MI.ChangementPerdu(mgB,pg,l,c)
            MI.Perdu +=1
        else:
            MI.Decouvrir(pg,10,10)
            CheckWin ()
            if MI.Victoire == 85:
                MI.Decouvrir(pg,10,10)
                MI.ChangementVictoire(mgB)
                MI.BombesRestantes(0)
        
CheckQuitter = 0
mg = magrille(10, 10)
mgB = putBomb(mg,15)
pg = grille_joueur(10,10)
gc = grille_controle(10,10)
checkbombgrille(mgB)
MI.InterfaceGrille(MI.m,10,10)
MI.MakeGrilleCheckDrapeau(10,10)
MI.MakeGrilleCheckWin(10,10)
MI.MakeDGrilleCheck(10,10)
while CheckQuitter == 0:
    action = input("Commande: ")
    if action == "q":
        CheckQuitter += 1
    elif action == "r":
        if MI.Perdu == 1:
            print("Vous avez perdu. Relancez le programme pour recommencer une partie.")
        elif MI.Victoire == 85:
            print("Vous avez gagné. Relancez le programme pour recommencer une partie.")
        else:
            c = int(input("Colonne: "))
            if c < 0 or c > 9:
                print("Veuillez choisir une colonne valide.")
            else:
                l = int(input("Ligne: "))
                if l < 0 or l > 9:
                    print("Veuillez choisir une ligne valide.")
                else:
                    r(c,l)
    elif action == "f":
        if MI.Perdu == 1:
            print("Vous avez perdu. Relancez le programme pour recommencer une partie.")
        elif MI.Victoire == 85:
            print("Vous avez gagné. Relancez le programme pour recommencer une partie.")  
        else:
            c = int(input("Colonne: "))
            if c < 0 or c > 9:
                print("Veuillez choisir une colonne valide.")
            else:
                l = int(input("Ligne: "))
                if l < 0 or l > 9:
                    print("Veuillez choisir une ligne valide.")
                else:
                    f(c,l)
    else:
        print("Veuillez choisir une commande valide.")

