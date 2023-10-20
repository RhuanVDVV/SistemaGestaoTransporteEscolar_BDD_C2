select m.CNPJ,
        m.NOME,
        m.TELEFONE,
        m.EMAIL,
        m.CONTA
        m.CODIGO_ESCOLA,
        e.nome as NOME_ESCOLA
from MOTORISTAS m
inner join escolas e
on m.CODIGO_ESCOLA = e.CODIGO_ESCOLA
order by m.nome, e.nome
