from pessoa_fisica import PessoaFisica

class Professor(PessoaFisica):
    def __init__(self, nome, cpf, rg , data_nascimento, forcacao, tipo_vinculo):
        super().__init__(nome, cpf, rg, data_nascimento)
        self.__formacao = forcacao
        self.__tipo_vinculo = tipo_vinculo

    @property
    def formacao(self):
        return self.__formacao

    @property
    def tipo_vinculo(self):
        return self.__tipo_vinculo

    def __str__(self):
        return f'Professor: {super().nome}\nCPF: {super().cpf}\n RG: {super().rg}\n Data de nascimento: {super().data_nascimento}\n \
Formação: {self.formacao}\n Vínculo: {self.tipo_vinculo}\n\n'
