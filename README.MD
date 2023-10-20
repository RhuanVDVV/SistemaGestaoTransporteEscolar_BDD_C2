# Sistema de Gestão de Transporte Escolar Utilizano Python e Oracle

Esse sistema é composto por um conjunto de tabelas qeu representam uma gestão de transporte escolar, contando tabelas como: Motoristas, peruas, Escolas,Alunos e Responsáveis

O sistema exige que as tabelas existam, então basta executar o script Python a seguir para criação das tabelas e preenchimento de dados de exemplos:
```shell
~$ python create_tables_and_records.py
```

Para executar o sistema basta executar o script Python a seguir:
```shell
~$ python principal.py
```

Para que possa testar as conexões com o banco de dados Oracle e o módulo Conexion desenvolvido para esse projeto, basta executar o script Python a seguir:
```shell
~$ python test.py
```

## Organização
- [diagrams](diagrams): Nesse diretório está o [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_GESTAO_TRANSPORTE_ESCOLAR.png) (lógico) do sistema.
    * O sistema possui cinco entidades: ESCOLAS, ALUNOS, RESPONSAVEIS, MOTORISTAS e PERUAS
- [sql](sql): Nesse diretório estão os scripts para criação das tabelas e inserção de dados fictícios para testes do sistema
    * Certifique-se de que o usuário do banco possui todos os privilégios antes de executar os scripts de criação, caso ocorra erro, execute o comando a seguir com o superusuário via SQL Developer: `GRANT ALL PRIVILEGES TO LABDATABASE;`
    * [create_tables_transporte_escolar.sql](sql/create_tables_transporte_escolar.sql): script responsável pela criação das tabelas, relacionamentos e criação de permissão no esquema LabDatabase.
    * [inserting_samples_records.sql](sql/inserting_samples_records.sql): script responsável pela inserção dos registros fictícios para testes do sistema.
    * [inserting_samples_related_records.sql](sql/inserting_samples_related_records.sql): script responsável pela inserção dos registros fictícios de motoristas, peruas e alunos para testes do sistema utilizando blocos PL/SQL.
- [src](src): Nesse diretório estão os scripts do sistema
    * [conexion](src/conexion): Nesse repositório encontra-se o [módulo de conexão com o banco de dados Oracle](src/conexion/oracle_queries.py). Esse módulo possui algumas funcionalidades úteis para execução de instruções DML e DDL, sendo possível obter JSON, Matriz e Pandas DataFrame.
      - Exemplo de utilização para consultas simples:

        ```python
        from conexion.oracle_queries import OracleQueries
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
        ```
      - Exemplo de utilização para alteração de registros

        ```python
        from conexion.oracle_queries import OracleQueries
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
        ```
      - Outros exemplos: [test.py](src/test.py)
      - Caso esteja utilizando na máquina virtual antiga, você precisará alterar o método connect de:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString()
                                  )
          ```
        Para:
          ```python
          self.conn = cx_Oracle.connect(user=self.user,
                                  password=self.passwd,
                                  dsn=self.connectionString(in_container=True)
                                  )
          ```
    * [controller](src/controller/): Nesse diretório encontram-sem as classes controladoras, responsáveis por realizar inserção, alteração e exclusão dos registros das tabelas.
    * [model](src/model/): Nesse diretório encontram-ser as classes das entidades descritas no [diagrama relacional](diagrams/DIAGRAMA_RELACIONAL_PEDIDOS.pdf)
    * [reports](src/reports/) Nesse diretório encontra-se a [classe](src/reports/relatorios.py) responsável por gerar todos os relatórios do sistema
    * [sql](src/sql/): Nesse diretório encontram-se os scripts utilizados para geração dos relatórios a partir da [classe relatorios](src/reports/relatorios.py)
    * [utils](src/utils/): Nesse diretório encontram-se scripts de [configuração](src/utils/config.py) e automatização da [tela de informações iniciais](src/utils/splash_screen.py)
    * [create_tables_and_records.py](src/create_tables_and_records.py): Script responsável por criar as tabelas e registros fictícios. Esse script deve ser executado antes do script [principal.py](src/principal.py) para gerar as tabelas, caso não execute os scripts diretamente no SQL Developer ou em alguma outra IDE de acesso ao Banco de Dados.
    * [principal.py](src/principal.py): Script responsável por ser a interface entre o usuário e os módulos de acesso ao Banco de Dados. Deve ser executado após a criação das tabelas.

### Bibliotecas Utilizadas
- [requirements.txt](src/requirements.txt): `pip install -r requirements.txt`

#### Em caso de problemas com a execução dos software dando a seguinte mensagem `ORA-28001: the password has expired`, execute as linhas de comando a seguir no Oracle:
- `ALTER PROFILE DEFAULT LIMIT PASSWORD_LIFE_TIME UNLIMITED;`
- `ALTER USER labdatabase IDENTIFIED BY "labDatabase2022";`
- `ALTER USER labdatabase IDENTIFIED BY  "labDatabase2022";`

### Instalando Oracle InstantClient
- Baixe a versão do [InstantClient](https://www.oracle.com/database/technologies/instant-client/linux-x86-64-downloads.html) de acordo com a versão do Banco de Dados
- Caso esteja utilizando uma distribuição Linux baseado em Debian, será necessário executar o comando a seguir para converter o arquivo .rpm para .deb.
  ```shell
  sudo alien --scripts oracle-instantclient18.5-basic-18.5.0.0.0-3.x86_64.rpm
  ```
- Descompacte o arquivo e será gerado um diretório em um diretório de fácil acesso.
- Mova os diretórios lib e share para dentro do diretório do InstantClient
  ```shell
  sudo mv lib /usr/local/oracle/instantclient_18_5/
  ```
  
  ```shell
  sudo mv share instantclient_18_5/
  ```
- Edite o arquivo `.bash_profile` incluindo as linhas a seguir ao final do arquivo:
  ```shell
  export ORACLE_HOME=/usr/local/oracle/instantclient_18_5/lib/oracle/18.5/client64
  export LD_LIBRARY_PATH=$ORACLE_HOME/lib
  export PATH=$PATH:$ORACLE_HOME/bin
  export PATH
  ```

