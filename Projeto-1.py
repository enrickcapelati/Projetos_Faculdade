opção = 0
class Carro:
    def __init__(self,marca,modelo,ano,placa):
        self.marca  = marca
        self.modelo = modelo
        self.ano    = ano
        self.placa  = placa

def user_input():        
    marca  = input('Digite a marca:')
    modelo = input('Digite o modelo:')
    ano    = input('Digite o ano: ')
    placa  = input('Digite a placa:') 

while opção != 5:
    print('''CADASTRO DE VEICULOS
[1] CADASTRAR NOVO VEICULO
[2] LISTAR VEICULOS
[3] PESQUISAR UM VEICULO
[4] MOSTRAR VEICULO A PARTIR DO ANO
[5] SAIR
''')
    opção = int(input('Digite sua opcao: '))
    if opção == 1:
        user_input()
        
    elif opção == 2:
        print('opcao 2')
        
    elif opção == 3:
        print('opcao 3')

    elif opção == 4:
        print('opcao 4')

    elif opção == 5:
        print('Finalizando...')

    else:
        print('Opção inválida tente novamente!')
    print('=-=' * 10)
print('Fim do programa!')