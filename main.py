import django


class Cliente:

    def __init__(self, nome, cpf, plano):
        self.nome = nome
        self.cpf = cpf
        self.plano = plano

    def setNome(self):
        Cliente.nome = self
        return 0

    def getNome():
        nome = Cliente.nome
        return nome


# noinspection PyTypeChecker
Cliente.setNome('Carlos')
print(Cliente.getNome())
