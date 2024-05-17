import networkx as nx
import matplotlib.pyplot as plt
import json

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
        print(f"{u} est un illustre inconnu")
        return None
    
    return {node for node, length in nx.single_source_shortest_path_length(G, u, cutoff=k).items()}

def est_proche(G, u, k):
    """Retourne la distance entre deux acteurs u et k."""
    if u not in G:
        print(f"{u} est un illustre inconnu")
        return None
    
    try:
        return nx.shortest_path_length(G, u, k)
    except nx.NetworkXNoPath:
        return None

def centralite(G, u):
    """Retourne la centralité d'un acteur dans le graphe."""
    if u not in G:
        print(f"{u} est un illustre inconnu")
        return None
    return G.degree(u)

def centre_hollywood(G):
    """Retourne l'acteur le plus central dans le graphe."""
    return max(G.degree, key=lambda x: x[1])

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

# Exemples d'utilisation (à commenter pour l'utilisation réelle)
# chemin = 'dataSimplifiee.txt'
# G = json_vers_nx(chemin)
# print(collabCommuns(G, 'Mohanlal', 'Salim Kumar'))
# print(collaborateurs_proches(G, 'Salim Kumar', 2))
# print(est_proche(G, 'Salim Kumar', 'Mohanlal'))
# print(centralite(G, 'Mohanlal'))
# print(centre_hollywood(G))
# print(eloignement_max(G))