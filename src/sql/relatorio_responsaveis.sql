select r.cpf,
        r.NOME,
        r.CIDADE,
        r.BAIRRO,
        r.LOGRADOURO,
        r.NUMERO,
        r.COMPLEMENTO,
        r.TELEFONE,
        r.EMAIL,
        
from responsaveis r

order by r.nome
