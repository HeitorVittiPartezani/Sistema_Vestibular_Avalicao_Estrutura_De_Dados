# Arquivo: main.py

from ClassLibrary import Vestibular

def linha():
    print("=" * 45)

# --- Início do Programa ---
vestibular_fatec = Vestibular()

# --- Loop do Menu Principal ---
while True:
    linha()
    print("                 Menu Principal")
    linha()
    print(" 1) Acessar Inscrições (Vestibulandos)")
    print(" 2) Acessar Cadastro (Funcionários)")
    print(" 3) Gerenciar Vestibular")
    print(" 4) Acessar Aprovados")
    print(" 5) Sair do Sistema")
    linha()
    
    opcao_menu = input(" Digite sua opção: ")

    # --- MÓDULO VESTIBULANDOS ---
    if opcao_menu == '1':
        while True:
            linha()
            print("         Sistema de Inscrição Vestibular")
            linha()
            print(" 1) Realizar Inscrição")
            print(" 2) Editar Cadastro")
            print(" 3) Listar Inscrições")
            print(" 4) Voltar ao Menu Principal")
            linha()
            
            opcao = input(" Digite sua opção: ")
            if opcao == '1':
                linha()
                print("           Realizando sua Inscrição")
                linha()
                nome = input(" Insira seu nome: ")
                
                # --- LÓGICA DE VALIDAÇÃO DO CPF ---
                while True:
                    cpf = input(" Insira seu CPF (apenas números): ")
                    if cpf.isdigit() and len(cpf) == 11:
                        break
                    else:
                        print("\n CPF inválido. Por favor, digite 11 números.")

                print("\n Cursos: 1) Inteligência Artificial | 2) Gestão ESG")
                curso = ""
                while curso == "":
                    opcao_curso = input(" Escolha o curso (1 ou 2): ")
                    if opcao_curso == '1': curso = "Inteligência Artificial"
                    elif opcao_curso == '2': curso = "Gestão ESG"
                    else: print(" Opção inválida.")
                status = ""
                while status not in ["PAGO", "PENDENTE"]:
                    pagou = input(" Pagar taxa de inscrição agora? (S/N): ").upper()
                    if pagou == 'S': status = "PAGO"
                    elif pagou == 'N': status = "PENDENTE"
                    else: print(" Opção inválida.")
                id_gerado = vestibular_fatec.realizar_inscricao(nome, cpf, curso, status)
                print(f"\n Inscrição realizada com sucesso! Seu ID é: {id_gerado}")

            elif opcao == '2':
                linha()
                print("               Editar Cadastro")
                linha()
                try:
                    id_busca = int(input(" Digite o ID da inscrição que deseja editar: "))
                except ValueError:
                    print("\n ID inválido. Por favor, digite um número.")
                    continue
                
                candidato_encontrado = vestibular_fatec.buscar_candidato_por_id(id_busca)

                if candidato_encontrado:
                    print("\nCandidato encontrado:")
                    print(candidato_encontrado)

                    print(" O que você deseja alterar?")
                    print(" 1) Nome")
                    print(" 2) CPF")
                    print(" 3) Curso")
                    print(" 4) Efetivar Pagamento da Inscrição")
                    print(" 5) Voltar")
                    
                    opcao_edicao = input(" Digite sua opção: ")

                    if opcao_edicao == '1':
                        novo_nome = input(" Digite o novo nome: ")
                        vestibular_fatec.editar_candidato(candidato_encontrado, 'nome', novo_nome)
                        print("\n Nome alterado com sucesso!")
                    elif opcao_edicao == '2':
                        # --- LÓGICA DE VALIDAÇÃO DO CPF (EDIÇÃO) ---
                        while True:
                            novo_cpf = input(" Digite o novo CPF (apenas números): ")
                            if novo_cpf.isdigit() and len(novo_cpf) == 11:
                                break
                            else:
                                print("\n CPF inválido. Por favor, digite 11 números.")
                        vestibular_fatec.editar_candidato(candidato_encontrado, 'cpf', novo_cpf)
                        print("\n CPF alterado com sucesso!")
                    elif opcao_edicao == '3':
                        print("\n Cursos: 1) Inteligência Artificial | 2) Gestão ESG")
                        novo_curso = ""
                        while novo_curso == "":
                            opcao_curso = input(" Escolha o novo curso (1 ou 2): ")
                            if opcao_curso == '1': novo_curso = "Inteligência Artificial"
                            elif opcao_curso == '2': novo_curso = "Gestão ESG"
                            else: print(" Opção inválida.")
                        vestibular_fatec.editar_candidato(candidato_encontrado, 'curso', novo_curso)
                        print("\n Curso alterado com sucesso!")
                    
                    elif opcao_edicao == '4':
                        if candidato_encontrado.status == "PENDENTE":
                            confirmar = input(" Confirmar pagamento da taxa de inscrição (S/N)? ").upper()
                            if confirmar == 'S':
                                vestibular_fatec.editar_candidato(candidato_encontrado, 'status', 'PAGO')
                                print("\n Pagamento efetivado com sucesso! A inscrição está confirmada.")
                            else:
                                print("\n Alteração cancelada.")
                        else:
                            print("\n Esta inscrição já está com o pagamento efetivado.")

                    elif opcao_edicao == '5':
                        pass
                    else:
                        print("\n Opção de edição inválida.")
                else:
                    print(f"\n Nenhuma inscrição encontrada com o ID {id_busca}.")

            elif opcao == '3':
                linha()
                print("          Lista de Candidatos Inscritos")
                linha()
                print(vestibular_fatec.listar_inscricoes())

            elif opcao == '4':
                print("\n Voltando ao menu principal...")
                break
            else:
                print("\n Opção inválida!")

    # --- MÓDULO FUNCIONÁRIOS ---
    elif opcao_menu == '2':
        while True:
            linha()
            print("         Sistema de Cadastro de Funcionários")
            linha()
            print(" 1) Realizar cadastro")
            print(" 2) Listar funcionários")
            print(" 3) Voltar ao Menu Principal")
            linha()
            
            opcao = input(" Digite sua opção: ")
            if opcao == '1':
                linha()
                print("            Cadastro de Funcionário")
                linha()
                nome = input(" Insira o nome do funcionário: ")
                cargo = input(" Insira o cargo do funcionário: ")
                vestibular_fatec.cadastrar_funcionario(nome, cargo)
                print("\n Funcionário cadastrado com sucesso!")

            elif opcao == '2':
                linha()
                print("           Lista de Funcionários")
                linha()
                print(vestibular_fatec.listar_funcionarios())

            elif opcao == '3':
                print("\n Voltando ao menu principal...")
                break
            else:
                print("\n Opção inválida!")

    # --- MÓDULO GERENCIAR VESTIBULAR ---
    elif opcao_menu == '3':
        while True:
            linha()
            print("            Gerenciamento do Vestibular")
            linha()
            print(" 1) Gerar Relatório de Salas")
            print(" 2) Gerar Relação Candidato/Vaga")
            print(" 3) Voltar ao Menu Principal")
            linha()

            opcao = input(" Digite sua opção: ")
            if opcao == '1':
                relatorio = vestibular_fatec.gerar_relatorio_de_salas()
                print(relatorio)
            elif opcao == '2':
                relatorio = vestibular_fatec.gerar_relacao_candidato_vaga()
                print(relatorio)
            elif opcao == '3':
                print("\n Voltando ao menu principal...")
                break
            else:
                print("\n Opção inválida!")
