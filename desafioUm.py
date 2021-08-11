import pandas as pd

de = pd.read_csv('DadosEmpresa.csv')

columnsDe = de.columns
print('\nColunas da tabela DadosEmpresa.csv: \n', columnsDe)

firstLines = de.head(10)
print('\n10 primeiras linhas da tabela DadosEmpresa.csv: \n', firstLines)

optionsSimplemSum = de.query('opcao_pelo_simples == "SIM"').count().value_counts()
print('\nQuantidade de empresas que optam pelo simples: \n', optionsSimplemSum)

sumShareCapital = de.sum().iloc[[5]]
print('\nSoma do capital social das empresas: \n', sumShareCapital)
