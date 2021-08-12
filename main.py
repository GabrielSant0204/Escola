from alunos import Aluno
from professor import Professor
from funcionario import Funcionario

aluno = Aluno('josé', '333.666.444.89', '987.456.489-8', '19/08/2003', '12332115', '3A', 'tarde')
print(aluno)

professor = Professor('Ana', '666.888.777.96', '555.888.444-3', '26/09/2000', 'Biologia', 'Formada')
print(professor)

funcionario = Funcionario('Maria', '222.333.444-89', '111.888.269.8','31/02/1999', 'R$1569,22', "Ens.Médio completo", 'concursada')
print(funcionario)