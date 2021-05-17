We developed our project using python version 2.7.
We used the following libraries:
-Pandas : library that will allow us to make the different studies and analyses of the csv files we want to study.
-csv : library which allows to manipulate the csv files 
-networkx : a python library for the creation, the manipulation and the study of graphs.
-PIL (pillow) : library that allows us to display randomly generated edges as a graph stored in an image.

The files that we can process are csv files with commas "," as separator, the headers of the csv file are the following: "id_1,id_2".

The code is launched with the following command:
"python2 AlgoProject.py n choice File.csv"

The additional arguments that the command takes are as follows:
-argument 3: n => the number of vertices in the random graph (example: 10)
-argument 4 : choice => the method with which we want to generate the graph (1 for Edgar's method and 2 for the Barabasi-Albert model)
-argument 5 : Name of the file we want to study for the second part.

The data of the random graph generated in the first part are stored in a file 

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Nous avons développé notre projet en utilisant la version 2.7 de python.
Nous avons utilisé les bibliothèques suivantes :
-Pandas : librairie qui va nous permettre de faire les différentes études et analyses des données des fichiers csv que l’on souhaite étudier.
-csv : librairie qui permet de manipuler les fichiers csv 
-networkx : une librairie python pour la création, la manipulation et l’étude des graphes.
-PIL (pillow) : librairie qui nous permet d’afficher les arêtes générées aléatoirement sous forme de graphe stocké dans une image.

Les fichiers que l’on peut traiter sont des fichiers csv avec des virgules “,” comme séparateur, les entêtes du fichier csv sont les suivants : “id_1,id_2”.

Le code se lance avec la commande suivante :
“ python2 AlgoProjet.py n choix Fichier.csv”

Les arguments supplémentaires que prend la commande sont les suivants :
-argument 3 :   n => le nombre de sommets du graphe aléatoire (exemple : 10)
-argument 4 : choix =>  la méthode avec laquelle nous souhaitons générer le graphe (1 pour la méthode d’Edgar et 2 pour le modèle Barabasi-Albert)
-argument 5 : Nom du fichier que l’on souhaite étudier pour la deuxième partie.

Les données du graphe aléatoire généré dans la première partie sont stockées dans un fichier “GrapheGenere.csv”.

