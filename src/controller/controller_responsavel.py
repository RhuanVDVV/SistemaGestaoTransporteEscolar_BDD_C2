from model.responsaveis import Responsavel
from conexion.oracle_queries import OracleQueries

class Controller_Responsavel:
    
    def __init__(self):
        pass
    
    
    def inserir_responsavel(self) -> Responsavel:    
        # Cria uma nova conexão com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()      
        cpf = str(input("Entre com o CPF do Responsável: "))
        if self.verifica_existencia_responsavel(oracle,cpf):
            # Solicita ao usuario o nome do responsável
            nome = str(input("Entre com o Nome do Responsável: "))            
            #Solicita ao usuario o Telefone do responsável
            telefone = str(input("Entre com o Telefone do Responsável"))            
            #Solicita ao usuario o email do responsável            
            email = str(input("Entre com o email do Responsável"))            
            #Solicita ao usuario a cidade do responsável
            cidade = str(input("Entre com a Cidade do Responsável"))    
            #Solicita ao usuario o bairro do responsável            
            bairro = str(input("Entre com o Bairro do Responsável"))            
            #Solicita ao usuario o logradouro do responsável            
            logradouro = str(input("Entre com o Logradouro do Responsável"))            
            #Solicita ao usuario o Numero da Residencia do Responsável            
            numero = str(input("Entre com o Número da residência do Responsável"))            
            #Solicita ao usuario o complemento do endereço do responsavel           
            complemento = str(input("Entre com o Complemento da  residência do responsável"))
            #Insere e persiste o novo responsavel            
            oracle.write(f"insert into responsaveis values ('{cpf}, {nome}, {cidade} , {bairro} , {logradouro}, {telefone}, {email}, {numero}, {complemento}')")   
            #Recupera os dados do novo responsavel criado transformando em um DataFrame           
            df_responsavel = oracle.sqlToDataFrame(f"selet cpf,nome, cidade, bairro, logradouro, telefone, email, numero, complemento from responsaveis where cpf = '{cpf}'")            
            #Cria um novo ojbeto do fornecedor            
            novo_responsavel = Responsavel(df_responsavel.cpf.values[0] , df_responsavel.nome[0], df_responsavel.cidade[0], df_responsavel.bairro[0], df_responsavel.logradouro[0], df_responsavel.telefone[0], df_responsavel.email[0], df_responsavel.numero[0], df_responsavel.complemento[0])            
            # Exibe os atributos do novo fornecedor           
            print(novo_responsavel.to_string())
            #Retorna o objeto novo_responsavel para utilização posterior, caso necessário  
            return novo_responsavel
        else:
            print(f"O CPF {cpf} já esta cadastrado")
            return None
    
    def atualizar_responsavel(self) -> Responsavel:
        
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        cpf = input("CPF do responsável que deseja atualizar: ")
        
        if not self.verifica_existencia_responsavel(oracle,cpf):
            
            # Solicita ao usuario o nome do responsável
            nome = str(input("Entre com o novo Nome do Responsável: "))
            
            #Solicita ao usuario o Telefone do responsável
            telefone = str(input("Entre com o novo Telefone do Responsável"))
            
            #Solicita ao usuario o email do responsável
            
            email = str(input("Entre com o novo email do Responsável"))
            
            #Solicita ao usuario a cidade do responsável
            cidade = str(input("Entre com a nova Cidade do Responsável"))
    
            #Solicita ao usuario o bairro do responsável
            
            bairro = str(input("Entre com o novo Bairro do Responsável"))
            
            #Solicita ao usuario o logradouro do responsável
            
            logradouro = str(input("Entre com o novo Logradouro do Responsável"))
            
            #Solicita ao usuario o Numero da Residencia do Responsável
            
            numero = str(input("Entre com o novo Número da residência do Responsável"))
            
            #Solicita ao usuario o completo do endereço do responsavel
            
            complemento = str(input("Entre com o novo Complemento da  residência do responsável"))
            
            #Atualiza os dados do responsavel existente
            
            oracle.write(f"update responsaveis set nome = '{nome}', telefone = '{telefone}', email = '{email}', cidade = '{cidade}', bairro = '{bairro}', logradouro = '{logradouro}', numero = '{numero}', complemento = '{complemento}' where cpf = {cpf}")
            
            #Recupera os novos dados do responsavel transformando em um DataFrame
            
            df_responsavel = oracle.sqlToDataFrame(f"select cpf, nome, cidade,bairro,logradouro,telefone,email,numero,complemento from responsaveis where cpf = {cpf}")
            
            # Cria um novo objeto fornecedor
            
            responsavel_atualizado = Responsavel(df_responsavel.cpf.values[0] , df_responsavel.nome[0], df_responsavel.cidade[0], df_responsavel.bairro[0], df_responsavel.logradouro[0], df_responsavel.telefone[0], df_responsavel.email[0], df_responsavel.numero[0], df_responsavel.complemento[0])
        
            print(responsavel_atualizado.to_string())
            
            return responsavel_atualizado
            
        else:
            print(f"O CPF {cpf} não existe")
            return None
            
    def excluir_responsavel(self):
        oracle = OracleQueries(can_write=True)
        oracle.connect()
        
        cpf = input("CPF do responsável que irá excluir: ")
        
        if not self.verifica_existencia_responsavel(oracle, cpf):
            df_responsavel = oracle.sqlToDataFrame(f"select cpf, nome, cidade,bairro,logradouro,telefone,email,numero,complemento from responsaveis where cpf = {cpf}")

            opcao_excluir = str(input(f"Tem certeza que deseja excluir o Responsável de CPF {cpf}? [S ou N]: ")).lower()

            if opcao_excluir == "s":
                print("Caso o Responsável possua alunos estes também serão excluídos!")
                opcao_excluir = str(input(f"Tem certeza que deseja excluir o Responsável de CPF {cpf}? [S ou N]: ")).lower()
                if opcao_excluir.lower() == "s":
                    oracle.write(f"delete from alunos where cpf = {cpf}")
                    print("Alunos do Responsável foram removidos com sucesso!")
                    oracle.write(f"delete from responsaveis where cpf = {cpf}")
                    responsavel_excluido = Responsavel(df_responsavel.cpf.values[0] , df_responsavel.nome[0], df_responsavel.cidade[0], df_responsavel.bairro[0], df_responsavel.logradouro[0], df_responsavel.telefone[0], df_responsavel.email[0], df_responsavel.numero[0], df_responsavel.complemento[0])
                    print("Responsável removido com sucesso!")
                    print(responsavel_excluido.to_string())
           
        else:
            print(f"O CPF {cpf} não existe")
    
    
    def verifica_existencia_responsavel(self, oracle:OracleQueries, cpf:str=None) -> bool:
        
        df_responsavel = oracle.sqlToDataFrame(f"select cpf, nome, cidade,bairro,logradouro,telefone,email,numero,complemento from responsaveis where cpf = {cpf}")
        return df_responsavel.empty