# -*- coding: utf-8 -*-
# Ce code permet d'ouvrir la base de données et de créer une (liste finale) de listes (chaque individu) de listes (chaque morceau)
# On pourra ensuite appeler chaque élément de cette liste pour lui appliquer le code de calcul
# Ces éléments auront la dénomination liste_finale[i]

from itertools import groupby
from Fonction_Calcul_Bovin import calcul_bovin # import du code Fonction_Calcul (permet de calculer les facteurs d'allocation biophysique, massique et économique)
from Fonction_Calcul_Ovin import calcul_ovin # import du code Fonction_Calcul (permet de calculer les facteurs d'allocation biophysique, massique et économique)
from Fonction_Calcul_Veau import calcul_veau # import du code Fonction_Calcul (permet de calculer les facteurs d'allocation biophysique, massique et économique)
import csv
import math


def preparation_bdd(bdd):
# On crée des une liste de listes qui représente le CSV
    Database = []
    for row in bdd:
        Database.append(row)

# On enlève la première ligne (titres de colonnes)
    del(Database[0])

# On crée un database_tuplée dont le premier élément correspond aux trois premiers éléments de database dans un tuple
    Database_tuplée = []
    for item in Database:
        [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] = item
        Database_tuplée.append([(a,b,c),d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])

# On construit un dictionnaire qui prend pour clé la première valeur de chaque liste
    dico = dict((i,list(j)) for i,j in  groupby(sorted(Database_tuplée), key=lambda i:i[0]))

# On construit la liste des individus
    liste_individus = []
    for i in range(0,len(Database_tuplée)):
        liste_individus.append(Database_tuplée[i][0])

# A laquelle on enlève les doublons
    liste_individus = list(set(liste_individus))

# On trie la liste (car sinon le dico sort des résultats dans un ordre qui semble aléatoire)
    liste_individus = sorted(liste_individus)

# On retransforme les tuples en liste et on les ajoute à la liste finale
    liste_individus_new = []
    liste_finale = []
    for t in range(0,len(liste_individus)):
        liste_individus_new = []
        for item in dico[liste_individus[t]]:
            [(a,b,c),d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z] = item
            liste_individus_new.append([a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z])
        liste_finale.append(liste_individus_new)

    return liste_finale
