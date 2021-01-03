
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

