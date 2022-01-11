#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import turtle

Fenetre = turtle.Screen()

#on importe les image
Fenetre.addshape('GrilleDemineur.gif')
Fenetre.addshape('CacheCase.gif')
Fenetre.addshape('DrapeauM.gif')
Fenetre.addshape('DrapeauV.gif')
Fenetre.addshape('BombeN.gif')
Fenetre.addshape('BombeR.gif')
Fenetre.addshape('UN.gif')
Fenetre.addshape('DEUX.gif')
Fenetre.addshape('TROIS.gif')
Fenetre.addshape('QUATRE.gif')
Fenetre.addshape('CINQ.gif')
Fenetre.addshape('SIX.gif')
Fenetre.addshape('SEPT.gif')
Fenetre.addshape('HUIT.gif')
Fenetre.addshape('BombeTrouvee.gif')
Fenetre.addshape('CadreGagner.gif')
Fenetre.addshape('CadrePerdu.gif')
Fenetre.addshape('Chargement.gif')

Tcarre = 50 #Taille d'un carré
Espace = 3 #Taille du coté d'un carré
TcarreEspace = Tcarre + Espace

OriginX = -235 #coordonnée x de départ de la première tortue de la grille
OriginY = 178 #coordonnée y de départ de la première tortue de la grille

#affichage du chargement
Interface = turtle.Turtle() #la tortue interface se charge du fond qui ne change pas, sauf chargement au début.
Interface.speed(0)
Interface.up()
Interface.goto(0,27)
Interface.down()
Interface.shape('Chargement.gif')

CompteurBombe = turtle.Turtle() #tortue en charge de mettre à jour le compteur de bombes/drapeau
CompteurBombe.hideturtle()
CompteurBombe.speed(0)

Fin = turtle.Turtle() #turtle qui nous affiche gentiment le message de fin quel qu'il soit
Fin.hideturtle()
Fin.speed(0)


GrilleCheckDrapeau = [] #grille qui permet de vérifier si une action en particulier a été faite
GrilleCheckWin = [] #grille qui permet de vérifier si une action en particulier a été faite
TortueCase = [] #grille qui contient les tortues créées
PositionGrille = [] #grille qui permet de vérifier si une action en particulier a été faite
DGrilleCheck = [] #grille qui permet de vérifier si une action en particulier a été faite

Victoire = 0 #variable permettant d'empêcher le joueur de faire une action lorsqu'il a gagné

Perdu = 0 #variable permettant d'empêcher le joueur de faire une action lorsqu'il a perdu

m = 15 #compteur de drapeau restant à placer (m veut dire marqueurs)

def MakeGrilleCheckWin(l,c):
    """Cette fonction sert à créer la GrilleCheckWin.
    """
    for i in range (l):
        GrilleCheckWin.append([0]*c)

def MakeGrilleCheckDrapeau(l,c):
    """Cette fonction sert à créer la GrilleCheckDrapeau.
    """
    for i in range (l):
        GrilleCheckDrapeau.append([0]*c)

def AfficherUnDrapeau(pg):
    """Cette fonction affiche dans l'interface graphique les drapeau qui sont dans pg.
    """
    for i in range(len(pg)): 
        for j in range(len(pg[i])):
            if pg[i][j] == "F":
                if DGrilleCheck[i][j] == 1:
                    continue
                elif DGrilleCheck[i][j] == 0:
                    TurtleChange(TortueCase[i][j],'DrapeauM.gif')
                
def EnleverDrapeau(l,c):
    """Cette fonction fait en sorte que la tortue de l'endroit demandé enlève le drapeau.
    """
    TortueCase[l][c].shape('CacheCase.gif')
    
def BombesRestantes(m):
    """Cette fonction met à jour le compteur de bombes.
    """
    CompteurBombe.clear()
    CompteurBombe.write(m, font=("Arial", 45, "normal"))

def TurtleChange(UneTortue, Sprite):
    """Cette fonction permet de changer l'aspect d'une tortue.
    """
    UneTortue.shape(Sprite)
    
    
def DessineGrille():
    """Cette fonction affiche la grille de fond, avec les coordonnées ainsi que la bombe du compteur de bombes.
    """
    Interface.shape('GrilleDemineur.gif')
    Interface.showturtle()

def AjoutePosGrille(l, c, x, y):
    tab = [x, y]
    PositionGrille[l][c].append(tab)
    
