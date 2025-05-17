| Module | Fichier | Description |
|--------|---------|-------------|
| achat | fournisseur.py | Fournisseur général avec toutes les relations intermodules |
| achat | commande_fournisseur.py | Commande globale à un fournisseur |
| achat | ligne_commande_fournisseur.py | Détail ligne par ligne de chaque commande |
| achat | reception.py | Réception physique des produits livrés |
| achat | facture_fournisseur.py | Facture fournisseur liée à une commande |
| achat | avoir_fournisseur.py | Avoir ou remboursement fournisseur |
| achat | evaluation_fournisseur.py | Évaluation qualité et délai fournisseur |
| achat | type_fournisseur.py | Catégories : matière, prestation, outillage |
| achat | suivi_reglement_fournisseur.py | Historique des paiements effectués |
| commercial | commande.py | Commande client validée issue d’un devis |
| commercial | ligne_commande.py | Lignes détaillées de chaque commande client |
| commercial | remise_client.py | Gestion des remises client |
| commercial | condition_paiement.py | Conditions commerciales appliquées |
| commercial | portefeuille_client.py | Suivi commercial par commercial ou secteur |
| commercial | historique_prix_client.py | Historique des tarifs négociés |
| config | parametre_systeme.py | Paramètres globaux du logiciel |
| config | config_metier.py | Configuration personnalisée métier |
| config | config_notification.py | Notification email/système activées |
| config | config_monnaie.py | Monnaie par défaut, taux de change |
| config | config_langue.py | Langues et traductions activées |
| config | config_tva.py | Règles de TVA par pays ou client |
| crm | client.py | Client enregistré |
| crm | contact_client.py | Personnes de contact liées au client |
| crm | adresse_client.py | Adresse principale ou de livraison |
| crm | opportunite.py | Prospection ou offre en cours |
| crm | fichier_client.py | GED client (contrats, courriers) |
| crm | relance.py | Relances automatiques ou manuelles |
| crm | historique_client.py | Historique des interactions |
| crm | tag.py | Tags génériques |
| crm | tag_client.py | Association de tags aux clients |
| entreprise | entreprise.py | Entité juridique de type société |
| entreprise | site.py | Sites physiques ou ateliers d'une entreprise |
| entreprise | utilisateur_site.py | Liaison utilisateur ↔ site |
| entreprise | profil_acces.py | Gestion des profils ERP multi-entreprises |
| entreprise | preference_entreprise.py | Logo, thème, TVA... |
| entreprise | parametrage_interne.py | Activation de modules par entité |
| finance | facture.py | Facture client |
| finance | ligne_facture.py | Lignes d’une facture client |
| finance | reglement.py | Règlement reçu ou à effectuer |
| finance | paiement.py | Paiement en attente, partiel ou complet |
| finance | journal_comptable.py | Export comptable SAGE/CEGID |
| finance | devis.py | Devis client |
| finance | ligne_devis.py | Détail de chaque ligne de devis |
| finance | commission.py | Commissions commerciales |
| finance | config_marge.py | Marge produit/service |
| finance | config_paiement.py | Modes de paiement |
| finance | aide_calcul_tva.py | Utilitaire de calcul |
| finance | export_comptable.py | Exports mensuels ou annuels |
| ged | document_qualite.py | Doc ISO, process, consignes |
| ged | documents_qhse.py | Fiches sécurité, fiches EPI... |
| ged | documents_reglementaires.py | Certificats, attestations légales |
| ged | documents_rh.py | Documents RH (CV, contrats...) |
| ged | signature_document.py | Signatures électroniques |
| ged | version_document.py | Historique de modification |
| ged | workflow_document.py | Cycle de validation des documents |
| ged | autorisation_document.py | Permissions d'accès GED |
| ia | analyse_fichier.py | Analyse fichiers G-code/STL... |
| ia | chiffrage.py | Estimation automatique d’un coût de pièce |
| ia | conditions_coupe.py | Paramètres d’usinage IA |
| ia | historique_chiffrage.py | Historique des simulations |
| ia | simulation_chiffrage.py | Résultat estimé en production |
| ia | suggestion_outil.py | Recommandations outils/coupes |
| ia | logs_ia.py | Logs d'activité IA |
| ia | assistant_ia.py | Copilote IA |
| ia | optimisation_production_ai.py | Optimisation automatique du cycle machine |
| ia | prediction_maintenance_ai.py | Panne prédite via IA |
| ia | reconnaissance_vocale.py | Dictée vocale / transcription |
| ia | code_generator.py | Générateur automatique de code |
| logistique | reception.py | Réception de livraison |
| logistique | expedition.py | Expédition client ou sous-traitant |
| logistique | transport.py | Transport interne ou externe |
| logistique | conditionnement.py | Méthodes de conditionnement |
| logistique | bordereau_livraison.py | Document de livraison |
| logistique | planning_livraison.py | Planification des envois |
| logistique | suivi_colis.py | Suivi d’expédition |
| maintenance | maintenance.py | Tâche de maintenance générique |
| maintenance | maintenance_preventive.py | Maintenance planifiée |
| maintenance | maintenance_corrective.py | Maintenance curative / panne |
| maintenance | intervention_maintenance.py | Opération détaillée sur machine |
| maintenance | historique_intervention.py | Historique machine / opération |
| maintenance | plan_maintenance.py | Planning des maintenances préventives |
| maintenance | demande_intervention.py | Demande soumise par utilisateur |
| maintenance | document_maintenance.py | Fiches machine ou checklists |
| maintenance | fournisseur_maintenance.py | Prestataires externes |
| maintenance | statut_intervention.py | Statuts des interventions |
| maintenance | type_intervention.py | Catégorie : curatif, préventif... |
| planning | planning_machine.py | Planification machine par OF |
| planning | planning_employe.py | Plan de charge RH |
| planning | affectation_machine.py | Affectation machine ↔ poste / OF |
| planning | heures_travaillees.py | Suivi des heures réelles |
| planning | pointages.py | Badgeuses et suivi poste |
| planning | calendrier_ferie.py | Jours fériés et arrêts |
| planning | conges.py | Congés planifiés |
| planning | planification_outil.py | Outils réservés à un poste |
| planning | rapport_poste.py | Rapport journalier poste |
