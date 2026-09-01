# 🌿 Au Fond du Jardin

## 🌱 Pourquoi Au Fond du Jardin ?

Les services professionnels d’agrométéorologie permettent déjà de croiser différentes données pour suivre finement les conditions environnementales autour des cultures.

Mais cette capacité reste difficilement accessible au particulier : les données ouvertes existent, mais elles sont dispersées entre de nombreuses sources, parfois techniques à exploiter et de résolutions différentes.

**Au Fond du Jardin cherche à rendre cette capacité d’observation accessible au plus grand nombre.**

À partir d’un simple point GPS, le projet recherche, croise et présente les meilleures informations environnementales ouvertes disponibles autour de ce lieu.

Dans un contexte de réchauffement climatique, où l’adaptation locale devient de plus en plus importante, mieux comprendre ce qui se passe réellement autour de son terrain ne devrait pas être réservé aux professionnels disposant de services spécialisés.

> **Mission : rendre gratuitement accessible une information environnementale locale qui existe déjà dans les données ouvertes, mais dont l’accès et le croisement sont aujourd’hui trop complexes pour l’utilisateur ordinaire.**

**Au Fond du Jardin observe, croise et hiérarchise. Il ne prescrit pas.**

---

## 🧭 Principe directeur

La question qui guide l’ajout d’une source, d’un indicateur ou d’une fonction est :

> **Est-ce que cette source permet, quelque part, d’améliorer la meilleure information disponible autour d’un point GPS ?**

Le projet ne cherche donc pas à accumuler les API.

Il cherche à déterminer, pour chaque information utile, **la meilleure donnée raisonnablement disponible autour du lieu demandé**.

La source la plus proche n’est pas nécessairement la meilleure.

Une donnée doit aussi être évaluée selon :

- sa pertinence physique ;
- sa fraîcheur ;
- sa qualité et sa documentation ;
- sa résolution spatiale ;
- sa distance au point GPS ;
- son altitude et son contexte topographique lorsque cela compte ;
- son bassin versant ou son contexte hydrologique lorsque cela compte ;
- son caractère mesuré ou modélisé ;
- la disponibilité d’un historique.

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

## Règle de mise en page

> **Ne jamais surcharger l’interface. L’information utile doit être identifiable immédiatement.**

La mise en page doit donner la priorité visuelle à l’essentiel :

- valeur ou information principale ;
- état ou vigilance uniquement lorsqu’ils sont réellement défendables ;
- contexte minimal nécessaire à la compréhension.

Les informations techniques détaillées — source, variable, résolution, méthode, licence ou autres métadonnées — doivent être documentées principalement dans le présent README plutôt que répétées dans le tableau de bord.

Lorsqu’un détail supplémentaire est nécessaire dans l’interface, il doit rester secondaire et ne pas gêner la lecture immédiate.

**Interface = information utile rapidement identifiable.  
README = traçabilité, sources, méthodes et limites.**

---

# 📊 Informations environnementales recherchées

Selon les sources disponibles autour du point GPS, le projet peut chercher à restituer notamment :

## Météo

- température de l’air ;
- températures minimales et maximales ;
- température ressentie comme information de contexte ;
- humidité atmosphérique ;
- vitesse du vent ;
- direction du vent ;
- précipitations et cumuls ;
- degrés-jours de croissance (GDD).

## Environnement

- évapotranspiration de référence **ET0** ;
- indice UV ;
- qualité de l’air ;
- ozone.

L’ET0 représente la demande évaporative de référence de l’atmosphère.

Elle ne doit pas être présentée comme une mesure directe de l’eau réellement perdue par une parcelle ni comme un besoin automatique d’arrosage.

## Eau, sol et territoire

- humidité superficielle du sol ;
- température du sol ;
- contexte hydrologique ;
- bassin versant ;
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
- une station officielle légèrement plus éloignée mais beaucoup mieux documentée ;
- une petite station locale bien située pouvant révéler un phénomène que la grille d’un modèle représente mal.

La sélection des sources doit progressivement pouvoir tenir compte de :

- distance ;
- fraîcheur de la donnée ;
- qualité et documentation de la source ;
- résolution spatiale ;
- altitude ;
- cohérence topographique ;
- bassin versant ou cours d’eau concerné ;
- disponibilité d’un historique ;
- caractère mesuré ou modélisé ;
- cohérence avec d’autres sources indépendantes.

## Stations météorologiques locales

Les petites stations locales constituent une famille de sources importante pour le projet.

Elles peuvent améliorer fortement certaines informations autour du point GPS, notamment :

