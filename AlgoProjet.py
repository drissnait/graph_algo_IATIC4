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
    # Get parameters
    #init_nodes = 3
    final_nodes = n
    m_parameter = 2
   
    g = nx.barabasi_albert_graph(final_nodes, m_parameter)
    EnregistrerGrapheAlea(g)
    
    
def EnregistrerGrapheAlea(g):
    print("liste des noeuds : ")
    print (g.nodes)
    print("liste des arrêtes : ")
    print(g.edges)
    nx.draw(g, with_labels=True, font_weight='bold')
    plt.savefig("graph.png")#enregistrer le graphe genere aleatoirement dans une image
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
Etude des fichiers de donnees csv (deuxieme partie du projet)
"""
####################################################################################
#Les fichiers de lecture sont des fichiers csv qui avec id_1 & id_2 comme entete
######################################################################################
def readFile():
    dataFile= sys.argv[3]
    dfData=pd.read_csv(dataFile, sep=",")
    listeSommets1=dfData.id_1
    listeSommets1SR=list(set(listeSommets1))
    listeSommets2=dfData.id_2
    listeSommets2SR=list(set(listeSommets2))
    listeSommets=listeSommets1SR+listeSommets2SR
    listeSommets=list(set(listeSommets))
    
    print("Nombre de sommets  : " + str(len(listeSommets)))
    print("Nombre d'arrêtes : " + str(dfData.shape[0])) #nombre de lignes
    ##########Degré maximal##########
    listeSommetsOccurences={}
    listeS=list(listeSommets1) + list(listeSommets2)
    for i in listeSommets:
        listeSommetsOccurences[i] = listeS.count(i)      #nombre d'occurence de chaque sommet
    sortedDict = sorted(listeSommetsOccurences.values()) #trier la liste par ordre croissant
    maxF = sortedDict[-1]   #le dernier elemnt de la liste
    
    print("Degré maximal : " + str(maxF) )
    degreMoyen= dfData.shape[0]/ float(len(listeSommets))
    print("Degré moyen : " + str(degreMoyen))


"""
Ditribution de degres sous forme de graphique (Qst 2.5)
"""
def graphique():
    dataFile= sys.argv[3]
    dfData=pd.read_csv(dataFile, sep=",")
    listeSommetsOccurences={}
    listeSommets1=list(dfData.id_1)
    listeSommets2=list(dfData.id_2)
    listeSommets=listeSommets1 + listeSommets2

    for i in listeSommets:
        listeSommetsOccurences[i] = listeSommets.count(i)



    plt.scatter(listeSommetsOccurences.keys(), listeSommetsOccurences.values(), c='r')
    plt.plot(listeSommetsOccurences.keys(), listeSommetsOccurences.values(), label='f(x)')
    plt.xlabel('degre')
    plt.ylabel('frequence')
    plt.show()



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
    graphique()

if __name__ == "__main__":
    main()
