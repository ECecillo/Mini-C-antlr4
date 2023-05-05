<!-- LTeX: language=fr -->
# Nouvelles du cours

Les nouvelles du cours apparaîtront ici au fur et à mesure.

## 5/05/2023 : extension de deadline

À la demande de certains étudiants, j'ai étendu la deadline du TP4 à mardi 9
mai, 20h. Deadline stricte. Vous pouvez faire plusieurs rendus successifs sur
TOMUSS, n'hésitez pas à faire un premier rendu tôt avec un TP non-terminé, et à
re-soumettre au fur et à mesure de votre avancée pour être certain de ne pas
rater la deadline.

## 23/03/2023 : Plus de tests fournis, erreurs Pyright

Comme annoncé précédemment, je vous ai ajouté quelque cas de tests pour vous
éviter un travail fastidieux et peu utile de test du code fourni.

Certains étudiants avaient des erreurs Pyright qui sont vraisemblablement dues à
un bug de Pyright 1.1.300, mais pour vous éviter des problèmes j'ai mis en place
un contournement dans le squelette.

Pour les deux mises à jour, faites :
```
git pull
```
pour récupérer la dernière version de mon code.

J'ai également précisé quelques points dans l'énoncé (la différence entre
`test_eval` et `test_expect` en particulier), le PDF du sujet est à jour.

## 22/2/2023 : typo TP1, TP2 en ligne

J'avais pourtant bien fait la modification, mais j'ai glissé au moment de la
mettre en ligne :-(. L'énoncé du TP1 vous donnait la mauvaise URL à cloner (avec
2021 dans l'URL, alors que nous sommes bien en 2023). Vous pouvez vérifier que
vous avez bien le bon dépôt avec :

```
$ git remote -v
origin  https://forge.univ-lyon1.fr/matthieu.moy/mif08-2023 (fetch)
origin  https://forge.univ-lyon1.fr/matthieu.moy/mif08-2023 (push)
```

Le TP2 est en ligne. Vous aurez une séance dédiée le 16/3, mais le délai pour le
rendu sera assez court et la deadline stricte, donc je vous recommande de
prendre un peu d'avance.
