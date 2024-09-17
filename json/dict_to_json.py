import json

data = {
    "name": "John",
    "age": 30,
    "children": [
        {"name": "Jane", "age": 10},
        {"name": "Jack", "age": 8}
    ],
    "address": {
        "street": "123 Elm Street",
        "city": "Somewhere",
        "postal_code": "12345"
    },
    "phone_numbers": ["123-456-7890", "987-654-3210"]
}

json_string = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)


print(json_string)

with open('./json/data.json', 'w') as file:
    json.dump(data, file, indent=4, sort_keys=True, ensure_ascii=False)
