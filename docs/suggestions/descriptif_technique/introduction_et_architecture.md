# Introduction et Architecture Générale

## 1. Introduction

### 1.1 Objectif du logiciel
Le logiciel de gestion d'entreprise est conçu pour répondre aux besoins spécifiques des entreprises industrielles, notamment dans le domaine de l'usinage. Il centralise et automatise la gestion des processus clés tels que la production, la qualité, la maintenance, les ressources humaines, et les stocks.

### 1.2 Public cible
Ce logiciel s'adresse principalement :
- Aux entreprises industrielles (usinage, fabrication mécanique, etc.).
- Aux responsables de production, qualité, maintenance, et RH.
- Aux opérateurs et techniciens utilisant des machines CNC ou des outils spécifiques.

### 1.3 Résumé des fonctionnalités principales
Le logiciel offre les fonctionnalités suivantes :
- Gestion des plannings (machines, opérateurs, tâches).
- Suivi de la traçabilité et de l'historique des actions.
- Gestion des ressources humaines (absences, formations, EPI, etc.).
- Gestion de la qualité (audits, non-conformités, fiches qualité).
- Planification et suivi des maintenances.
- Gestion des stocks (outils, matières premières).
- Gestion des programmes FAO et des post-processeurs.
- Centralisation des documents (RH, qualité, production).
- Analyse automatique des plans techniques et chiffrage intelligent.
- Suivi des jalons et des délais des projets.

---

## 2. Architecture générale

### 2.1 Description de l'architecture logicielle
Le logiciel est basé sur une architecture modulaire et évolutive, permettant d'ajouter ou de désactiver des fonctionnalités selon les besoins de l'entreprise.

#### **Composants principaux :**
1. **Backend :**
   - Langage : Python
   - Framework : Flask ou FastAPI
   - Base de données : PostgreSQL
   - ORM : SQLAlchemy

2. **Frontend :**
   - Framework : Vue.js ou React.js
   - Interface utilisateur : Tableaux de bord, formulaires dynamiques, graphiques interactifs.

3. **API :**
   - API REST pour la communication entre le frontend et le backend.
   - Documentation API générée automatiquement (Swagger ou Redoc).

4. **Base de données :**
   - PostgreSQL pour la gestion des données relationnelles.
   - Modèles relationnels pour les utilisateurs, machines, outils, etc.

5. **Sécurité :**
   - Gestion des rôles et permissions.
   - Authentification sécurisée (bcrypt, JWT).
   - Traçabilité des actions des utilisateurs.

---

### 2.2 Modules principaux et leurs interactions
Le logiciel est divisé en plusieurs modules fonctionnels, chacun étant responsable d'un domaine spécifique. Ces modules interagissent via des relations définies dans la base de données et des API internes.

#### **Liste des modules :**
1. **Gestion des plannings :**
   - Planification des machines et des opérateurs.
   - Suivi des tâches et des plages horaires.

2. **Traçabilité et historique :**
   - Suivi des actions des utilisateurs.
   - Traçabilité des pièces, outils, et machines.

3. **Ressources humaines (RH) :**
   - Gestion des absences, formations, sanctions, et EPI.
   - Suivi des compétences et des notations RH.

4. **Qualité (QHSE) :**
   - Gestion des audits qualité, non-conformités, et fiches qualité.
   - Collecte des résultats des contrôles.

5. **Maintenance :**
   - Planification et suivi des maintenances préventives et correctives.
   - Gestion des interventions sur les machines.

6. **Stocks :**
   - Suivi des outils et matières premières.
   - Gestion des seuils d'alerte et des réapprovisionnements.

7. **FAO et programmes :**
   - Gestion des programmes FAO et des post-processeurs.
   - Suivi des fichiers de programmes et de leur traçabilité.

8. **Gestion documentaire :**
   - Centralisation des documents RH, qualité, et production.
   - Gestion des versions et des dates de validité.

9. **Analyse et chiffrage :**
   - Analyse automatique des plans techniques.
   - Chiffrage intelligent des projets.

10. **Jalons et délais :**
    - Suivi des jalons des projets.
    - Gestion des délais pour les commandes et les projets.

---

### 2.3 Diagramme d'architecture

Voici un diagramme simplifié représentant les interactions entre les modules fonctionnels :

```plantuml
@startuml
!define RECTANGLE_COLOR #ADD8E6

rectangle "Gestion des Plannings" as Planning #RECTANGLE_COLOR
rectangle "Traçabilité et Historique" as Traceabilite #RECTANGLE_COLOR
rectangle "Ressources Humaines (RH)" as RH #RECTANGLE_COLOR
rectangle "Qualité (QHSE)" as QHSE #RECTANGLE_COLOR
rectangle "Maintenance" as Maintenance #RECTANGLE_COLOR
rectangle "Gestion des Stocks" as Stocks #RECTANGLE_COLOR
rectangle "FAO et Programmes" as FAO #RECTANGLE_COLOR
rectangle "Gestion Documentaire" as Documentation #RECTANGLE_COLOR
rectangle "Analyse et Chiffrage" as Analyse #RECTANGLE_COLOR
rectangle "Jalons et Délais" as Jalons #RECTANGLE_COLOR

Planning --> Traceabilite : Enregistre les actions
Planning --> RH : Intègre les absences
Planning --> Maintenance : Prend en compte les maintenances
Planning --> Stocks : Vérifie la disponibilité des outils

Traceabilite --> RH : Historique des actions RH
Traceabilite --> QHSE : Historique des audits et non-conformités
Traceabilite --> Maintenance : Historique des interventions

RH --> Documentation : Stocke les documents RH
QHSE --> Documentation : Stocke les audits et fiches qualité
Maintenance --> Documentation : Stocke les rapports de maintenance

FAO --> Stocks : Vérifie les outils nécessaires
FAO --> Documentation : Stocke les programmes FAO

Analyse --> Jalons : Génère des jalons pour les projets
Analyse --> Documentation : Stocke les rapports d'analyse
@enduml