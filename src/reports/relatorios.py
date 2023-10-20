from conexion.oracle_queries import OracleQueries

class Relatorio:
    def __init__(self):
        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_escolas_qtd_alunos.sql") as f:
            self.query_relatorio_escolas_qtd_alunos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_alunos.sql") as f:
            self.query_relatorio_alunos = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_escolas.sql") as f:
            self.query_relatorio_escolas = f.read()


        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_motoristas.sql") as f:
            self.query_relatorio_motoristas = f.read()

        # Abre o arquivo com a consulta e associa a um atributo da classe
        with open("sql/relatorio_peruas.sql") as f:
            self.query_relatorio_peruas = f.read()

        with open("sql/relatorio_responsaveis.sql") as f:
            self.query_relatorio_responsaveis = f.read()

    def get_relatorio_escolas_qtd_alunos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_escolas_qtd_alunos))
        input("Pressione Enter para Sair do Relatório de Escolas e respectivos Alunos")

    def get_relatorio_alunos(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_alunos))
        input("Pressione Enter para Sair do Relatório de Alunos")

    def get_relatorio_escolas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_escolas))
        input("Pressione Enter para Sair do Relatório de Escolas")



    def get_relatorio_motoristas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_motoristas))
        input("Pressione Enter para Sair do Relatório de Motoristas")

    def get_relatorio_peruas(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_peruas))
        input("Pressione Enter para Sair do Relatório de Peruas")
        
    def get_relatorio_responsaveis(self):
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries()
        oracle.connect()
        # Recupera os dados transformando em um DataFrame
        print(oracle.sqlToDataFrame(self.query_relatorio_responsaveis))
        input("Pressione Enter para Sair do Relatório de Responsaveis")