from resolucao import caminho_arquivo, Pessoa, fazer_dump

import json

with open(caminho_arquivo, 'r') as arquivo:
    pessoas = json.load(arquivo)

    p1 = Pessoa(**pessoas[0])
    p2 = Pessoa(**pessoas[1])
    p3 = Pessoa(**pessoas[2])

    print(p1.nome, p1.idade)
    print(p2.nome, p1.idade)
    print(p3.nome, p1.idade)

print(__name__)
