# 🌿 Au Fond du Jardin

**Au Fond du Jardin** est un projet libre et local-first qui cherche à rendre compréhensibles et utiles des données environnementales ouvertes autour d’un terrain.

Il est pensé d’abord pour les **jardiniers, vergers, petits terrains et observateurs de leur environnement** qui veulent comprendre ce qui se passe réellement autour d’eux sans devoir apprendre Python, JSON, les API ou les outils scientifiques utilisés en arrière-plan.

> **Mission : rendre gratuitement accessible une information environnementale locale qui existe déjà dans les données ouvertes, mais dont l’accès et le croisement sont aujourd’hui trop complexes pour l’utilisateur ordinaire.**

---

## 🧭 Principe directeur

La question qui guide l’ajout d’une source, d’un indicateur ou d’une fonction est :

> **Est-ce que cette source permet, quelque part, d’améliorer la meilleure information disponible autour d’un point GPS ?**

Le projet ne cherche donc pas à accumuler les API.

Il cherche à déterminer, pour chaque information utile, **la meilleure donnée raisonnablement disponible autour du lieu demandé**.

La source la plus proche n’est pas nécessairement la meilleure.

Une donnée doit aussi être évaluée selon sa pertinence physique, sa fraîcheur, sa qualité et sa résolution.

---

# 🌱 Ce que doit vivre l’utilisateur

L’objectif est une utilisation aussi simple que possible.

À terme, l’utilisateur ne devrait avoir besoin de fournir que :

- un nom pour son terrain ;
- sa latitude ;
- sa longitude.

Lorsque cela est possible, le logiciel doit déterminer automatiquement le reste :

- commune et contexte géographique ;
- bassin versant ;
- altitude et contexte topographique ;
- stations disponibles ;
- sources environnementales pertinentes ;
- résolution ou distance de chaque donnée.

Le tableau de bord doit pouvoir être compris rapidement.

Les détails techniques doivent rester accessibles à celui qui souhaite savoir **pourquoi** une donnée a été retenue.

---

# 📊 Informations environnementales recherchées

Selon les sources disponibles autour du point GPS, le projet peut chercher à restituer notamment :

- température de l’air ;
- températures minimales et maximales ;
- précipitations et cumuls ;
- degrés-jours de croissance (GDD) ;
- qualité de l’air ;
- ozone ;
- humidité superficielle du sol ;
- température du sol ;
- contexte hydrologique ;
- débit des cours d’eau ;
- niveau des nappes ;
- autres indicateurs environnementaux apportant une information locale réellement utile.

Toutes ces données ne sont **pas encore implémentées**.

Le projet évolue progressivement sans prétendre disposer d’une information qui n’existe pas encore dans le logiciel.

---

# 🔎 Choisir la meilleure information disponible

## Proximité ≠ pertinence

Une station située à 2 km peut être moins représentative qu’une station située à 8 km.

Exemples :

- une station hydrologique proche mais située sur un autre bassin versant ;
- une station météo privée très proche mais mal exposée ;
- une station officielle légèrement plus éloignée mais beaucoup mieux documentée.

La sélection des sources doit progressivement pouvoir tenir compte de :

- distance ;
- fraîcheur de la donnée ;
- qualité et documentation de la source ;
- résolution spatiale ;
- altitude ;
- cohérence topographique ;
- bassin versant ou cours d’eau concerné ;
- disponibilité d’un historique ;
- caractère mesuré ou modélisé.

## Transparence

Le logiciel doit distinguer clairement :

**mesure réelle / donnée modélisée / estimation / donnée indisponible.**

Exemple :

```text
Humidité du sol en surface
Valeur : 0,31 m³/m³
Source : Copernicus ERA5-Land
Type : donnée modélisée
Résolution : ~9 km
```

Une absence de donnée est préférable à une fausse précision.

Le programme doit pouvoir dire simplement :

```text
Donnée locale indisponible
```

---

# 🧪 Mesure, modèle et observation du jardinier

Une donnée environnementale extérieure ne représente pas nécessairement exactement ce qui se passe dans une petite parcelle.

Le projet cherche donc à fournir un **contexte objectif** autour du terrain.

À terme, ce contexte pourra être croisé avec les observations réalisées directement dans le jardin.

```text
             observations du jardinier
                       │
                       ▼
                    terrain
                       ▲
          ┌────────────┼────────────┐
          │            │            │
       météo       hydrologie     satellite
          └────────────┼────────────┘
                       ▼
              contexte objectif
```

Plusieurs indicateurs indépendants et cohérents peuvent constituer un **faisceau de preuves** plus utile qu’une valeur isolée.

---

# 🚨 Vigilances et seuils

Le prototype contient actuellement des niveaux :

