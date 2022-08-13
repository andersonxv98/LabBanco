import mysql.connector


class Conexao:
    def __init__(self):
        super().__init__()

        self.condb = self.Con()

    def Con(self):
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="estoque"
            )
            #print(mydb)

            print("Conectadopr com SUCESSO")
            return mydb

        except:
            print("ERRO AO CONECTAR")
            return