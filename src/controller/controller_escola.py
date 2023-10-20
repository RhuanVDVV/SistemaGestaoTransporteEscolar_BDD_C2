from model.escolas import Escola
from conexion.oracle_queries import OracleQueries


class Controller_Escola:
    def __init__(self):
        pass

    def inserir_escola(self) -> Escola:


        # Cria uma nova conexão com o banco
        oracle = OracleQueries(can_write=True)
        # Recupera o crusos para executar um bloco PL/SQL anonimo
        cursor = oracle.connect()
        #Cria a varaivel de saída com o tipo especificado
        output_value = cursor.var(int)

        #Solicita ao usuario o nome da escola
        novo_nome = str(input("Entre com o nome da escola: "))

        #Solicita ao usuario a cidade da escola
        novo_cidade = str(input("Entre com a cidade da escola: "))

        #Solicita ao usuario o bairro da escola
        novo_bairro = str(input("Entre com o bairro da escola: "))

        #Solicita ao usuario o logradouro da escola
        novo_logradouro = str(input("Entre com o logradouro da escola: "))

        #Solicita ao usuario o telefone da escola
        novo_telefone = str(input("Entre com o telefone da Escola"))

        #Cria um dicionario para mapear as variaveis da entrada e saída
        data = dict(codigo = output_value, nome = novo_nome, cidade = novo_cidade, bairro = novo_bairro, logradouro = novo_logradouro, telefone = novo_telefone)

        # Executa o bloco PL/SQL anonimo para inserção da nova escola e recuperação da chave rimeira criada pela sequence
        cursor.execute("""
                        begin
                            :codigo := ESCOLAS_CODIGO_ESCOLA_SEQ.NEXTVAL;
                            insert into escolas values(:codigo, :nome, :cidade, :bairro, :logradouro, :telefone);
                        end;                   
                       """, data)
        #Recupera o codigo da nova escola
        codigo_escola = output_value.getvalue()
        #Persiste (confirma) as alterações
        oracle.conn.commit()
        #Recupera os dados do novo produto criado trasnformando em um DataFrame
        df_escola = oracle.sqlToDataFrame(f"select codigo_escola, nome, cidade, bairro, logradouro, telefone from escolas where codigo_escola = {codigo_escola}")
        # Cria um novo objeto da Escola
        nova_escola = Escola(df_escola.codigo_escola.values[0],df_escola.nome.values[0], df_escola.cidade.values[0],df_escola.bairro.values[0],df_escola.logradouro.values[0],df_escola.telefone.values[0])
        #Exibe os atributos da nova escola
        print(nova_escola.to_string())
        return nova_escola
    
    def atualizar_escola(self) -> Escola:
        # Cria uma Nova conexao com o banco que permite alteração
        oracle = OracleQueries(can_write= True)

        oracle.connect()

        codigo_escola = int(input("Código da Escola que irá alterar: "))

        if not self.verifica_exitencia_escola(oracle, codigo_escola):
            #Solicita ao usuario o nome da escola
            novo_nome = str(input("Entre com o nome da escola: "))

            #Solicita ao usuario a cidade da escola
            novo_cidade = str(input("Entre com a cidade da escola: "))

            #Solicita ao usuario o bairro da escola
            novo_bairro = str(input("Entre com o bairro da escola: "))

            #Solicita ao usuario o logradouro da escola
            novo_logradouro = str(input("Entre com o logradouro da escola: "))

            #Solicita ao usuario o telefone da escola
            novo_telefone = str(input("Entre com o telefone da Escola"))
            # Atualiza os dados de uma escola existente
            oracle.write(f"update escolas set nome = '{novo_nome}', cidade = '{novo_cidade}', bairro = '{novo_bairro}', logradouro = '{novo_logradouro}', telefone = '{novo_telefone}' where codigo_escola = {codigo_escola}")
            # Recupra os dados a escola atualizada transformando em um data frame
            df_escola = oracle.sqlToDataFrame(f"select codigo_escola, nome, cidade, bairro, logradouro, telefone from escolas where codigo_escola = {codigo_escola}")
            #Cria um objeto Escola do dataframe
            escola_atualizado = Escola(df_escola.codigo_escola.values[0], df_escola.nome.values[0], df_escola.cidade.values[0], df_escola.bairro.values[0], df_escola.logradouro.values[0], df_escola.telefone.values[0])
            #Exibe os atributos da escola atualizada
            print(escola_atualizado.to_string())
            return escola_atualizado   
            
        else:
            print(f"O código da escola {codigo_escola} não existe ")
            return None
        

    def excluir_escola(self):
        # Cria uma nova conexao com o banco que permite alteração
        oracle = OracleQueries(can_write=True)
        oracle.connect()

        # Solicita ao usuario o codgio da escola a ser excluido

        codigo_escola = int(input("Código da Escola que irá excluir: "))

        if not self.verifica_existencia_escola(oracle,  codigo_escola):
            
            opcao_excluir = str(input(f"Tem certeza que deseja excluir a Escola com Código {codigo_escola}? [S ou N]: ")).lower()

            if opcao_excluir == "s":
                print("Caso a Escola possua alunos, motoristas e motorista possua peruas estes também serão excluídos!")
                opcao_excluir = str(input(f"Tem certeza que deseja excluir a Escola com Código {codigo_escola}? [S ou N]: ")).lower()
                if opcao_excluir.lower() == "s":

                    df_escola = oracle.sqlToDataFrame(f"select codigo_escola, nome, cidade, bairro, logradouro, telefone from escolas where codigo_escola = {codigo_escola}")

                    oracle.write(f"delete from escolas where codigo_escola = {codigo_escola}")
                    
                    escola_excluida = Escola(df_escola.codigo_escola.values[0], df_escola.nome.values[0], df_escola.cidade.values[0], df_escola.bairro.values[0], df_escola.logradouro.values[0], df_escola.telefone.values[0])

                    print("Escola removida com sucesso! Caso a escola possua alunos, motoristas e motorista possua peruas estes também foram excluídos")
                    print(escola_excluida.to_string())
            
        else:
            print(f"O Código da Escola {codigo_escola} não existe")

    
    def verifica_existencia_escola(self, oracle: OracleQueries, codigo:int = None) -> bool:
        df_escola = oracle.sqlToDataFrame(f"select codigo_escola, nome, cidade, bairro, logradouro, telefone from escolas where codigo_escola = {codigo}")
        return df_escola.empty