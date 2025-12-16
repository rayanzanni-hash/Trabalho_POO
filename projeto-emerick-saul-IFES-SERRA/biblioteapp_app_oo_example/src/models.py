class Usuario:
    def __init__(self, id, nome, email):
        self.id = id
        self.nome = nome
        self.email = email

class Aluno(Usuario):
    def __init__(self, id, nome, email, matricula):
        super().__init__(id, nome, email)
        self.matricula = matricula

class Professor(Usuario):
    def __init__(self, id, nome, email, matricula_professor):
        super().__init__(id, nome, email)
        self.matricula_professor = matricula_professor

class Resultado:
    def __init__(self, id, aluno_id, nome_datapoint, tempo, valor, processado, comentario):
        self.id = id
        self.aluno_id = aluno_id
        self.nome_datapoint = nome_datapoint
        self.tempo = tempo
        self.valor = valor
        self.processado = processado
        self.comentario = comentario
