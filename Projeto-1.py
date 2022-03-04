opção = 0
carro=0
lista=[]


class Carro:

    def __init__(self,marca,modelo,ano,placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


    def __str__(self):

        '''Retorna os atributos do objeto em formato de dicionário'''

        return('=-=' * 10) + '\n' +  '\n' + '\n'.join(('{} = {}'
        .format(item, self.__dict__[item]) for item in self.__dict__)) + '\n' 


def menu():

    '''Imprime o menu ao usuário'''

    print('CATÁLOGO DE VEÍCULOS')
    print('[1] CADASTRAR NOVO VEICULO', f"({vagas_livres()} vagas)")
    print('[2] LISTAR VEICULOS')
    print('[3] PESQUISAR UM VEICULO')
    print('[4] MOSTRAR VEICULO A PARTIR DO ANO')
    print('[5] SAIR')


def user_input():     

    '''Recebe dados do usuário e atribui ás variaveis da classe Carro()'''

    marca = input('Digite a marca:').lower()
    modelo = input('Digite o modelo:').lower()
    ano = input('Digite o ano: ').lower()
    placa = input('Digite a placa:').lower() 
    global carro
    carro = Carro(marca,modelo,ano,placa)
    lista.append(carro)
 

def listar():

    '''Imprime os valores da lista para o usuário quando solicitado'''

    for l in lista:
        print(l)


def busca_modelo():

    '''Realiza busca de carros por modelo'''

    modelo = input ('Digite o modelo a ser pesquisado: ').lower()
    for l in lista:
        if l.modelo == modelo:
            print(l)
        else:
            print('Modelo não encontrado!')
            

def ano_busca():

    '''Realiza busca de carros a partir de um ano'''

    ano = input ('Digite o ano a ser pesquisado: ').lower()

    for l in lista:
        if l.ano >= ano:
            print(l)
        else:
            print('Não foram encontrados veiculos')
            continue


def vagas_livres():

    '''Retorna a quantidade de vagas restantes para cadastro de carros'''

    return 10-len(lista)        


while opção != 5:

    menu()

    opção = input('Digite sua opção: ')

    if opção == '1':

        if len(lista) <=10:
            user_input()

        else:
            print('O limite de cadastros é 10!')

    elif opção == '2':
        listar()

    elif opção == '3':
        busca_modelo()

    elif opção == '4':
        ano_busca()

    elif opção == '5':
        print('Finalizando...')

    else:
        print('Opção inválida tente novamente!')
    print('=-=' * 10)
    
print('Fim do programa!')