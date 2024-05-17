import requetes

def demander_charger():
    """Demande si l'utilisateur veut utiliser un de ces fichiers
    """
    rep = " "
    while rep not in "ON":
        rep = input("Voulez vous utilisez un de vos fichier txt? O/N : ")
    if rep == "O":
        nom_fic =input("Quel est le nom du fichier? : ")
    
        try:  
            return requetes.json_vers_nx(nom_fic)
        
        except:  
            print("Je ne connais pas ce fichier nous avons utiliser un fichier par défaut")
            requetes.json_vers_nx('dataSimplifiee.txt')
    elif rep == "N":
        return requetes.json_vers_nx('dataSimplifiee.txt')

def demander_2_acteurs():
    """Demande à l'utilisateur les 2 acteurs à utiliser
    """
    G = demander_charger()
    rep1 = input("Quel est le premier acteur : ")
    rep2 = input("Quel est le deuxième acteur : ")
    if (rep1 in G.nodes and rep2 in G.nodes):
        return (rep1,rep2,G)
    print("Un des 2 acteurs n'est pas dans le graphe")
    return "","",""

def demander_1_acteur():
    """Demande à l'utilisateur l'acteur à utiliser
    """
    G = demander_charger()
    rep1 = input("Quel est le premier acteur : ")
    if (rep1 in G.nodes):
        return (rep1,G)
    print ("L'acteur n'est pas dans le graphe")
    return "",""

def demander_distance():
    """Demande à l'utilisateur la distance qu'il veut étudier
    """
    rep = input("Quelle distance souhaitez vous étudiez : ")
    try:
        int(rep)
        rep1 =int(rep)
        return rep1
    except:
        print("Ceci n'est pas un nombre")
        return None


# ici votre programme principal"
def programme_principal():
    ok = True
    rep1 = " "
    while ok:
        print("Bienvenue")
        print("1 : Voir le graphe")
        print("2 : Voir le graphe a partir d'un de fichier *.txt")
        print("3 : Voir le centre du graphe")
        print("4 : Voir tout les acteurs qui ont travaillé avec 2 acteurs donnés")
        print("5 : Voir le couple d'acteurs qui sont le plus éloignés du graphe")
        print("6 : Voir la distance qui sépare deux acteurs")
        print("7 : Voir tous les acteurs qui sont à une distance donnée d'un acteur donné")
        print("8 : Voir la centralité d'un acteur")
        print("9 : Arrêter le programme")
        rep1 = (input("Que Voulez vous faire? (répondre avec 1 2 3 4 5 6 7 8 ou 9 ) : "))
        try:
             int(rep1)
             rep1 =int(rep1)
        except:
            print("Ceci n'est pas un nombre")
            return None
        if rep1 >=1 and rep1 <= 9:
            if rep1 == 1 :
                G = requetes.json_vers_nx('dataSimplifiee.txt')
            elif rep1 == 2 :
                try:
                    G = demander_charger()
                except:
                    print("Le fichier donné ne fonctionne pas")
            elif rep1 == 3 :
                try:
                    G = demander_charger()
                    print(requetes.centre_hollywood(G))
                except:
                    print("Le fichier donné ne fonctionne pas")
            elif rep1 == 4:
                try:
                    act = demander_2_acteurs()
                    print(requetes.collabCommuns(act[0],act[1]))
                except:
                    print("Un des deux acteurs n'est pas dans le graphe")
            elif rep1 ==5:
                try:
                    G = demander_charger()
                    print(requetes.eloignement_max(G))
                except:
                    print("Le fichier donné ne fonctionne pas")
            elif rep1 == 6:
                try:
                    act = demander_2_acteurs()
                    G = act[2]
                    print(requetes.est_proche(G,act[0],act[1]))
                except:
                    print("Un des deux acteurs n'est pas dans le graphe")
            elif rep1 == 7:
                try:
                    act = demander_1_acteur()
                    G = act[1]
                    distance = demander_distance()
                    print(requetes.collaborateurs_proches(G,act[0],distance))
                except:
                    print("L'acteur n'est pas dans le graphe ")
            elif rep1 == 8:
                try:
                    act = demander_1_acteur()
                    G = act[1]
                    print(requetes.centralite(G,act[0]))
                except:
                    print("Le fichier donné ne fonctionne pas")
            elif rep1 == 9:
                ok = False
        else:
            print("Ceci n'est pas un nombre compris dans la plage")


programme_principal()
