import sys
import os

# 
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from fastapi.testclient import TestClient

# 
from src.main import app, format_and_validate_name

# 
client = TestClient(app)

# ----------------------------------------------------
# 1. Tests Unitaires de la Logique Pure
# ----------------------------------------------------

def test_validate_name_success():
    """Vérifie le formatage correct (Alice)."""
    assert format_and_validate_name("alice") == "Alice"

def test_validate_name_failure():
    """Vérifie l'exception pour une trop courte longueur."""
    with pytest.raises(ValueError) as excinfo:
        format_and_validate_name("a")
    assert "at least 3 characters" in str(excinfo.value)

# ----------------------------------------------------
# 2. Tests d'Intégration des Endpoints
# ----------------------------------------------------

def test_hello_endpoint_valid_input():
    """Teste l'endpoint /hello avec une entrée valide."""
    response = client.get("/hello/Dexter")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, Dexter!"}

def test_hello_endpoint_invalid_input():
    """Teste l'endpoint /hello avec une entrée non valide, vérifiant le message d'erreur."""
    response = client.get("/hello/D")
    assert response.status_code == 200
    assert "at least 3 characters" in response.json()["error"]

def test_status_endpoint():
    """Teste l'endpoint de statut (health check)."""
    response = client.get("/status")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"