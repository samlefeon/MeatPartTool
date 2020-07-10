# -*- coding: utf-8 -*-
# Ce code sert à calculer les facteurs d'allocation à partir d'une liste représentant une espèce

import csv
import math


def calcul_ovin(Tableau):
# On définit les listes. Tableau est une liste de listes. Les autres listes sont les différentes colonnes du csv
    Coproducts = [] # Liste des coproduits
    Destination = [] # Destination (ex : Human Food)
    Group_of_Tissus = [] # Nature des tissus (ex : Carcass)
    BW = [] # Pourcentage du poids total
    Water = [] # Pourcentage d'eau
    Dry_Matter = [] # Pourcentage de matière sèche
    Lipids = [] # Pourcentage de lipides
    Protein = [] # Pourcentage de protéines
    Economic_Value = [] # Valeur économique
    E_maint = [] # Energie pour l'entretien des tissus

# On définit des variables importantes pour le calcul
    Coeff_Gompertz = float(Tableau[0][12])
    P_0 = float(Tableau[0][13]) # Poids à la naissance
    P_m = float(Tableau[0][14]) # Poids à maturité
    P_ab = float(Tableau[0][15]) # Poids à l'abattage
    FAT_0 = float(Tableau[0][16]) # Pourcentage de graisse à la naissance
    FAT_m = float(Tableau[0][17]) # Pourcentage de graisse à maturité
    FAT_max = float(Tableau[0][18]) # Pourcentage maximal de graisse
    Ratio_water_prot = float(Tableau[0][19]) # Ratio eau-protéine
    z_1_prot = float(Tableau[0][20]) # Taux de rétention pour la croissance des protéines
    z_2_lip = float(Tableau[0][21]) # Taux de rétention pour la croissance des lipides
    Coeff_act = float(Tableau[0][22]) # Coefficient d'activité

# On récupère les "sous listes" du Tableau
    n = len(Tableau)
    for i in range(0,n):
        Coproducts.append(Tableau[i][4])
        Destination.append(Tableau[i][5])
        Group_of_Tissus.append(Tableau[i][6])
        BW.append(float(Tableau[i][7]))
        Water.append(float(Tableau[i][8]))
        Dry_Matter.append(float(Tableau[i][9]))
        Lipids.append(float(Tableau[i][10]))
        Protein.append(float(Tableau[i][11]))
        Economic_Value.append(float(Tableau[i][24]))
        E_maint.append(float(Tableau[i][23]))


# on calcule les pourcentages du poids total pour chaque paramètre et on les stocke dans des nouvelles listes
    Water_on_BW = []
    Dry_Matter_on_BW = []
    Lipids_on_BW = []
    Protein_on_BW = []
    n = len(BW)
    for i in range(n):
        Water_on_BW.append((BW[i]/100)*Water[i]/100)
        Dry_Matter_on_BW.append((BW[i]/100)*Dry_Matter[i]/100)
        Lipids_on_BW.append((BW[i]/100)*Lipids[i]/100)
        Protein_on_BW.append((BW[i]/100)*Protein[i]/100)

# on crée une liste similaire à BW mais en mettant à 0 la valeur lorsque la destination est Spreading/Compost
    BW_spreading = []
    n = len(BW)
    for i in range(n):
        if Destination[i]=='Spreading/Compost':
            BW_spreading.append(0)
        else:
            BW_spreading.append(BW[i]/100)

# on crée une liste EBW qui est la liste précédente normalisée
    EBW = []
    n = len(BW_spreading)
    for i in range(n):
        EBW.append(BW_spreading[i]/sum(BW_spreading))

# on calcule les pourcentages du poids total vide (EBW) pour chaque paramètre et on les stocke dans des nouvelles listes
    Water_on_EBW = []
    Dry_Matter_on_EBW = []
    Lipids_on_EBW = []
    Protein_on_EBW = []
    n = len(BW)
    for i in range(n):
        Water_on_EBW.append(EBW[i]*Water[i]/100)
        Dry_Matter_on_EBW.append(EBW[i]*Dry_Matter[i]/100)
        Lipids_on_EBW.append(EBW[i]*Lipids[i]/100)
        Protein_on_EBW.append(EBW[i]*Protein[i]/100)

