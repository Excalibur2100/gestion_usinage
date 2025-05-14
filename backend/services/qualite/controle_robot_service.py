from sqlalchemy.orm import Session
from typing import List, Optional
from db.models.tables.controle_robot import ControleRobot
from backend.db.schemas.controle_robot_schemas.controle_robot_schemas import ControleRobotCreate


# ========== CRÉATION ==========
def creer_controle_robot(db: Session, data: ControleRobotCreate) -> ControleRobot:
    controle = ControleRobot(**data.model_dump())
    db.add(controle)
    db.commit()
    db.refresh(controle)
    return controle


# ========== LECTURE ==========

def get_tous_controles_robot(db: Session) -> List[ControleRobot]:
    return db.query(ControleRobot).all()


def get_controle_robot_par_id(db: Session, controle_id: int) -> Optional[ControleRobot]:
    return db.query(ControleRobot).filter(ControleRobot.id == controle_id).first()


# ========== MISE À JOUR ==========

def update_controle_robot(db: Session, controle_id: int, data: ControleRobotCreate) -> Optional[ControleRobot]:
    controle = get_controle_robot_par_id(db, controle_id)
    if controle:
        for key, value in data.model_dump().items():
            setattr(controle, key, value)
        db.commit()
        db.refresh(controle)
    return controle


# ========== SUPPRESSION ==========

def supprimer_controle_robot(db: Session, controle_id: int) -> None:
    controle = get_controle_robot_par_id(db, controle_id)
    if controle:
        db.delete(controle)
        db.commit()
