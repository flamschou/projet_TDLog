# projet_TDLog
Projet long de TDLog. Corentin Caris, Wandrille Flamant, Abel Salmona.

Jeu de plateau avec des cases hexagonales qui voit s'affronter un attaquant et un défenseur. Le défenseur doit résister jusqu'à ce que la durée du jeu expire. L'attaquant doit éliminer ou chasser le défenseur avant la fin du jeu. Le logiciel permet de jouer contre l'autre joueur (IA ou humain) et affiche le plateau, la liste d'actions et des informations supplémentaires. Il ne fonctionne que par point & click. 

Fonctionnalités à ajouter/débugger : 
- avoir un bot fonctionnel
- adrenalin qui augmente la speed de manière exponentielle
- zones pour placer les troupes à l'initialisation ?
- bouton pour désélectionner une troupe ?
- implémentation du son ?

Rôles : 
- Clean le code et implémenter les tests
- Faire un affichage plus complet
- Implémenter un bot (IA + Glouton)

Initialisation : 
- le défenseur clique sur l'hexagone qu'il veut défendre 
- le défenseur place ses troupes
- l'attaquant place ses troupes à une certaine distance de l'hexagone cible

Interface : 
- le joueur clique sur la troupe qu'il veut déplacer
- les hexagones accessibles changent de couleur 
- le joueur clique sur l'hexagone où il déplace la troupe ou l'adversaire qu'il veut attaquer

Board : Le plateau est composé d'hexagones de plusieurs types
- basic : pas d'attributs
- sand : ralenti les troupes
- forest : augmente la portée des troupes
- rock : ne peut pas devenir sand

Troops : il existe plusieurs types de troupes
- Attaque (bleu) : 
    - assassin : rapide et léger, représenté par des épées
    - magician : empoisonne l'ennemi qui perd de la vie pendant 2 tours et peut soigner les troupes amies, représenté par un chapeau
    - turret : grande portée et lent, représenté par une tourelle
- Défense (bleu) : 
    - archer : rapide et grande portée, représenté par des flèches
    - engineer : peut déplacer l'hexagone à défendre sur sa position en se suicidant, représenté par un marteau
    - shield : défensif et lent, représenté par un bouclier

Events : à chaque tour se produit un évènement
- sandstorm : augmentation des sands
- fire : réduction des forêts
- rescue : la durée de fin du jeu se rapproche
- betrayal : la durée de fin du jeu s'éloigne
- adrenalin : les déplacements et dégats des troupes sont multipliés par 2
- expansion : certains hexagones deviennent accessibles

Objectif : créer ensuite un joueur virtuel qui va pouvoir jouer contre l'humain de manière éaquilibrée, qu'il soit au poste d'attaquant ou de défenseur. On va déjà créer un bot, puis l'obectif serait de l'entrainer avec l'IA pour que le jeu soit relativement équilibré et que le bot soit relativement fort au jeu. 

Bot implémentation : regarder les stratégies aussi sur le jeu dans l'absolu 
