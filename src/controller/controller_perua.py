from model.peruas import Perua
from model.motoristas import Motorista
from conexion.oracle_queries import OracleQueries
from controller.controller_motorista import Controller_Motorista
from controller.controller_escola import Controller_Escola

class Controller_Perua:
    def __init__(self) -> None:
        self.ctrl_motorista = Controller_Motorista()


    def inserir_perua(self) -> Perua:
        oracle = OracleQueries()


        # Lista os motoristas existentes para inserir nas peruas
        self.listar_motoristas(oracle, need_connect=True)
        cnpj = str(input("Entre com o CNPJ do Motorista: "))
        motorista = self.valida_motorista(oracle,cnpj)
        if motorista == None:
            return None
        
        # SOlicita ao usuario a placa da Perua
        placa = str(input("Entre com a placa da Perua"))

        if self.verifica_existencia_perua(oracle,placa):

             # SOlicita ao usuario o modelo da Perua
            modelo = str(input("Entre com o modelo da Perua"))

            # SOlicita ao usuario a capacidade de pessoa na Perua
            capacidade = str(input("Entre com a capacidade de pessoas na Perua"))

            # Insere e persiste a nova Perua

            oracle.write(f"inser into peruas values ('{placa}', '{modelo}', '{capacidade}', '{motorista.get_CNPJ()}')")

            #Recupera os dados da nova Perua criada transformando em um Data Frame

            df_perua = oracle.sqlToDataFrame(f"select placa,modelo,capacidade, cnpj from peruas where placa = '{placa}'")

            #Cria um novo objeto de perua

            nova_perua = Perua(df_perua.placa.values[0], df_perua.modelo.values[0], df_perua.capacidade.values[0], motorista)


            # Exibe os atributos da nova Perua

            print(nova_perua.to_string())

            return nova_perua

        else:
            print(f"A Placa {placa} já está cadastrada")
            return None
        

    def atualizar_perua(self) -> Perua:

        oracle = OracleQueries(can_write=True)

        oracle.connect()

        placa = input("Placa da Perua que deseja atualizar: ")

        if not self.verifica_existencia_perua(oracle,placa):
            # Lista os motoristas existentes para inserir nas peruas
            self.listar_motoristas(oracle, need_connect=True)
            cnpj = str(input("Entre com o CNPJ do Motorista: "))
            motorista = self.valida_motorista(oracle,cnpj)
            if motorista == None:
                return None
            
            # Solicita ao usuario o novo modelo da Perua
            modelo = str(input("Entre com o modelo da Perua"))

            # Solicita ao usuario a nova capacidade de pessoa na Perua
            capacidade = str(input("Entre com a capacidade de pessoas na Perua"))
            #Atualiza os dados da perua existente
            oracle.write(f"update peruas set cnpj = '{cnpj}', modelo = '{modelo}', capacidade = '{capacidade}' where placa = {placa}")
            #Recupera os novos dados da perua transformando em um DataFrame

            df_perua = oracle.sqlToDataFrame(f"select placa,modelo, capacidade,cnpj where placa = {placa}")

            # cria um novo objeto perua 
            perua_atualizada = Perua(df_perua.placa.values[0], df_perua.modelo.values[0], df_perua.capacidade.values[0], motorista)

            print(perua_atualizada.to_string())

            return perua_atualizada
        
        else:
            print(f"A placa {placa} não nexiste")
            return None
        

    def excluir_perua(self):
        
        # Cria uma nova conexão com banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()


        # SOlicita ao usuário a placa da perua que deseja ser excluida
        placa = input("Placa da Perua que irá excluir: ")
        # verifica se existe a placa na base de dados
        if not self.verifica_existencia_perua(oracle,placa):
            # Recupera os dados da placa transformada em um dataFrame
            df_perua = oracle.sqlToDataFrame(f"select placa,modelo, capacidade,cnpj where placa = {placa}")

            motorista = self.valida_motorista(oracle, df_perua.cnpj.values[0])

            oracle.write(f"delete from peruas where placa = {placa}")
            perua_excluida = Perua(df_perua.placa.values[0], df_perua.modelo.values[0], df_perua.capacidade.values[0], motorista)
            print("Perua excluida com sucesso!")
            print(perua_excluida.to_string())

        else:
            print(f"A Perua de placa {placa} não existe")



    def verifica_existencia_perua(self, oracle:OracleQueries, placa:str = None) -> bool:
        df_perua = oracle.sqlToDataFrame(f"select placa,modelo, capacidade,cnpj where placa = {placa}")
        return df_perua.empty


    def listar_motoristas(self, oracle:OracleQueries, need_connect:bool=False):
        query = """
                select m.cnpj,
                m.nome,
                m.telefone,
                m.email,
                m.conta,
                m.codigo_escola
                from motoristas m 
                order by m.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))
        
    def valida_motorista(self, oracle:OracleQueries, cnpj:str = None) -> Motorista:
        if self.ctrl_motorista.verifica_existencia_motorista(oracle,cnpj):
            print(f"O CNPJ {cnpj} informado não existe na base de dados")
            return None
        else:
            oracle.connect()
            #Recupera os dados do motorista transfomando em data frame
            df_motorista = oracle.sqlToDataFrame(f"select cnpj, nome, telefone, email, conta, codigo_escola from motoristas where cnpj = {cnpj}")
            escola = self.ctrl_motorista.valida_escola(oracle, df_motorista.codigo_escola.values[0])

            #Cria um novo objeto de motorista
            motorista = Motorista(df_motorista.cnpj.values[0], df_motorista.nome.values[0], df_motorista.telefone.values[0], df_motorista.email.values[0], df_motorista.conta.values[0], escola)

            return motorista