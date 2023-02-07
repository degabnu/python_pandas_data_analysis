import pandas as pd
v_dados = pd.read_csv("precos-semestrais-ca-2022-01.csv", on_bad_lines='skip')
print(v_dados)
