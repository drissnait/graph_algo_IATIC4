# -*- coding: utf-8 -*-

import pandas as pd #Pour traitement des fichiers csv
import csv
import os
import sys
import networkx as nx #generation des graphes
import matplotlib.pyplot as plt # graphes
from jgraph import *
import matplotlib.image as mpimg
from networkx.generators.random_graphs import erdos_renyi_graph
import os
from PIL import Image #Afficher les images
import numpy as np

"""
Pour lancer le programme : python AlgoProjet.py [nbr de sommets] [fichierCSV à traiter]
exemple : python AlgoProjet.py 10 choix GrapheGenere.csv
choix = 1 EdgarGilbert
choix = 2 BarabasiAlbert
"""

"""
Generer un graphe aleatoire avec la methode de edgard Gilbert
"""
def generationGrapheAleatoireEdgarGilbert():
    n= int(sys.argv[1])
    p=0.5
    g=erdos_renyi_graph(n,p)
    EnregistrerGrapheAlea(g)

"""
Generer un graphe aleatoire avec la methode de edgard Gilbert
"""
def generationGrapheAleatoireBarabasiAlbert():
    n= int(sys.argv[1])
    #parametres
    final_nodes = n
    m_parameter = 2
   
    g = nx.barabasi_albert_graph(final_nodes, m_parameter)
    EnregistrerGrapheAlea(g)

