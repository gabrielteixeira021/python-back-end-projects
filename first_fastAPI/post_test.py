import requests

# URL da API
BASE_URL = "http://127.0.0.1:8000/items"

# Lista de itens de teste
test_items = [
    "Banana",
    "Maçã",
    "Laranja",
    "Abacaxi",
    "Manga",
    "Melancia",
    "Uva",
    "Pera",
    "Coco",
    "Morango",
]

for text in test_items:
    payload = {"text": text, "is_done": False}  # JSON esperado pela API
    response = requests.post(BASE_URL, json=payload)
    if response.status_code in {200, 201}:
        print(f"Criado: {response.json()}")
    else:
        print(f"Erro ao criar {text}: {response.status_code} {response.text}")
