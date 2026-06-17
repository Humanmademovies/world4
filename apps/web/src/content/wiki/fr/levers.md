# Leviers de demande — ce que fait un curseur

Un **levier** réduit la **demande finale** d'un secteur (au choix, dans un seul pays).
La « demande finale » = ce qui est consommé au bout (ménages, État, investissement,
exports) — pas les ventes intermédiaires entre industries.

## Quand tu bouges un curseur

Mettre un secteur à **−30 %** retire 30 % de sa demande finale. Le moteur :

1. propage la baisse **en amont** dans toute la chaîne (`Δproduction = L · Δdemande`) ;
2. recalcule chaque **impact écologique** (`Δimpact = intensité · Δproduction`) ;
3. recalcule les **heures de production** nécessaires à chaque pays (ce qui alimente
   le panneau Travail).

Réduire un secteur en touche donc beaucoup d'autres, dans beaucoup de pays — c'est
tout l'intérêt.

## Les règles du socle (honnêtes par construction)

- **Baisses seules.** On ne peut jamais *ajouter* de demande ; on n'explore que le « faire moins ».
- **Pas de réinjection.** L'argent ou le travail « libéré » par une coupe n'est pas redépensé ailleurs comme par magie.
- **Technologie constante.** Les intensités ne s'améliorent pas ; ce n'est pas un modèle de transition verte.

## Lire un secteur

Ouvre l'onglet **Secteurs** et choisis-en un : tu vois, pour le pays sélectionné, la
**part de chaque empreinte qu'il porte** et le **travail qu'il mobilise** — c'est-à-dire
exactement ce que son levier déplacerait, et de combien.
