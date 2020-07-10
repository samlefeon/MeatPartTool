# -*- coding: utf-8 -*-
# Ce code dessine l'interface graphique de l'outil

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from PandasModel import PandasModel
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFont, QPixmap


app = QApplication([])
screen_resolution = app.desktop().screenGeometry()
width = screen_resolution.width()
height = screen_resolution.height()
ratio_largeur = width/1920
ratio_police = height/1200
ratio_hauteur = ratio_largeur


class Application(object):
    def setupUi(self, Application):

        # Création de la fenêtre principale
        Application.setObjectName("Application") # Nomme l'objet
        Application.setWindowTitle("MeatPartTool V4.0") # Modifie le nom de la fenêtre
        Application.resize(ratio_largeur*1900, ratio_hauteur*900) # Dimensionne la fenêtre

        self.font = QtGui.QFont()
        self.font.setPointSize(10*ratio_police)

        # Création du support à onglets
        self.tabWidget = QtWidgets.QTabWidget(Application) # Crée un support pour onglets sur la fenêtre principale
        self.tabWidget.setGeometry(QtCore.QRect(ratio_largeur*0, ratio_hauteur*0, ratio_largeur*1900, ratio_hauteur*900)) # Dimensionne et positionne
        self.tabWidget.setObjectName("tabWidget") # Nomme l'ensemble d'onglets
        self.tabWidget.setFont(self.font)

        # Création de l'onglet d'introduction et de son contenu
        self.tab_intro = QtWidgets.QWidget() # Crée un onglet
        self.tab_intro.setObjectName("tab_intro") # Nomme le premier objet onglet
        self.tabWidget.addTab(self.tab_intro, "Introduction") # Crée l'onglet et modifie le nom affiché
        self.title = QtWidgets.QLabel(self.tab_intro)
        self.title.setGeometry(QtCore.QRect(ratio_largeur*300,ratio_hauteur*100,ratio_largeur*1500,ratio_hauteur*100))
        self.title.setText("MeatPartTool")
        self.title.setFont(QFont("Arial", 50))
        self.title.setStyleSheet("color: #F24C04; font : bold")
        self.general_introduction = QtWidgets.QLabel(self.tab_intro)
        self.general_introduction.setGeometry(QtCore.QRect(ratio_largeur*400,ratio_hauteur*100,ratio_largeur*1500,ratio_hauteur*500))
        self.general_introduction.setText("Design to Access and Assess \n           Economic, Mass and Biophysical Allocation Factors \n                     for the Life Cycle Assessment of meat coproducts")
        self.general_introduction.setStyleSheet("color: blue")
        self.general_introduction.setFont(QFont("Arial", 30))
        self.developpers = QtWidgets.QLabel(self.tab_intro)
        self.developpers.setGeometry(QtCore.QRect(ratio_largeur*400,ratio_hauteur*300,ratio_largeur*1500,ratio_hauteur*500))
        self.developpers.setText("Developped by INRAE, IDELE, CELENE and Samuel Le Féon \nFunded by Interbev (SECU 19-20)")
        self.developpers.setStyleSheet("color: black")
        self.developpers.setStyleSheet("font: italic")
        self.developpers.setFont(QFont("Arial", 15))
        #self.zone_logoMeatPartTool2 = QtWidgets.QLabel(self.tab_intro)
        #self.zone_logoMeatPartTool2.setGeometry(QtCore.QRect(ratio_largeur*500,ratio_hauteur*100,ratio_largeur*800,ratio_hauteur*600))
        #self.logoMeatPartTool2 = QPixmap('D:/Professionnel/Recherche/2019/Interbev/Logos/MeatPartTool_total.png')
        #self.zone_logoMeatPartTool2.setPixmap(self.logoMeatPartTool2.scaled(ratio_largeur*800,ratio_hauteur*600))
        #self.bouton_tuto = QtWidgets.QPushButton(self.tab_intro)
        #self.bouton_tuto.setGeometry(QtCore.QRect(ratio_largeur*525, ratio_hauteur*650, ratio_largeur*150, ratio_hauteur*30)) # Positionne puis dimensionne le bouton
        #self.bouton_tuto.setText("Open Tutorial") # Modifie le label du bouton
        #self.bouton_tuto.setFont(self.font)
        #self.bouton_tuto.setStyleSheet("QPushButton{ background-color: #55CA9F }")
        #self.bouton_rapport = QtWidgets.QPushButton(self.tab_intro)
        #self.bouton_rapport.setGeometry(QtCore.QRect(ratio_largeur*525, ratio_hauteur*700, ratio_largeur*150, ratio_hauteur*30)) # Positionne puis dimensionne le bouton
        #self.bouton_rapport.setText("Open Report") # Modifie le label du bouton
        #self.bouton_rapport.setFont(self.font)
        #self.bouton_rapport.setStyleSheet("QPushButton{ background-color: #55CA9F }")


        # Création de l'onglet 1 et de son contenu
        self.tab = QtWidgets.QWidget() # Crée un onglet
        self.tab.setObjectName("tab") # Nomme le premier objet onglet
        self.tabWidget.addTab(self.tab, "Open Database") # Crée l'onglet et modifie le nom affiché
        # Création d'un bouton
        self.pushButton = QtWidgets.QPushButton(self.tab) # Crée un bouton sur l'onglet tab de la fenêtre Application
        self.pushButton.setGeometry(QtCore.QRect(ratio_largeur*20, ratio_hauteur*50, ratio_largeur*200, ratio_hauteur*30)) # Positionne puis dimensionne le bouton
        self.pushButton.setObjectName("Chargement") # Nomme le bouton
        self.pushButton.setText("Open Database") # Modifie le label du bouton
        self.pushButton.setFont(self.font)
        # Creation de la barre de texte sur le premier onglet
        self.pathLE = QtWidgets.QLineEdit(self.tab)
        self.pathLE.setGeometry(QtCore.QRect(ratio_largeur*30,ratio_hauteur*100,ratio_largeur*1500,ratio_hauteur*30))
        self.pathLE.setFont(self.font)
        # Création du tableau pour afficher la bdd sur le premier onglet
        self.pandasTv = QtWidgets.QTableView(self.tab)
        self.pandasTv.setGeometry(QtCore.QRect(ratio_largeur*30,ratio_hauteur*150,ratio_largeur*1500,ratio_hauteur*600))
        self.pandasTv.setSortingEnabled(True)
        self.pandasTv.setFont(self.font)

        # Création de l'onglet 2 et de son contenu
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "Select an Item")
        # Création de 4 combobox (espèce, race, catégorie, mode d'élevage)
        self.combobox_especes_tab_2 = QtWidgets.QComboBox(self.tab_2)
        self.combobox_especes_tab_2.setGeometry(QtCore.QRect(ratio_largeur*400, ratio_hauteur*50, ratio_largeur*200, ratio_hauteur*20))
        self.combobox_especes_tab_2.setFont(self.font)
        self.combobox2 = QtWidgets.QComboBox(self.tab_2)
        self.combobox2.setGeometry(QtCore.QRect(ratio_largeur*700, ratio_hauteur*50, ratio_largeur*200, ratio_hauteur*20))
        self.combobox2.setFont(self.font)
        self.combobox3 = QtWidgets.QComboBox(self.tab_2)
        self.combobox3.setGeometry(QtCore.QRect(ratio_largeur*1000, ratio_hauteur*50, ratio_largeur*200, ratio_hauteur*20))
        self.combobox3.setFont(self.font)
        self.combobox7 = QtWidgets.QComboBox(self.tab_2)
        self.combobox7.setGeometry(QtCore.QRect(ratio_largeur*1300, ratio_hauteur*50, ratio_largeur*200, ratio_hauteur*20))
        self.combobox7.setFont(self.font)
        # Création du tableau pour l'affichage sur l'onglet 2
        self.tableIndividu = QtWidgets.QTableWidget(70,26,self.tab_2)
        self.tableIndividu.setGeometry(QtCore.QRect(ratio_largeur*100, ratio_hauteur*150, ratio_largeur*1500, ratio_hauteur*600))
        self.tableIndividu.setHorizontalHeaderLabels(['Species','Breed','Category',"Rearing Method",'Co-product','Destination','Group of tissues','BW (%)',
                                                     'Water (%)','DM  (%)','Lipids  (%)','Proteins (%)','Gompertz Coeff.','EBW0','EBWm',
                                                     'EBWsl','FAT0','FATm','FATsl','Rwp','Z1prot','Z2lip','Act. Coeff.','Energy for Maint.','Value','Carcass Yield'])
        self.tableIndividu.setFont(self.font)
        self.tableIndividu.horizontalHeader().setFont(self.font)
        self.tableIndividu.resizeColumnsToContents()


        # Création de l'onglet 3 et de son contenu
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.tabWidget.addTab(self.tab_3, "Allocation Factors")
        # Création du tableau pour l'affichage des facteurs d'allocation bruts sur l'onglet 3
        self.table_facteurs = QtWidgets.QTableWidget(70,8,self.tab_3)
        self.table_facteurs.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*50, ratio_largeur*800, ratio_hauteur*700))
        self.table_facteurs.setHorizontalHeaderLabels(['Co-product','Destination','Total Impact \n Weighting with \n Biophysical \n Allocation \n (per coproduct)','Total Impact \n Weighting with \n Mass \n Allocation \n (per coproduct)','Total Impact \n Weighting with \n Economic \n Allocation \n (per coproduct)', 'Allocation \n Factors with \n Biophysical \n Allocation \n (per kg of \n coproduct)', 'Allocation \n Factors with \n Mass \n Allocation \n (per kg of \n coproduct)','Allocation \n Factors with \n Economic \n Allocation \n (per kg of \n coproduct)'])
        self.table_facteurs.setFont(self.font)
        self.table_facteurs.horizontalHeader().setFont(self.font)
        self.table_facteurs.resizeColumnsToContents()
        self.result_title_1 = QtWidgets.QLabel(self.tab_3)
        self.result_title_1.setGeometry(QtCore.QRect(ratio_largeur*50,ratio_hauteur*15,ratio_largeur*800,ratio_hauteur*25))
        self.result_title_1.setText("Results per coproduct")
        self.result_title_1.setStyleSheet("color: black")
        self.result_title_1.setFont(QFont("Arial",15))
        self.result_title_1.setStyleSheet("font: bold")
        self.result_title_2 = QtWidgets.QLabel(self.tab_3)
        self.result_title_2.setGeometry(QtCore.QRect(ratio_largeur*900,ratio_hauteur*15,ratio_largeur*800,ratio_hauteur*25))
        self.result_title_2.setText("Results per destination")
        self.result_title_2.setStyleSheet("color: black")
        self.result_title_2.setFont(QFont("Arial",15))
        self.result_title_2.setStyleSheet("font: bold")
        # Création du tableau pour l'affichage des facteurs d'allocation bruts sur l'onglet 3
        self.table_facteurs_par_destination = QtWidgets.QTableWidget(8,4,self.tab_3)
        self.table_facteurs_par_destination.setGeometry(QtCore.QRect(ratio_largeur*900, ratio_hauteur*400, ratio_largeur*500, ratio_hauteur*300))
        self.table_facteurs_par_destination.setHorizontalHeaderLabels(['Destination','Total Impact \n Weighting with \n Biophysical \n Allocation','Total Impact \n Weighting with \n Mass \n Allocation','Total Impact \n Weighting with \n Economic \n Allocation'])
        self.table_facteurs_par_destination.setFont(self.font)
        self.table_facteurs_par_destination.horizontalHeader().setFont(self.font)
        self.table_facteurs_par_destination.resizeColumnsToContents()
        # Création d'une zone de graphe sur l'onglet 3
        self.graphe = QtWidgets.QGraphicsView(self.tab_3)
        self.graphe.setFont(self.font)
        self.graphe.setGeometry(QtCore.QRect(ratio_largeur*900, ratio_hauteur*50, ratio_largeur*900, ratio_hauteur*300))
        # Création d'un bouton
        self.Bouton_Excel = QtWidgets.QPushButton(self.tab_3) # Crée un bouton sur l'onglet tab de la fenêtre Application
        self.Bouton_Excel.setGeometry(QtCore.QRect(ratio_largeur*100, ratio_hauteur*775, ratio_largeur*250, ratio_hauteur*60)) # Positionne puis dimensionne le bouton
        self.Bouton_Excel.setText("Export to Excel") # Modifie le label du bouton
        self.Bouton_Excel.setFont(self.font)
        self.texte_specie_result = QtWidgets.QTextEdit(self.tab_3)
        self.texte_specie_result.setGeometry(QtCore.QRect(ratio_largeur*1600, ratio_hauteur*450, ratio_largeur*200, ratio_hauteur*30))
        self.texte_race_result = QtWidgets.QTextEdit(self.tab_3)
        self.texte_race_result.setGeometry(QtCore.QRect(ratio_largeur*1600, ratio_hauteur*500, ratio_largeur*200, ratio_hauteur*30))
        self.texte_category_result = QtWidgets.QTextEdit(self.tab_3)
        self.texte_category_result.setGeometry(QtCore.QRect(ratio_largeur*1600, ratio_hauteur*550, ratio_largeur*200, ratio_hauteur*30))
        self.texte_rearing_result = QtWidgets.QTextEdit(self.tab_3)
        self.texte_rearing_result.setGeometry(QtCore.QRect(ratio_largeur*1600, ratio_hauteur*600, ratio_largeur*200, ratio_hauteur*30))


        # Création de l'onglet 4 et de son contenu
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "Create a New Item")

        self.table4 = QtWidgets.QTableWidget(70,9,self.tab_4)
        self.table4.setGeometry(QtCore.QRect(ratio_largeur*300, ratio_hauteur*50, ratio_largeur*1100, ratio_hauteur*600))
        self.table4.setHorizontalHeaderLabels(['Co-products','Destination','Group of tissues','BW (%)','Water (%)','Dry Matter  (%)','Lipids  (%)','Proteins (%)','Value (€/t)'])
        self.table4.setFont(self.font)
        self.table4.horizontalHeader().setFont(self.font)
        self.table4.resizeRowsToContents()
        self.table4.resizeColumnsToContents()
        self.table4.setColumnWidth(0,220)
        self.table4.setColumnWidth(1,140)
        self.table4.setColumnWidth(2,120)

        for i in range(0,self.table4.rowCount()):
            self.combobox_Destination_table4 = QtWidgets.QComboBox()
            liste_Destination = ['To be specified', 'Pet food', 'PAP C3', 'Gelatin C3', 'C1-C2 for disposal', 'Skin tannery C3', 'Human food', 'Fat and greaves C3', 'Spreading/Compost']
            self.combobox_Destination_table4.addItems(liste_Destination)
            self.table4.setCellWidget(i, 1, self.combobox_Destination_table4)

        for i in range(0,self.table4.rowCount()):
            self.combobox_Tissues_table4 = QtWidgets.QComboBox()
            liste_Tissues = ['To be specified', 'whole body', 'Carcass', 'GIT', 'Liver', 'Others']
            self.combobox_Tissues_table4.addItems(liste_Tissues)
            self.table4.setCellWidget(i, 2, self.combobox_Tissues_table4)

        self.table5 = QtWidgets.QTableWidget(12,1,self.tab_4)
        self.table5.setGeometry(QtCore.QRect(ratio_largeur*1420, ratio_hauteur*50, ratio_largeur*400, ratio_hauteur*480))
        self.table5.setVerticalHeaderLabels(['Gompertz Coefficient','Empty Body Weight at Birth (kg)','Empty Body Weight at Maturity (kg)',"Empty Body Weight at Slaughter Age (kg)",
                                            'Birth body Fat Percentage','Normal mature body Fat Percentage','Fat percentage at slaughter age','Ratio of Body Weight Water to Protein',
                                            'Protein Energy Content (MJ/kg)','Lipid Energy Content (MJ/kg)','Coefficient for Activity Energy','Carcass Yield'])
        self.table5.setHorizontalHeaderLabels(['Value'])
        self.table5.setFont(self.font)
        self.table5.horizontalHeader().setFont(self.font)
        self.table5.resizeColumnsToContents()
        self.table6 = QtWidgets.QTableWidget(5,1,self.tab_4)
        self.table6.setGeometry(QtCore.QRect(ratio_largeur*1420, ratio_hauteur*550, ratio_largeur*400, ratio_hauteur*225))
        self.table6.setHorizontalHeaderLabels(['Energy for maintenance'])
        self.table6.setVerticalHeaderLabels(['Whole Body','Carcass','GIT','Liver','Others'])
        self.table6.setFont(self.font)
        self.table6.horizontalHeader().setFont(self.font)
        self.table6.resizeColumnsToContents()
        self.Bouton_Valider = QtWidgets.QPushButton(self.tab_4) # Crée un bouton sur l'onglet tab de la fenêtre Application
        self.Bouton_Valider.setGeometry(QtCore.QRect(ratio_largeur*600, ratio_hauteur*700, ratio_largeur*300, ratio_hauteur*60)) # Positionne puis dimensionne le bouton
        self.Bouton_Valider.setObjectName("Validate") # Nomme le bouton
        self.Bouton_Valider.setText("Save the New Item") # Modifie le label du bouton
        self.Bouton_Valider.setFont(self.font)
        # Création de 3 combobox (espèce, race, mois)
        self.combobox4 = QtWidgets.QComboBox(self.tab_4)
        self.combobox4.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*500, ratio_largeur*200, ratio_hauteur*20))
        self.combobox4.setFont(self.font)
        self.combobox5 = QtWidgets.QComboBox(self.tab_4)
        self.combobox5.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*530, ratio_largeur*200, ratio_hauteur*20))
        self.combobox5.setFont(self.font)
        self.combobox6 = QtWidgets.QComboBox(self.tab_4)
        self.combobox6.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*560, ratio_largeur*200, ratio_hauteur*20))
        self.combobox6.setFont(self.font)
        self.combobox8 = QtWidgets.QComboBox(self.tab_4)
        self.combobox8.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*590, ratio_largeur*200, ratio_hauteur*20))
        self.combobox8.setFont(self.font)
        self.Bouton_Modele = QtWidgets.QPushButton(self.tab_4) # Crée un bouton sur l'onglet tab de la fenêtre Application
        self.Bouton_Modele.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*640, ratio_largeur*200, ratio_hauteur*30)) # Positionne puis dimensionne le bouton
        self.Bouton_Modele.setObjectName("Modele") # Nomme le bouton
        self.Bouton_Modele.setText("Use a template") # Modifie le label du bouton
        self.Bouton_Modele.setFont(self.font)
        self.Bouton_Effacer = QtWidgets.QPushButton(self.tab_4) # Crée un bouton sur l'onglet tab de la fenêtre Application
        self.Bouton_Effacer.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*690, ratio_largeur*200, ratio_hauteur*30)) # Positionne puis dimensionne le bouton
        self.Bouton_Effacer.setObjectName("Effacer") # Nomme le bouton
        self.Bouton_Effacer.setText("Reset") # Modifie le label du bouton
        self.Bouton_Effacer.setFont(self.font)
        # Création de 3 zones de textes pour que l'utilisateur entre les infos sur son individu
        self.texte_espece = QtWidgets.QTextEdit(self.tab_4)
        self.texte_espece.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*100, ratio_largeur*200, ratio_hauteur*30))
        self.texte_race = QtWidgets.QTextEdit(self.tab_4)
        self.texte_race.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*180, ratio_largeur*200, ratio_hauteur*30))
        self.texte_mois = QtWidgets.QTextEdit(self.tab_4)
        self.texte_mois.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*260, ratio_largeur*200, ratio_hauteur*30))
        self.texte_elevage = QtWidgets.QTextEdit(self.tab_4)
        self.texte_elevage.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*340, ratio_largeur*200, ratio_hauteur*30))
        self.label_espece = QtWidgets.QLabel(self.tab_4)
        self.label_espece.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*70, ratio_largeur*200, ratio_hauteur*30))
        self.label_espece.setText("Species")
        self.label_espece.setFont(self.font)
        self.label_race = QtWidgets.QLabel(self.tab_4)
        self.label_race.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*150, ratio_largeur*200, ratio_hauteur*30))
        self.label_race.setText("Breed")
        self.label_race.setFont(self.font)
        self.label_mois = QtWidgets.QLabel(self.tab_4)
        self.label_mois.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*230, ratio_largeur*200, ratio_hauteur*30))
        self.label_mois.setText("Category")
        self.label_mois.setFont(self.font)
        self.label_elevage = QtWidgets.QLabel(self.tab_4)
        self.label_elevage.setGeometry(QtCore.QRect(ratio_largeur*50, ratio_hauteur*310, ratio_largeur*200, ratio_hauteur*30))
        self.label_elevage.setText("Rearing Method")
        self.label_elevage.setFont(self.font)

        # Création de l'onglet 5 et de son contenu
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tabWidget.addTab(self.tab_5, "Lexicon")
        self.table_lexicon = QtWidgets.QTableWidget(26,4,self.tab_5)
        self.table_lexicon.setGeometry(QtCore.QRect(ratio_largeur*20, ratio_hauteur*20, ratio_largeur*1760, ratio_hauteur*800))
        self.table_lexicon.setHorizontalHeaderLabels(['Abbreviation','English','French','Unit'])
        Abbreviations = ['Species','Breed','Category',"Rearing Method",'Co-product','Destination','Group of tissues','BW (%)',
                        'Water (%)','DM  (%)','Lipids  (%)','Proteins (%)','Gompertz Coeff.','EBW0','EBWm',
                        'EBWsl','FAT0','FATm','FATsl','Rwp','Z1prot','Z2lip','Act. Coeff.','Energy for Maint.','Value','Carcass Yield']
        English = ['Species','Breed','Category',"Rearing Method",'Co-product','Destination','Group of tissues','Percentage of Total Weight',
                  'Percentage of Water','Percentage of Dry Matter','Percentage of Lipids','Percentage of Proteins','Gompertz Coefficient',
                  'Empty Body Weight at Birth','Empty Body Weight at Maturity','Empty Body Weight at Slaughter Age',
                  'Birth Body Fat Percentage','Normal Mature Body Fat Percentage','Fat Percentage at Slaughter Age',
                  'Ratio of Body Weight Water to Protein','Retention rate for growth of proteins','Retention rate for growth of lipids',
                  'Coefficient for Activity Energy','Energy parameter for maintenance','Economic Value','Carcass Yield']
        French = ['Espèce','Race','Catégorie',"Mode d'élevage",'Co-produit','Destination','Group de tissus','Pourcentage du poids total',
                  "Pourcentage d'eau",'Pourcentage de matière sèche','Pourcentage de lipides','Pourcentage de protéines','Coefficient de Gompertz',
                  'Poids vif vide à la naissance','Poids vif vide à maturité',"Poids vif vide à l'abattoir",
                  'Pourcentage de graisses à la naissance','Pourcentage de graisses à maturité',"Pourcentage de graisses à l'abattoir",
                  'Ratio Eau-Protéines','Taux de rétention pour la croissance des protéines','Taux de rétention pour la croissance des lipides',
                  "Coefficient d'activité","Paramètre énergétique pour l'entretien",'Valeur économique','Rendement carcasse']
        Unit = ['Dimensionless','Dimensionless','Dimensionless','Dimensionless','Dimensionless','Dimensionless','Dimensionless',
                '%','%','%','%','%','Dimensionless','kg','kg','kg','Dimensionless','%','%','%','Dimensionless','MJ/kg','MJ/kg',
                'Dimensionless','MJ/kg/d','€/ton','%']
        for i in range(0,len(Abbreviations)):
            valeur_numerique_defaut = QtWidgets.QTableWidgetItem(str(Abbreviations[i]))
            self.table_lexicon.setItem(i,0,valeur_numerique_defaut)
            valeur_numerique_defaut_2 = QtWidgets.QTableWidgetItem(str(English[i]))
            self.table_lexicon.setItem(i,1,valeur_numerique_defaut_2)
            valeur_numerique_defaut_3 = QtWidgets.QTableWidgetItem(str(French[i]))
            self.table_lexicon.setItem(i,2,valeur_numerique_defaut_3)
            valeur_numerique_defaut_4 = QtWidgets.QTableWidgetItem(str(Unit[i]))
            self.table_lexicon.setItem(i,3,valeur_numerique_defaut_4)
        self.table_lexicon.setFont(self.font)
        self.table_lexicon.horizontalHeader().setFont(self.font)
        self.table_lexicon.resizeColumnsToContents()

        self.retranslateUi(Application)
        QtCore.QMetaObject.connectSlotsByName(Application)

    def retranslateUi(self, Application):
        _translate = QtCore.QCoreApplication.translate
