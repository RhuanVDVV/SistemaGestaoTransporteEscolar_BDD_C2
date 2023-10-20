from model.motoristas import Motorista
from controller.controller_escola import Controller_Escola
from conexion.oracle_queries import OracleQueries
from model.escolas import Escola

class Controller_Motorista:
    def __init__(self):
        self.ctrl_escola = Controller_Escola()



    def inserir_motorista(self) -> Motorista:
        oracle = OracleQueries()

        # Listar as escolas existentes para inserir nos motoristas

        self.listar_escolas(oracle, need_connect = True)

        codigo_escola = int(input("Entre com o Codigo da Escola: "))
        escola = self.valida_escola(oracle,codigo_escola)
        if escola == None:
            return None

        # Solicita  ao usuario o cnpj do Motorista
        cnpj = str(input("Entre com o CNPJ do Motorista: "))

        if self.verifica_existencia_motorista(oracle, cnpj):
            # solicita ao usuario o nome do Motorista
            nome = str(input("Entre com o nome do Motorista: "))
            #Solicita ao usuario o Telefone do Motorista
            telefone = str(input("Entre com o telefone do Motorista:"))
            #Solicita ao usuario o email do motorista
            email = str(input("Entre com o email do Motorista: "))
            #Solicita ao usuario a conta do motorista
            conta = str(input("Entre com a conta do Motorista"))
            #Insere e persite o novo motorista
            oracle.write(f"insert into motoristas values ('{cnpj}','{nome}', '{telefone}', '{email}', '{conta}', '{escola.get_codigo_escola()}' )")
            # Recupera os dados do Novo Motorista criado transformando em um data Frame
            df_motorista = oracle.sqlToDataFrame(f"select cnpj,nome, telefone, email, conta, codigo_escola from motoristas where cnpj = '{cnpj}' ")
            #Cria um novo objeto de motorista
            novo_motorista = Motorista(df_motorista.cnpj.values[0], df_motorista.nome.values[0], df_motorista.telefone.values[0], df_motorista.email.values[0], df_motorista.conta.values[0], escola)
            print(novo_motorista.to_string())
            return novo_motorista

        else:
            print(f"O CNPJ {cnpj} já está cadastrado")
            return None


    def atualizar_motorista(self) -> Motorista:
        oracle = OracleQueries(can_write = True)

        oracle.connect()
            
        cnpj = str(input("Entre com o CNPJ do motorista que irá alterar: "))

        if not self.verifica_existencia_motorista(oracle,cnpj):
            self.listar_escolas(oracle, need_connect = True)
            codigo_escola = int(input("Entre com o Codigo da Escola: "))
            escola = self.valida_escola(oracle,codigo_escola)
            if escola == None:
                return None
            
            # solicita ao usuario o nome do Motorista
            nome = str(input("Entre com o nome do Motorista: "))

            #Solicita ao usuario o Telefone do Motorista
            telefone = str(input("Entre com o telefone do Motorista:"))

            #Solicita ao usuario o email do motorista
            email = str(input("Entre com o email do Motorista: "))

            #Solicita ao usuario a conta do motorista
            conta = str(input("Entre com a conta do Motorista"))

            # Atualiza os dados do motorista existente
            oracle.write(f"update motoristas set nome = '{nome}', telefone = '{telefone}', email = '{email}' conta = '{conta}'  codigo_escola = '{escola.get_codigo_escola()}' where cnpj = {cnpj}")
            
            # Recupera os novos dados do motorista transformand oem um dataframe

            df_motorista = oracle.sqlToDataFrame(f"select cnpj,nome, telefone, email, conta, codigo_escola from motoristas where cnpj = '{cnpj}' ")

            #cria um novo objeto de motorista

            motorista_atualizado = Motorista(df_motorista.cnpj.values[0], df_motorista.nome.values[0], df_motorista.telefone.values[0], df_motorista.email.values[0], df_motorista.conta.values[0], escola)
            
            print(motorista_atualizado.to_string())

            return motorista_atualizado
        else:
            print(f"O CNPJ {cnpj} não existe")


    def excluir_motorista(self):
        oracle = OracleQueries(can_write= True)

        oracle.connect()

        cnpj = input("CNPJ do motorista que irá excluir: ")

        if not self.verifica_existencia_motorista(oracle, cnpj):
            opcao_excluir = str(input(f"Tem certeza que deseja excluir o Motorista de CNPJ {cnpj}? [S ou N]: ")).lower()

            if opcao_excluir == "s":
                print("Caso o Motorista possua peruas estas também serão excluídas!")
                opcao_excluir = str(input(f"Tem certeza que deseja excluir o motorista de CNPJ {cnpj}? [S ou N]: ")).lower()
                if opcao_excluir.lower() == "s":
                    df_motorista =  oracle.sqlToDataFrame(f"select cnpj,nome, telefone, email, conta, codigo_escola from motoristas where cnpj = '{cnpj}' ")
                    escola = self.valida_escola(oracle, df_motorista.codigo_escola.values[0])
                    oracle.write(f"delete from motoristas where cnpj = {cnpj}")
                    motorista_removido = Motorista(df_motorista.cnpj.values[0], df_motorista.nome.values[0], df_motorista.telefone.values[0], df_motorista.email.values[0], df_motorista.conta.values[0], escola)
                    print("Motorista removido com sucesso! Caso o motorista possua Peruas, estas também foram excluídas! ")
                    print(motorista_removido.to_string())
        
        else:
            print(f"O CNPJ {cnpj} não existe")

    

    def verifica_existencia_motorista(self, oracle:OracleQueries, cnpj:str = None) -> bool:
        df_motorista = oracle.sqlToDataFrame(f"select cnpj,nome, telefone, email, conta, codigo_escola from motoristas where cnpj = '{cnpj}' ")
        return df_motorista.empty
    
    def listar_escolas(self, oracle:OracleQueries, need_connect:bool =False):
        query = """
                select e.codigo_escola,
                select e.nome,
                select e.cidade,
                select e.bairro,
                select e.logradouro,
                select e.telefone
                from escolas e
                order by e.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))

    def valida_escola(self, oracle:OracleQueries, codigo_escola:int = None) -> Escola:
        if self.ctrl_escola.verifica_existencia_escola(oracle,codigo_escola):
            print(f"O Codigo da Escola {codigo_escola} informado não existe na base de dados")
            return None
        else:
            oracle.connect()
            df_escola = oracle.sqlToDataFrame(f"select codigo_escola, nome, cidade, bairro ,logradouro, telefone from escolas where codigo_escola = {codigo_escola}")
            escola = Escola(df_escola.codigo_escola.values[0], df_escola.nome.values[0],df_escola.cidade.values[0], df_escola.bairro.values[0], df_escola.logradouro.values[0], df_escola.telefone.values[0])
            return escola
        


