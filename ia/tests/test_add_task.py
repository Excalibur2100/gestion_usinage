import requests

url = "http://127.0.0.1:8080/add-task/"  # Mettez à jour le port ici
data = {"task_description": "Créer un modèle CRUD pour une entité Produit avec SQLAlchemy"}
response = requests.post(url, json=data)

print(response.status_code)
print(response.json())