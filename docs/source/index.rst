Documentation de l'ensemble des TP de Python du S9
==================================================
Clément LACAÏLE - Groupe 3 SI2

TP1 : Prise en main 
-------------------------------------

Ce TP a pour but de se familiariser avec le langage Python. Puisque c’est un langage 
avec lequel j’ai déjà de bonnes bases (je l’ai étudié lors d’un semestre en mobilité 
internationale), j’ai décidé d’aller un peu plus loin et d’ajouter les deux particularités :
l'utilisation de la convention `PEP8` et l'outil de compilation de documentation `Sphinx`.

.. automodule:: TP1
   :members:
.. automodule:: ex3_class_Date
   :members:

TP2 : TKinter
-------------------------------------

Le but de ce TP est de se familiariser avec la création d'interface graphique en Python en utilisant la librairie TKinter.

.. automodule:: TP2
   :members:

TP3 : Exceptions et chiffrement
-------------------------------------

Le but de ce TP est de se familiariser avec la gestion des exceptions en Python ainsi que le chiffrement. Pour cela, j'ai adapté le code de l'éditeur de fichier vu dans le TP1 afin qu'il gère la connexion d'utilisateurs par mot de passes chiffrés à l'aide de la librairie bcrypt. Ensuite, j'ai modifié toutes les fonctions et autres lignes afin qu'elles puissent, dans le cas où celà était nécessaire, lever des exceptions, ou les gérer

.. automodule:: TP3
   :members:

TP4 : Matplotlib
-------------------------------------

Le but de ce TP est de prendre en main l'outil Matplotlib qui permet de dessiner des graphiques dans une fenêtre, en reprenant une syntaxe similaire à celle de Matlab/Scilab. Le TP est composé de 6 questions qui sont présentées dans les sous-parties suivantes

.. automodule:: TP4
   :members:

TP5 : SQLite
------------------------------------

Le but de ce TP est de mettre en place une base de données avec SQLite. L'exécutable `sqlite3` est déjà présent dans le dossier de ce TP, il est inutile de le réinstaller. En outre, j'ai décidé de ne pas utiliser la librairie ORM SQLAlchemy, car c'est une librairie que je connais déjà. Je perds du temps, mais cela m'a permis de manipuler plus en profondeur le langage.

.. automodule:: TP5
   :members:

.. automodule:: Commune
   :members:

.. automodule:: Departement
   :members:

.. automodule:: Region
   :members:

.. automodule:: TP5_XML
   :members:

TP6 : Numpy/Scipy
------------------------------------

Le but de ce TP est de prendre en main les librairies Numpy et Scipy.

.. automodule:: TP6
   :members:


TP7 : Numpy/Scipy
------------------------------------

Le but de ce TP était de créer un serveur web et de pouvoir afficher du contenu en fonction de la connexion ou non d'un utilisateur présent dans un fichier. J'ai décidé de mettre en place une application Flask très simple, remplissant le même rôle.

.. automodule:: TP7
   :members:

   

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
