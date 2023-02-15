# Avancée / Planning du cours de MIF08 (Compilation)
_Année 2022-2023_

* Matthieu Moy, Université Lyon 1, LIP https://matthieu-moy.fr/

## Communication et nouvelles du cours

* [NEWS.md](NEWS.md) contient les nouvelles du cours (envoyées par email également).
<!-- 
## Organisation du cours à distance

* Tous les enseignements passent à distance pendant le mois de novembre (au moins) -->

* Cette année, nous ~~utiliserons~~ détournerons le système d'issues de GitLab
  comme forum minimaliste. Vous pouvez poser vos questions en ajoutant une issue
  sur le dépôt : https://forge.univ-lyon1.fr/matthieu.moy/mif08-2023/-/issues 

## Intervenants

**CM**

Matthieu Moy

**TD**
- A: Matthieu Moy (34 étudiants)
- B: Hugo Thievenaz (31 étudiants)
- C: Gregoire Pichon (31 étudiants)

**TP**
- A1: Matthieu Moy
- A2: Nicolas Louvet
- B1: Hugo Thievenaz
- B2: Gregoire Pichon
- C1: Gabriel Radanne
- C2: Guillaume Bouchard

## Vidéos des CM

Les vidéos réalisées pendant le COVID sont encore disponibles. Elles ne sont pas totalement à jour, mais peuvent vous aider si besoin :

