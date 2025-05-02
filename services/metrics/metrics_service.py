from sqlalchemy.orm import Session
from fastapi import HTTPException
from db.models.tables import MetricsMachine, Machine

def add_metric(db: Session, machine_id: int, temperature: float, vibration: float):
    # Vérifie si la machine existe
    machine = db.query(Machine).filter(Machine.id == machine_id).first()
    if not machine:
        raise HTTPException(status_code=400, detail="Machine not found")

    # Insère les métriques
    metric = MetricsMachine(
        machine_id=machine_id,
        temperature=temperature,
        vibration=vibration
    )
    db.add(metric)
    db.commit()
    db.refresh(metric)
    return metric