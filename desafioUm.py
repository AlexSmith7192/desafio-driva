import pandas as pd

de = pd.read_csv('DadosEmpresa.csv')

columnsDe = de.columns
print('\nColunas da tabela DadosEmpresa.csv: \n', columnsDe)

firstLines = de.head(10)
print('\n10 primeiras linhas da tabela DadosEmpresa.csv: \n', firstLines)
