import networkx as nx
import matplotlib.pyplot as plt
import json

#Q1
def json_vers_nx(chemin):
    films = []
    with open(chemin, 'r') as f:
        # Lire chaque ligne du fichier
        for line in f:
            # Analyser la ligne en tant qu'objet JSON
            data = json.loads(line)

            cleaned_data = {}

            # Nettoyer les valeurs du dictionnaire
            for key, value in data.items():
                if key == 'cast':  # Si la clé est 'cast'
                    # Nettoyer les noms des acteurs
                    cleaned_value = [actor.strip('"').replace('[[', '').replace(']]', '') for actor in value]
                elif isinstance(value, list):
                    # Si la valeur est une liste, nettoyer chaque élément de la liste
                    cleaned_value = [item.strip('"').replace('[[', '').replace(']]', '') if isinstance(item, str) else item for item in value]
                elif isinstance(value, str):
                    # Si la valeur est une chaîne de caractères, nettoyer simplement la valeur
                    cleaned_value = value.strip('"').replace('[[', '').replace(']]', '')
                else:
                    # Sinon, laisser la valeur telle quelle
                    cleaned_value = value
                cleaned_data[key.strip('"')] = cleaned_value

            films.append(cleaned_data)

    G = nx.Graph()
    # Vérification : Afficher le résultat pour voir si les acteurs ont été ajoutés correctement
    for film in films:
        act1 = film["cast"][0]
        for acteur in film['cast']:
            if acteur != act1:
                G.add_edge(act1,acteur)
    return G
#json_vers_nx('dataSimplifiee.txt')

G = json_vers_nx('dataSimplifiee.txt')


#Q2 
def collabCommuns(G,acteur1, acteur2):
    collab1 = list(G.neighbors(acteur1))
    collab2 = list(G.neighbors(acteur2))
    return collab1 + collab2
#print(collabCommuns(G,'Mohanlal','Salim Kumar'))

#Q3
def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs




def est_proche(G,u,k):
    """Fonction renvoyant la distance entre l'acteur k et l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: le sommet d'arrivée
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    i = 0
    voisin = ""
    while k != voisin:
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
            i+=1
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return i
#print(collabProch(G,'Salim Kumar', 'Mohanlal'))

#Q4
def centralite(G,acteur):
    distanceMax = collabProch(acteur,20)[-1][1]
    return distanceMax
#print(centralite(G,'Salim Kumar'))

#Q5
def eloignement_max(G):
    return ""