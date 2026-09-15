#creation des données et du tableau
releve1 = ("laser_avant", 2.35, "m")
releve2 = ("laser_arriere", 1.10, "m")
releve3 = ("gyroscope", 87.5, "deg")
releves = [releve1, releve2, releve3]

#fonction pour afficher les données
def afficher_releve(releve):
    nom = releve[0]
    val = releve[1]
    unite = releve[2]
    return f"Capteur {nom} : {val} {unite}"

#fonction permettant de changer une valeur pour un capteur donné
def recalibrer(liste_releve,nom,nouvelle_val):
    nouveaux_releves = []
    for i in range(len(liste_releve)):
        if liste_releve[i][0] == nom:
            releve_liste = list(liste_releve[i])
            releve_liste[1] = nouvelle_val   
            nouveaux_releves.append(tuple(releve_liste))
        else:
            nouveaux_releves.append(liste_releve[i])
            
    return nouveaux_releves


#test pour la 1ere fonction
assert len(releves) == 3
assert releves[0][0] == "laser_avant"
assert afficher_releve(releve1) == "Capteur laser_avant : 2.35 m"

#test pour la 2eme fonction
nouveaux_releves = recalibrer(releves, "laser_avant", 2.40)
assert nouveaux_releves[0] == ("laser_avant", 2.40, "m")
assert nouveaux_releves[1] == releve2
assert nouveaux_releves[2] == releve3