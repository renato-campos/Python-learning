import jinja2


modelo = "Olá {{nome}}! Seja bem-vindo ao Jinja2! Você mora em {{cidade}} e seu e-mail é {{email}}."
template = jinja2.Template(modelo)

dados = [
    {"nome": "João",
    "cidade": "São Paulo",
    "email": "joao@balbla.com.br"},
    {"nome": "Maria",
    "cidade": "Rio de Janeiro",
    "email": "maria@balbla.com.br"},
    {"nome": "José",
    "cidade": "Curitiba",
    "email": "jose@balbla.com.br"
    }
]


for dado in dados:
    mensagem = template.render(dado)
    print(mensagem)
    print()
