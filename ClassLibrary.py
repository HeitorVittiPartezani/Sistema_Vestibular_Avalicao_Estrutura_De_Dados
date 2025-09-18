# Arquivo: ClassLibrary.py

from ListaEncadeada import ListaEncadeada
import math

class Candidato:
    def __init__(self, id, nome, cpf, curso, status):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
        self.status = status
        
    def __repr__(self):
        return (f"\n--- Inscrição Nº: {self.id} ---\n"
                f"  Nome: {self.nome}\n"
                f"  CPF: {self.cpf}\n"
                f"  Curso: {self.curso}\n"
                f"  Status Pagamento: {self.status}\n"
                f"---------------------------")
    
class AlunoAprovado:
    """
    Nova classe para representar os dados do aluno aprovado.
    """
    def __init__(self, nome, cpf, curso):
        self.nome = nome
        self.cpf = cpf
        self.curso = curso
    
    def __repr__(self):
        return (f"  - Nome: {self.nome} | CPF: {self.cpf} | Curso: {self.curso}")
    
class Funcionario:
    def __init__(self, nome, cargo):
        self.nome = nome
        self.cargo = cargo

    def __repr__(self):
        return f"  Nome: {self.nome} | Cargo: {self.cargo}"
