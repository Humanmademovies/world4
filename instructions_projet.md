# Instructions du projet — Modèle d'impact physique de la consommation mondiale

*(titre de travail ; à renommer)*

## Mission

Construire un **cadre comptable physique mondial** interactif : un bac à sable où un planificateur règle des curseurs (niveau d'activité par produit, âge de retraite, heures/semaine, taux d'emploi cible, par pays) et voit se propager les conséquences **physiques** (carbone, eau, énergie, matières, terres) et **sociales** (heures-homme libérées, emplois) à travers toute la chaîne d'approvisionnement mondiale, comparées à des cibles de soutenabilité elles-mêmes réglables.

Livrable final : un dashboard avec globe (44 pays), filtrable par type d'impact, où l'on sélectionne un pays pour manipuler ses variables de politique d'emploi.

## Cadre épistémique — à ne jamais perdre de vue

**Ce n'est PAS un modèle économique au sens comportemental.** C'est un modèle **physique** : « si tel secteur baisse, que se passe-t-il mécaniquement, partout ? » On ne prédit aucun comportement (pas d'élasticité, pas de prix, pas d'équilibre de marché). Le scénario postule une **gouvernance mondiale** qui décide directement des niveaux d'activité ; le capital productif est **figé dans son état physique actuel**.

Conséquence assumée : c'est un **modèle purement décroissant à apparatus constant**. On ferme l'écart de soutenabilité en faisant *moins*, jamais en investissant dans du « vert » (pas de substitution, pas de transition par construction de capital nouveau). Toute hausse d'activité est hors périmètre.

Trois choix de cadrage tranchés, à respecter :

1. **Leviers = demande, moteur = Leontief.** Un levier réduit l'usage final d'un produit ; l'inverse de Leontief propage la baisse vers l'amont (fournisseurs, dans tous les pays). Rétroaction **uniquement négative** : on ne postule jamais de hausse. Le modèle de Ghosh (propagation aval, pénurie d'intrant) et la fermeture directe d'un secteur-pays précis sont **hors socle** (notés plus bas).
2. **Pas de revenu/travail libéré réinjecté.** Économie physique : la quantité de biens en circulation ne peut pas augmenter. Couper un secteur ne « finance » rien ailleurs. Concrètement : aucun Δdemande positif n'est ajouté — c'est le comportement par défaut, rien à coder.
3. **Cibles de soutenabilité réglables, par limite.** Jour du dépassement paramétré ; budget carbone, seuils de limites planétaires et leur downscaling par habitant traités comme **paramètres sourcés** (jamais en dur). Curseurs d'ambition : 1,5 °C / 2 °C / neutralité d'impact / régime régénératif. **Jamais d'indice agrégé unique** : chaque limite est affichée côte à côte avec sa propre métrique.

## Principe anti-mathwashing

Toute hypothèse qui pourrait être cachée dans le moteur doit devenir un **curseur explicite, sourcé, avec fourchette d'incertitude**. Exemple canonique : « quelle fraction de la demande finale est non-nécessaire / soutenue par la publicité » n'est pas un fait du modèle, c'est un paramètre que l'utilisateur règle. On ne présente jamais un résultat dépendant d'une hypothèse contestée avec la fausse rigueur d'un calcul comptable. La rigueur du socle (Leontief) et l'incertitude des paramètres d'usage sont visuellement distinctes.

## Socle technique (certain, préfabriqué)

- **Stack : Python pur.** `pymrio` + **EXIOBASE 3**, résolution **44 pays + 5 régions RoW**. Données : empreintes GES, eau, énergie, usage des sols, extraction de matières, et **emploi en heures travaillées** par pays × secteur.
- **Moteur :** inverse de Leontief `L` calculé **une seule fois** ; chaque scénario = `S @ (L @ Δy)` avec `Δy` ne contenant que des baisses. Architecture **precompute-then-serve** : un mouvement de curseur n'est qu'un produit matrice-vecteur → temps réel.
- **Emploi :** EXIOBASE donne les **heures**. `emplois = heures ÷ heures-par-ETP`, où heures-par-ETP, âge de retraite et taux d'emploi cible sont des **curseurs**. La distinction heures/emplois est centrale et native.
- **Vecteur d'impacts inégalement renseigné, affiché honnêtement.** Carbone / eau / matières / terres : bon mapping économie→pression. Biodiversité, entités nouvelles (chimie), flux N/P : mapping lacunaire → afficher la couverture réelle, ne jamais inventer une couverture uniforme.
- **Test de validation binaire** à chaque jalon : reproduire un chiffre publié (p. ex. empreinte carbone/eau par habitant de la France) avant d'avancer.
- **UI cible :** dashboard + globe 44 pays (projection 2D/3D), filtres par type d'impact, code couleur, sélection pays → variables de politique d'emploi. Front-end Python-natif (NiceGUI/Reflex) côté serveur avant toute migration éventuelle.

## Hors socle — noté, différé, ne pas ingénier sans demande explicite

Ces couches sont de vrais objets séparés, à ne pas greffer sur le socle comptable au risque de le casser ou de produire de la fausse précision :

- **Offre / fermeture d'un secteur-pays précis** (modèle de Ghosh ou couche de réallocation). Le socle dérive les effets pays via les chaînes d'appro à partir de leviers demande ; couper directement « l'Inde produit zéro acier » est un module ultérieur.
- **Co-bénéfices santé** (« retraite plus tôt → santé »). Couplage épidémiologique lâche au physique → au mieux un **badge qualitatif optionnel**, jamais un calcul central.
- **Couche dynamique-ludique** (projection temporelle année par année, bonheur, inégalités → guerres/famines/révolutions, condition de défaite « effondrement en 2100 »). Ce serait un **second modèle de type system dynamics (lignée World3/Limits to Growth)** branché sur le socle, pas une extension du socle. Réservé à la phase créative.

## Conventions de travail (appliquer strictement)

- **Une brique à la fois, critère de succès binaire.** Pas d'empilement.
- **Citations exigées** avant d'accepter toute affirmation « méthode documentée ». Vérifier avant d'asserter qu'une option d'UI ou une capacité existe ; ne jamais inventer d'attribution.
- **`uv run python`** pour tout Python serveur (pas le conda de base).
- **Un seul command par snippet de code.** Jamais `nano` sauf impossibilité absolue.
- **Code-first, concis.** Contenu complet d'un fichier quand le placement est ambigu.
- Pushback ferme sur les claims d'UI non vérifiés.

## Références de départ

- **O'Neill, Fanning, Lamb & Steinberger (2018), *A good life for all within planetary boundaries*** — le plus proche de l'objectif final, à résolution nationale (cibles + downscaling par habitant quasi clés en main).
- **Raworth — Doughnut Economics** (cadre).
- **Hot or Cool Institute — *1.5-Degree Lifestyles*** (cibles de conso par habitant).
- **Richardson et al. (2023)** — limites planétaires actualisées (6/9 transgressées).
- **Autonomy, Jackson, Kallis** — temps de travail / décroissance.
- **Docs EXIOBASE 3 & pymrio** — structure des comptes, comptes emploi en heures.
