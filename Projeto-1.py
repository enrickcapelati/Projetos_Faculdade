opção = 0
carro=0
class Carro:
    def __init__(self,marca,modelo,ano,placa):
        self.marca  = marca
        self.modelo = modelo
        self.ano    = ano
        self.placa  = placa
    def __str__(self):
        return  ('=-=' * 10) + '\n' +  '\n' + '\n'.join(('{} = {}'.format(item, self.__dict__[item]) for item in self.__dict__)) + '\n' 

lista=[]

def user_input():     
    marca  = input('Digite a marca:').lower()
    modelo = input('Digite o modelo:').lower()
    ano    = input('Digite o ano: ').lower()
    placa  = input('Digite a placa:').lower() 
    global carro
    carro  = Carro(marca,modelo,ano,placa)
    lista.append(carro)
 

def listar():
    for l in lista:
        print(l)

def busca_modelo():
    modelo = input ('Digite o modelo a ser pesquisado: ').lower()
    for l in lista:
        if l.modelo == modelo:
            print(l)
        else:
            print('Modelo não encontrado!')
            continue

def ano_busca():
    ano = input ('Digite o ano a ser pesquisado: ').lower()
    for l in lista:
        if l.ano >= ano:
            print(l)
        else:
            print('Não foram encontrados veiculos')
            continue
    
while opção != 5:
    print('''CADASTRO DE VEICULOS
[1] CADASTRAR NOVO VEICULO
[2] LISTAR VEICULOS
[3] PESQUISAR UM VEICULO
[4] MOSTRAR VEICULO A PARTIR DO ANO
[5] SAIR
''')
    opção = int(input('Digite sua opção: '))

    if opção == 1:
         user_input()
    elif opção == 2:
        listar()
    elif opção == 3:
        busca_modelo()
    elif opção == 4:
        ano_busca()
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida tente novamente!')
    print('=-=' * 10)
print('Fim do programa!')