- température ;
- humidité de l’air ;
- vent ;
- précipitations ;
- parfois rayonnement ou autres variables.

Leur valeur dépend toutefois de leur installation, de leur exposition, de leur entretien, de leur fraîcheur et de la documentation disponible.

Le projet doit donc chercher à **évaluer** une station locale, et non simplement à la choisir parce qu’elle est proche.

## Transparence

Le logiciel doit distinguer clairement :

**mesure réelle / donnée modélisée / estimation / observation / donnée indisponible.**

Exemple :

```text
Humidité du sol en surface
Valeur : 31 %
Source : Copernicus ERA5-Land
Type : donnée modélisée
Couche : 0–7 cm
Résolution native : ~9 km
```

Une absence de donnée est préférable à une fausse précision.

Le programme doit pouvoir dire simplement :

```text
Donnée locale indisponible
```

---

# 🧪 Mesure, modèle et observation du terrain

Une donnée environnementale extérieure ne représente pas nécessairement exactement ce qui se passe dans une petite parcelle.

Le projet cherche donc à fournir le meilleur **contexte objectif** possible autour du terrain.

Ce contexte peut être confronté aux observations réalisées directement sur place.

```text
données mesurées
      +
données modélisées
      +
sources locales
      ↓
signal / tendance
      ↓
observation directe du terrain
      ↓
corroboration ou remise en question
```

L’observation du terrain n’efface pas les limites des données.

Inversement, un modèle ne doit jamais être présenté comme une mesure effectuée dans le jardin.

Lorsque plusieurs informations indépendantes convergent et sont cohérentes avec l’observation directe, elles peuvent constituer un **faisceau de preuves** plus robuste qu’une valeur isolée.

---

# 🚨 Vigilances, indices et seuils

Le prototype contient actuellement des niveaux :

**VERT / JAUNE / ORANGE / ROUGE**

Ils sont encore **expérimentaux**.

Ils ne doivent pas être interprétés comme des seuils agronomiques ou écologiques validés.

La règle scientifique du projet est :

> **Pas de phénomène défendable → pas d’indice.**

Un indice ne doit pas être créé simplement parce qu’une représentation en couleur serait pratique.

Avant d’afficher un indice, il faut pouvoir relier :

```text
données disponibles
        ↓
phénomène physique identifiable
        ↓
relation documentée entre variables et phénomène
        ↓
méthode et seuils défendables
        ↓
indice éventuel
```

Selon le phénomène, la méthode pourra utiliser :

- des seuils absolus documentés lorsqu’ils existent ;
- la situation locale habituelle ;
- des anomalies ou percentiles ;
- la durée ou la persistance du phénomène ;
- la convergence de plusieurs signaux indépendants ;
- des pondérations issues d’une méthode documentée ;
- le contexte spatial et la résolution des données ;
- l’observation du terrain comme corroboration.

Aucune pondération ne doit être inventée arbitrairement.

## Reproductibilité

> **Tout indice affiché doit être reproductible à partir de sa définition documentée dans le README.**

Pour chaque indice retenu, la documentation devra préciser au minimum :

- le phénomène observé ;
- les variables utilisées ;
- les sources des données ;
- la zone ou la résolution spatiale ;
- la période statistique de référence ;
- la méthode de calcul ;
- les seuils ;
- la durée ou persistance nécessaire ;
- la fréquence de mise à jour ;
- la signification de chaque niveau ;
- les limites et incertitudes.

Si ces éléments ne peuvent pas être défendus, le projet doit afficher les données elles-mêmes sans fabriquer d’indice global.

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
- observations du terrain.

---

# 🛰️ Sources de données

## Sources actuellement utilisées

### Open-Meteo

Le prototype actuel utilise principalement les services **Open-Meteo** pour :

- température actuelle ;
- historique des températures ;
- précipitations ;
- altitude ;
- qualité de l’air et ozone.

Les GDD, cumuls et synthèses sont ensuite calculés localement.

### Copernicus / ERA5-Land

L’humidité superficielle du sol est désormais récupérée depuis **ERA5-Land**.

La variable utilisée représente l’eau volumique dans la couche superficielle du sol, **0–7 cm**.

La donnée est associée à la cellule de grille ERA5-Land correspondant au point demandé.

Elle doit toujours être présentée comme :

- une **donnée modélisée** ;
- associée à une grille d’environ **9 km** de résolution native ;
- différente d’une mesure effectuée physiquement dans la parcelle.

Le prototype calcule actuellement une moyenne journalière à partir des valeurs horaires disponibles.

