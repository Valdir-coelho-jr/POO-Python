import json


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade


dados = {'nome': 'Japinha', 'idade': 17}

p1 = Pessoa(**dados)

print(vars(p1))

dados_json = json.dumps(dados, indent=True)

with open('abc.json', 'w+') as file:
    file.write(dados_json)
