
class Clientes():
    def __init__(self, codigo, nome, cidade, estado):
        super(Clientes, self).__init__()
        self.codigo = codigo
        self.nome = nome
        self.cidade = cidade
        self.estado = estado

    def getNome(self):
        return self.nome

    def getCidade(self):
        return self.cidade

    def getCodigo(self):
        return self.codigo

    def getEstado(self):
        return self.estado