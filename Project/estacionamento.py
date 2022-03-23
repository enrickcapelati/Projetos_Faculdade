from carro import Carro


class Estacionamento:
    opcao = 0


    def menu():
        '''Imprime o menu ao usuário'''

        dialogo = f"""CATÁLOGO DE VEÍCULOS \n
[1] CADASTRAR NOVO VEICULO', {Estacionamento.vagas_livres()} vagas \n
[2] LISTAR VEICULOS \n
[3] PESQUISAR UM VEICULO \n
[4] MOSTRAR VEICULO A PARTIR DO ANO \n
[5] SAIR \n"""
        print(dialogo)


    def listar():
        '''Retorna os valores da lista para o usuário quando solicitado'''

        for l in Carro.lista:
            return l


    def buscar(chave, valor):
        '''Realiza busca de carros por modelo ou ano'''
        
        for l in Carro.lista:
            if vars(l)[chave] == valor:
                return l
            else:
                None


    def vagas_livres():
        '''Retorna a quantidade de vagas restantes para cadastro de carros'''

        valor_maximo_veiculos = 10
        return valor_maximo_veiculos-len(Carro.lista)        

