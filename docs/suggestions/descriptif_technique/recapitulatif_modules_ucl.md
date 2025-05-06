🌐 NOM DU LOGICIEL

UCL (Usinage Central Logiciel)

📄 STRUCTURE GLOBALE DU LOGICIEL

🔹 1. MODULE UTILISATEURS & AUTHENTIFICATION

Gestion des comptes (nom, email, mot de passe, rôle, actif)

Rôles définis : Admin, Responsable prod, Opérateur, RH, Client, IA

Authentification sécurisée (JWT ou session)

Droits d’accès à tous les modules via "gestion_acces"

🔹 2. MODULE CLIENTS & FOURNISSEURS

CRUD complet des clients

Données : nom, SIRET, tva, email, site web, secteur, commentaire

CRUD fournisseurs + évaluations & catalogue

🔹 3. MODULE DEVIS & COMMANDES

Génération de devis automatique (via analyse PDF)

Statut : brouillon, validé, refusé

Conversion devis → commande (en cours, livrée)

Lien vers client & factures

🔹 4. MODULE FACTURATION

Factures avec lignes de facturation

Calculs automatiques

Suivi des paiements (payée, validée, annulée)

🔹 5. MODULE CHIFFRAGE AUTOMATIQUE (IA)

Lecture PDF (plans pièces, tolérances, matières)

Extraction données tech : dimensions, matière, opérations

Calcul : matière, outils, temps, perso, marge

Devis client (PDF propre)

Visualisation interne des coûts

Validation avant lancement

🔹 6. MODULE PIÈCES & GAMMES DE PRODUCTION

CRUD pièces (liées aux clients)

Gammes avec opérations (temps estimé, machine, outil)

Association à plans, programme CFAO, outils

🔹 7. MODULE PROGRAMMES MACHINE / CFAO

Post-processeurs définis (SolidCAM, TopSolid, etc.)

Upload programme .nc / .gcode

Liens à pièce + gamme

🔹 8. MODULE MACHINES & OUTILS

CRUD machines (CNC, fraiseuse, imprimante 3D, etc.)

Liées aux programmes, gammes, planning

Outillage : CRUD outils + affectation machine

Etat, stock, fournisseurs

🔹 9. MODULE PLANIFICATION & CHARGES

Planning opérateur + machine

Affectation automatique ou manuelle

Optimisation IA possible (en attente)

Charge machine / poste

🔹 10. MODULE EMPLOYÉS & RH

CRUD employés (données RH complètes)

Absences, formations, entretiens, sanctions

Notation RH, docs RH

Accès restreint selon rôle

🔹 11. MODULE QHSE & DOCUMENTS

Documents QHSE, réglementaires, qualité

Archivage, statut actif/archivé

Gestion des EPI & affectation

🔹 12. MODULE CONTRÔLE & NON-CONFORMITÉS

Contrôles de pièces via instruments

Notation : conforme / non conforme

Non-conformités : cause, action corrective, IA possible

🔹 13. MODULE TRACABILITÉ

Historique de chaque pièce

Opération effectuée, utilisateur, date

Lien à gamme, programme, production

🔹 14. MODULE FINANCES

Transactions : dépenses, revenus, salaires, achats

Affectation à projet, pièce, fournisseur

Statistiques financières + analyses

🔹 15. MODULE IA & ANALYSE INTELLIGENTE

IA de lecture (PDF, code G, etc.)

IA future : suggestion gamme / opération

Logs IA + scores de confiance

🔹 16. MODULE SÉCURITÉ & SURVEILLANCE

Logs sécurité : actions utilisateurs

Caméras de surveillance

IA sécurité future : détection comportements anormaux

🔹 17. MODULE QR CODES / IDENTIFICATION

Génération QR codes pour pièces, outils, machines

Scan en atelier pour consultation rapide

🔹 18. MODULE STATISTIQUES GLOBALES

Production, RH, finance, machine

Vue mensuelle, annuelle

Filtrage par client, utilisateur, machine

🔹 CONCLUSION

Ce fichier constitue la base de documentation officielle du logiciel. Il sera utilisé pour la planification des développements, le suivi et la validation.

✅ Suggestions pour le logiciel de gestion d’usinage
Module	Amélioration proposée
Stock	Intégration de caméras + IA pour mise à jour automatique du stock en temps réel. Possibilité de basculer en mode manuel à tout moment.
Chiffrage	Extraction automatique des données (dimensions, matériaux, tolérances…) depuis un fichier PDF pour générer un devis clair et complet.
Production	Création automatique des gammes de production à partir du chiffrage validé, jusqu’à l’envoi de la pièce.
IA	Analyse de données (maintenance, efficacité, qualité…) avec recommandations intelligentes + simulation de production.
Sécurité	Système de rôles avancé pour accès limité à certaines sections ou documents selon le poste ou les autorisations.

💡 Bonus / Inspiration HiPaas / Too Wee :

Supervision en temps réel avec dashboards par module (qualité, prod, RH…)

Recherche avancée avec filtrage multicritères (par pièce, outil, opérateur…)

Notification automatique (maintenance, rupture stock, dépassement de délai, anomalie qualité…)

Historique des actions utilisateur pour audit (type "log utilisateur")

IA de prédiction pour : délai livraison, charge machine, besoin d’achat