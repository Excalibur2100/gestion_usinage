# 🧠 Plan de Développement Structuré - Logiciel de Gestion Usinage (UCL)

## 📁 Structure du Projet

```
/gestion_usinage
├── backend/
│   ├── models/
│   ├── migrations/
│   ├── services/
│   ├── api/
│   └── ...
├── frontend/
│   ├── components/
│   ├── pages/
│   └── ...
├── data/               # Données clients, PDF, fichiers d’analyse
├── docs/               # Documents exportés, PDF de devis, fiches techniques
├── scripts/            # Scripts IA, OCR, automatisation
└── .env, README.md, etc.
```

---

## ✅ Étapes Clés du Développement

### 1. 📦 MODULE CHIFFRAGE – Devis Automatique à partir d’un PDF

* [ ] Intégration d’un OCR pour lecture PDF
* [ ] Extraction automatique : dimensions, tolérances, matière, finition, traitement, quantité
* [ ] Génération automatique du devis :

  * Temps usinage
  * Coût matière (liaison avec stock ou fournisseur)
  * Coût main d’œuvre
  * Coût finition/traitement
* [ ] Export PDF du devis (vision client)
* [ ] Interface validation par l’utilisateur + confirmation client

### 2. 🔐 MODULE GESTION DES DROITS / UTILISATEURS

* [ ] Définition des rôles (admin, prod, client, RH, QHSE...)
* [ ] Accès par module (lecture / écriture / suppression)
* [ ] Historique des actions sensibles

### 3. 🏗 MODULE GAMMES DE PRODUCTION

* [ ] Génération de la gamme à partir du devis validé
* [ ] Affichage des étapes : machine, outil, programme, durée
* [ ] Liaison avec planning machine & employé

### 4. 🧾 INTERFACE VALIDATION CLIENT

* [ ] Visualisation du devis final
* [ ] Suivi de commande (gammes, étapes, statut prod)
* [ ] Historique des commandes / factures

### 5. 🧠 MODULE STOCK IA + CAMÉRA (V1 Simplifiée)

* [ ] Script de simulation de prise/ajout via caméra
* [ ] Mise à jour du stock automatique
* [ ] Historique & alertes de seuil
* [ ] Mode manuel / automatique activable

### 6. 📊 MODULE PREDICTIF & IA (maintenance, qualité, rendement)

* [ ] Analyse des historiques machines (température, vibrations)
* [ ] Prévision d’arrêt ou défaut qualité
* [ ] Alertes + recommandations

---

## 🔐 Sécurité

* Connexions sécurisées, gestion des tokens
* Journalisation des actions
* Sauvegarde automatique de la base

## 🧪 Tests

* [ ] Tests unitaires : OCR, chiffrage, gammes
* [ ] Tests d’intégration : flux devis → prod
* [ ] Tests d’interface (à automatiser plus tard)

## 🔄 CI/CD

* [ ] Git versionné
* [ ] GitHub Actions pour test/lint
* [ ] Dockerisation complète (DB, backend, IA)

---

## 📅 Suivi

* Création Trello ou Notion en parallèle (pour suivi rapide)
* Lié au fichier `/docs/plan_de_developpement.md`

## 💬 Prochaine étape immédiate :

* Démarrer **Module Chiffrage** (OCR + extraction + devis)
