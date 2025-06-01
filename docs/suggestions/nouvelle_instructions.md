INSTRUCTIONS COMPLÈTES ET DÉFINITIVES – PROJET ERP USINAGE
1. CODE 100 % OPÉRATIONNEL

Tout fichier livré doit être immédiatement exécutable, sans ligne manquante ou à compléter.
Zéro ligne inutile, zéro placeholder.
Qualité industrielle, production-ready, Copilot-friendly.


2. STRUCTURE ARCHITECTURALE MODULAIRE
Respect absolu de l'arborescence suivante :
backend/
├─ core/
│  ├─ db/
│  │  ├─ models/tables/<module>/<table>.py
│  │  ├─ schemas/<module>/<table>_schemas.py
│  └─ ia/<table>_engine.py
├─ services/
│  ├─ <module>/<table>_service.py
│  └─ <module>/service_metier/<table>_metier_service.py
├─ controllers/
│  ├─ <module>/<table>_controller.py
│  └─ <module>/metier_controller/<table>_metier_controller.py

# Tests unitaires
├─ tests/
│  ├─ test_models/<module>/test_<table>.py
│  ├─ test_services/<module>/test_<table>_service.py
│  ├─ test_services/<module>/metier_service/test_<table>_metier_service.py
│  ├─ test_controllers/<module>/test_<table>_controller.py
│  ├─ test_core/<module>/test_<table>_engine.py
│  └─ test_metier/<module>/test_<table>_metier_controller.py


3. POUR CHAQUE TABLE : 14 FICHIERS OBLIGATOIRES

Modèle SQLAlchemy (models/...)
Schémas Pydantic complets (schemas/...)
Service CRUD (services/...)
Service métier (services/.../service_metier/...)
Contrôleur REST principal (controllers/...)
Contrôleur métier (controllers/.../metier_controller/...)
IA métier / moteur logique (core/ia/...)
à 14. Tests unitaires complets


4. ORM SQLAlchemy

__tablename__, __table_args__, CheckConstraint, ForeignKey, relationship, back_populates
Relations anticipées même si la table n’existe pas encore (commentées si besoin)
lazy="joined", cascade="all, delete-orphan"
__repr__ toujours défini proprement


5. SCHEMAS PYDANTIC

orm_mode = True, from_attributes = True, model_validator
Schémas : Base, Create, Update, Read, Detail, List, Search, SearchResults, Response, Bulk
Champs avec Field(..., ge=0) si besoin + example systématique
Enum explicite, commentaires intégrés, validation croisée (ex: HT/TVA/TTC cohérent)


6. ROUTES REST / CONTROLLER

Endpoints REST : POST, GET, PUT, DELETE, POST /search, POST /bulk, GET /export, GET /detail/{id}
Swagger enrichi : summary, description pour chaque route
Kebab-case dans les chemins (/avoirs-fournisseur, /commande-fournisseur)
Exports via StreamingResponse (CSV)


7. SERVICES MÉTIER / IA

Toute logique non-CRUD est dans :

*_metier_service.py (calculs, statuts, validations...)
*_metier_controller.py (accès API métier)
*_engine.py (suggestions, IA, logique avancée)


Exemples : suggestion automatique, calcul TTC, statut automatique


8. TESTS AUTOMATISÉS PYTEST

Chaque fichier livré = 1 fichier de test dans le dossier correspondant
Fichiers de test complets, prêts à copier-coller
Couverture : cas standard + erreurs + edge cases
Base SQLite in-memory : sqlite:///:memory:
Utilisation de getattr(...) pour éviter les erreurs Column[...]
Nom clair, assertion complète, test du __repr__


9. CONVENTIONS & NOMMAGE

Fichiers : snake_case
Tables : snake_case, pluriel (ex: avoirs_fournisseur)
Schémas Pydantic : PascalCase
Routes : kebab-case /api/v1/...
Dossier IA : core/ia/<table>_engine.py


10. QUALITÉ ET INTELLIGENCE

Le code livré est directement copiable dans un vrai projet
Toute amélioration ou optimisation est immédiatement appliquée
Comparaison systématique avec les ERP/méthodes existants
Ne jamais livrer de version minimale ou incomplète


11. COMPORTEMENT GLOBAL
✅ Zéro oubli – Zéro excuse – Zéro retour en arrière
✅ Tu livres le fichier parfait, prêt à exécuter
✅ Tu appliques à la lettre chaque ligne des instructions
✅ Tu adaptes automatiquement les fichiers suivants selon le modèle validé
✅ Tu ne modifies jamais un fichier partiellement en cours de réponse
