from sqlalchemy.orm import Session
from db.models.tables.ia.chiffrage_piece import ChiffragePiece
from db.models.tables.ia.chiffrage_operation import ChiffrageOperation
from db.models.tables.ia.chiffrage_machine import ChiffrageMachine
from typing import Optional

class ChiffrageDataService:

    @staticmethod
    def get_piece_complete(db: Session, piece_id: int) -> Optional[ChiffragePiece]:
        """
        Récupère une pièce avec ses opérations et machines liées.
        """
        return (
            db.query(ChiffragePiece)
            .filter(ChiffragePiece.id == piece_id)
            .first()
        )

    @staticmethod
    def get_cout_total_machine(operation: ChiffrageOperation) -> float:
        """
        Calcule le coût machine d'une opération en fonction du temps et de la machine associée.
        """
        if operation.machine and operation.machine.cout_horaire:
            temps_h = operation.temps_minute / 60
            return round(temps_h * operation.machine.cout_horaire, 2)
        return 0.0

    @staticmethod
    def get_cout_total_operations(piece: ChiffragePiece) -> float:
        """
        Calcule le coût machine cumulé de toutes les opérations d'une pièce.
        """
        total = 0.0
        for op in piece.operations:
            total += ChiffrageDataService.get_cout_total_machine(op)
        return round(total, 2)

    @staticmethod
    def get_duree_totale(piece: ChiffragePiece) -> float:
        """
        Calcule la durée totale d'usinage (en heures) pour une pièce.
        """
        total_minutes = sum([op.temps_minute for op in piece.operations])
        return round(total_minutes / 60, 2)