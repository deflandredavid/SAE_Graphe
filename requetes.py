def collabCommuns(acteur1, acteur2):
    lesActeurs = set()
    for film in films:
        for (cle,valeur) in film.items():
            if(cle == "Cast"):
                for val in valeur:
                    lesActeurs.add(val)
    return lesActeurs

def collabProch(acteur, distance):
    collab = set()
    i = 1
    act = acteur
    while i <distance:
        for film in films:
            for (cle,valeur) in film.items():
                if (cle == "Cast"):
                    if(act in valeur):
                            for val in valeur:
                                collab.add(val,i)
                            act = val
                            i = i+1
    return collab

def centralite(acteur):
    distanceMax = 0
    acteurMax = None
    for act in collab:
        if(act in film):
            for actor in cast:
                collab.add(actor,i)
        i = i+1
        distanceMax = i
        acteurMax = act
    return (acteurMax,distanceMax)