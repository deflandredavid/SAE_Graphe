import requetes
import networkx as nx
import matplotlib.pyplot as plt

def demander_charger():
    """Demande si l'utilisateur veut utiliser un de ces fichiers"""
    rep = ""
    while rep not in ["O", "N"]:
        rep = input("Voulez vous utiliser un de vos fichiers txt? O/N : ").upper()
    if rep == "O":
        nom_fic = input("Quel est le nom du fichier? : ")
        try:
            return requetes.json_vers_nx(nom_fic)
        except Exception as e:
            print(f"Erreur : {e}")
            print("Je ne connais pas ce fichier, nous allons utiliser un fichier par défaut.")
    return requetes.json_vers_nx('dataSimplifiee.txt')

def demander_2_acteurs(G):
    """Demande à l'utilisateur les 2 acteurs à utiliser"""
    rep1 = input("Quel est le premier acteur : ")
    rep2 = input("Quel est le deuxième acteur : ")
    if rep1 in G.nodes and rep2 in G.nodes:
        return rep1, rep2
    print("Un des deux acteurs n'est pas dans le graphe")
    return None, None

def demander_1_acteur(G):
    """Demande à l'utilisateur l'acteur à utiliser"""
    rep1 = input("Quel est l'acteur : ")
    if rep1 in G.nodes:
        return rep1
    print("L'acteur n'est pas dans le graphe")
    return None

def demander_distance():
    """Demande à l'utilisateur la distance qu'il veut étudier"""
    rep = input("Quelle distance souhaitez-vous étudier : ")
    try:
        return int(rep)
    except ValueError:
        print("Ceci n'est pas un nombre")
        return None

def programme_principal():
    print("Bienvenue")
    options = [
        "\n",
        "1 : Voir le graphe",
        "2 : Voir le centre du graphe",
        "3 : Voir tous les acteurs qui ont travaillé avec deux acteurs donnés",
        "4 : Voir le couple d'acteurs qui sont le plus éloignés du graphe",
        "5 : Voir la distance qui sépare deux acteurs",
        "6 : Voir tous les acteurs qui sont à une distance donnée d'un acteur donné",
        "7 : Voir la centralité d'un acteur",
        "8 : Arrêter le programme",
        "\n"
    ]
    G = demander_charger()
    while True:
        for option in options:
            print(option)
        try:
            rep1 = int(input("Que voulez-vous faire? (répondre avec 1, 2, 3, 4, 5, 6, 7 ou 8) : "))
        except ValueError:
            print("Ceci n'est pas un nombre")

        if rep1 == 8:
            break

        if rep1 == 1:
            nx.draw(G, with_labels=True)
            plt.show()
        elif rep1 == 2:
            
            print(requetes.centre_hollywood(G))
        elif rep1 == 3:
            
            acteur1, acteur2 = demander_2_acteurs(G)
            if acteur1 and acteur2:
                print(requetes.collabCommuns(G, acteur1, acteur2))
        elif rep1 == 4:
            
            print(requetes.eloignement_max(G))
        elif rep1 == 5:
            
            acteur1, acteur2 = demander_2_acteurs(G)
            if acteur1 and acteur2:
                print(requetes.est_proche(G, acteur1, acteur2))
        elif rep1 == 6:
            
            acteur = demander_1_acteur(G)
            if acteur:
                distance = demander_distance()
                if distance is not None:
                    print(requetes.collaborateurs_proches(G, acteur, distance))
        elif rep1 == 7:
            acteur = demander_1_acteur(G)
            if acteur:
                print(requetes.centralite(G, acteur))
        else:
            print("Option non reconnue. Veuillez choisir un nombre entre 1 et 9.")

programme_principal()