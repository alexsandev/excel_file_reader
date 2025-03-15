import pandas as pd

def excel_para_dicionario(diretorio):
    dic = {}

    # Faz a leitura do arquivo Excel e retorna um objeto DataFrame(estrutura de dados bidimensional) 
    df = pd.read_excel(diretorio)

    # Seleciona as colunas 'id_cliente' e 'quantidade', agrupa por 'id_cliente' e soma as linhas 'quantidade' de cada grupo.
    quantidade_total_cliente = df[['id_cliente','quantidade']].groupby('id_cliente').sum('quantidade')

    # Percorre as linhas da nova tabela
    for tupla in quantidade_total_cliente.itertuples():
        id_cliente = tupla[0]
        quantidade = tupla[1]
        dic[id_cliente] = quantidade

    return dic
    
print(excel_para_dicionario('./base_pedidos_v2.xlsx'))
    
