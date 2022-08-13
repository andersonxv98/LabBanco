class DaoViewCliente:
    def __init__(self, conexao):
        super(DaoViewCliente, self).__init__()
        self.connexao = conexao

    def getClientes(self):
        print("entrou getClientes")
        query = "select * from viewCliente order by nome desc"
        print(query)
        mycursor = self.connexao.condb
        stmycursos = mycursor.cursor()

        try:
            stmycursos.execute(query)
            # s.commit()
            myresult = stmycursos.fetchall()
            print(myresult)
            return myresult
            # mycursor.execute(query)

        except:
            print("ERRO AO TENTAR CHAMAR query")
            return ("ERROR")



