def collabCommuns(acteur1, acteur2):
    lesActeurs = set()
    for film in films:
        if(acteur1 in film or acteur2 in film):
            for acteur in cast:
                lesActeurs.add(acteur)
    return lesActeurs

def collabProch(acteur, distance):
    collab = set()
    i = 1
    act = acteur
    while i <distance:
        for act in collab:
            if(act in film):
                for actor in cast:
                    collab.add(actor,i)
            i = i+1
    return collab

def centralite(acteur):
    distanceMax = 0
    for act in collab:
        if(act in film):
            for actor in cast:
                collab.add(actor,i)
        i = i+1