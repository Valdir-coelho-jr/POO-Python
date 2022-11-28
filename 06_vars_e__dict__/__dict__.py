# __dict__ e vars para atributos e instância

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.get_ano_nascimento - self.idade


dados = {'nome': 'João', 'idade': 35}
p1 = Pessoa(**dados)
# p1 = Pessoa('Rogério', 28)
# print(p1.nome, p1.idade)
# p1.nome = 'LUCIANO'
# del p1.nome
# p1.__dict__['outra'] = 'Coisa'
# p1.__dict__['nome'] = 'Etemon'
# del p1.__dict__['Nome']
# print(p1.__dict__)
# print(vars(p1))
# print(p1.outra)
# print(p1.nome)

print(vars(p1))
print(p1.nome)
