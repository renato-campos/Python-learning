import jinja2
from datetime import datetime, timedelta

arquivo = "jinja2/header.html"
saida = "jinja2/saida.html"

with open(arquivo) as f:
    modelo = f.read()
    template = jinja2.Template(modelo)

inicio = datetime.now()
termino = inicio + timedelta(hours=12)
team = "Equipe 1"
header = template.render(inicio=inicio, fim=termino, equipe=team)
#print(header)

# Salvar o HTML em um arquivo
with open(saida, "w", encoding="utf8") as f:
    f.write(header)