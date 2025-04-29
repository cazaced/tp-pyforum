# Ajout de fonctionnalités et Git

Maintenant que le MVP est terminé, vous allez ajouter des fonctionnalités
supplémentaires à votre projet PyForum. Pour vous permettre de mettre en pratique
la collaboration avec Git, le travail sera divisé en deux parties. Chaque étudiant
travaillera sur une partie différente du projet et vous devrez fusionner vos
modifications par la suite.

## Objectifs

L'objectif de cette étape est d'ajouter une composante multi-utilisateur à votre
projet PyForum. Les utilisateurs pourront également interagir entre eux en votant
pour les publications.

## Fonctionnalités à développer

Les fonctionnalités seront divisées entre deux étudiants.

### Étudiant A

L'étudiant A sera responsable de la création d'un système de vote pour les
publications et du système de connexion.

#### Système de vote

- Un utilisateur peut voter pour une publication ou un commentaire.
- Le vote est enregistré comme un attribut de la classe `Publication` ou
  `Commentaire`.
- Puisqu'un utilisateur ne peut pas voter plusieurs fois pour la même
  publication ou le même commentaire, l'attribut `vote` doit être une liste
  d'identifiants d'utilisateurs qui ont voté.

#### Système de connexion

Il existe dans le MVP une fonctionnalité pour ajouter des utilisateurs.
Il faut maintenant ajouter une fonctionnalité de connexion. Un utilisateur peut se
connecter à son compte en fournissant son nom d'utilisateur et son mot de passe ou
créer un compte s'il n'en a pas encore.

Ainsi, avant d'arriver à la boucle principale du MVP qui affiche le menu
principal via `afficher_menu`, il faut afficher un menu de connexion. Voici les
étapes à implanter.

- Afficher un menu de connexion qui propose deux options :
  - Se connecter
  - Créer un utilisateur
- Si l'utilisateur choisit de se connecter, il doit entrer son nom
  d'utilisateur et son mot de passe. Vous devez vérifier si le nom
  d'utilisateur et le mot de passe correspondent à un utilisateur existant. La 
  fonctionalité `charger_utilisateurs` de la base de donnée `BD` vous
    permettra de charger la liste des utilisateurs et de vérifier si le
  nom d'utilisateur et le mot de passe correspondent à un utilisateur.
- Si l'utilisateur choisit de créer un utilisateur, cela revient à la
  fonctionnalité de création d'un utilisateur du MVP déjà en place.
- Ensuite, vous devez afficher le menu principal du MVP via la fonction
  `afficher_menu` en enlevant la possibilité de créer un utilisateur.

## Étudiant B

L'étudiant B sera responsable de la création d'un système de tags et de la
gestion des rôles (admin et modérateur).

#### Système de tags

- Un utilisateur peut ajouter un ou plusieurs tags à *ses* publication. Les
  tags sont un attribut de la classe `Publication`. Seul l'auteur de la
  publication peut ajouter ou supprimer des tags.
- Un utilisateur peut rechercher une publication par tag. La recherche
  doit retourner toutes les publications qui contiennent le tag recherché.
  Cette fonctionalité doit être ajouter au menu principal du MVP.
- Un utilisateur peut voir la liste de tous les tags utilisés dans PyForum.
  Cette fonctionalité doit être ajouter au menu principal du MVP.

#### Gestion des rôles

En plus des utilisateurs de base, il existe deux types de rôles :
administrateur et modérateur. 

Chaque forum possède au moins un modérateur. Le modérateur par défaut est
l'utilisateur qui a créé le forum. Un modérateur peut :
- Supprimer une publication
- Supprimer un commentaire
- Ajouter un tag à une publication
- Supprimer un tag d'une publication

Attention, ceci s'applique uniquement aux forum qu'il modère. Un modérateur ne
peut pas supprimer une publication ou un commentaire d'un autre forum.

Il existe aussi un administrateur qui a tous les droits. L'administrateur est
en quelque sorte le "super-utilisateur" de PyForum. Il peut être vu comme un
modérateur de tous les forums.

## À vous de jouer !

### Étape 1

- Créer un dépôt Git publique sur GitHub pour votre projet PyForum avec le MVP déjà
  implanté.
- La branche principale doit être `main`.

### Étape 2

- Identifier qui sera l'étudiant A et qui sera l'étudiant B.
- Chaque étudiant travaille sur sa *propre branche* en local.

### Étape 3

- Chaque étudiant doit fusioner sa branche avec la branche principale `main`.
- Vous n'avez pas à attendre de terminer votre fonctionnalité pour fusionner
  votre branche. Vous pouvez fusionner votre branche à tout moment, tant que le
    code à fusionner est fonctionnel. Cela va éviter d'avoir à fusionner un
    gros morceau de code à la fin.