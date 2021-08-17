from abc import ABCMeta, abstractmethod

class PessoaFisica(metaclass = ABCMeta):
    def __init__(self, nome, cpf, rg, data_nascimento):
        self.__nome = nome
        self.__cpf = cpf
        self.__rg = rg
        self.__data_nascimento = data_nascimento

    @abstractmethod
    def acessarEscola(self):
        pass

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def rg(self):
        return self.__rg

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @nome.setter
    def nome(self,novo_nome):
        self.__nome = novo_nome
        return self.__nome


    def __str__(self):
        pass




# pessoa1 = PessoaFisica('josé', 11122233344, 1231235,14)
# pessoa1.nome = 'ana'
# print(pessoa1.nome)