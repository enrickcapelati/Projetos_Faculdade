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



class Estacionamento:
    __opcao = 0
    __lista = []


    def menu(self):
        '''Imprime o menu ao usuário'''

        dialogo = f"""CATÁLOGO DE VEÍCULOS \n
[1] CADASTRAR NOVO VEICULO', {self.vagas_livres()} vagas \n
[2] LISTAR VEICULOS \n
[3] PESQUISAR UM VEICULO \n
[4] MOSTRAR VEICULO A PARTIR DO ANO \n
[5] SAIR \n"""
        print(dialogo)


    def cadastro(self):     
        '''Recebe dados do usuário e atribui ás variaveis da classe Carro()'''

        marca = input('Digite a marca:').lower()
        modelo = input('Digite o modelo:').lower()
        ano = input('Digite o ano: ').lower()
        placa = input('Digite a placa:').lower() 
        carro = Carro(marca,modelo,ano,placa)
        self.__lista.append(carro)

    def listar(self):
        '''Retorna os valores da lista para o usuário quando solicitado'''

        for l in self.__lista:
            return l


    def buscar(self, chave, valor):
        '''Realiza busca de carros por modelo ou ano'''
        
        for l in self.__lista:
            if vars(l)[chave] == valor:
                return l
            else:
                None


    def vagas_livres(self):
        '''Retorna a quantidade de vagas restantes para cadastro de carros'''

        valor_maximo_veiculos = 10
        return valor_maximo_veiculos-len(self.__lista)        


    def main(self):
        '''Função principal'''

        while self.__opcao != 5:

            self.menu()

            self.__opcao = input('Digite sua opção: ')

            if self.__opcao == '1':

                if len(self.__lista) <=10:
                    self.cadastro()

                else:
                    print('O limite de cadastros é 10!')

            elif self.__opcao == '2':

                print(self.listar())

            elif self.__opcao == '3':

                modeloValor = input("Digite o modelo a ser pesquisado: ")
                print(self.buscar('modelo',modeloValor))

            elif self.__opcao == '4':

                anoValor = input("Digite o ano a ser pesquisado: ")
                print(self.buscar('ano', anoValor))

            elif self.__opcao == '5':

                print('Finalizando...')
                quit()

            else:
                print('Opção inválida tente novamente!')
            print('=-=' * 10)
