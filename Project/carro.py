class Carro:


    lista = []


    def __init__(self,marca,modelo,ano,placa):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa


    def __str__(self):

        '''Retorna os atributos do objeto em formato de dicionário'''

        return('=-=' * 10) + '\n' +  '\n' + '\n'.join(('{} = {}'
        .format(item, self.__dict__[item]) for item in self.__dict__)) + '\n' 


    def cadastro():     
        '''Recebe dados do usuário e atribui ás variaveis da classe'''
        marca = ''
        while (marca == ''):
            marca = input('Digite a marca:').lower()
        modelo = ''
        while (modelo == ''):
            modelo = input('Digite o modelo:').lower()
        ano = ''
        while (ano == ''):
            ano = input('Digite o ano: ').lower()
        placa = ''
        while (placa == ''):
            placa = input('Digite a placa:').lower() 
        carro = Carro(marca,modelo,ano,placa)
        Carro.lista.append(carro)

   