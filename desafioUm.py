import pandas as pd

de = pd.read_csv('DadosEmpresa.csv')

columnsDe = de.columns
print('\nColunas da tabela DadosEmpresa.csv: \n', columnsDe)

firstLines = de.head(10)
print('\n10 primeiras linhas da tabela DadosEmpresa.csv: \n', firstLines)

optionsSimplemSum = de.query('opcao_pelo_simples == "SIM"').count().iloc[[4]]
print('\nQuantidade de empresas que optam pelo simples: \n', optionsSimplemSum)

sumShareCapital = de.sum().iloc[[5]]
print('\nSoma do capital social das empresas: \n', sumShareCapital)

filterCapitalSocial = de.query('capital_social > 10000 & capital_social < 20000')
print('\nEmpresas que tem capital social maior que 10.000 e menor que 20.000: \n', filterCapitalSocial)