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
class Vestibular:
    def __init__(self):
        self.lista_inscritos = ListaEncadeada()
        self.lista_funcionarios = ListaEncadeada()
        self.lista_aprovados = ListaEncadeada() # Nova lista para aprovados
        self.vagas_por_curso = 40 #
        self.candidatos_por_sala = 30 #

    # --- Métodos para Candidatos ---
    def realizar_inscricao(self, nome, cpf, curso, status):
        id_candidato = self.lista_inscritos.obter_tamanho() + 1
        novo_candidato = Candidato(id_candidato, nome, cpf, curso, status)
        self.lista_inscritos.inserir_no_final(novo_candidato)
        return id_candidato

    def listar_inscricoes(self):
        return str(self.lista_inscritos)
        
    def buscar_candidato_por_id(self, id_candidato):
        return self.lista_inscritos.buscar_por_id(id_candidato)

    def editar_candidato(self, candidato, campo, novo_valor):
        if campo == 'nome':
            candidato.nome = novo_valor
        elif campo == 'cpf':
            candidato.cpf = novo_valor
        elif campo == 'curso':
            candidato.curso = novo_valor
        elif campo == 'status':
            candidato.status = novo_valor
        else:
            return False
        return True

    # --- Métodos para Funcionários ---
    def cadastrar_funcionario(self, nome, cargo):
        novo_funcionario = Funcionario(nome, cargo)
        self.lista_funcionarios.inserir_no_final(novo_funcionario)

    def listar_funcionarios(self):
        return str(self.lista_funcionarios)

    # --- Métodos da Etapa "O Vestibular" ---
    def _obter_inscritos_efetivados(self):
        lista_efetivados = ListaEncadeada()
        no_atual = self.lista_inscritos.cabeca
        while no_atual:
            candidato = no_atual.dado
            if candidato.status == "PAGO":
                lista_efetivados.inserir_no_final(candidato)
            no_atual = no_atual.proximo
        return lista_efetivados

    def gerar_relatorio_de_salas(self):
        lista_efetivados = self._obter_inscritos_efetivados()
        total_candidatos = lista_efetivados.obter_tamanho()
        if total_candidatos == 0:
            return "Não há candidatos com inscrição efetivada para gerar o relatório de salas."
        salas_necessarias = math.ceil(total_candidatos / self.candidatos_por_sala) #
        relatorio = f"{'='*45}\n          Relatório de Distribuição de Salas\n{'='*45}"
        relatorio += f"\nTotal de candidatos que realizarão a prova: {total_candidatos}"
        relatorio += f"\nSalas necessárias ({self.candidatos_por_sala} candidatos por sala): {salas_necessarias}\n{'='*45}"
        no_sala = lista_efetivados.cabeca
        sala_atual, contador_sala = 1, 0
        while no_sala:
            if contador_sala == 0: relatorio += f"\n\n--- SALA {sala_atual} ---"
            relatorio += f"\n  - {no_sala.dado.nome}"
            contador_sala += 1
            if contador_sala == self.candidatos_por_sala:
                contador_sala, sala_atual = 0, sala_atual + 1
            no_sala = no_sala.proximo
        relatorio += f"\n{'='*45}"
        return relatorio

    def gerar_relacao_candidato_vaga(self): #
        lista_efetivados = self._obter_inscritos_efetivados()
        total_ia, total_esg = 0, 0
        no_total = self.lista_inscritos.cabeca
        while no_total:
            if no_total.dado.curso == "Inteligência Artificial": total_ia += 1
            else: total_esg += 1
            no_total = no_total.proximo
        efetivados_ia, efetivados_esg = 0, 0
        no_efetivado = lista_efetivados.cabeca
        while no_efetivado:
            if no_efetivado.dado.curso == "Inteligência Artificial": efetivados_ia += 1
            else: efetivados_esg += 1
            no_efetivado = no_efetivado.proximo
        relacao_total_ia = total_ia / self.vagas_por_curso if self.vagas_por_curso > 0 else 0
        relacao_total_esg = total_esg / self.vagas_por_curso if self.vagas_por_curso > 0 else 0
        relacao_efetivados_ia = efetivados_ia / self.vagas_por_curso if self.vagas_por_curso > 0 else 0
        relacao_efetivados_esg = efetivados_esg / self.vagas_por_curso if self.vagas_por_curso > 0 else 0
        relatorio = f"{'='*45}\n                 Relação Candidato/Vaga\n{'='*45}"
        relatorio += f"\n\nConsiderando TODAS as inscrições:"
        relatorio += f"\n  - Inteligência Artificial: {total_ia} inscritos | {relacao_total_ia:.2f} c/v."
        relatorio += f"\n  - Gestão ESG: {total_esg} inscritos | {relacao_total_esg:.2f} c/v."
        relatorio += f"\n\nConsiderando somente INSCRIÇÕES EFETIVADAS:"
        relatorio += f"\n  - Inteligência Artificial: {efetivados_ia} inscritos | {relacao_efetivados_ia:.2f} c/v."
        relatorio += f"\n  - Gestão ESG: {efetivados_esg} inscritos | {relacao_efetivados_esg:.2f} c/v."
        relatorio += f"\n{'='*45}"
        return relatorio
        
    # --- NOVOS MÉTODOS PARA APROVADOS ---
    def aprovar_candidato(self, candidato):
        """
        Aprova um candidato, verificando o limite de vagas e o status de pagamento.
        """
        if candidato.status != "PAGO":
            return "ERRO: O candidato precisa ter a inscrição efetivada (paga)."
            
        # Verifica se o candidato já foi aprovado
        no_aprovado = self.lista_aprovados.cabeca
        while no_aprovado:
            if no_aprovado.dado.cpf == candidato.cpf:
                return f"ERRO: O candidato {candidato.nome} já consta na lista de aprovados."
            no_aprovado = no_aprovado.proximo

        # Conta as vagas já preenchidas para o curso do candidato
        vagas_preenchidas = 0
        no_aprovado = self.lista_aprovados.cabeca
        while no_aprovado:
            if no_aprovado.dado.curso == candidato.curso:
                vagas_preenchidas += 1
            no_aprovado = no_aprovado.proximo
            
        if vagas_preenchidas >= self.vagas_por_curso: #
            return f"ERRO: O limite de {self.vagas_por_curso} vagas para o curso de {candidato.curso} foi atingido."

        # Se passar em todas as verificações, aprova o aluno
        novo_aprovado = AlunoAprovado(candidato.nome, candidato.cpf, candidato.curso) #
        self.lista_aprovados.inserir_no_final(novo_aprovado)
        return f"SUCESSO: Candidato {candidato.nome} aprovado em {candidato.curso}!"
        
    def listar_aprovados(self):
        """
        Retorna uma string formatada com a lista de todos os alunos aprovados.
        """
        if self.lista_aprovados.esta_vazia():
            return "Nenhum aluno aprovado até o momento."
            
        relatorio = f"{'='*45}\n                   Alunos Aprovados\n{'='*45}"
        
        # Filtra e lista por curso
        aprovados_ia = ""
        aprovados_esg = ""
        total_ia = 0
        total_esg = 0
        
        no_atual = self.lista_aprovados.cabeca
        while no_atual:
            aprovado = no_atual.dado
            if aprovado.curso == "Inteligência Artificial":
                aprovados_ia += f"\n{aprovado}"
                total_ia += 1
            else:
                aprovados_esg += f"\n{aprovado}"
                total_esg += 1
            no_atual = no_atual.proximo
            
        relatorio += f"\n\n--- Inteligência Artificial ({total_ia}/{self.vagas_por_curso} vagas) ---"
        relatorio += aprovados_ia if aprovados_ia else "\n  Nenhum aprovado neste curso."
        
        relatorio += f"\n\n--- Gestão ESG ({total_esg}/{self.vagas_por_curso} vagas) ---"
        relatorio += aprovados_esg if aprovados_esg else "\n  Nenhum aprovado neste curso."
        
        relatorio += f"\n{'='*45}"
        return relatorio
