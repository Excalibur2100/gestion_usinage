import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.main import app
from backend.db.models.base import Base
from backend.dependencies import get_db

@pytest.fixture
def client():
    engine = create_engine("sqlite:///:memory:")
    TestingSessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)
    app.dependency_overrides[get_db] = lambda: TestingSessionLocal()
    with TestClient(app) as c:
        yield c

def test_create_and_get_avoir(client):
    response = client.post("/api/v1/avoirs-fournisseur/", json={
        "reference": "AVF-200",
        "reference_externe": None,
        "fournisseur_id": 1,
        "montant_ht": 100.0,
        "taux_tva": 20.0,
        "montant_ttc": 120.0,
        "motif": None
    })
    assert response.status_code == 200
    data = response.json()
    get_resp = client.get(f"/api/v1/avoirs-fournisseur/{data['id']}")
    assert get_resp.status_code == 200

def test_export_route(client):
    response = client.get("/api/v1/avoirs-fournisseur/export")
    assert response.status_code == 200
    assert response.headers["content-type"] == "text/csv"

def test_bulk_create_route(client):
    payload = {
        "avoirs": [
            {
                "reference": "AVF-BULK-1",
                "reference_externe": None,
                "fournisseur_id": 1,
                "montant_ht": 50.0,
                "taux_tva": 20.0,
                "montant_ttc": 60.0,
                "motif": None
            },
            {
                "reference": "AVF-BULK-2",
                "reference_externe": None,
                "fournisseur_id": 1,
                "montant_ht": 60.0,
                "taux_tva": 20.0,
                "montant_ttc": 72.0,
                "motif": None
            }
        ]
    }
    response = client.post("/api/v1/avoirs-fournisseur/bulk", json=payload)
    assert response.status_code == 200
    assert len(response.json()) == 2