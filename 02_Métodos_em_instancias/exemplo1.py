# Métodos em instâncias de classe Python
# Hard Coded - É algo que foi escrito diretamente no código
# Self é uma convenção, ou seja, pode ser qualquer nome, mas o primeiro parâmetro
# Como Self é por pura conveniência
# Classe - Molde (Geralmente sem dados)
# Instância da class (objeto) - Tem os dados
# Uma classe pode gerar várias instâncias.
# Na classe o self é a própria instância.

class Carro:
    def __init__(self, nome ):
        self.nome = nome  # Não é mais Hard coded
#       self.nome = 'Fusca'  # Hard Coded

    def acelerar(self):
        print(f'{self.nome} está acelerando . . .')


fusca = Carro('fusca')
print(fusca.nome)
fusca.acelerar()


celta = Carro('celta')
print(celta.nome)
celta.acelerar()