Une indisponibilité de Copernicus ne doit pas empêcher le reste du tableau de bord de fonctionner.

## Sources prévues ou étudiées

### Réseaux météorologiques

Le projet prévoit d’étudier et comparer :

- stations officielles ;
- stations contributives ouvertes ;
- petites stations locales ;
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
informations / indices défendables
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
    agrégation
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

## Séparation logique actuelle

Le projet tend vers une séparation claire entre récupération, préparation et présentation :

```text
sources / modules Python
        ↓
générateur Python
        ↓
template.html
        ↓
index.html
```

Le HTML ne doit pas être enfoui inutilement dans le générateur Python.

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

Dans sa forme actuelle, le programme Python génère un fichier `index.html` à partir de `template.html`, puis peut l’ouvrir dans le navigateur.

L’interface fonctionne comme un petit tableau de bord web local.

Une connexion Internet reste nécessaire pour interroger les sources de données distantes.

## Régler son terrain

Le bouton **⚙️ Mon terrain** permet actuellement de modifier :

- le nom du site ;
- la latitude ;
- la longitude.

Les coordonnées sont conservées localement par le navigateur.

La version cible doit déterminer automatiquement autant que possible les informations géographiques complémentaires.

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

## Humidité superficielle du sol

La valeur affichée actuellement provient de Copernicus ERA5-Land.

Elle décrit l’humidité volumique moyenne de la couche superficielle **0–7 cm** de la cellule de grille associée au point GPS.

Elle fournit un contexte régionalisé du sol et ne constitue pas une mesure directe de la parcelle.

## Qualité de l’air

Le prototype affiche actuellement un indice européen de qualité de l’air et une concentration d’ozone lorsque les données sont disponibles.

Voir la section **Pourquoi surveiller la qualité de l’air ?** pour comprendre son intérêt.

## Comprendre une donnée absente

Une donnée absente n’est pas une panne si aucune source suffisamment pertinente n’est disponible.

Le logiciel doit distinguer :

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
- récupération de l’humidité superficielle du sol via Copernicus ERA5-Land ;
- gestion d’une indisponibilité de Copernicus sans bloquer le reste du tableau de bord ;
- séparation du générateur Python et du modèle HTML ;
- documentation HTML accessible depuis le tableau de bord ;
- premières vigilances expérimentales.

## Encore expérimental

- niveaux de vigilance ;
- méthode future de sélection et hiérarchisation des sources ;
- interprétation croisée de plusieurs signaux.

## Pas encore implémenté

- sélection automatique de la meilleure source ;
- ET0 ;
- indice UV dans la vue cible ;
- vent et direction dans la vue cible ;
- température ressentie dans la vue cible ;
- température du sol ;
- Hub’Eau ;
- sélection automatique de stations météo locales ;
- détermination automatique du bassin versant ;
- indication systématique de la provenance et de la précision ;
- indice global scientifiquement défendable.

---

# 🗺️ Feuille de route

### Étape 1 — Consolider le noyau actuel

- maintenir la séparation Python / HTML ;
- conserver la gestion d’erreur par source ;
- préserver un prototype immédiatement utilisable ;
- maintenir le README comme cahier des charges maître.

### Étape 2 — Enrichir le contexte atmosphérique

Tester puis intégrer progressivement :

- ET0 ;
- vent et direction ;
- humidité atmosphérique lorsque pertinente ;
- température ressentie comme contexte ;
- indice UV.

Chaque donnée doit d’abord être testée directement auprès de sa source avant son intégration au programme.

### Étape 3 — Sélection des sources météo locales

Chercher automatiquement les stations pertinentes autour du point GPS et comparer notamment :

- distance ;
- altitude ;
- exposition lorsque documentée ;
- fraîcheur ;
- qualité ;
- historique ;
- cohérence avec les autres sources.

### Étape 4 — Eau et territoire

Ajouter progressivement :

- contexte du bassin versant ;
- sources pertinentes de Hub’Eau ;
- données hydrométriques ;
- données piézométriques lorsque pertinentes.

### Étape 5 — Indices défendables

Étudier les phénomènes pour lesquels un indice peut réellement être justifié.

Aucun indice ne doit être ajouté tant que sa méthode, ses seuils et ses limites ne sont pas documentés et reproductibles.

---

# 🤝 Contributions

**Au Fond du Jardin** a vocation à être un projet ouvert.

Une contribution peut concerner :

- une nouvelle source ;
- un connecteur vers une API ;
- un indicateur scientifiquement défendable ;
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
