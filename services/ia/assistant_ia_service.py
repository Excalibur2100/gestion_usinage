# services/ia/assistant_ia_service.py

from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
import random

# Simule une IA métier (ça évoluera)
class IAResponse(BaseModel):
    message: str
    suggestion_code: Optional[str] = None
    impact: Optional[str] = None
    created_at: datetime = datetime.utcnow()


def analyse_module_status(modules_actifs: List[str]) -> IAResponse:
    manquants = {"controleur", "service", "schema", "vue"}
    suggestions = []

    for module in modules_actifs:
        missing_parts = manquants - set(module.get("elements", []))
        if missing_parts:
            suggestions.append(f"Module '{module['nom']}' : il manque {', '.join(missing_parts)}.")

    if suggestions:
        return IAResponse(
            message="Des éléments manquent dans certains modules.",
            suggestion_code="\n".join(suggestions),
            impact="Certains modules ne fonctionneront pas correctement sans ces composants."
        )

    return IAResponse(message="Tous les modules sont complets et bien structurés.")