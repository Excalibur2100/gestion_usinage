import requests

url = "http://127.0.0.1:8000/generate-code/"
data = {"task_description": "Créer un modèle CRUD pour une entité Produit avec SQLAlchemy"}
response = requests.post(url, json=data)
print(response.json())