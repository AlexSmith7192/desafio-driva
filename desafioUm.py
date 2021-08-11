import pandas as pd

dEmp = pd.read_csv('DadosEmpresa.csv')

columnsDe = dEmp.columns
print('\nColunas da tabela DadosEmpresa.csv: \n', columnsDe)

firstLines = dEmp.head(10)
print('\n10 primeiras linhas da tabela DadosEmpresa.csv: \n', firstLines)

optionsSimplemSum = dEmp.query('opcao_pelo_simples == "SIM"').count().iloc[[4]]
print('\nQuantidade de empresas que optam pelo simples: \n', optionsSimplemSum)

sumShareCapital = dEmp.sum().iloc[[5]]
print('\nSoma do capital social das empresas: \n', sumShareCapital)

filterCapitalSocial = dEmp.query('capital_social > 10000 & capital_social < 20000')
print('\nEmpresas que tem capital social maior que 10.000 e menor que 20.000: \n', filterCapitalSocial)

dEnd = pd.read_csv('DadosEndereco.csv')

mergeDatas = pd.merge(dEmp, dEnd)
empCuritiba = mergeDatas.query('municipio == "CURITIBA"')
empCuritiba.to_csv(path_or_buf='DadosEmpresasCuritiba.csv' ,index=False)

