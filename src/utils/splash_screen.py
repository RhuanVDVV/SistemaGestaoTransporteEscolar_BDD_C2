from conexion.oracle_queries import OracleQueries
from utils import config

class SplashScreen:

    def __init__(self):
        # Consultas de contagem de registros - inicio
        self.qry_total_escolas = config.QUERY_COUNT.format(tabela="escolas")
        self.qry_total_responsaveis = config.QUERY_COUNT.format(tabela="responsaveis")
        self.qry_total_alunos = config.QUERY_COUNT.format(tabela="alunos")
        self.qry_total_motoristas = config.QUERY_COUNT.format(tabela="motoristas")
        self.qry_total_peruas = config.QUERY_COUNT.format(tabela="peruas")
        # Consultas de contagem de registros - fim

        # Nome(s) do(s) criador(es)
        self.created_by = "Rhuan Vitor Pratti Peixoto, Werley Oliveria Gonçalves, Werliane Oliveira Gonçalves"
        self.professor = "Prof. M.Sc. Howard Roatti"
        self.disciplina = "Banco de Dados"
        self.semestre = "2023/2"

    def get_total_alunos(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_alunos)["total_alunos"].values[0]
    
    def get_total_responsaveis(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_responsaveis)["total_responsaveis"].values[0]
    
    def get_total_escolas(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_escolas)["total_escolas"].values[0]
    
    def get_total_motoristas(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_motoristas)["total_motoristas"].values[0]
    
    def get_total_peruas(self):
        oracle = OracleQueries()
        oracle.connect()
        return oracle.sqlToDataFrame(self.qry_total_peruas)["total_peruas"].values[0]
    
  
    def get_updated_screen(self):
        return f"""
        ########################################################
        #                   SISTEMA DE TRANSPORTE ESCOLAR                     
        #                                                         
        #  TOTAL DE REGISTROS:                                    
        #      1 - ESCOLAS:        {str(self.get_total_escolas()).rjust(5)}
        #      2 - ALUNOS:         {str(self.get_total_alunos()).rjust(5)}
        #      3 - RESPONSÁVEIS:   {str(self.get_total_responsaveis()).rjust(5)}
        #      4 - MOTORISTAS:     {str(self.get_total_motoristas()).rjust(5)}
        #      5 - PERUAS:         {str(self.get_total_peruas()).rjust(5)}
        #
        #  CRIADO POR: {self.created_by}
        #
        #  PROFESSOR:  {self.professor}
        #
        #  DISCIPLINA: {self.disciplina}
        #              {self.semestre}
        ########################################################
        """""