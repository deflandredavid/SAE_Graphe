

import json

films = []

with open('dataSimplifiee.txt', 'r') as f:
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

# Vérification : Afficher le résultat pour voir si les acteurs ont été ajoutés correctement
# for film in films:
#      print(film['title'], ":", film['cast'])

def dicoActeur(acteur):
    dictActeurs = dict()
    listeActeur = set()
    #renvoi liste acteurs
    for film in films:
        for (cle,valeur) in film.items():
            if(cle == "cast"):
                if acteur in valeur:
                    valeur.remove(acteur)
                    for val in valeur:
                        listeActeur.add(val)
    dictActeurs[acteur]=listeActeur
    return dictActeurs

#print(dicoActeur('Mohanlal'))


    
def collabCommuns(acteur1, acteur2):
    lesActeurs = set()
    for film in films:
        for (cle,valeur) in film.items():
            if(cle == "cast"):
                if acteur1 in valeur or acteur2 in valeur:
                    for val in valeur:
                        lesActeurs.add(val)
    return lesActeurs

#print(collabCommuns('Mohanlal','Salim Kumar'))

def collabProch(acteur, distance):
    acteurs_connaissant = set()  # Ensemble pour stocker les acteurs connaissant l'acteur donné
    acteurs_visites = set()  # Ensemble pour stocker les acteurs déjà visités
    acteurs_a_visiter = set([(acteur, 0)])  # Ensemble pour stocker les acteurs à visiter, avec leur distance
    i = 0

    while i < distance:  # Itération jusqu'à la distance spécifiée
        nouveaux_acteurs = set()  # Ensemble pour stocker les nouveaux acteurs à visiter
        for act, d in acteurs_a_visiter:  # Pour chaque acteur à visiter
            if act not in acteurs_visites:  # Vérifier si l'acteur n'a pas déjà été visité
                acteurs_visites.add(act)  # Ajout de l'acteur à l'ensemble des acteurs visités
                dico_acteur = dicoActeur(act)  # Obtenir les collaborateurs de l'acteur
                for valeurs in dico_acteur.values():  # Pour chaque valeur dans le dictionnaire
                    for val in valeurs:  # Pour chaque valeur dans les valeurs du dictionnaire
                        if isinstance(val, str): 
                            if val not in acteurs_connaissant : # Vérifier si la valeur est une chaîne de caractères (nom de l'acteur)
                                nouveaux_acteurs.add((val, d+1))  # Ajout du nouvel acteur avec une distance incrémentée
                                acteurs_connaissant.add((val, d+1))  # Ajout du nouvel acteur à ceux qui connaissent l'acteur donné
        acteurs_a_visiter = nouveaux_acteurs  # Mettre à jour les acteurs à visiter avec les nouveaux acteurs découverts
        i += 1
        d+=1

    liste_triee = sorted(list(acteurs_connaissant), key=lambda x: x[1])

    return liste_triee  # Retourner la liste des acteurs connaissant l'acteur donné jusqu'à la distance spécifiée

#print(collabProch('Salim Kumar',6))

def centralite(acteur):
    distanceMax = collabProch(acteur,20)[-1][1]
    return distanceMax
print(centralite('Salim Kumar'))