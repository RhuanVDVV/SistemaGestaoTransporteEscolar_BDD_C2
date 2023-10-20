MENU_PRINCIPAL = """Menu Principal
1 - Relatórios
2 - Inserir Registros
3 - Atualizar Registros
4 - Remover Registros
5 - Sair
"""

MENU_RELATORIOS= """Relatórios
1 - Relatório de Escolas
2 - Relatório de Alunos
3 - Relatório de Escolas e Quantidade de Alunos
4 - Relatório de Responsáveis
5 - Relatório de Motoristas
6 - Relatório de Peruas
0 - Sair
"""

MENU_ENTIDADES = """ENTIDADES
1 - ESCOLA
2 - ALUNOS
3 - RESPONSÁVEIS
4 - MOTORISTAS
5 - PERUAS
"""

QUERY_COUNT = 'select count(1) as total_{tabela} from {tabela}'

def clear_console(wait_time:int=3):
    import os
    from time import sleep
    sleep(wait_time)
    os.system("clear")