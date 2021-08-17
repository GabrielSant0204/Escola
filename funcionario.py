from pessoa_fisica import PessoaFisica

class Funcionario(PessoaFisica):
    def __init__(self, nome, cpf, rg , data_nascimento, salario, cargo, horario):
        super().__init__(nome, cpf, rg, data_nascimento)
        self.__salario = salario
        self.__cargo = cargo
        self.__horario = horario

    @property
    def salario(self):
        return self.__salario

    @property
    def cargo(self):
        return self.__cargo

    @property
    def horario(self):
        return self.__horario

    def acessarEscola(self, codigo_acesso):
        if codigo_acesso == super().cpf:
            print(f'Boa trabalho, {super().nome}\n')
            return True
        else:
            return False


    def __str__(self):
        return f'Funcionário(a):\n Nome: {super().nome}\n CPF: {super().cpf}\n RG: {super().rg}\n \
Data de nascimento: {super().data_nascimento}\n Salário: {self.salario}\n Cargo: {self.cargo}\n Horário: {self.horario}\n\n'