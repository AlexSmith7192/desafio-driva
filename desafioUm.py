import pandas as pd

de = pd.read_csv('DadosEmpresa.csv')

columnsDe = de.columns

print('Colunas da tabela DadosEmpresa.csv: ', columnsDe)
