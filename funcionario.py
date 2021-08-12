from pessoa_fisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, rg , data_nascimento, salario, formacao, vinculo):
        super().__init__(nome, cpf, rg, data_nascimento)
        self.__salario = salario
        self.__formacao = formacao
        self.__vinculo = vinculo

    @property
    def salario(self):
        return self.__salario

    @property
    def formacao(self):
        return self.__formacao

    @property
    def vinculo(self):
        return self.__vinculo

    def __str__(self):
        return f'Funcionário(a):\n Nome: {super().nome}\n CPF: {super().cpf}\n RG: {super().rg}\n \
Data de nascimento: {super().data_nascimento}\n Salário: {self.salario}\n Formação: {self.formacao}\n Vínculo: {self.vinculo}\n\n'