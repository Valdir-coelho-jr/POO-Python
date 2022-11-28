# class - Classes são moldes para criar novos objetos
# As classes geram novos objetos (instâncias) que
# podem ter seus próprios atributos e métodos.
# Os objetos gerados pela classe podem usar seus dados
# internos para realizar várias ações.
# Por convenção, usamos PascalCase para nomes de
# classes
# stromg = 'Luiz' # String
# print(string.upper())
# print(instance(string. str))

class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome


p1 = Pessoa('Rogério', 'Pigatto')
# p1.nome = 'Rogério'
# p1.sobrenome = 'Pigatto'

p2 = Pessoa('Japinha', 'Lokao')
# p2.nome = 'Japinha'
# p2.sobrenome = 'Lokao'

print(p1.nome)
print(p1.sobrenome)

print(p2.nome)
print(p2.sobrenome)
