import json
from pprint import pprint


file_path = 'json/data.json'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    pprint(data, indent=4)
except FileNotFoundError:
    print(f"O arquivo {file_path} não foi encontrado.")
except json.JSONDecodeError as e:
    print(f"Erro ao decodificar JSON: {e}")