[La playlist Youtube MIF08](https://www.youtube.com/playlist?list=PLtjm-n_Ts-J9HSZ9ahpbsC_kTQMzUZQPx)

Il est tout de même très fortement recommandé de venir en présentiel.

## Infrastructure technique, logiciels à installer

Les TP utilisent la chaîne d'outils RiscV, un peu lourde à installer. Voir [INSTALL.md](INSTALL.md) pour les consignes. À faire avant les TPs si vous voulez travailler sur vos machines personnelles.

Si vous n'arrivez pas à installer les outils sur vos machines, vous pourrez travailler sur les ordinateurs de la fac, et en dernier recours nous fournissons aussi des machines virtuelles pré-installées : [VM.md](VM.md).

## Planning

## Jeudi 16/02/2023

- :book: 8h: Cours 1: Introduction, machine cible (RISCV), lexing :
    - Introduction au cours, à la compilation et à l'architecture cible : [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours01_intro_et_archi.pdf)
    - Lexing (et parsing) : [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours02_lexing_parsing.pdf) <!-- Lexing nécessaire pour TD1 -->
    - [Vidéo "teaser"](https://youtu.be/ny7HlqyuM9E)
    - [vidéo d'introduction au cours](https://www.youtube.com/watch?v=zGifE8MfPWA)
    - [vidéo sur RISCV](https://youtu.be/ZdElX9e_tAI)
    - [vidéo lexing](https://www.youtube.com/watch?v=UlUTSsOA9Qc)
    - Extrait de la documentation RISCV: [riscv_isa.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/riscv_isa.pdf)
    - :100: QCM sur TOMUSS, à faire avant mardi 21/2/2023, 23:59

- :pencil2: 9h45: TD1 : Architecture RISCV, Lexing, Parsing
    - [Énoncé du TD1](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/td1.pdf)
    - Rappel, extrait de la documentation RISCV : [riscv_isa.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/riscv_isa.pdf)

- :hammer: 11h30: TP1 : Python et RiscV
    - Énoncé : [TP1 python/archi](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/tp1.pdf)
    - Fichiers du TP1 : [TP01/](TP01/).

## Jeudi 23/2/2023

- :book: 8h: Cours 2: Lexing, Parsing, interprétation
    - Parsing : [deuxième partie des transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours02_lexing_parsing.pdf)
    - [vidéo parsing](https://www.youtube.com/watch?v=y9MrfDzrAmA)
    - [transparents sémantique et interprète](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours03_interpreters.pdf)
    - [vidéo sémantique et interprète](https://youtu.be/8PYhBsgRO6g)

- :100: QCM sur TOMUSS, à faire avant vendredi 3 mars 2023, 23:59.

- :pencil2: 9h45: TD, Arbres abstraits, attributions, types
    - [Énoncé du TD2](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/td2.pdf)

## Jeudi 16/3/2023

- :hammer: 8h-11h15: TP2, ANTLR
    - Transparents de présentation : [capmif_labs.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_labs.pdf)
    - Si besoin : des VM pour vous dépanner en cas de problème sur machine perso : [VM.md](VM.md)
    - Énoncé : [TP2 antlr](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/tp2.pdf)
    - Fichiers du TP2 : [TP02/](TP02/).
    - **Date limite pour le rendu (noté) : mercredi 22 mars 2023, 23h59. (deadline stricte)**

## Jeudi 23/3/2023

- :book: Cours 3, Typage : 8h-9h30
    - [transparents typage](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours04_typing.pdf)
    - [vidéo typage](https://youtu.be/2A-hQy_6YlE)
- :100: QCM sur TOMUSS, à faire avant vendredi 31 mars 2023, 23:59.

- :hammer: TP3, interprète MiniC : 9h45-13h
    - Énoncé : [TP3 frontend, interprète](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/tp3.pdf)
    - Fichiers du TP3 : [TP03/](TP03/) puis [MiniC/](MiniC/).
    - **Date limite de rendu du TP3 : dimanche 16 avril 2023, 23h59 (deadline stricte). Il y a une séance TP3 le jeudi 13 avril 2023 mais on enchaîne sur le TP4 donc il est vivement recommandé d'avoir presque terminé le TP3 pour le jeudi 13/4/2023.**

## Jeudi 13/4/2023

- :book: Cours 4 : 8h-9h30
    - génération de code 3 adresses + allocation naive, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours05_3ad_codegen.pdf), [vidéo](https://youtu.be/m2x7leFnCN4)
    - Représentations intermédiaires, [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours06_irs.pdf), [vidéo 6a](https://youtu.be/dD9bRhLfykM), [vidéo 6b](https://youtu.be/Xico_JTK3XQ).

- :100: QCM sur TOMUSS, à faire avant mardi 18 avril 2023, 23:59.

- :pencil2: TD 3, génération de code : 9h45-11h15
    - Sujet : [TD3 génération de code](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/td3.pdf)

- :hammer: TP 4, génération de code : 11h30-13h
    - Transparents de présentation : [capmif_labs.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-20/capmif_labs.pdf)
    - Rappel : des VM pour vous dépanner en cas de problème sur machine perso : [VM.md](VM.md)
    - Énoncé : [TP4 génération de code](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/tp4.pdf)
    - Fichiers du TP4 : [MiniC/TP04/](MiniC/TP04/).
    - **Date limite pour le rendu (noté) : vendredi 5 mai 2023, 23h59 (malus 2 points par jour de retard, aucun rendu accepté après le dimanche soir).**

## Jeudi 20/4/2023

- :hammer: TP 4 (suite), 8h-11h15 : cf. ci-dessus pour les supports.

## Jeudi 11/5/2023

- :book: Cours 5, allocation de registres : 8h-9h30
    - Register allocation + data-flow analyses : [transparents](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/capmif_cours07_regalloc.pdf), [vidéo première partie](https://youtu.be/9902mMgDIK8), [vidéo deuxième partie](https://youtu.be/LknSDccweFw).
    - :100: QCM sur TOMUSS, à faire avant vendredi 19 mai 2023, 23:59.


- :hammer: TP5, nouvelles fonctionnalités de langage : 15h45-17h15
    - Énoncé : [TP5 allocation de registres](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/tp5.pdf)
    - Fichiers du TP5 : [MiniC/TP05/](MiniC/TP05/).
     - **Date limite pour le rendu (noté) : vendredi 2 juin 2023, 23h59 (malus 2 points par jour de retard, aucun rendu accepté après le dimanche soir).**

## Jeudi 8/6/2023

- :pencil2: TD4, analyse de vivacité : 9h45-11h15
    - Énoncé : [TD4 liveness](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/td4.pdf)


- :pencil2: TD5, allocation de registres intelligente : 11h30-13h
    - Énoncé : [TD5 regalloc](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/td5.pdf)

## Jeudi 15/06/2023

- :100: Examen.

## Pondération des notes (indicative pour l'instant sauf l'examen final qui sera forcément 40%)
  - QCM : non pris en compte dans la moyenne d'UE
  - TP2 parsing et évaluation d'expression : 7%
  - TP3 interprète : 13%
  - TP4 génération de code : 20%
  - TP5 extension de langage : 20%
  - Examen final : 40 %

La session 2 remplace la note d'examen final.

## Annales et consignes pour l'examen

* Aide mémoire fourni avec le sujet en 2021 (un document similaire sera fourni cette année): [mif08_companion.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/mif08_companion.pdf)

* L'examen session 1 2021-2022 : [exam_mif08_2022.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/exam_mif08_2022.pdf) et éléments de corrigé : [exam_mif08_2022_corr.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/exam_mif08_2022_corr.pdf)

* L'examen Session 1 2020-2021 : [exam_mif08_2020.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/exam_mif08_2020.pdf) et les éléments de corrigé : [exam_mif08_2020_corr.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/exam_mif08_2020_corr.pdf)

* L'examen 2019-2020 : [mif08_exam1920.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/mif08_exam1920.pdf) et les éléments de corrigés : [mif08_exam1920-corr.pdf](https://compil-lyon.gitlabpages.inria.fr/mif08-files-2023/mif08_exam1920-corr.pdf).

* [Consignes pour l'examen](https://compil-lyon.gitlabpages.inria.fr/mif08-20/exam_mif08_2020-page1.pdf)
