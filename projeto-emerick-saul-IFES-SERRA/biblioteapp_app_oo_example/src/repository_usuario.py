import sqlite3
from src.models import Usuario, Aluno, Professor

class UsuarioRepository:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self._create_table()

    def _connect(self):
        return sqlite3.connect(self.db_name)

    def _create_table(self):
        with self._connect() as con:
            con.execute("""
                CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    matricula TEXT,
                    matricula_professor TEXT
                )
            """)

    def add(self, usuario: Usuario):
        with self._connect() as con:
            if isinstance(usuario, Aluno):
                con.execute(
                    "INSERT INTO usuarios (nome, email, matricula) VALUES (?, ?, ?)",
                    (usuario.nome, usuario.email, usuario.matricula)
                )
            elif isinstance(usuario, Professor):
                con.execute(
                    "INSERT INTO usuarios (nome, email, matricula_professor) VALUES (?, ?, ?)",
                    (usuario.nome, usuario.email, usuario.matricula_professor)
                )
            else:
                con.execute(
                    "INSERT INTO usuarios (nome, email) VALUES (?, ?)",
                    (usuario.nome, usuario.email)
                )

    def get(self, user_id):
        with self._connect() as con:
            cur = con.execute(
                "SELECT id, nome, email, matricula, matricula_professor FROM usuarios WHERE id=?",
                (user_id,)
            )
            row = cur.fetchone()
            if not row:
                return None

            if row[3]:
                return Aluno(row[0], row[1], row[2], row[3])
            if row[4]:
                return Professor(row[0], row[1], row[2], row[4])
            return Usuario(row[0], row[1], row[2])

    def get_all(self):
        with self._connect() as con:
            cur = con.execute(
                "SELECT id, nome, email, matricula, matricula_professor FROM usuarios"
            )
            rows = cur.fetchall()
            usuarios = []
            for row in rows:
                if row[3]: usuarios.append(Aluno(row[0], row[1], row[2], row[3]))
                elif row[4]: usuarios.append(Professor(row[0], row[1], row[2], row[4]))
                else: usuarios.append(Usuario(row[0], row[1], row[2]))
            return usuarios