**VERT / JAUNE / ORANGE / ROUGE**

Ils sont encore **expérimentaux**.

Ils ne doivent pas être interprétés comme des seuils agronomiques ou écologiques validés.

Le futur système de vigilance devra utiliser, selon l’indicateur :

- des seuils absolus documentés lorsqu’ils existent ;
- la situation locale habituelle ;
- des anomalies ou percentiles ;
- la durée du phénomène ;
- la convergence de plusieurs indicateurs ;
- éventuellement une observation effectuée sur le terrain.

L’objectif n’est pas de produire une alerte spectaculaire.

L’objectif est de pouvoir expliquer **pourquoi** un niveau de vigilance est affiché.

---

# 🌬️ Pourquoi surveiller la qualité de l’air ?

Pour le jardinier, la qualité de l’air n’est pas seulement une information destinée à la santé humaine.

L’**ozone troposphérique** peut également affecter le fonctionnement des végétaux.

Une exposition importante peut perturber les échanges gazeux et modifier la conductance stomatique. Selon l’espèce, l’intensité et la durée du stress, cela peut participer à une fermeture partielle des stomates ou à une régulation moins efficace.

Ces perturbations peuvent influencer :

- les échanges de CO₂ ;
- la transpiration ;
- la photosynthèse ;
- le fonctionnement hydrique de la plante.

L’IQA ou la concentration d’ozone **ne mesurent cependant pas directement l’ouverture des stomates**.

Ils constituent un indicateur de contexte à croiser avec notamment :

- température ;
- humidité atmosphérique ;
- disponibilité en eau du sol ;
- durée du phénomène ;
- observations du jardinier.

---

# 🛰️ Sources de données

## Sources actuellement utilisées

Le prototype actuel utilise principalement les services **Open-Meteo** pour :

- température actuelle ;
- historique des températures ;
- précipitations ;
- altitude ;
- qualité de l’air et ozone.

Les GDD, cumuls et synthèses sont ensuite calculés localement.

## Sources prévues ou étudiées

### Copernicus / ERA5-Land

Prévu notamment pour apporter un contexte spatial continu et des informations telles que :

- humidité superficielle du sol ;
- température du sol ;
- historique environnemental ;
- anomalies par rapport aux conditions habituelles.

Une donnée Copernicus devra toujours être présentée comme une donnée modélisée avec sa résolution réelle, et non comme une mesure effectuée dans le jardin.

### Réseaux météorologiques

Le projet prévoit d’étudier et comparer :

- stations officielles ;
- stations contributives ouvertes ;
- stations privées dont les conditions d’accès et de réutilisation sont compatibles avec le projet.

### Hub’Eau

Prévu pour les données françaises liées notamment :

- à l’hydrométrie ;
- aux cours d’eau ;
- aux nappes souterraines.

### Autres sources

D’autres sources peuvent être ajoutées si elles respectent le principe directeur du projet.

Une source n’entre pas dans le noyau uniquement parce qu’elle est techniquement accessible.

---

# 🧱 Architecture visée

```text
Point GPS
   │
   ▼
localisation
   │
   ▼
recherche des sources disponibles
   │
   ▼
évaluation de leur pertinence
   │
   ▼
normalisation
   │
   ▼
indicateurs
   │
   ▼
affichage simple
```

Les sources doivent progressivement devenir indépendantes du reste du programme.

Exemple conceptuel :

```text
core/
    localisation
    dates
    sélection_sources
    indicateurs

sources/
    open_meteo
    copernicus
    hubeau
    qualité_air
    stations_meteo
    ...

interface/
    web
```

## Règle d’évolution

> **Évolutif ne doit jamais vouloir dire incomplet.**

Le noyau doit rester fonctionnel pendant son évolution.

Une nouvelle source doit améliorer l’application sans rendre le reste du programme dépendant de cette source.

## Règle de distribution

> **Le packaging doit s’adapter à la plateforme ; le noyau ne doit jamais dépendre du packaging.**

À terme, le même noyau pourra être distribué sous différentes formes :

- Windows ;
- Linux ;
- macOS ;
- code source Python.

Le traitement doit rester autant que possible **local**.

Le projet cherche ainsi à éviter qu’un serveur central, un abonnement ou une infrastructure coûteuse deviennent nécessaires à son fonctionnement.

---

# 📘 Aide utilisateur

## Lancer le prototype actuel

Dans sa forme actuelle, le programme Python génère un fichier `index.html` puis l’ouvre dans le navigateur.

L’interface fonctionne comme un petit tableau de bord web local.

Une connexion Internet reste nécessaire pour interroger les sources de données distantes.

## Régler son terrain

Le bouton **⚙️ Réglages Mon Terrain** permet actuellement de modifier les informations utilisées par le prototype.

