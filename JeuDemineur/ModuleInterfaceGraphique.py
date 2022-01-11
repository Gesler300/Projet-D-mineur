#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import turtle

Fenetre = turtle.Screen()

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

Tcarre = 50
Espace = 3
TcarreEspace = Tcarre + Espace

OriginX = -235
OriginY = 178

Interface = turtle.Turtle()
Interface.speed(0)
Interface.up()
Interface.goto(0,27)
Interface.down()
Interface.shape('Chargement.gif')

CompteurBombe = turtle.Turtle()
CompteurBombe.hideturtle()
CompteurBombe.speed(0)

Fin = turtle.Turtle()
Fin.hideturtle()
Fin.speed(0)

GrilleCheckDrapeau = []
GrilleCheckWin = []
TortueCase = []
PositionGrille = []
DGrilleCheck = []

Victoire = 0

Perdu = 0

m = 15

def MakeGrilleCheckWin(l,c):
    for i in range (l):
        GrilleCheckWin.append([0]*c)

def MakeGrilleCheckDrapeau(l,c):
    for i in range (l):
        GrilleCheckDrapeau.append([0]*c)

def AfficherUnDrapeau(pg):
    for i in range(len(pg)): 
        for j in range(len(pg[i])):
            if pg[i][j] == "F":
                if DGrilleCheck[i][j] == 1:
                    continue
                elif DGrilleCheck[i][j] == 0:
                    TurtleChange(TortueCase[i][j],'DrapeauM.gif')
                
def EnleverDrapeau(l,c):
    TortueCase[l][c].shape('CacheCase.gif')
    
def BombesRestantes(m):
    CompteurBombe.clear()
    CompteurBombe.write(m, font=("Arial", 45, "normal"))

def TurtleChange(UneTortue, Sprite):
    UneTortue.shape(Sprite)
    
def DessineGrille():
    Interface.shape('GrilleDemineur.gif')
    Interface.showturtle()

def AjoutePosGrille(l, c, x, y):
    tab = [x, y]
    PositionGrille[l][c].append(tab)
    
def CreateTurtles(lignes, colonnes):
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
    for i in range(lignes):
        for j in range(colonnes):
            TortueCase[i][j].shape('CacheCase.gif')
            TortueCase[i][j].showturtle()
            
def InterfaceGrille(NBbombe,l,c):
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
    for i in range (l):
        DGrilleCheck.append([0]*c)

def Decouvrir(pg,l,c):
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