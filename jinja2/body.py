import jinja2
import json
from datetime import datetime
import pyodbc
import os
from dotenv import load_dotenv

# Carregar variáveis de ambiente
load_dotenv()


def connect(driver='{ODBC Driver 18 for SQL Server}'):
    """
    Connects to a SQL Server database and returns a connection object.

    Args:
        driver (str, optional): The ODBC driver to use. Defaults to '{ODBC Driver 18 for SQL Server}'.

    Returns:
        pyodbc.Connection: A connection object to the SQL Server database.
        or
        None: If a connection error occurs.
    """
    # Obter variáveis de ambiente
    driver   = os.getenv('DB_DRIVER')
    server   = os.getenv('DB_SERVER')
    database = os.getenv('DB_DATABASE')
    username = os.getenv('DB_USERNAME')
    password = os.getenv('DB_PASSWORD')
    
    if not all([server, database, username, password]):
        print("Error: Missing database credentials in .env file.")
        return None
    
    try:
        connection_string = (
            r'DRIVER=' + driver + ';'
            r'SERVER=' + server + ';'
            r'DATABASE=' + database + ';'
            r'UID=' + username + ';'
            r'PWD=' + password + ';'
        )
        conn = pyodbc.connect(connection_string)
        print("Connected to SQL Server successfully!")
        return conn
    except pyodbc.Error as ex:
        sqlstate = ex.args[0]
        print(f"Error connecting to SQL Server: {sqlstate}")
        return None


def close(conn):
    """
    Closes the connection to the SQL Server database.

    Args:
        conn (pyodbc.Connection): A connection object to the SQL Server database.
    """
    if conn:
        try:
            conn.close()
            print("Connection to SQL Server closed successfully!")
        except pyodbc.Error as ex:
            sqlstate = ex.args[0]
            print(f"Error closing connection to SQL Server: {sqlstate}")
    else:
        print("No connection to close.")

def query_boletim(conn, boletim):
    
    
    
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

