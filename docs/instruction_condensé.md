# INSTRUCTIONS TECHNIQUES OFFICIELLES — ERP GESTION USINAGE

## 1. GÉNÉRATION DE CODE

- Donne-moi du **code complet, structuré et fonctionnel**, sans exemple ni raccourci.
- Ne change **jamais ma logique de programmation**.
- Si tu modifies un fichier existant :
  - Tu m’expliques **ce qui change**,
  - Tu me fournis le **fichier complet corrigé**,
  - Et **on valide ensemble**.
- Analyse **ma structure existante** et **intègre-toi proprement**.
- Si un dossier est manquant, **tu me dis où le créer** et sous quel nom.
- C’est **toi** qui me livres le code, pas moi.

---

## 2. STRUCTURE MODULAIRE PARFAITE

Chaque module (achat, crm, rh, etc.) doit contenir **systématiquement** :

### 2.1 Backend principal
| Type                | Dossier                   | Nom                     |
| ------------------- | ------------------------- | ----------------------- |
| Modèle SQLAlchemy   | `models/tables/<module>/` | `<table>.py`            |
| Schémas Pydantic    | `schemas/<module>/`       | `<table>_schemas.py`    |
| Service métier CRUD | `services/<module>/`      | `<table>_service.py`    |
| Controller REST     | `controllers/<module>/`   | `<table>_controller.py` |

### 2.2 Backend métier IA
| Type          | Dossier                 | Nom                            |
| ------------- | ----------------------- | ------------------------------ |
| Schémas IA    | `schemas/<module>/`     | `<table>_metier_schemas.py`    |
| Services IA   | `services/<module>/`    | `<table>_metier_service.py`    |
| Controller IA | `controllers/<module>/` | `<table>_metier_controller.py` |

### 2.3 Tests automatisés
| Type         | Dossier                   | Nom                          |
| ------------ | ------------------------- | ---------------------------- |
| Test modèle  | `tests/test_models/`      | `test_<table>.py`            |
| Test service | `tests/test_services/`    | `test_<table>_service.py`    |
| Test API     | `tests/test_controllers/` | `test_<table>_controller.py` |

---

## 3. CONTENU DES FICHIERS OBLIGATOIRE

### Schémas Pydantic :
- `Base`, `Create`, `Update`, `Read`, `Detail`
- `Search`, `SearchResults`, `List`
- `CreateResponse`, `UpdateResponse`, `DeleteResponse` si utile
- Tous les champs doivent être **validés strictement** (`Field(...)`, `max_length`, `ge=0`, etc.)
- UTF-8, compatible accents et multilingue

### Modèles SQLAlchemy :
- `__repr__`, `__table_args__`, `CheckConstraint`
- Toutes les `ForeignKey`, `relationship`, `back_populates` **incluses d’office** même si les tables liées ne sont pas encore créées
- Commenter la relation si nécessaire pour éviter les erreurs de chargement

### Endpoints REST :
- `/`, `/search`, `/list`, `/detail/{id}`, `/bulk`, `/export`, `/delete/{id}`, `/metier/*`
- Tous les endpoints doivent être versionnés (`/api/v1/...`)

---

## 4. CONFIGURATION ET INTÉGRATION

- Un dossier `config/` doit contenir :
  - `database_config.py`
  - `logging_config.py`
  - `config_base.py`
- Toute valeur sensible (clé, URL, options) doit venir du `.env`, **jamais en dur**
- Prévoir un dossier `core/ia/` pour les moteurs IA transversaux
- Prévoir un dossier `integrations/` pour :
  - FTP, mails, API externes, OCR, PDF, Excel

---

## 5. SÉCURITÉ ET ROLES

- JWT obligatoire
- Middleware `get_current_user()` + `role_required()`
- Chaque modèle sensible doit contenir :
  - `created_by`, `updated_by`, `deleted_by`
- Journaux :
  - `logs/` technique
  - `journal_metier/` fonctionnel
  - `audit_trail/` (full trace utilisateur)

---

## 6. IA MÉTIER / LOGIQUE AVANCÉE

- Chaque table métier doit avoir :
  - son moteur IA (`*_metier_service`)
  - ses schémas IA (`*_metier_schemas`)
  - son endpoint IA (`*_metier_controller`)
- Tous les calculs (prévision, suggestion, scoring, estimation) doivent être :
  - **centralisés** dans des fichiers IA ou
  - **rattachés directement aux modules**

---

## 7. NOTIFICATIONS ET DASHBOARDS

- Service `notification_service.py` :
  - `notif_app` (toast, signal)
  - `notif_email` (relances, alertes)
- Dossier `dashboard/` :
  - services métiers par module
  - widgets (`nb en retard`, `% marge`, `taux dispo`, etc.)

---

## 8. INDUSTRIALISATION

- Docker (`Dockerfile`, `docker-compose.yml`, `start.sh`)
- Fichier `.env.template` prêt à remplir
- `/admin/export` pour :
  - `dump-bdd.zip`
  - export CSV module
  - export PDF/printable
- Tous les modules exportables via `/export` ou `/download`

---

## 9. SCALABILITÉ & MULTI-STRUCTURE

- Toutes les entités (clients, devis, etc.) doivent avoir :
  - `entreprise_id` obligatoire
  - `site_id` si multi-site activé
- Paramétrage entreprise isolé :
  - `config_personnalisee`
  - `parametrage_metier_entreprise`

---

## 10. DOCUMENTATION & SUPPORT

- Code toujours commenté en ligne claire si utile
- README du module à jour
- `INSTRUCTIONS.md` à la racine
- Accès au dépôt GitHub public :
  https://github.com/Excalibur2100/gestion_usinage.git

---

## 11. APPLICATION FINALE : OBJECTIFS

| Objectif                                 | Statut |
| ---------------------------------------- | ------ |
| Code 100 % prêt pour le front            | ✅      |
| Backend industrialisable                 | ✅      |
| Extensible IA & automatisation           | ✅      |
| Testé automatiquement                    | ✅      |
| Modulaire, maintenable                   | ✅      |
| Multi-entreprise, multi-site, multi-rôle | ✅      |
| Sécurisé, loggué, audité                 | ✅      |
| Exportable, API-compatible               | ✅      |
| Front ready (React, Tauri, Android/Scan) | ✅      |

---

**Chaque fichier livré doit être définitif, propre, optimisé et jamais à reprendre.**

---