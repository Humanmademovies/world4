# Leviers de temps de travail

Combien de travail un pays doit-il faire, et comment se le **répartir** ? Ce panneau
est une identité comptable :

> `heures à faire = travailleurs × heures hebdo × semaines/an`
> `travailleurs = population en âge de travailler × (1 − n%)`

Les **heures à faire** viennent d'EXIOBASE (heures de production) et baissent quand
tu réduis des industries. La **population en âge de travailler** vient des données
démographiques de l'ONU et dépend de la tranche d'âge choisie.

## Les quatre boutons

- **Âge de début** / **Âge de retraite** — définissent qui est en âge de travailler.
  Tranche plus large = plus de travailleurs potentiels.
- **n% (non-emploi)** — la part des gens en âge de travailler qui ne sont *pas* en
  emploi à plein temps (chômage + études, soins, invalidité…). Défaut 20 %.
- **Semaines par an** — semaines travaillées (baisse-la pour modéliser congés/fériés).

## Dans les deux sens

- **Direct** : tu règles les boutons → tu lis les heures hebdo par travailleur.
- **Inverse** : tu fixes une *cible* (ex. 32 h/sem) → le panneau calcule ce qu'il
  faudrait (un âge de retraite, ou un n%). Si la cible est hors d'atteinte avec ces
  réglages, il affiche **« impossible »** plutôt que d'inventer un chiffre.

Coupe une industrie et regarde les heures libérées apparaître — moins d'heures pour
chacun, ou la possibilité de partir plus tôt.
