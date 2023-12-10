# projet_TDLog
Projet long de TDLog. Corentin Caris, Wandrille Flamant, Abel Salmona.

Jeu de plateau avec des cases hexagonales qui voit s'affronter un attaquant et un défenseur. Le défenseur doit résister jusqu'à ce que la durée du jeu expire. L'attaquant doit éliminer ou chasser le défenseur avant la fin du jeu. Le logiciel permet de jouer contre l'autre joueur (IA ou humain) et affiche le plateau, la liste d'actions et des informations supplémentaires. Il ne fonctionne que par point & click. 

Fonctionnalités à ajouter/débugger : 
- élimination des troupes
- attaque sur les troupes amies
- zones pour placer les troupes à l'initialisation
- continuer IA
- troupes joueur non actif en noir et blanc / troupes actives mises en valeur
- affichage du joueur actif 

Rôles : 
- Clean le code et implémenter les tests
- Faire un affichage plus complet
- Implémenter un bot (IA + Glouton)

Initialisation : 
- le défenseur clique sur l'hexagone qu'il veut défendre (hors de la périphérie du plateau)
- l'attaquant place ses 3 troupes en périphérie du plateau
- le défenseur place ses 3 troupes autour de l'hexagone à défendre

Interface : 
- le joueur clique sur la troupe qu'il veut déplacer
- les hexagones accessibles changent de couleur
- les troupes adverses accessibles changent de couleur 
- le joueur clique sur l'hexagone où il déplace la troupe ou l'adversaire qu'il veut attaquer

Board : Le plateau est composé d'hexagones de plusieurs types
- basic : pas d'attributs
- swamp : ralenti les troupes
- forest : réduit la portée des attaques des troupes
- rock : ne peut pas devenir swamp

Troops : il existe plusieurs types de troupes
- Attaque (rouge) : 
    - assassin : rapide et léger : représenté par un 
    - magician : capacités spéciales : représenté par un disque
    - turret : défensif et lent : représenté par un rectangle
- Défense (bleu) : 
    - archer : rapide et léger : représenté par un triangle
    - engineer : capacités spéciales : représenté par un disque
    - shield : défensif et lent représenté par un rectangle

Events : à chaque tour se produit un évènement
- rain : augmentation des swamps
- fire : réduction des forêts
- rescue : la durée de fin du jeu se rapproche
- betrayal : la durée de fin du jeu s'éloigne
- adrenalin : les déplacements et dégats des troupes sont multipliés par 2
- expansion : certains hexagones deviennent accessibles

Objectif : créer ensuite un joueur virtuel qui va pouvoir jouer contre l'humain de manière éaquilibrée, qu'il soit au poste d'attaquant ou de défenseur. On va déjà créer un bot, puis l'obectif serait de l'entrainer avec l'IA pour que le jeu soit relativement équilibré et que le bot soit relativement fort au jeu. 

Bot implémentation : regarder les stratégies aussi sur le jeu dans l'absolu 