def CreateTurtles(lignes, colonnes):
    """Cette fonction crée et place une tortue par case.
    """
    for l in range(lignes):
        Li = []
        for c in range(colonnes):
            t = turtle.Turtle()
            Li.append(t)
            t.hideturtle()
            t.speed(0)
            t.up()
            posXturtle = OriginX + c*TcarreEspace
            posYturtle = OriginY - l*TcarreEspace
            t.goto(posXturtle, posYturtle)
            AjoutePosGrille(l, c, posXturtle, posYturtle)
            t.down()
        TortueCase.append(Li)

def CreateTabPosGrille(lignes, colonnes):
    for i in range(lignes):
        li = []
        for j in range (colonnes):
            li.append([])
        PositionGrille.append(li)

def EcritCase(lignes, colonnes):
    """Cette fonction affiche l'apparence de base des tortues de la grille, à savoir des case grises.
    """
    for i in range(lignes):
        for j in range(colonnes):
            TortueCase[i][j].shape('CacheCase.gif')
            TortueCase[i][j].showturtle()
            
def InterfaceGrille(NBbombe,l,c):
    """Cette fonction met en place toute l'interface graphique.
    """
    CreateTabPosGrille(l, c)
    CreateTurtles(l, c)
    Interface.hideturtle()
    Interface.up()
    Interface.goto(0,0)
    Interface.down()
    DessineGrille()
    CompteurBombe.up()
    CompteurBombe.goto(5,281)
    CompteurBombe.down()
    CompteurBombe.write(NBbombe, font = ("Arial", 45, "normal"))
    EcritCase(l, c)             

def ChangementVictoire(mgB):
    """Cette fonction affiche des drapeaux verts sur chaque case ou il y a une bombe et affiche "Tu as gagné!" en cas de victoire.
    """
    Fin.up()
    Fin.goto(0,-363)
    Fin.down()
    Fin.shape('CadreGagner.gif')
    Fin.showturtle()
    for i in range(len(mgB)): 
        for j in range (len(mgB[i])):
            if mgB[i][j] == "B":
                TurtleChange(TortueCase[i][j],'DrapeauV.gif')

def ChangementPerdu(mgB,pg,l,c):
    """Cette fonction affiche toutes les bombes en cas de défaite: celles qui étaient sous un drapeaux, avec une croix, les bombes non révélées en noir, et la bombe révélée par le joueur, entourée de rouge.
    """
    Fin.up()
    Fin.goto(0,-363)
    Fin.down()
    Fin.shape('CadrePerdu.gif')
    Fin.showturtle()
    for i in range(len(mgB)): 
        for j in range (len(mgB[i])):
            if mgB[i][j] == "B" and pg[i][j] == "B":
                TurtleChange(TortueCase[i][j],'BombeTrouvee.gif')
            elif mgB[i][j] == "B" and pg[i][j] == "b":
                TurtleChange(TortueCase[i][j],'BombeN.gif')
    TurtleChange(TortueCase[l][c],'BombeR.gif')

def MakeDGrilleCheck(l,c):
    """Cette fonction permet de créer la grille qui vérifie ou il y à des drapeaux placés.
    """
    for i in range (l):
        DGrilleCheck.append([0]*c)

def Decouvrir(pg,l,c):
    """Cette fonction affiche ce qu'il y à dans pg lorsqu'il s'agit de chiffre ou de 0, avec des images sur l'interface graphique.
    """
    for i in range(len(pg)):
        for j in range(len(pg[i])):
            if pg[i][j] == "?" or pg[i][j] == "F":
                continue
            elif DGrilleCheck[i][j] == 1:
                continue
            elif DGrilleCheck[i][j] == 0:  
                if pg[i][j] > 0:
                    TortueCase[i][j].clear()
                    if pg[i][j] == 1:
                        TortueCase[i][j].shape('UN.gif')
                    elif pg[i][j] == 2:
                        TortueCase[i][j].shape('DEUX.gif')
                    elif pg[i][j] == 3:
                        TortueCase[i][j].shape('TROIS.gif')
                    elif pg[i][j] == 4:
                        TortueCase[i][j].shape('QUATRE.gif')
                    elif pg[i][j] == 5:
                        TortueCase[i][j].shape('TROIS.gif')
                    elif pg[i][j] == 6:
                        TortueCase[i][j].shape('SIX.gif')
                    elif pg[i][j] == 7:
                        TortueCase[i][j].shape('SEPT.gif')
                    elif pg[i][j] == 8:
                        TortueCase[i][j].shape('HUIT.gif')
                    DGrilleCheck[i][j] += 1
                elif pg[i][j] == 0:
                    TortueCase[i][j].hideturtle()
                    DGrilleCheck[i][j] += 1