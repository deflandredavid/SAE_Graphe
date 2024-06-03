import requetes
import networkx as nx
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox

def demander_charger():
    """Demande si l'utilisateur veut utiliser un de ces fichiers"""
    rep = messagebox.askquestion("Fichier", "Voulez-vous utiliser un de vos fichiers txt?")
    if rep == "yes":
        nom_fic = simpledialog.askstring("Fichier", "Quel est le nom du fichier?")
        try:
            return requetes.json_vers_nx(nom_fic)
        except Exception as e:
            messagebox.showerror("Erreur", f"Erreur : {e}\nJe ne connais pas ce fichier, nous allons utiliser un fichier par défaut.")
    return requetes.json_vers_nx('data.txt')

def demander_2_acteurs(G):
    """Demande à l'utilisateur les 2 acteurs à utiliser"""
    rep1 = simpledialog.askstring("Acteur", "Quel est le premier acteur?")
    rep2 = simpledialog.askstring("Acteur", "Quel est le deuxième acteur?")
    if rep1 in G.nodes and rep2 in G.nodes:
        return rep1, rep2
    messagebox.showerror("Erreur", "Un des deux acteurs n'est pas dans le graphe")
    return None, None

def demander_1_acteur(G):
    """Demande à l'utilisateur l'acteur à utiliser"""
    rep1 = simpledialog.askstring("Acteur", "Quel est l'acteur?")
    if rep1 in G.nodes:
        return rep1
    messagebox.showerror("Erreur", "L'acteur n'est pas dans le graphe")
    return None

def demander_distance():
    """Demande à l'utilisateur la distance qu'il veut étudier"""
    rep = simpledialog.askstring("Distance", "Quelle distance souhaitez-vous étudier?")
    try:
        return int(rep)
    except ValueError:
        messagebox.showerror("Erreur", "Ceci n'est pas un nombre")
        return None



def voir_graphe(G):
    nx.draw(G, with_labels=True)
    plt.show()

def voir_centre_graphe(G):
    centre = requetes.centre_hollywood(G)
    messagebox.showinfo("Centre du Graphe", centre)

def voir_acteurs_collab(G):
    acteur1, acteur2 = demander_2_acteurs(G)
    if acteur1 and acteur2:
        result = requetes.collabCommuns(G, acteur1, acteur2)
        messagebox.showinfo("Acteurs Collaborants", result)

def voir_acteurs_eloignes(G):
    result = requetes.eloignement_max(G)
    messagebox.showinfo("Couple d'Acteurs Éloignés", result)

def voir_acteurs_proche(G):
    acteur1, acteur2 = demander_2_acteurs(G)
    if acteur1 and acteur2:
        result = requetes.est_proche(G, acteur1, acteur2)
        messagebox.showinfo("Acteurs proches", result)

def voir_acteurs_distance(G):
    acteur = demander_1_acteur(G)
    if acteur:
        distance = demander_distance()
        if distance is not None:
            result = requetes.collaborateurs_proches(G, acteur, distance)
            messagebox.showinfo("Acteurs à Distance", result)

def voir_centralite_acteur(G):
    acteur = demander_1_acteur(G)
    if acteur:
        result = requetes.centralite(G, acteur)
        messagebox.showinfo("Centralité d'un Acteur", result)

def voir_distance_2_acteurs(G):
    act1,act2 = demander_2_acteurs(G)
    if act1 and act2:
        result = requetes.distance_entre_acteurs(G,act1,act2)
        messagebox.showinfo("Distance séparant deux acteurs", result)



def programme_principal():
    G = demander_charger()

    root = tk.Tk()
    root.title("Analyse du Graphe Hollywoodien")

    options = [
        ("Voir le graphe", lambda: voir_graphe(G)),
        ("Voir le centre du graphe", lambda: voir_centre_graphe(G)),
        ("Voir tous les acteurs qui ont travaillé avec deux acteurs donnés", lambda: voir_acteurs_collab(G)),
        ("Voir le couple d'acteurs qui sont le plus éloignés du graphe", lambda: voir_acteurs_eloignes(G)),
        ("Voir si deux acteurs sont proches", lambda: voir_acteurs_proche(G)),
        ("Voir tous les acteurs qui sont à une distance donnée d'un acteur donné", lambda: voir_acteurs_distance(G)),
        ("Voir la centralité d'un acteur", lambda: voir_centralite_acteur(G)),
        ("Voir la distance séparant deux acteurs", lambda: voir_distance_2_acteurs(G)),
        ("Arrêter le programme", root.quit)
    ]

    for text, command in options:
        button = tk.Button(root, text=text, command=command)
        button.pack(fill=tk.X, padx=20, pady=20)

    root.mainloop()

programme_principal()
