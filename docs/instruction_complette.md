# INSTRUCTIONS TECHNIQUES DÉFINITIVES — ERP GESTION USINAGE

## 1. GÉNÉRATION DE CODE

- Code 100 % complet, structuré, directement exploitable.
- Aucun exemple, uniquement du code prêt à produire.
- Ne jamais changer ma logique de programmation.
- Toute modification doit être :
  - Expliquée clairement
  - Envoyée sous forme de fichier complet corrigé
- Je ne dois **jamais revenir sur un fichier livré**.

---

## 2. STRUCTURE MODULAIRE PAR MODULE

Pour chaque module (`achat`, `crm`, `ia`, etc.) :

### 2.1 Backend métier
- `models/tables/<module>/<table>.py`
- `schemas/<module>/<table>_schemas.py`
- `services/<module>/<table>_service.py`
- `controllers/<module>/<table>_controller.py`

### 2.2 Backend logique métier IA
- `schemas/<module>/<table>_metier_schemas.py`
- `services/<module>/<table>_metier_service.py`
- `controllers/<module>/<table>_metier_controller.py`

### 2.3 Tests
- `tests/test_models/test_<table>.py`
- `tests/test_services/test_<table>_service.py`
- `tests/test_controllers/test_<table>_controller.py`

---

## 3. CONTENU DES FICHIERS

- Schémas : `Base`, `Create`, `Update`, `Read`, `Detail`, `Search`, `SearchResults`, `List`, `Response`
- Modèles : `__repr__`, `__table_args__`, `CheckConstraint`
- Routes REST : `POST`, `GET`, `PUT`, `DELETE`, `/search`, `/bulk`, `/export`, `/detail/{id}`
- Toujours versionné : `/api/v1/...`

---

## 4. RELATIONS ET JOINTURES

- Toutes les `ForeignKey`, `relationship`, `back_populates` doivent être incluses, même si la table liée n’existe pas encore.
- Les jointures doivent être commentées proprement si la table n’est pas encore générée.

---

## 5. OBJECTIF FINAL

- Backend 100 % prêt pour le front
- Modules isolés, testables, modifiables sans impact
- Compatible Tauri, Android, Scan, Industrie
- Zéro fichier à reprendre

---

## 6. TESTS AUTOMATISÉS

- Chaque service, modèle et controller doit avoir un test unitaire.
- Tests positifs et négatifs, sur BDD SQLite mémoire.
- TestAPI via FastAPI `TestClient`.

---

## 7. NORME DE CODE

- Respect strict de la norme PEP8
- Pas de variable ou fonction ambiguë
- Fichiers triés, imports propres
- `orm_mode = True`, `from_attributes = True` dans tous les schémas

---

## 8. IA MÉTIER / LOGIQUE DÉCOUPLÉE

- Jamais de logique IA dans les CRUD classiques
- IA toujours dans `*_metier_service.py`
- Appels IA via `/metier/*` dédiés
- IA transversale centralisée dans `core/ia/`

---

## 9. VALIDATION STRICTE

- Tous les champs validés avec `Field(...)`
- Champs numériques : `ge=0`, `le=100`, etc.
- Champs texte : `max_length`, `nullable`, `format`
- UTF-8, accents, multilingue supporté

---

## 10. CONFIGURATION CENTRALISÉE

- Fichier `.env` unique
- Dossier `config/` contenant :
  - `config_base.py`
  - `database_config.py`
  - `logging_config.py`

---

## 11. MAIN.PY BIEN STRUCTURÉ

- Tous les routeurs doivent être inclus explicitement
- Aucun oubli ou conflit d'import
- Static files + templates déclarés une fois

---

## 12. RÔLES / AUTHENTIFICATION

- JWT obligatoire
- Séparation des rôles (`admin`, `usine`, `client`)
- Middleware de permission
- Tables avec `created_by`, `updated_by`, `deleted_by` si sensible

---

## 13. JOURNAL MÉTIER

- Créer table `journal_metier` :
  - `module`, `action`, `timestamp`, `user_id`, `données`
- Pour toute action importante ou logique complexe

---

## 14. LOGGING ET MONITORING

- Dossier `logs/` avec rotation possible
- Middleware de journalisation technique (requêtes, erreurs)
- Table `audit_trail` pour la traçabilité complète

---

## 15. EXPORT / IMPORT / SAUVEGARDE

- Chaque module doit supporter :
  - Export CSV, Excel, PDF
  - `/export`, `/print`, `/download`
- Export global possible : `dump-bdd.zip`, script JSON ou SQL

---

## 16. MULTI-ENTREPRISE / SITE / UTILISATEUR

- Chaque table principale doit inclure :
  - `entreprise_id`
  - `site_id` si applicable
- Middleware pour filtrage automatique des données par structure

---

## 17. DASHBOARDS MÉTIER

- Chaque module doit avoir un `dashboard_service.py`
- Indicateurs : volumes, alertes, taux, retards, efficacité
- Format : résumé, badge, pourcentage, variation

---

## 18. NOTIFICATIONS / ALERTE MÉTIER

- Centraliser dans `core/notification_service.py`
- Support :
  - `notif_app` (toast)
  - `notif_email`
  - `notif_critique` (workflow, maintenance…)

---

## 19. PARAMÉTRAGE MÉTIER ENTREPRISE

- Table `parametrage_metier_entreprise` pour :
  - préférences, colonnes, alertes
- Accessible via middleware ou injection automatique

---

## 20. PLANIFICATION / TÂCHES AUTOMATIQUES

- Prévoir support de :
  - tâches planifiées (ex : `crontab`, `APScheduler`)
  - traitement async (FastAPI + Celery)
- Pour IA, archivage, relance, purge

---

## 21. INTEROPÉRABILITÉ

- Dossier `integrations/`
  - FTP, Excel, PDF OCR, API externes, eFacture
- Toute donnée externe doit être logguée + historisée

---

## 22. EXPORT CONFIGURATION + MODULE

- Route `/admin/export`
  - dump complet config + modules + paramétrage
- Route `/export/module_name` pour lister les objets d’un module

---

## 23. FORMATAGE DES ROUTES API

- Toutes les routes doivent être :
  - versionnées : `/api/v1/...`
  - format `kebab-case`
- Aucun camelCase ou snake_case dans les URLs

---

## 24. FRONT-END READY

- Tous les endpoints testés pour React/Tauri
- Routes REST et métier prêtes à être branchées
- Prévoir hook `useModuleApi()` ou équivalent
- Export JSON standardisés

---

## 25. ARCHITECTURE DEPLOYABLE

- Dossier `deployment/` :
  - `Dockerfile`
  - `docker-compose.yml`
  - `start.sh`
  - `.env.template`
- Projet déployable immédiatement en local ou cloud

---

## 26. LIVRABLES ET DOCUMENTATION

- Chaque module livré est documenté :
  - Schémas, routes, réponse, logique métier
- Fichier `INSTRUCTIONS.md` à jour
- README par module si besoin
- Rien ne doit rester implicite

---

👉 Ces instructions sont définitives. Tu dois les appliquer **à chaque fichier généré**.