#création du dictionnaire
pieces_stock = {
"ModeleA": {"moteurs": 10, "capteurs": 25, "roues": 40},
"ModeleB": {"moteurs": 6, "capteurs": 15, "roues": 24},
}

def quantite_piece(stock, modele, type_piece):
    """Retourne la quantité disponible d'une pièce pour un modèle donné"""
    return stock[modele][type_piece]

def consommer_piece(stock, modele, type_piece, quantite):
    """Retire une quantité d'une pièce pour un modèle donné"""
    stock[modele][type_piece] = stock[modele][type_piece] - quantite

def ajouter_modele(stock, modele, moteurs, capteurs, roues):
    """Ajoute un nouveau modèle avec son stock initial"""
    stock[modele] = {"moteurs": moteurs, "capteurs": capteurs, "roues": roues}

def total_pieces(stock):
    """Calcule le nombre total de chaque pièce"""
    total_moteurs = 0
    total_capteurs = 0
    total_roues = 0
    for modele in stock:
        total_moteurs = total_moteurs + stock[modele]["moteurs"]
        total_capteurs = total_capteurs + stock[modele]["capteurs"]
        total_roues = total_roues + stock[modele]["roues"]
    return {"moteurs": total_moteurs, "capteurs": total_capteurs, "roues": total_roues}

consommer_piece(pieces_stock, "ModeleA", "moteurs", 3)
assert pieces_stock["ModeleA"]["moteurs"] == 7

ajouter_modele(pieces_stock, "ModeleC",
                moteurs=4, capteurs=10, roues=16)
assert pieces_stock["ModeleC"] == \
                {"moteurs": 4, "capteurs": 10, "roues": 16}
totaux = total_pieces(pieces_stock)
assert totaux == {"moteurs": 17, "capteurs": 50, "roues": 80}