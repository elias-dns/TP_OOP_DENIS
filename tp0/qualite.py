def f(d, t, x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if t == "R" :
        c = dist * 1.0
    elif t == "H" :
        c = dist * 1.5
    elif t == "S" :
        c = dist * 2.0
    else:
        c = dist * 3.0
    print("cout:", c)
    return c

#pylint montre plusieurs problèmes sur ce code : 
#argument d non utilisé
#trop d'argument dans la focntion
#pas d'explications sur ce que fait la fonction
#on peut ecrire une meilleure version de la fonction

def cout_deplacement_propre(terrain,x1,y1,x2,y2):
    """calcule la distance et renvoie le cout suivant le type de terrain"""
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if terrain == "R" :
        cout = dist * 1.0
    elif terrain == "H" :
        cout = dist * 1.5
    elif terrain == "S" :
        cout = dist * 2.0
    else:
        cout = dist * 3.0
    print("cout:", cout)
    return cout

#permet de passer de la note de 4 à 8