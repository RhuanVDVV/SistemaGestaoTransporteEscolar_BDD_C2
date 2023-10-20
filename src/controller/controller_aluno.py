from model.alunos import Aluno
from model.escolas import Escola
from model.responsaveis import Responsavel

from controller.controller_motorista import Controller_Motorista
from controller.controller_responsavel import Controller_Responsavel
from conexion.oracle_queries import OracleQueries



class Controller_Aluno:
    def __init__(self):
        self.ctrl_motorista = Controller_Motorista()
        self.ctrl_responsavel = Controller_Responsavel()

    
    def inserir_aluno(self) -> Aluno:
        
        #Cria uma nova conexao com o banco
        oracle = OracleQueries()

        # Lista as Escolas existentes para inserir no aluno

        self.ctrl_motorista.listar_escolas(oracle, need_connect=True)
        codigo_escola = int(input("Entre com o Codigo da Escola do Aluno: "))
        escola = self.ctrl_motorista.valida_escola(oracle, codigo_escola)
        if escola == None:
            return None
        

        #Lista os responsaveis existentes para inserir no aluno

        self.listar_responsaveis(oracle,need_connect=True)
        cpf = str(input("Entre com o CPF do Responsavel do Aluno"))
        responsavel = self.valida_responsavel(oracle,cpf)
        if responsavel == None:
            return None
        
        #Solicita o nome do Aluno

        nome = str(input("Entre com o nome do aluno: "))
        # Solicita a matricula do ALuno
        matricula = str(input("Entre com a matricula do aluno: "))
        #Solicita a turma do aluno
        turma = str(input("Entre com a turma do Aluno: "))

        #Solicita o Horario das AUlas do ALuno:
        horario_aula = str(input("Entre com os horarios das aulas do aluno: "))
        
        #Recupera o cursor para executar um bloco PL/SQL anonimo

        cursor = oracle.connect()
        # Cria a variavel de saída com o tipo especificado
        output_value = cursor.var(int)
        # Cria um dicionario para mapear as varaiveis de entrada e saida
        data = dict(codigo=output_value, cpf = responsavel.get_cpf(), codigo_escola = escola.get_codigo_escola(), horario_aula = horario_aula, nome= nome, turma = turma, matricula = matricula)

        # executa o bloco PL/SQL anonimo para insercao do novo aluno e recuperacao da chave primeira pela sequence

        cursor.execute(""" 
                        begin
                            :codigo := ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL;
                            insert into alunos values(:codigo, :cpf, :codigo_escola, :horario_aula, :nome, :turma, :matricula);
                        end;
                    """, data)
        
        #Recupera o codigo do novo aluno
        codigo_aluno = output_value.getvalue()

        #Persiste (confirma) as alterações
        oracle.conn.commit()

        # Recupera os dados do novo aluno criado transformado em um DataFrame

        df_aluno = oracle.sqlToDataFrame(f"select codigo_aluno, cpf, codigo_escola, horario_aula, nome, turma, matricula from alunos where codigo_aluno = {codigo_aluno}")

        #cria um novo objeto de ALuno
        novo_aluno = Aluno(df_aluno.codigo_aluno.values[0],df_aluno.horario_aula.values[0], df_aluno.nome.values[0], df_aluno.turma.values[0], df_aluno.matricula.values[0], escola, responsavel)
        print(novo_aluno.to_string())
        return novo_aluno
    

    def atualizar_aluno(self) -> Aluno:
        # Cria uma nova conexao com o banco que permite alteraçãop

        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        codigo_aluno = int(input("Entre com o Código do Aluno que irá alterar: "))

        if not self.verifica_existencia_aluno(oracle,codigo_aluno):
            # Lista as Escolas existentes para inserir no aluno

            self.ctrl_motorista.listar_escolas(oracle, need_connect=True)
            codigo_escola = int(input("Entre com o Codigo da Escola do Aluno: "))
            escola = self.ctrl_motorista.valida_escola(oracle, codigo_escola)
            if escola == None:
                return None


            #Lista os responsaveis existentes para inserir no aluno

            self.listar_responsaveis(oracle,need_connect=True)
            cpf = str(input("Entre com o CPF do Responsavel do Aluno"))
            responsavel = self.valida_responsavel(oracle,cpf)
            if responsavel == None:
                return None
            

            #Solicita o nome do Aluno

            nome = str(input("Entre com o nome do aluno: "))
            # Solicita a matricula do ALuno
            matricula = str(input("Entre com a matricula do aluno: "))
            #Solicita a turma do aluno
            turma = str(input("Entre com a turma do Aluno: "))

            #Solicita o Horario das AUlas do ALuno:
            horario_aula = str(input("Entre com os horarios das aulas do aluno: "))

            oracle.write(f"update alunos set nome = '{nome}', matricula = '{matricula}', turma = '{turma}', horario_aula = '{horario_aula}', codigo_escola = {escola.get_codigo_escola()}, cpf = {responsavel.get_cpf()}  where codigo_aluno = {codigo_aluno}")

            df_aluno_atualizado = oracle.sqlToDataFrame(f"select codigo_aluno, cpf, codigo_escola, horario_aula, nome, turma, matricula from alunos where codigo_aluno = {codigo_aluno}")

            #cria um novo objeto de ALuno
            aluno_atualizado = Aluno(df_aluno_atualizado.codigo_aluno.values[0],df_aluno_atualizado.horario_aula.values[0], df_aluno_atualizado.nome.values[0], df_aluno_atualizado.turma.values[0], df_aluno_atualizado.matricula.values[0], escola, responsavel)
            
            print(aluno_atualizado.to_string())

            return aluno_atualizado

        else:
            print(f"O Codigo do Auno {codigo_aluno} não existe")
            return None

    def excluir_aluno(self):
        oracle = OracleQueries(can_write= True)

        oracle.connect()

        codigo_aluno = int(input("Entre com o Código do Aluno que irá excluir: "))

        if not self.verifica_existencia_aluno(oracle, codigo_aluno):

            df_aluno = oracle.sqlToDataFrame(f"select codigo_aluno, cpf, codigo_escola, horario_aula, nome, turma, matricula from alunos where codigo_aluno = {codigo_aluno}")

            escola = self.ctrl_motorista.valida_escola(df_aluno.codigo_escola.values[0])
           
            responsavel = self.valida_responsavel(df_aluno.cpf.values[0])

            oracle.write(f"delete from alunos where codigo_aluno = {codigo_aluno}")

            aluno_excluido = Aluno(df_aluno.codigo_aluno.values[0],df_aluno.horario_aula.values[0], df_aluno.nome.values[0], df_aluno.turma.values[0], df_aluno.matricula.values[0], escola, responsavel)

            print("Aluno removido com sucesso!")

            print(aluno_excluido.to_string())



        else:
            print(f"O Codigo do Aluno {codigo_aluno} não existe")


    def verifica_existencia_aluno(self,oracle: OracleQueries, codigo:int =None) -> bool:
        df_aluno = oracle.sqlToDataFrame(f"select codigo_aluno, cpf, codigo_escola, horario_aula, nome, turma, matricula from alunos where codigo_aluno = {codigo}")
        return df_aluno.empty
    
    def listar_responsaveis(self, oracle:OracleQueries, need_connect:bool = False):
        query = """
                select r.cpf,
                    r.nome,
                    r.cidade,
                    r.bairro,
                    r.logradouro,
                    r.telefone,
                    r.email,
                    r.numero,
                    r.complemento
                from responsaveis r
                order by r.nome
                """
        if need_connect:
            oracle.connect()
        print(oracle.sqlToDataFrame(query))
    
    def valida_responsavel(self,oracle:OracleQueries, cpf:str = None ) -> Responsavel:
        if self.ctrl_responsavel.verifica_existencia_responsavel(oracle, cpf):
            print(f"O responsável com cpf {cpf} informado não existe na base")
            return None
        else:
            oracle.connect()

            df_responsavel = oracle.sqlToDataFrame(f"selet cpf,nome, cidade, bairro, logradouro, telefone, email, numero, complemento from responsaveis where cpf = '{cpf}'")
            
            #Cria um novo ojbeto do fornecedor
            
            responsavel = Responsavel(df_responsavel.cpf.values[0] , df_responsavel.nome[0], df_responsavel.cidade[0], df_responsavel.bairro[0], df_responsavel.logradouro[0], df_responsavel.telefone[0], df_responsavel.email[0], df_responsavel.numero[0], df_responsavel.complemento[0])
            return responsavel