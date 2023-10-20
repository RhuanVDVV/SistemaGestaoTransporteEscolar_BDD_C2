
-- CONSULTA REALIZANDO SUMERIZACAO

with sumariza_alunos as(
    select codigo_escola,
    count(1) as qtd_alunos
    from alunos
    group by codigo_escola
)

select e.nome as nome_escola,
        e.LOGRADOURO || ' ' || e.BAIRRO || ' ' || e.CIDADE || ' '  as endereco,
        sa.qtd_alunos

    from escolas e
    inner join sumariza_alunos sp
    on e.codigo_escola = sp.codigo_escola
    group by sp.qtd_alunos, e.nome
    order by e.nome
        


