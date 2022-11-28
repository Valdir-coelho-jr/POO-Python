# Atributos de classe

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def data_de_nascimento(self):
        return Pessoa.ano_atual - self.idade


p1 = Pessoa('Rogério', 28)
print(p1.data_de_nascimento())

print(Pessoa.ano_atual)

p2 = Pessoa('Rafaela', 23)
print(p2.data_de_nascimento())
