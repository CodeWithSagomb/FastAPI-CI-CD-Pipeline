from fastapi import FastAPI

app = FastAPI(title="CI/CD Demo API")

# Logique métier : valide un nom et le formate
def format_and_validate_name(name: str):
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long.")
    return name.title()

@app.get("/hello/{name}")
def read_hello(name: str):
    """Endpoint principal qui utilise la logique de validation."""
    try:
        validated_name = format_and_validate_name(name)
        return {"message": f"Hello, {validated_name}!"}
    except ValueError as e:
        # Retourne une erreur 200 avec un message d'erreur (pour la démonstration)
        return {"error": str(e)}

@app.get("/status")
def get_status():
    """Endpoint de santé (Health Check)."""
    return {"status": "OK", "version": "1.0"}