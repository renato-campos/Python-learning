import jinja2
import json
from datetime import datetime
import webbrowser

def converter_data(data_string):
    """Converte uma string de data e hora para um objeto datetime."""
    if data_string:
        try:
            return datetime.fromisoformat(data_string)
        except ValueError:
            # Tenta outro formato se o primeiro falhar
            try:
                return datetime.strptime(data_string, "%d/%m/%Y às %H:%M")
            except ValueError:
                return None
    return None

arquivo_modelo = "jinja2/body.html"
arquivo_dado = "jinja2/boletim.json"
saida = "jinja2/saida.html"

with open(arquivo_modelo) as f:
    template = jinja2.Template(f.read())

with open(arquivo_dado) as f:
    dados = json.load(f)

# Converter datas para objetos datetime
dados["data_inclusao"] = converter_data(dados["data_inclusao"])
dados["data_fato"] = converter_data(dados["data_fato"])
dados["data_comunicacao"] = converter_data(dados["data_comunicacao"])
for pessoa in dados.get("Pessoas Físicas", []):
    pessoa["data_nascimento"] = converter_data(pessoa.get("data_nascimento"))


#opcao = 1 #para testar o historico completo
opcao = 2 #para testar o historico resumido

body = template.render(dados=dados, opcao=opcao)

# Salvar o HTML em um arquivo
with open(saida, "a", encoding="utf-8") as f:
    f.write(body)

