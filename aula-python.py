# from IPython.display import display
import pandas as pd
# v_combustiveis_csv = pd.read_csv("precos-semestrais-ca-2022-01.csv", sep=';')
v_combustiveis_excel = pd.read_excel("ca-2021-02.xlsx")

# print(pd.options.display.max_rows)
# print(v_combustiveis_csv)
# print(v_combustiveis_excel)
# display(v_combustiveis_excel)
# print(v_combustiveis_excel.head())
# print(v_combustiveis_excel.head(15))
# print(v_combustiveis_excel.shape)
# print(v_combustiveis_excel.shape[0])
# print(v_combustiveis_excel.shape[1])
# print(v_combustiveis_excel.info())
# print(v_combustiveis_excel.describe())
# print(v_combustiveis_excel['Revenda'])
# print(v_combustiveis_excel['Revenda'][0:10])
# v_ca_df = v_combustiveis_excel[[
#     'Revenda', 'Municipio', 'Produto', 'Valor de Venda']]
# # print(v_ca_df)
# print(v_ca_df.loc[0:10])
v_ca_df = v_combustiveis_excel[[
    'Revenda', 'Municipio', 'Produto', 'Valor de Venda']]
v_gas_df = v_ca_df.loc[v_ca_df['Produto'] == 'GASOLINA']
print(v_gas_df['Valor de Venda'].max())
print(v_gas_df[['Municipio', 'Revenda', 'Valor de Venda']].max())