"""
afficher le graphe et l'enregistrer dans une image et le stocker dans un fichier csv  "GrapheGenere.csv"    
"""    
def EnregistrerGrapheAlea(g):
    print("liste des noeuds : ")
    print (g.nodes)
    print("liste des arrêtes : ")
    print(g.edges)
    
    
    #enregistrer le graphe genere aleatoirement dans une image
    nx.draw(g, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")
    
    #stocker le graphe dans un fichier csv "GrapheGenere.csv"
    listeArretes=list(g.edges)
    if os.path.exists('GrapheGenere.csv'):
        os.remove('GrapheGenere.csv')
    f = open('GrapheGenere.csv','ab')
    listeEntete=["id_1","id_2"]
    writer=csv.writer(f, delimiter="," )
    writer.writerow(listeEntete)
    for i in listeArretes:
        sommet1=str(i).split(",")[0]
        sommet2=str(i).split(",")[1]
        sommet1=sommet1.replace("(", '')
        sommet2=sommet2.replace(")", '')
        sommet1=sommet1.strip()
        sommet2=sommet2.strip()
        f = open('GrapheGenere.csv','ab')
        with f as csvfile:
            writer=csv.writer(csvfile, delimiter="," )
            listeSommetInsert=[sommet1,sommet2]
            writer.writerow(listeSommetInsert)
    plt.close()
    f.close()

"""
Afficher le graphe aleatoire genere dans la methode precedente (stocké dans l'image graph.png)
"""
def showGeneratedGraph():
   img = Image.open('graph.png')
   img.show()

"""
Partie 2 :Etude des fichiers de donnees csv 
"""
#########################################################################################################
#Les fichiers de lecture sont des fichiers csv qui avec id_1 & id_2 comme entete et ',' comme separateur
#########################################################################################################
def readFile():

    dataFile= sys.argv[3]                    #fichier donné en entreé ==>sys.argv[3]
    dfData=pd.read_csv(dataFile, sep=",")
    listeSommets1=dfData.id_1
    
    #enlever les doublons pour calculer le nombre des sommets 
    listeSommets1SR=list(set(listeSommets1))  
    listeSommets2=dfData.id_2
    listeSommets2SR=list(set(listeSommets2))
    listeSommets=listeSommets1SR+listeSommets2SR
    listeSommets=list(set(listeSommets))
    
    print("Nombre de sommets  : " + str(len(listeSommets)))
    print("Nombre d'arrêtes : " + str(dfData.shape[0]))     #nombre de lignes
    
    ##########Degré maximal##########
    listeSommetsOccurences={}
    listeS=list(listeSommets1) + list(listeSommets2)
    for i in listeSommets:
        listeSommetsOccurences[i] = listeS.count(i)      #nombre d'occurence de chaque sommet
    listeDegre = sorted(listeSommetsOccurences.values()) #trier la liste des degres par ordre croissant
    maxF = listeDegre[-1]                                #le dernier element de la liste (le maximum)
    
    print("Degré maximal : " + str(maxF) )
    
    ##########Degré moyen ##########
    degreMoyen= sum(listeDegre) / float(len(listeSommets))  #degreMoyen=somme(degre)/nombre de sommets
    print("Degré moyen : " + str(degreMoyen))


"""
Ditribution de degres sous forme de graphique (Qst 2.5.1)
"""
def graphiqueDegres():
    dataFile= sys.argv[3]
    dfData=pd.read_csv(dataFile, sep=",")
    listeSommetsOccurences={}
    listesDegreOccurences={}
    listeSommets1=list(dfData.id_1)
    listeSommets2=list(dfData.id_2)
    listeSommets=listeSommets1 + listeSommets2

    for i in listeSommets:
        listeSommetsOccurences[i] = listeSommets.count(i) 
    for i in listeSommetsOccurences.values():
        listesDegreOccurences[i] = listeSommetsOccurences.values().count(i)
    
    #afficher la distribution des degrés sous forme de graphique (en abscisse des degrés, et en ordonnée leurs distributions).
    plt.scatter(listesDegreOccurences.keys(), listesDegreOccurences.values(), c='r')
    plt.plot(listesDegreOccurences.keys(), listesDegreOccurences.values(), label='f(x)')
    plt.xlabel('degre')
    plt.ylabel('frequence')
    plt.show()
    
"""
supplementaire:
Ditribution de sommets sous forme de graphique (Qst 2.5.2)
"""   
def graphiqueSommets():
    dataFile= sys.argv[3]
    dfData=pd.read_csv(dataFile, sep=",")
    listeSommetsOccurences={}
    listeSommets1=list(dfData.id_1)
    listeSommets2=list(dfData.id_2)
    listeSommets=listeSommets1 + listeSommets2

    for i in listeSommets:
        listeSommetsOccurences[i] = listeSommets.count(i)


    #afficher la distribution des sommets sous forme de graphique (en abscisse des sommets, et en ordonnée leurs distributions).
    plt.scatter(listeSommetsOccurences.keys(), listeSommetsOccurences.values(), c='r')
    plt.plot(listeSommetsOccurences.keys(), listeSommetsOccurences.values(), label='f(x)')
    plt.xlabel('sommet')
    plt.ylabel('frequence')
    plt.show()

"""
le diamétre d'un graphe (le plus long chemin )
"""
def diametreGraphe(g,n,si,sf):
    #initialisation
    Dict={}
    Dict[si]=[0,[si]]        #O(1) operations
    for i in list(g.nodes):
        if(i!=si):
            Dict[i]=[-1,[]]  #O(n) operations
   
    #-------
    for i in list(g.nodes): #la boucle est éxecutée O(n) fois 
        for j in list(g.neighbors(i)): #la boucle est éxecutée O(n) fois
            if(j>i):
                if((Dict.get(i)[0] + 1) > Dict.get(j)[0]):
                   Dict.get(j)[0] = Dict.get(i)[0] + 1
            else:
                continue
               



def main():
    choix = int(sys.argv[2])
    if(choix==1):
        print("Modéle Edgar Gilbert")
        generationGrapheAleatoireEdgarGilbert()
    elif(choix==2):
        print("Modéle Barbasi-Albert")
        generationGrapheAleatoireBarabasiAlbert()
    else:
       print("choix invalide")
       sys.exit()
    
    #
    showGeneratedGraph()
    readFile()
    graphiqueDegres()
    graphiqueSommets()

if __name__ == "__main__":
    main()
