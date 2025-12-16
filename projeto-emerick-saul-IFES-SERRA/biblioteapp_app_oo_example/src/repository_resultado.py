import sqlite3
from src.models import Resultado

class ResultadoRepository:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS resultados (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    aluno_id INTEGER,
                    nome_datapoint TEXT,
                    tempo TEXT,
                    valor TEXT,
                    processado TEXT,
                    comentario TEXT
                )
            """)

    def add_csv(self, aluno_id, lista_resultados):
        with self._connect() as con:
            for r in lista_resultados:
                con.execute(
                    "INSERT INTO resultados (aluno_id, nome_datapoint, tempo, valor, processado, comentario) VALUES (?, ?, ?, ?, ?, ?)",
                    (aluno_id, r["Nome do data point"], r["Tempo"], r["Valor"], r["Processado"], r["Comentário"])
                )

    def get_by_professor(self):
        with self._connect() as con:
            cur = con.execute("SELECT * FROM resultados")
            return cur.fetchall()

    def get_by_aluno(self, aluno_id):
        with self._connect() as con:
            cur = con.execute("SELECT * FROM resultados WHERE aluno_id=?", (aluno_id,))
            return cur.fetchall()
