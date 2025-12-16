from src.repository_usuario import UsuarioRepository
from src.repository_resultado import ResultadoRepository
from src.models import Aluno, Professor

class UsuarioService:
    def __init__(self):
        self.repo = UsuarioRepository()

    def registrar_aluno(self, nome, email, matricula):
        aluno = Aluno(None, nome, email, matricula)
        self.repo.add(aluno)

    def registrar_professor(self, nome, email, matricula_professor):
        prof = Professor(None, nome, email, matricula_professor)
        self.repo.add(prof)

class ResultadoService:
    def __init__(self):
        self.repo = ResultadoRepository()

    def registrar_csv(self, aluno_id, resultados):
        self.repo.add_csv(aluno_id, resultados)
