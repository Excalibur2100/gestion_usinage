from sqlalchemy.orm import Session
from db.models.tables.log_securite import LogsSecurite

def creer_log_securite(db: Session, evenement: str, description: str, niveau: str = "INFO") -> LogsSecurite:
    """
    Crée un nouveau log de sécurité.
    """
    log = LogsSecurite(evenement=evenement, description=description, niveau=niveau)
    db.add(log)
    db.commit()
    db.refresh(log)
    return log

def get_tous_logs_securite(db: Session):
    """
    Récupère tous les logs de sécurité.
    """
    return db.query(LogsSecurite).all()

def get_log_securite_par_id(db: Session, log_id: int) -> LogsSecurite:
    """
    Récupère un log de sécurité par son ID.
    """
    return db.query(LogsSecurite).filter(LogsSecurite.id == log_id).first()

def supprimer_log_securite(db: Session, log_id: int) -> None:
    """
    Supprime un log de sécurité par son ID.
    """
    log = get_log_securite_par_id(db, log_id)
    if log:
        db.delete(log)
        db.commit()