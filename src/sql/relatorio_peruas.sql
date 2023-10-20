select p.PLACA,
        p.MODELO,
        p.CAPACIDADE,
        p.CNPJ as CNPJ_MOTORISTA,
        m.nome as NOME_MOTORISTA

from PERUAS p
inner join MOTORISTAS m
on p.cnpj = m.cnpj
order by m.nome
