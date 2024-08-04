from pathlib import Path
usuarios = Path(__file__).parent / 'usuarios.txt'

if not usuarios.exists():
    usuarios.touch()


def verificar_opcao(valor_opcao:int, qnt_opcao: int):
    while valor_opcao not in range(1, qnt_opcao+1):
        try:
            valor_opcao = int(input('Escolha uma opção válida: '))
        except ValueError:
            print('Valor inválido!')
    return valor_opcao


def isUsuarioExiste(cpf):
    with open(usuarios, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if cpf + '\n' == line:
                return True
        return False    
                 

def salvar_usuario(*dados):
    with open(usuarios, 'a', encoding='utf-8') as arquivo:
        for dado in dados:
            arquivo.write(str(dado) + '\n')


def localizarUsuario(cpf):
    with open(usuarios, 'r', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
        for index ,line in enumerate(dados):
            if cpf +'\n' == line:
                return index


def getDadosUsuario(indexUser):
    with open(usuarios, 'r', encoding='utf-8') as arquivo:
        dadosUser = {}
        dadosAll = arquivo.readlines()
        
        dadosUser['CPF'] = dadosAll[indexUser].replace('\n', '')
        dadosUser['Nome'] = dadosAll[indexUser + 1].replace('\n', '')
        dadosUser['Idade'] = dadosAll[indexUser + 2].replace('\n', '')
        dadosUser['Cidade'] = dadosAll[indexUser + 3].replace('\n', '')
        dadosUser['Sexo'] = dadosAll[indexUser + 4].replace('\n', '')
    return dadosUser    


def atualizar_usuario(indexUser, optionToUpdate, valueToUpdate):
    with open(usuarios, 'r+', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
        dados[indexUser+optionToUpdate] = str(valueToUpdate) + '\n'
    
    with open(usuarios, 'w', encoding='utf-8') as arquivo:
        arquivo.writelines(dados)


def deletar_usuario(indexUser):
    with open(usuarios, 'r+', encoding='utf-8') as arquivo:
        dados = arquivo.readlines()
    with open(usuarios, 'w', encoding='utf-8') as arquivo:
        for dado in dados:
            if dado == dados[indexUser]:
                for info in range(0, 5):
                    dados.pop(indexUser)
                break
        arquivo.writelines(dados)    

        
if __name__ == '__main__':
    pass
    