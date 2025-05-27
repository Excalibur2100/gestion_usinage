from typing import Optional
from datetime import timedelta
from sqlalchemy.orm import Session
from db.models.tables.production.piece import Piece
from backend.core.ia.chiffrage_data_service import ChiffrageDataService


class ChiffrageEngine:

    @staticmethod
    def chiffrage_complet(db: Session, piece_id: int, taux_marge: float = 15.0) -> dict:
        piece: Piece = db.query(Piece).filter(Piece.id == piece_id).first()
        if not piece:
            raise ValueError("Aucune opération ou pièce invalide.")

        duree_h = ChiffrageDataService.get_duree_totale(piece)
        cout_ht = ChiffrageDataService.get_cout_total_operations(piece)
        cout_ttc = ChiffrageEngine.calculer_cout_total(cout_ht, taux_marge)

        return {
            "piece": piece.nom,
            "matiere": piece.matiere,
            "quantite": piece.quantite,
            "duree_h": duree_h,
            "cout_ht": cout_ht,
            "marge": taux_marge,
            "cout_ttc": cout_ttc,
            "resume": ChiffrageEngine.generer_resume(str(piece.nom), duree_h, cout_ht, cout_ttc, taux_marge)
        }

    @staticmethod
    def calcul_complet(nb_operations: int, temps_moyen_op: float, cout_horaire: float,
                       marge: float = 0.0, description: str = "") -> dict:
        """
        Calcule un chiffrage brut (sans modèle), à partir du nombre d’opérations, temps et coût horaire.
        """
        duree_h = round((nb_operations * temps_moyen_op) / 60, 2)
        cout_ht = round(duree_h * cout_horaire, 2)
        cout_ttc = ChiffrageEngine.calculer_cout_total(cout_ht, marge)

        return {
            "nb_operations": nb_operations,
            "temps_moyen_op": temps_moyen_op,
            "duree_h": duree_h,
            "cout_ht": cout_ht,
            "marge": marge,
            "cout_ttc": cout_ttc,
            "resume": ChiffrageEngine.generer_resume(
                description or "Sans description", duree_h, cout_ht, cout_ttc, marge
            )
        }

    @staticmethod
    def calculer_cout_total(cout_ht: float, taux_marge: float = 0.0) -> float:
        """
        Calcule le coût total TTC à partir du HT et d'une marge.
        """
        marge = cout_ht * (taux_marge / 100)
        return round(cout_ht + marge, 2)

    @staticmethod
    def generer_resume(nom: str, duree: float, cout_ht: float, cout_ttc: float, marge: float) -> str:
        """
        Génère un texte résumant le chiffrage.
        """
        lignes = [
            f"Pièce : {nom}",
            f"Durée estimée : {duree} h",
            f"Coût HT : {cout_ht} €",
            f"Marge : {marge} %",
            f"Coût TTC : {cout_ttc} €"
        ]
        return "\n".join(lignes)