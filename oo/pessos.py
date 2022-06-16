class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    taylor = Pessoa(nome='Taylor')
    miguel = Pessoa(nome='Miguel')
    thiago = Pessoa(taylor, miguel, nome='Thiago Teixeira')
    #print(Pessoa.cumprimentar(thiago))
    #print(id(thiago))
    #print(thiago.cumprimentar())
    print(thiago.nome)
    print(thiago.idade)
    for filho in thiago.filhos:
        print(filho.nome)
