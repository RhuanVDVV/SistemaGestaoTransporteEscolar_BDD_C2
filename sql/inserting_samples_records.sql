/*INSERE DADOS NA TABELA DE ESCOLAS*/

INSERT INTO LABDATABASE.ESCOLAS VALUES(ESCOLAS_CODIGO_ESCOLA_SEQ.NEXTVAL, "CEEFMTI Antonella Stella", "Colatina","Fazenda Vitali", "Rua  ngelo Gonçalves", "2735805957")
INSERT INTO LABDATABASE.ESCOLAS VALUES(ESCOLAS_CODIGO_ESCOLA_SEQ.NEXTVAL, "CEEFMTI Ramos Figueredo", "Vitória", "Santa Lúcia", "Rua das Palmeiras 795", "272756-9015")

--INSERE DADOS NA TABELA DE RESPONSAVEIS
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("29481065758", "Michele Lima Carrara", "Serra", "Morada de Laranjeiras", "Rua dos Calafates", "27998282428", "michelelcarrara@gmail.com", "48", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("04290211780", "Alan Hamilton Silva", "Serra", "André Carloni", "Rua Hamilton Honorino Soares", "27999986068", "alanhamilton@hotmail.com", "1", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("19573909723", "Camila Vanessa Ribeiro", "Serra", "Novo Porto Canoa", "Rua Carcará", "27993934368", "camilaribeiro@gmail.com", "18", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("51353131769 ", "Guilherme Martins da Cruz", "Serra", "Parque Residencial de Tubarão", "Rua Aimorés", "27986755125", "guimartinscruz@hotmail.com", "34", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("55740119723", "Juliana Ferraz Fernandes", "Vitória", "Jardim Camburi", "Rua Oswaldo Bastos de Souza Freitas", "27997338535", "julianaferraz@gmail.com", "14", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("68484762777", "Felipe Burgos Almeida", "Vitória", "Enseada do Suá", "Rua Marília de Rezende Scarton Coutinho", "27993153203", "felipeburgosalm@hotmail.com", "57", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("15134676704", "Rodrigo Raí Brito", "Vitória", "Ilha das Caieiras", "Rua São João", "27986257833", "rodrigorbrito@gmail.com", "4", "")
INSERT INTO LABDATABASE.RESPONSAVEIS VALUES ("32402641703", "Danielle Machado Gomes", "Vitória", "Santos Dumont", "Rua Doutor Gastão Pache de Faria", "27987720530", "danimachadogomes@hotmail.com", "13", "")

--INSERE DADOS NA TABELA DE MOTORISTAS
INSERT INTO LABDATABASE.MOTORISTAS VALUES("08742284000101", "Silvana Ferreira", "27996659591", "silvanaferreira@gmindustria.com.br", "20966584", 1)
INSERT INTO LABDATABASE.MOTORISTAS VALUES("82790608000121", "Marcelo Santos", "27984639027", "marcelosantos@gmindustria.com.br", "3497248", 2)

--INSERE DADOS NA TABELA DE PERUAS
INSERT INTO LABDATABASE.PERUAS VALUES("MPE3348", "Sprinter 415", 15, "08742284000101")
INSERT INTO LABDATABASE.PERUAS VALUES("MTD4911", "Sprinter 415", 15, "82790608000121")

--INSERE DADOS NA TABELA DE ALUNOS
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "29481065758", 1, "07:00 - 12:00", "Maria Lima", "M0102", "20230402")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "29481065758", 1, "07:00 - 12:00", "João Lima", "M0102", "20230307")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "04290211780",1, "13:00 - 18:00","Ana Luiza Hamilton", "V0103", "20230307")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "19573909723",1, "13:00 - 18:00", "Felipe Ribeiro", "V0103", "20230506")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "51353131769",1, "13:00 - 18:00", "Rafaela Martins", "V0104", "20230805")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "55740119723",2, "07:00 - 12:00", "Pedro Ferraz", "M0101", "20230109")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "55740119723",2, "07:00 - 12:00", "Camila Ferraz", "M0101", "20230507")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "68484762777",2, "13:00 - 18:00", "Letícia Almeida", "V0102", "20230208")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "15134676704",2, "13:00 - 18:00", "Rafaela Brito", "V0107", "20230807")
INSERT INTO LABDATABASE.ALUNOS VALUES(ALUNOS_CODIGO_ALUNO_SEQ.NEXTVAL, "32402641703",2, "13:00 - 18:00", "Marcos Gomes", "V0204", "20230603")



