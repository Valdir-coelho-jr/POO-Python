# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo de Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo
# Geralmente é usada nas seguintes situações:
# - como um getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/executar ações ao obter um atributo
# Código Cliente - é o código que usa o seu código


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor


    @property
    def cor(self):
        print('PROPERTY')
        return self.cor_tinta


caneta = Caneta('Azul')
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)
print(caneta.cor)


"""
class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor

    def get_cor(self):
        print('GET COR!')
        return self.cor_tinta

caneta = Caneta('Azul')
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
print(caneta.get_cor())
"""
