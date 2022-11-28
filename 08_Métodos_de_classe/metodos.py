# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


    @classmethod
    def metodo_de_classe(cls):
        print('Hey!')


    @classmethod
    def encontra_idade(cls, nome):
        return cls(nome, 50)

    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('Japinha', 18)
p2 = Pessoa.encontra_idade('Maria')
p3 = Pessoa('Anônima', 28)
p4 = Pessoa.criar_sem_nome(18)

print(p2.nome, p2.idade)
print(p3.nome, p3.idade)
print(p4.nome, p4.idade)