# On calcule les Pi et les Qi pour chaque morceau (part du total des protéines et lipides)
    Q_i = []
    P_i = []
    n = len(Lipids_on_EBW)
    for i in range(n):
        Q_i.append(Lipids_on_EBW[i]/sum(Lipids_on_EBW))
        P_i.append(Protein_on_EBW[i]/sum(Protein_on_EBW))

# On calcule des paramètres importants
    EBW_pourcentage = sum(BW_spreading)/(sum(BW)/100) # Pourcentage de corps vide dans le poids total
    EBW_ab = EBW_pourcentage * P_ab # Poids vide à l'abattage
    EBW_0 = EBW_pourcentage * P_0 # Poids vide à la naissance
    EBW_m = EBW_pourcentage * P_m # Poids vide à maturité
    LIP_0 = EBW_0 * FAT_0 # Quantité de lipides sur poids vide à la naissance
    LIP_m = EBW_m * FAT_m # Quantité normale de lipides sur le poids vide à maturité
    PROT_0 = EBW_0 * ((1-FAT_0)/(1+Ratio_water_prot)) # Quantité de protéines à la naissance
    PROT_m = EBW_m * ((1-FAT_m)/(1+Ratio_water_prot)) # Quantité de protéines à maturité
    Gompertz_Parameter = Coeff_Gompertz/math.log(PROT_m/PROT_0) # Paramètre de Gompertz
    a_t = (FAT_m-FAT_0)/(EBW_m-EBW_0) # a(t)

# On calcule PROT(t)
    PROT_t_init = []
    for i in range(0,10000):
        PROT_t_init.append(PROT_0*math.exp(Coeff_Gompertz*(1-math.exp(-Gompertz_Parameter*i))/Gompertz_Parameter))

# On calcule b(t) et c(t)
    b_t_init = []
    c_t_init = []
    for i in range(0,10000):
        b_t_init.append((FAT_0-1)+a_t*(2*PROT_t_init[i]*(1+Ratio_water_prot)-EBW_0))
        c_t_init.append(FAT_0*PROT_t_init[i]*(1+Ratio_water_prot)+a_t*PROT_t_init[i]*(1+Ratio_water_prot)*(PROT_t_init[i]*(1+Ratio_water_prot)-EBW_0))

# On calcule LIP(t)
    LIP_t_init = []
    for i in range(0,10000):
        LIP_t_init.append((1/(2*a_t))*(-b_t_init[i]-math.sqrt(b_t_init[i]*b_t_init[i]-4*a_t*c_t_init[i])))

# On calcule W(t)
    W_t_init = []
    for i in range(0,10000):
        W_t_init.append(Ratio_water_prot*PROT_t_init[i])

# On calcule EBW(t)
    EBW_t_init = []
    for i in range(0,10000):
        EBW_t_init.append(PROT_t_init[i]+LIP_t_init[i]+W_t_init[i])

# On calcule BW_t
    BW_t_init = []
    for i in range(0,10000):
        BW_t_init.append(EBW_t_init[i]/EBW_pourcentage)

# On réduit les listes précédentes au bon nombre de jour (par rapport au poids final)
    i = 0
    while BW_t_init[i] < P_ab :
        jour = i
        i = i+1
    jour=jour+1

    PROT_t = []
    b_t = []
    c_t = []
    LIP_t = []
    W_t = []
    EBW_t = []
    BW_t = []

    for i in range (0,jour+1):
        PROT_t.append(PROT_t_init[i])
        b_t.append(b_t_init[i])
        c_t.append(c_t_init[i])
        LIP_t.append(LIP_t_init[i])
        W_t.append(W_t_init[i])
        EBW_t.append(EBW_t_init[i])
        BW_t.append(BW_t_init[i])

