# Arquivo: ListaEncadeada.py

class No:
    """
    Classe que representa um único nó em uma Lista Encadeada.
    """
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

    def __repr__(self):
        return str(self.dado)

class ListaEncadeada:
    """
    Classe que implementa a estrutura de dados Lista Encadeada Simples.
    """
    def __init__(self):
        self.cabeca = None
        self.tamanho = 0

    def __repr__(self):
        if self.esta_vazia():
            return "Nenhuma inscrição encontrada."
        
        nodes = []
        no_atual = self.cabeca
        while no_atual:
            # O __repr__ de cada objeto Candidato será chamado aqui
            nodes.append(str(no_atual.dado))
            no_atual = no_atual.proximo
        # Junta todos os __repr__ com uma quebra de linha
        return "\n".join(nodes)

    def esta_vazia(self):
        return self.cabeca is None

    def obter_tamanho(self):
        return self.tamanho

    def inserir_no_final(self, dado):
        novo_no = No(dado)
        if self.esta_vazia():
            self.cabeca = novo_no
        else:
            ultimo_no = self.cabeca
            while ultimo_no.proximo:
                ultimo_no = ultimo_no.proximo
            ultimo_no.proximo = novo_no
        self.tamanho += 1
        
    def buscar_por_cpf(self, cpf_procurado):
        """
        Busca por um objeto na lista que tenha um atributo 'cpf' correspondente.
        Retorna o DADO (o objeto inteiro) se encontrar, caso contrário, retorna None.
        """
        no_atual = self.cabeca
        while no_atual:
            if hasattr(no_atual.dado, 'cpf') and no_atual.dado.cpf == cpf_procurado:
                return no_atual.dado
            no_atual = no_atual.proximo
        return None

    # --- NOVO MÉTODO ADICIONADO PARA ATENDER AO PEDIDO ---
    def buscar_por_id(self, id_procurado):
        """
        Busca por um objeto na lista que tenha um atributo 'id' correspondente.
        Retorna o DADO (o objeto inteiro) se encontrar, caso contrário, retorna None.
        """
        no_atual = self.cabeca
        while no_atual:
            # hasattr verifica se o objeto tem o atributo 'id'
            if hasattr(no_atual.dado, 'id') and no_atual.dado.id == id_procurado:
                return no_atual.dado # Retorna o objeto encontrado
            no_atual = no_atual.proximo
        return None