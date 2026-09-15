robots_exploration = {"R2", "R5", "R7"}
robots_transport = {"R5", "R9", "R7", "R3"}

def robots_double_mission(exploration, transport):
    """Retourne les robots pour l'exploration et le transport"""
    return exploration & transport

def robots_toutes_missions(exploration, transport):
    """Retourne tous les robots utilisés sans doublon"""
    return exploration | transport

def robots_exploration_seulement(exploration, transport):
    """Retourne les robots qui font uniquement de l'exploration"""
    return exploration - transport

#test pour ces fonctions
double_mission = robots_double_mission(robots_exploration, robots_transport)
toutes_missions = robots_toutes_missions(robots_exploration, robots_transport)
exploration_seule = robots_exploration_seulement(robots_exploration, robots_transport)

assert double_mission == {"R5", "R7"}
assert toutes_missions == {"R2", "R3", "R5", "R7", "R9"}
assert exploration_seule == {"R2"}

def ajouter_robot_mission(ensemble_robots, nouveau_robot):
    """Renvoie un nouvel ensemble avec le nouveau robot ajouté sans modifier l'original"""
    return ensemble_robots | {nouveau_robot}

def retirer_robot_mission(ensemble_robots, robot_a_retirer):
    """Renvoie un nouvel ensemble sans le robot en panne et sans modifier l'original"""
    return ensemble_robots - {robot_a_retirer}

#test pour ces fonctions
ajout = ajouter_robot_mission(robots_exploration, "R8")
retrait = retirer_robot_mission(robots_transport, "R9")
assert ajout == {"R2", "R5", "R7", "R8"}
assert retrait == {"R3", "R5", "R7"}
# L’ensemble d’origine ne doit pas avoir été modifié
assert robots_transport == {"R5", "R9", "R7", "R3"}


