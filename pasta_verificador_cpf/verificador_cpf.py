from funcoes import *
from time import sleep
    
def menuPrincipal(modo:str):
    if modo == 'Formal':
        while True:
            main_menu_opcao = int(input('''
Escolha uma das opções abaixo:
[ 1 ] Cadastro 
[ 2 ] Login
[ 3 ] Sair                                                                                                                                        
--> '''))
            main_menu_opcao = verificar_opcao(main_menu_opcao, 3)
            print()

            if main_menu_opcao == 1:
                print('Bem vindo ao CADASTRO!')
                print('--'*20)
                sleep(1)

                cpf = input('Digite seu cpf: \n-->').strip()
                while len(cpf) != 11 or not cpf.isdigit():
                    cpf = input('Formato inválido!!! Digite novamente: \n-->').strip()

                while isUsuarioExiste(cpf):
                    cpf = input('CPF já cadastrado!!! Digite novamente: \n-->').strip()
                    while len(cpf) != 11 or not cpf.isdigit():
                        cpf = input('Formato inválido!!! Digite novamente: \n-->').strip()


                nome = input('Digite um nome de usuário: \n-->').strip()
          
                
                while True:
                    try: 
                        idade = int(input('Digite sua idade: \n-->'))
                        break
                    except ValueError:
                        print('Valor inválido!!')

                cidade = input('Qual a sua cidade? \n-->').strip()

                opcaoGenero = {1:'M', 2:'F', 3:'Prefiro não informar'}
                generoUsuario = verificar_opcao(int(input('Qual seu gênero? [1- M] [2- F] [3- Prefiro não informar] \n-->')), 3)

                salvar_usuario(cpf, nome, idade, cidade, opcaoGenero[generoUsuario])

            elif main_menu_opcao == 2:
                print('OLÁ! PARA FAZER LOGIN DIGITE SEU CPF LOGO ABAIXO:')
                loginCpf = input('--> ').strip()
                while len(loginCpf) != 11 or not loginCpf.isdigit():
                    loginCpf = input('Formato inválido!!! Digite novamente: \n-->').strip()

                while not isUsuarioExiste(loginCpf):
                    loginCpf = input('CPF NÃO EXISTE!!! Digite novamente: \n-->').strip()
                    while len(loginCpf) != 11 or not loginCpf.isdigit():
                        loginCpf = input('Formato inválido!!! Digite novamente: \n-->').strip()
                
                print('LOGIN FEITO COM SUCESSO!')

                while True:
                    print()
                    menuLogin = verificar_opcao(int(input('O que desejas fazer?\n\n [ 1 ] Informar Dados\n\n [ 2 ] Atualizar Dados\n\n [ 3 ] Deletar Usuário\n\n [ 4 ] Sair\n--> ')), 4)
                        
                    confirmacao = 0
                    match (menuLogin):
                        case 1:
                            print('Seus dados:\n')
                            dadosUsuario = getDadosUsuario(localizarUsuario(loginCpf))

                            for key, value in dadosUsuario.items():
                                print(f'{key}: {value}')
                                print('--'*12)
                            sleep(1)
                        case 2:
                            opcaoAtualizar = verificar_opcao(int(input('O que desejas atualizar? \n[ 1 ] Nome \n[ 2 ] Idade \n[ 3 ] Cidade \n[ 4 ] Gênero \n[ 5 ] Sair')), 5)
                            if opcaoAtualizar == 5:
                                break
                            elif opcaoAtualizar == 1:
                                atualizar = input('Digite o novo valor do campo nome: ').strip()
                            elif opcaoAtualizar == 2:
                                while True:
                                    try:
                                        atualizar = int(input('Digite o novo valor do campo idade: '))
                                        break
                                    except ValueError:
                                        print('Valor inválido!')
                            elif opcaoAtualizar == 3:
                                atualizar = input('Digite o novo valor do campo cidade: ').strip()

                            elif opcaoAtualizar == 4:
                                atualizar = input('Digite o novo valor do campo gênero')
                            atualizar_usuario(localizarUsuario(loginCpf), opcaoAtualizar, atualizar)

                        case 3:
                            confirmacao = verificar_opcao(int(input('Tem certeza que quer deletar este usuário? [ 1 ] Sim [ 2 ] Não\n-->')), 2)
                        case 4:
                            break

                    if confirmacao == 1:
                        deletar_usuario(localizarUsuario(loginCpf))
                        print('Usuario deletado com sucesso!\n')
                        break


            elif main_menu_opcao == 3:
                print('Programa FINALIZADO!')
                break


menuPrincipal('Formal')