Les coordonnées sont conservées localement par le navigateur.

Certains champs présents aujourd’hui, comme le code INSEE et le bassin hydrographique, sont des héritages de la phase expérimentale.

**Ils ne devraient pas avoir à être renseignés manuellement dans la version cible.**

## Température

La température affichée correspond à la donnée fournie par la source pour les coordonnées configurées.

Elle ne doit pas être présentée comme une mesure effectuée physiquement dans le jardin lorsqu’elle provient d’un modèle ou d’une grille météorologique.

## Pluie 7 jours / 30 jours

Ces valeurs correspondent aux cumuls de précipitations calculés sur les périodes indiquées à partir des données disponibles.

## GDD

Les **Growing Degree Days**, ou degrés-jours de croissance, représentent une accumulation de chaleur au-dessus d’une température de base.

Le prototype utilise actuellement une base de **10 °C**.

Cette valeur n’est pas universelle.

Les besoins et seuils biologiques varient selon les espèces et les usages.

## Qualité de l’air

Le prototype affiche actuellement un indice européen de qualité de l’air et une concentration d’ozone lorsque les données sont disponibles.

Voir la section **Pourquoi surveiller la qualité de l’air ?** pour comprendre son intérêt pour le jardin.

## Comprendre une donnée absente

Une donnée absente n’est pas une panne si aucune source suffisamment pertinente n’est disponible.

Le logiciel doit progressivement apprendre à distinguer :

```text
Donnée indisponible
```

de :

```text
Erreur lors de la récupération des données
```

## Comprendre la précision

Lorsque cela est possible, chaque donnée importante devra pouvoir indiquer :

- sa source ;
- sa date ou fraîcheur ;
- sa distance si elle provient d’une station ;
- sa résolution si elle provient d’une grille ;
- son caractère mesuré ou modélisé.

---

# 🛠️ État actuel du prototype

## Déjà fonctionnel

- interface web locale ;
- coordonnées GPS configurables ;
- configuration conservée localement ;
- température actuelle ;
- altitude ;
- cumuls de pluie sur 7 et 30 jours ;
- historique Tmin/Tmax ;
- calcul des GDD ;
- qualité de l’air ;
- ozone ;
- synthèse mensuelle ;
- premières vigilances expérimentales.

## Encore expérimental

- caractérisation du relief ;
- niveaux de vigilance ;
- seuils spécifiques aux cultures ;
- code INSEE renseigné manuellement ;
- bassin hydrographique renseigné manuellement.

## Pas encore implémenté

- sélection automatique de la meilleure source ;
- Copernicus / ERA5-Land ;
- humidité du sol ;
- température du sol ;
- Hub’Eau ;
- sélection de stations météo locales ;
- détermination automatique du bassin versant ;
- indication systématique de la provenance et de la précision.

---

# 🗺️ Feuille de route

### Étape 1 — Stabiliser le prototype

- finaliser le présent cahier des charges ;
- nettoyer l’interface actuelle ;
- supprimer les informations présentées avec une précision excessive ;
- conserver un prototype immédiatement utilisable.

### Étape 2 — Première nouvelle source

Intégrer **Copernicus / ERA5-Land** en commençant par l’humidité superficielle du sol.

Objectifs :

- récupérer la donnée autour du GPS ;
- conserver sa provenance ;
- indiquer qu’elle est modélisée ;
- afficher sa résolution ;
- ne pas inventer de seuil « sec / humide » sans justification.

### Étape 3 — Sélection des sources météo

Chercher automatiquement les stations pertinentes autour du point GPS et commencer à comparer :

- distance ;
- altitude ;
- fraîcheur ;
- qualité ;
- disponibilité historique.

### Étape 4 — Hydrologie

Ajouter progressivement les sources pertinentes de Hub’Eau et le contexte du bassin versant.

### Étape 5 — Faisceau d’indicateurs

Faire évoluer les vigilances vers une interprétation fondée sur plusieurs informations indépendantes et documentées.

---

# 🤝 Contributions

**Au Fond du Jardin** a vocation à être un projet ouvert.

Une contribution peut concerner :

- une nouvelle source ;
- un connecteur vers une API ;
- un indicateur ;
- une amélioration de l’interface ;
- une correction scientifique ;
- une amélioration de la documentation ;
- le support d’une autre région ou d’un autre pays.

Avant d’ajouter quelque chose, la question reste :

> **Est-ce que cette source permet, quelque part, d’améliorer la meilleure information disponible autour d’un point GPS ?**

---

# ⚖️ Licence

Le prototype actuel est publié sous **GNU General Public License v3.0 (GPLv3)**.

---

**Auteur : Bruno Romero — _Curl est ton ami_**
