-- RELACAO DE JUNCAO DE TABELAS

select a.CODIGO_ALUNO,
        a.HORARIO_AULA,
        a.NOME,
        a.TURMA,
        a.MATRICULA
        a.CODIGO_ESCOLA,
        a.CPF AS CPF_RESPONSAVEL
        r.NOME as NOME_RESPONSAVEL,
        r.LOGRADOURO,
        r.BAIRRO,
        r.CIDADE,
        e.CODIGO_ESCOLA
        e.nome AS NOME_ESCOLA

from alunos a
inner join responsaveis r
on a.cpf = r.cpf
inner join escolas e
on a.codigo_escola = e.codigo_escola
order by a.nome
