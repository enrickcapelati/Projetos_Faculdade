from estacionamento import Estacionamento
from carro import Carro


def main():
        '''Função principal'''

        while Estacionamento.opcao != 5:

            Estacionamento.menu()

            Estacionamento.opcao = input('Digite sua opção: ')

            if Estacionamento.opcao == '1':

                if len(Carro.lista) <=10:
                    Carro.cadastro()

                else:
                    print('O limite de cadastros é 10!')

            elif Estacionamento.opcao == '2':

                print(Estacionamento.listar())

            elif Estacionamento.opcao == '3':

                modeloValor = input("Digite o modelo a ser pesquisado: ")
                print(Estacionamento.buscar('modelo',modeloValor))

            elif Estacionamento.opcao == '4':

                anoValor = input("Digite o ano a ser pesquisado: ")
                print(Estacionamento.buscar('ano', anoValor))

            elif Estacionamento.opcao == '5':

                print('Finalizando...')
                quit()

            else:
                print('Opção inválida tente novamente!')
            print('=-=' * 10)



if __name__ == '__main__':
    main()