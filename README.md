# projet_TDLog
Projet long de TDLog. Corentin Caris, Wandrille Flamant, Abel Salmona.

Jeu de plateau avec des cases hexagonales qui voit s'affronter un attaquant et un défenseur. Le défenseur doit résister jusqu'à ce que la durée du jeu expire. L'attaquant doit éliminer ou chasser le défenseur avant la fin du jeu. 

Chaque tour commence par un évènement aléatoire, puis l'attaquant peut réaliser ses actions avant que le défenseur ne réagisse. 

Le logiciel permet de jouer contre l'autre joueur (IA ou humain) et affiche le plateau, la liste d'actions et des informations supplémentaires. Il ne fonctionne que par point & click. 

Board : Le plateau est composé d'hexagones de plusieurs types
- basic : pas d'attributs
- swamp : ralenti les troupes
- forest : réduit la portée des attaques des troupes

Troops : il existe plusieurs types de troupes
- Attaque : 
    - assassin : rapide et léger
    - magician : capacités spéciales
    - turret : défensif et lent
- Défense : 
    - archer : rapide et léger
    - engineer : capacités spéciales
    - shield : défensif et lent

Events : à chaque tour se produit un évènement
- rain : augmentation des swamps
- fire : réduction des forêts
- rescue : la durée de fin du jeu se rapproche
- betrayal : la durée de fin du jeu s'éloigne
- adrenalin : les déplacements et dégats des troupes sont multipliés par 2
- expansion : certains hexagones deviennent accessibles

