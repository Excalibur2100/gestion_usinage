# filepath: /home/excalibur/gestion_usinage/scripts/create_missing_schemas.py

import os

schemas_path = "/home/excalibur/gestion_usinage/db/schemas/schemas.py"

schemas_to_add = {
    "SurveillanceCameraCreate": """
class SurveillanceCameraCreate(BaseModel):
    camera_id: int
    emplacement: str
    statut: str
""",
    "SurveillanceCameraRead": """
class SurveillanceCameraRead(BaseModel):
    id: int
    camera_id: int
    emplacement: str
    statut: str

    class Config:
        from_attributes = True
""",
}

if os.path.exists(schemas_path):
    with open(schemas_path, "r+") as f:
        content = f.read()
        for schema_name, schema_code in schemas_to_add.items():
            if schema_name not in content:
                f.write("\n" + schema_code)
                print(f"Ajouté : {schema_name}")
else:
    print(f"Le fichier {schemas_path} n'existe pas.")