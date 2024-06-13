import networkx as nx
import matplotlib.pyplot as plt
import json
from collections import deque

def json_vers_nx(chemin):
    """Convertit un fichier .json en graphe NetworkX."""
    with open(chemin, 'r') as f:
        films = [json.loads(line) for line in f]

    G = nx.Graph()
    for film in films:
        cast = [actor.strip('"').replace('[[', '').replace(']]', '') for actor in film.get('cast', [])]
        if cast:
            G.add_edges_from((cast[0], acteur) for acteur in cast[1:])
    
    
    return G

def collabCommuns(G, acteur1, acteur2):
    """Retourne les collaborateurs communs entre deux acteurs."""
    return list(set(G.neighbors(acteur1)) | set(G.neighbors(acteur2)))

def collaborateurs_proches(G, u, k):
    """Retourne les acteurs à distance k de l'acteur u."""
    if u not in G:
        print(u +" est un illustre inconnu")
        return None
    
    return {node for node, length in nx.single_source_shortest_path_length(G, u, cutoff=k).items()}



def distance_entre_acteurs(G, acteur_source, acteur_cible):
    if acteur_source not in G.nodes or acteur_cible not in G.nodes:
        print("Au moins un des acteurs est inconnu dans le graphe.")
        return None
    
    queue = deque([(acteur_source, 0)])  # File contenant des tuples (acteur, distance)
    visite = set([acteur_source])  # Ensemble des acteurs déjà visités

    while queue:
        acteur_actuel, distance_actuelle = queue.popleft()
        
        if acteur_actuel == acteur_cible:
            return distance_actuelle
        
        for voisin in G.adj[acteur_actuel]:
            if voisin not in visite:
                visite.add(voisin)
                queue.append((voisin, distance_actuelle + 1))
    
    return -1





def est_proche(G, u, k):
    """Retourne si deux acteurs u et k. sont proches"""
    if u not in G:
        print(u + " est un illustre inconnu")
        return None
    if k not in G:
        print(k + " est un illustre inconnu")
        return None
    try:
        if (distance_entre_acteurs(G,u,k) <=3):
            return "Oui"
        return "Non"
    except nx.NetworkXNoPath:
        return "Non"



def centralite(G, acteur):
    # Calculer les distances les plus courtes depuis l'acteur à tous les autres nœuds
    distances = nx.shortest_path_length(G, source=acteur)
    # Retourner la plus grande distance trouvée
    return max(distances.values())



def centre_hollywood(G):
    # Initialiser la centralité minimale à une valeur élevée
    centralite_minimale = float('inf')
    acteur_central = None
    # Parcourir tous les nœuds dans le graphe
    for acteur in G.nodes():
        # Calculer la centralité de l'acteur
        centraliteact = centralite(G, acteur)
        # Mettre à jour l'acteur le plus central si nécessaire
        if centraliteact < centralite_minimale:
            centralite_minimale = centraliteact
            acteur_central = acteur
    return acteur_central



def eloignement_max(G):
    """Retourne le couple d'acteurs ayant la plus grande distance dans le graphe."""
    max_distance = 0
    max_couple = (None, None)
    for u in G.nodes:
        for v, length in nx.single_source_shortest_path_length(G, u).items():
            if length > max_distance:
                max_distance = length
                max_couple = (u, v)
    return max_couple, max_distance


# Exemples d'utilisation 
# chemin = 'dataSimplifiee.txt'
#G = json_vers_nx("data.txt")
# print(collabCommuns(G, 'Mohanlal', 'Salim Kumar'))
# print(collaborateurs_proches(G, 'Salim Kumar', 2))
#print(est_proche(G, 'Salim Kumar', 'Mohanlal'))
# print(centralite(G, 'Mohanlal'))
# print(centre_hollywood(G))
# print(eloignement_max(G))
#G=json_vers_nx("data.txt")
#print(distance_entre_acteurs(G, 'Bruce Willis', 'Mohanlal'))