# On calcule l'énergie nécessaire pour l'entretien
    Emaint = []
    n = len(Group_of_Tissus)
    for i in range(n):
        #Emaint.append(P_i[i]*Emaint_par[i]*sum(PROT_t))
        Emaint.append(P_i[i]*E_maint[i]*sum(PROT_t))

# On calcule l'énergie nécessaire pour la croissance
    Ecroiss = []
    n = len(Group_of_Tissus)
    for i in range(n):
        Ecroiss.append(z_1_prot*(PROT_t[jour]-PROT_t[0])*P_i[i]+z_2_lip*(LIP_t[jour]-LIP_t[0])*Q_i[i])

# On calcule l'énergie pour l'activité
    Eact = []
    n = len(Group_of_Tissus)
    for i in range(n):
        Eact.append(Emaint[i]*BW_t[i])

# On calcule la répartition biophysique (somme des activités pour chaque partie sur somme totale des activités)
    Biophys_Part_init = []
    n = len(Group_of_Tissus)
    for i in range(n):
        Biophys_Part_init.append((Emaint[i]+Ecroiss[i]+Eact[i])/(sum(Emaint)+sum(Ecroiss)+sum(Eact)))

# On calcule la répartition biophysique (somme des activités pour chaque partie sur somme totale des activités) mais en mettant à zéro les valeurs pour lesquelles la destination est le déchet
    Biophys_Part = []
    n = len(Group_of_Tissus)
    for i in range(n):
        if Destination[i] == 'C1-C2 for disposal':
            Biophys_Part.append(0)
        else:
            Biophys_Part.append(Biophys_Part_init[i])

# Enfin, on calcule les facteurs d'allocation biophysique !
    Biophys_alloc_fact = []
    n = len(Group_of_Tissus)
    for i in range(n):
        Biophys_alloc_fact.append(Biophys_Part[i]/(sum(Biophys_Part)))

# Et les facteurs d'allocation biophysique par kg !
    Biophys_alloc_fact_kg = []
    n = len(Group_of_Tissus)
    for i in range(n):
        if EBW[i] != 0:
            Biophys_alloc_fact_kg.append(Biophys_alloc_fact[i]/(EBW[i]*P_ab))
        else:
            Biophys_alloc_fact_kg.append(0)

# On calcule également les facteurs d'allocation massique
    Mass_alloc_fact = []
    BW_corrected = []
    n = len(Group_of_Tissus)
    for i in range(n):
        if Destination[i] == 'C1-C2 for disposal' or Destination[i] == 'Spreading/Compost':
            BW_corrected.append(0)
        else:
            BW_corrected.append(BW[i])
    for i in range(n):
            Mass_alloc_fact.append((BW_corrected[i]/100)/(sum(BW_corrected)/100))


# Et les facteurs d'allocation massique par kg !
    Mass_alloc_fact_kg = []
    n = len(Group_of_Tissus)
    for i in range(n):
        if EBW[i] != 0:
            Mass_alloc_fact_kg.append(Mass_alloc_fact[i]/(EBW[i]*P_ab))
        else:
            Mass_alloc_fact_kg.append(0)

# On calcule également les facteurs d'allocation économique
    Eco_alloc_fact = []
    BW_Eco = []
    n = len(Group_of_Tissus)
    for i in range(n):
        BW_Eco.append((BW[i]/100)*Economic_Value[i])
    for i in range(n):
        Eco_alloc_fact.append((BW_Eco[i])/(sum(BW_Eco)))

# Et les facteurs d'allocation économique par kg !
    Eco_alloc_fact_kg = []
    n = len(Group_of_Tissus)
    for i in range(n):
        if EBW[i] != 0:
            Eco_alloc_fact_kg.append(Eco_alloc_fact[i]/(EBW[i]*P_ab))
        else:
            Eco_alloc_fact_kg.append(0)

# On crée une liste avec les 3 listes de facteurs d'allocation
    Alloc_fact = [Biophys_alloc_fact, Mass_alloc_fact, Eco_alloc_fact, Biophys_alloc_fact_kg, Mass_alloc_fact_kg, Eco_alloc_fact_kg]

    return(Alloc_fact)
