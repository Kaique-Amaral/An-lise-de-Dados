# aula 1: importando dataset
import pandas as pd

# vamos abrir, como exemplo, um dataset de preços médios de gasolina
# note que o arquivo está no formato TSV, e queremos convertê-lo para CSV
# que é um formato mais utilizado

# para carregar um dataset no formato csv, basta usar o comando read_csv do Pandas
# por padrão ele considera ',' como separador
# como o python está assumindo que 'c:/Users/Kaique Amaral/Downloads/VSCODE Testes/'
# é o diretório principal, a gente vai fazer assim pra que ele encontre:
data = pd.read_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019.csv')

print(data)

# note que o arquivo printará cada linha como se todas as colunas fossem uma coisa só
# isso é pq ele está esperando ler um ',' como separação
# no entanto, as colunas são separadas por ';'
# isso faz com que ele tenha 106822 linhas, mas só uma coluna
# vamos fazer com que ele leia por ';':
data = pd.read_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019.csv', sep=';')
print(data)

# agora está certo!
# vê como agora ele tem 21 colunas?

# suponhamos agora que eu queira ver as n primeiras linhas do dataset
# para isso, usamos a função head(n)
# vamos ver as 10 primeiras linhas (da linha 0 até a 9):
print(data.head(10))

# ou talvez as 20 primeiras linhas (da linha 0 até a 19):
print(data.head(20))

# se eu quiser ver as últimas n linhas, utilizamos a função tail(n)
# a exemplo:
print(data.tail(10)) # as 10 últimas linhas (106813 até 106822)





# aula 2: informações do dataset
print(data.info()) 
# printamos umas informações gerais sobre o dataset
# a quantidade de valores válidos por coluna, o tipo de valor por coluna
# o nome de cada coluna, etc
# podemos notar algumas coias estranhas
# por exemplo, o preço médio de distribuição tá sendo dado como "objeto"
# objeto, nesse caso, seria algo parecido com uma string
# um troço que diz o preço deveria ser uma string? não né? deveria ser um float
# vamos ver se isso é problemático mais para frente
# a primeira coluna da tabela, chamada 'Unnamed: 0', parece não significar nada
# na verdade, ela é os índices da tabela, que foram salvos como uma coluna
# vamos removê-la jajá
# além disso, nenhuma coluna (atributo) possui valores nulos, como dá pra ver
# mas veremos que não é bem assim pra esse caso





# Aula 3: DataFrame

# todo DataSet carregado é um DataFrame;
# ou seja, uma tabela bi-dimensional, mutável e heterogêneo normalmente

# podemos checar que de fato é um DataFrame utilizando:
print(type(data)) # imprime "<class 'pandas.core.frame.DataFrame'>"

# podemos printar as dimensões do DataFrame utilizando o atributo .shape
print(data.shape) # printa (106823, 21), o valor correto

# poderíamos printar algo mais bonitinho:
print(f'O Dataframe possui {data.shape[0]} linhas/atributos e {data.shape[1]} colunas.')

# vamos criar um DataFrame
# podemos criar um DataFrame a partir de um dicionário (basicamente Struct em C)
# as chaves representam colunas e cada um dos valores da lista representam linhas
personagens_df = pd.DataFrame({
    'nome': ['Luke Skywalker', 'Yoda', 'Palpatine'],
    'idade': [15, 1000, 70],
    'peso': [70.2, 15.1, 60.9],
    'eh jedi': [True, True, False]
})

print(personagens_df)

print(personagens_df.info())

#### RENOMEANDO COLUNAS DO DATAFRAME ####

# o atributo DataFrame.columns retorna uma "lista" com todas as colunas do data frame
print(personagens_df.columns) # note que isso é um índice, não de fato uma lista
# se quisermos imprimir uma lista, sem a parte do index, podemos converter:
print(list(personagens_df.columns))

# se quisermos renomear colunas do DataFrame, usamos DataFrame.rename
# supunhamos que queiramos renomear a coluna 'nome' e a coluna 'idade'
# alteraremos ela para 'Nome Completo' e 'Idade'
personagens_df_renomeados = personagens_df.rename(columns={
    'nome': 'Nome Completo',
    'idade': 'Idade'
})

print(personagens_df) # antes
print(personagens_df_renomeados) # depois

# se quisermos alterar o próprio personagens_df, não criar uma cópia, fazemos:
personagens_df.rename(columns={
    'nome': 'Nome Completo',
    'idade': 'Idade'
}, inplace=True)

print(personagens_df) # veja como agora o personagens_df está alterado

# por fim, se eu quiser alterar várias colunas de uma só vez, eu posso simplesmente:
# como a lista de colunas é ['Nome Completo',  'Idade',  'peso',  'eh jedi']
personagens_df.columns = ['NOME', 'IDADE', 'PESO', 'EH JEDI']

print(personagens_df)




# Aula 4: Séries
# suponha que eu queira selecionar uma coluna inteira
# vamos voltar lá pros preços do gás no Brasil
# caso você tenha se esquecido:
print(data)

# vamos selecionar a coluna estado
# para selecioná-la, podemos fazer assim:
# printaremos a coluna estado inteira
print(data['ESTADO']) # eba

# também poderíamos com um .
# mas note que só podemos usar com . se não houver espaços, acentos ou sla no nome
print(data.ESTADO)

# hmmmm... qual o tipo dessa coluna "ESTADO", quando selecionamos ela?
print(type(data.ESTADO))
# é uma "Series"

# podemos, também, pegar a observação indexada no índice 1(ou seja, o segundo) 
# do Dataframe:
print(data.iloc[1])
# é como se tivéssemos pêgo a linha 1
# que é a segunda linha, já que a primeira linha é a linha 0
print(data.iloc[0])

# podemos criar uma series a partir de uma lista de elementos
# por exemplo:
print(pd.Series([5.5, 6.0, 9.5])) # no índice 1, 5.5, no 2, 6.0, no 3, 9.5

# podemos alterar o nome dos índices
# por exemplo, colocar índice 1 = Prova 1, índice 2 = Prova 2, índice 3 = Projeto
print(pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto']))

# eu posso inclusive dar um nome pra essa series
# por exemplo, suponhamos que essas sejam as notas do Luke Skywalker
print(pd.Series([5.5, 6.0, 9.5], index=['prova 1', 'prova 2', 'projeto'], name='Notas do Luke Skywalker'))





# Aula 5: Atribuindo Valores a um DataFrame
# aqui poderemos alterar os valores e criar novas colunas
# vejamos a series PRODUTO:
print(data['PRODUTO']) # a series retornada referente à coluna NÃO É UMA CÓPIA! 
# é uma forma de visualização
# ou seja, é tipo um ponteiro apontando diretamente pra memória
# ao ponto de podermos, por exemplo:
visualizar_produtos = data['PRODUTO']

# se quiséssemos criar uma cópia, faríamos:
produto_copia_backup = data['PRODUTO'].copy() # retorna uma cópia da coluna 'PRODUTO'

# se eu quisesse alterar todos os valores da coluna PRODUTO, olha o que ocorreria:
data['PRODUTO'] = 'Combustível' # alteramos todos os valores para 'Combustível'

print(data['PRODUTO'])

# suponhamos que eu queira atribuir listas ou séries
# vamos, primeiro, ver a quantidade de linhas e colunas
nrows, ncols = data.shape
print(nrows, ncols)

# vamos printar os índices dos produtos
# assim, o produto do índice 1 vai ser "Produto 1", do índice 0 vai ser "Produto 0"
# do índice 526 vai ser "Produto 526" e assim por diante
novos_produtos = [f'Produto {i}' for i in range (nrows)]
print(novos_produtos)

# agora, vamos alterar os produtos do data
data['PRODUTO'] = novos_produtos
# como o visualizar_produtos ainda está apontando para o lugar antigo do data
# reatribuímos:
visualizar_produtos = data['PRODUTO']

# veja que:
# o visualizar produtos vai mostrar os produtos de data['PRODUTO']
# enquanto o backup que criamos ali em cima permanece paradão
print(visualizar_produtos)
print("\n")
print(produto_copia_backup)

# note que o primeiro é diferente do segundo

# vamos retornar o valor dos produtos pros do backup
data['PRODUTO'] = produto_copia_backup
print(data['PRODUTO'])





# Aula 6: Criando uma Coluna
# a gente pode criar uma coluna e atribuir a todas as linhas desta coluna um valor
# a exemplo, vamos criar uma nova coluna aleatória e atribuir a ela o valor Default:
data['coluna fodase'] = 'DEFAULT'
print(data)

# suponhamos que eu queira criar uma nova coluna, e adicionar a ela os valores 0 a 106822
# ou seja, colocar o valor do índice da linha em cada linha da nova coluna
data['coluna índice'] = range(data.shape[0]) # eu meio que estou copiando a coluna 0 pra coluna índice
print(data)

# note que eu não poderia adicionar uma quantidade menor que 106823 de valores
# pra uma coluna criada
# isso, porque o data tem 106823 linhas 
# se eu tentar fazer isso, por exemplo:
#data['vai dar ruim'] = [1, 2, 3] vai dar erro

# podemos também criar uma nova coluna com base em uma coluna já existente
# a exemplo:
data['PREÇO MÉDIO REVENDA (DÓLARES)'] = data['PREÇO MÉDIO REVENDA'] * 5.5
print(data['PREÇO MÉDIO REVENDA']) 
print(data['PREÇO MÉDIO REVENDA (DÓLARES)'])
# eba




# Aula 7: Índices
# para acessarmos os índices de um DataFrame, existe um comando para isso:
print(data.index)

# neste caso, os índices são numerais
# mas os índices também podem ser texto
# por exemplo, olhe um exemplo de dataframe:
pesquisa_de_satisfacao = pd.DataFrame({
    'bom': [50, 21, 100],
    'ruim': [131, 2, 30],
    'pessimo': [30, 20, 1]
}, index=['Xbox One', 'Playstation 4', 'Switch']) # aqui, os índices são esses 3 textos

print(pesquisa_de_satisfacao)
print(pesquisa_de_satisfacao.index)




# Aula 8: Busca por Índices

# mostrando linhas específicas de um Dataframe:
# utilizamos, com base no índice, o .iloc
# assim, ao usarmos data.iloc[10], pegamos todas as informações do índice 10
print(data.iloc[1])

# selecionando múltiplas observações/linhas:
# podemos utilizar algo chamado "slicing"

# pra selecionarmos as linhas de índice de 0 a 5 (incluso):
print(data.iloc[:6]) # mostra os 6 primeiros índices (0 a 5)
print(data.iloc[10:26]) # mostra os índices do 10 ao 26
print(data.iloc[[1, 4, 5, 10, 15]]) # mostra os índices 1, 4, 5, 10, 15
print(data.iloc[[2, 100, 4, 268, 145]]) # pode ser em ordens diferentes

print(data.iloc[1, 4]) # retornar o valor da quarta coluna do primeiro índice (segunda linha, já que começa no índice 0)





# Aula 9: Seleção por Labels(Rótulos)

# veja o seguinte DataFrame:
print(pesquisa_de_satisfacao)
# note que os índices dele não são numéricos; são textuais
# o que aconteceria se fizéssemos:
print(pesquisa_de_satisfacao.iloc[0])
# ele printou o primeiro índice, que é o do Xbox One

# isso acontece porque, mesmo nos DataFrames onde o índice é feito por texto, há um índice implícito
# quando usamos iloc, ele printa com base nesse índice implícito
print(pesquisa_de_satisfacao.iloc[0, 1])

# se quisermos printar com base no índice de texto, utilizamos o .loc
print(pesquisa_de_satisfacao.loc['Xbox One'])
print(pesquisa_de_satisfacao.loc['Xbox One', 'bom']) # não podemos utilizar texto e número, precisamos utilizar só texto com .loc

# se quisermos duas linhas:
print(pesquisa_de_satisfacao.loc[['Xbox One', 'Switch']])

# podemos, também, printar só as colunas "bom" e "péssimo"
print(pesquisa_de_satisfacao[['bom', 'pessimo']])

# podemos também usar o loc:
print(pesquisa_de_satisfacao.loc[:, ['bom', 'pessimo']]) # printa nenhuma linha em específico(todas) e printa as colunas bom e pessimo

# note, no entanto, que por existir um índice implícito e um índice explícito no data, podemos acessar usando o índice e o loc
print(data.loc[1])




# Aula 10: Seleção de Colunas

# já vimos que podemos printar determinada coluna das seguintes formas:
print(data['ESTADO']) # funciona pra tudo
print(data.ESTADO) # só funciona se o nome da coluna não possuir caracteres inválidos(espaços, acentos, cedilhas, etc)
print(data.loc[:, 'ESTADO']) # funciona pra tudo também
# todas funcionam, apesar de terem suas peculiaridades

# para a seleção de várias colunas, podemos usar o primeiro e o último método:
print(data[['ESTADO', 'PRODUTO', 'REGIÃO']])
print("\n")
print(data.loc[:, ['ESTADO', 'PRODUTO', 'REGIÃO']])




# Aula 11: Salvando um DataSet

# Removendo Colunas:
print(data.head())
# como podemos ver, adicionamos algumas colunas que não queremos ter nos nossos arquivos
# como a 'coluna fodase', a 'coluna índice' e o 'PREÇO MÉDIO REVENDA (DÓLARES)'
# também tem a coluna Unnamed: 0, que parece ser um ruído desnecessário
# para removê-la diretamente no dataframe, basta:
del data['Unnamed: 0'] 
print(data)
# removido com sucesso!
# agora vamos remover as outras colunas
del data['coluna fodase']
del data['coluna índice']
del data['PREÇO MÉDIO REVENDA (DÓLARES)']
print(data.head())

# Salvando um Data Frame:
# para salvarmos um Data Frame pra um arquivo CSV, basta usarmos o método .to_csv
# por padrão, esse método salva os índices da tabela como uma coluna no CSV
# como no geral tais índices são números de 0 a n-1, não há necessidade
# (veja que removemos a coluna Unnamed: 0, que foi justamente esse caso)
# desta forma, use o parâmetro index=False
# por padrão, o método utilizará a ',' como separador de colunas
# para alterar, usa-se o parâmetro sep
data.to_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019PREPROCESSADO.csv', index=False, sep=';')
# note que o Microsoft Excel lê com ';'
# enquanto o Pandas lê com ',' por padrão
# então se formos ler os dados preprocessados, utilizaremos sep=';'
data_preprocessado = pd.read_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019PREPROCESSADO.csv', sep=';')
print(data_preprocessado)




# Aula 12: Filtragem (Parte 1 de 5)

# agora, vamos pra uma das coisas mais importantes: busca condicional
# durante nossas análises, frequentemente filtraremos nossas amostras para fins de análise mais específica
# existem algumas maneiras de fazermos isso:
data = pd.read_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019PREPROCESSADO.csv', sep=';')

# vamos ver quais estados foram analisados:
print(data['ESTADO']) # poxa, ficou muitos dados!
# o que eu vou fazer? são muitas linhas!
#simples: utilizamos o .unique, para dizer a quantidade de valores únicos
print(data['ESTADO'].unique())

# agora, vamos escrever um código simples
# o código vai analisar cada um dos estados da coluna ESTADO, e retornar True caso seja São Paulo
# e falso pra caso não seja
print(data['ESTADO'] == 'SAO PAULO')

# vamos salvar essa series de booleanos em uma variável:
selecao = data['ESTADO'] == 'SAO PAULO'

# podemos confirmar que de fato é uma series ao fazer:
print(type(selecao))

# assim, se quisermos filtrar os registros de postos do estado de São Paulo, podemos:
print(data[selecao]) # aqui, vai retornar somente as linhas em que os valores são "True"
# fazendo a filtragem, descobrimos que apenas 4263 linhas, das 106 mil, são de São Paulo

# poderíamos usar loc também:
print(data.loc[selecao])

# ou seja, para fazer uma seleção, basta passar uma series de booleanos com a mesma quantidade de linhas que
# o dataframe original




# Aula 13: Filtragem (Parte 2 de 5)
# vamos ver outro método para fazer aquilo
# é o método "Query", como se fizéssemos uma pergunta
# poderemos dizer "Me mostra apenas as linhas onde Estado = São Paulo"
print(data.query('ESTADO == "SAO PAULO"')) # a sintática é importante; como estamos comparando com a string Sao Paulo
# precisamos colocar a string dentro da string que é o argumento do .query

# uma boa prática é salvar o Data Frame filtrado em uma nova variável
# isso simplifica a complexidade do código para futuras análises pros postos de São Paulo
postos_sp = data.query('ESTADO == "SAO PAULO"') # o tipo é um DataFrame, não uma Series
# podemos, assim, fazer coisas como:
print(postos_sp.head())
print(postos_sp.shape)

# note, no entanto, que os registros após a filtragem permanecem os mesmos do DataFrame original
# em muitas situações manter essa informação é importante
# mas caso queiramos resetar os índices, podemos fazer:
print(postos_sp.reset_index()) # note que foi criada uma nova coluna chamada "index", com os índices originais
# caso isso não seja necessário, podemos passar o parâmetro drop=True:
print(postos_sp.reset_index(drop=True))
# note que isso tudo é mexer com uma cópia
# caso queiramos alterar o postos_sp original, passamos o argumento inplace=True
print(postos_sp.reset_index(drop=True, inplace=True))
print(postos_sp) # veja como esses dois são a mesma coisa, pois ele alterou o original

# a alternativa muito comum é fazer tudo de uma vez só
# veja:
postos_sp = data.query('ESTADO == "SAO PAULO"').reset_index(drop=True) # salvamos uma cópia já resetando os índices
print(postos_sp)




# Aula 14: Filtragem (Parte 3 de 5)
# vamos fazer mais comparações
# vamos selecionar os registros de postos do Rio de Janeiro com preços acima de 2 reais

# como sabemos, podemos criar um boolean só os do Rio de Janeiro fazendo:
print(data['ESTADO'] == 'RIO DE JANEIRO') 
# mas podemos adicionar o segundo argumento também:
print((data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0))
# IMPORTANTE!
# em Python, o "And" é dado por "&", não "&&" como é o normal
# em Python, o "Or" é dado por "|", não "||" como é o normal
# em Python, o "Not" é dado por "~", não "!" como é o normal

# prosseguindo:
selecao = (data['ESTADO'] == 'RIO DE JANEIRO') & (data['PREÇO MÉDIO REVENDA'] > 2.0)
print(data[selecao]) # o mesmo que já fizemos antes

# poderíamos usar o query também
# mas para esse caso, isso não é possível
# isso, pois o query não aceita caracteres inválidos (acento, cedilha)
# funcionaria, no entanto, algo tipo:
print(data.query('ESTADO == "RIO DE JANEIRO" or ESTADO == "SAO PAULO"')) # printa tudo do Rio e SP

# vamos nos aprofundar mais ainda:
# a primeira comparação, (data['ESTADO'] == 'RIO DE JANEIRO) checa, linha a linha, quais são aquelas que o Estado é o RJ
# como resultado, temos uma série de booleanos que respondem apenas a essa pergunta
# a segunda comparação, (data['PREÇO MÉDIO REVENDA'] > 2.0) checa, linha a linha, quais são aquelas com preço maior que 2
# como resultado, temos outra série de booleanos que respondem apenas a essa pergunta
# e daí as duas perguntas são unidas pelo AND (&), que retorna a pergunta completa

# essa abordagem é ineficiente
# mesmo que o Pandas temte otimizar isso ao máximo por detrás dos panos, se tivermos um dataset muito grande, a abordagem será lenta
# isso, pois os condicionais percorrem todas as 100 mil linhas só pra isso, duas vezes
# assim, poderíamos fazer filtragem com múltiplos condicionais em partes:

selecao_1 = data['ESTADO'] == 'RIO DE JANEIRO'
postos_rj = data[selecao_1] # se printarmos, teremos somente 4263 linhas
# agora, podemos fazer a segunda pergunta, sendo bem mais rápida pois há menos linhas:
selecao_2 = postos_rj['PREÇO MÉDIO REVENDA'] > 2

# e daí fazemos o postos_rj com a seleção, colocando ele em mais uma variável
postos_rj_preco_minimo = postos_rj[selecao_2]

print(postos_rj_preco_minimo) # isso agora retornará um dataframe com somente 3054 linhas, e de forma bem mais rápida




# Aula 15: Filtragem (Parte 4 de 5)

# agora, vamos fazer algo um pouco mais complexo
# vamos tentar selecionar os registros de São Paulo ou Rio de Janeiro com gasolina comum acima de 2 reais

# podemos fazer isso do jeito ineficiente, consultando o dataset inteiro 4 vezes:
selecao_variascoisa = data.query('ESTADO in ["SAO PAULO", "RIO DE JANEIRO"] and PRODUTO == "GASOLINA COMUM" and `PREÇO MÉDIO REVENDA` > 2.0')
# note que precisamos colocar o "PREÇO MÉDIO REVENDA" entre crases, pois há caracteres inválidos
print(selecao_variascoisa)

# ou, alternativamente:
selecao_1 = (data['ESTADO'] == "SAO PAULO") | (data['ESTADO'] == "RIO DE JANEIRO")
selecao_2 = data['PRODUTO'] == "GASOLINA COMUM"
selecao_3 = data['PREÇO MÉDIO REVENDA'] > 2.0

selecao_4 = selecao_1 & selecao_2 & selecao_3

sp_rj_preco_gasolina = data[selecao_4]

print(sp_rj_preco_gasolina)

# podemos confirmar também que tá tudo certinho, já que temos a filtragem
print(sp_rj_preco_gasolina['ESTADO'].unique()) # vai printar só SAO PAULO e RIO DE JANEIRO, já que só tem esses
print(sp_rj_preco_gasolina['PRODUTO'].unique()) # vai printar só gasolina

# agora, vamos fazer isso de um jeito mais eficiente
# porque atualmente, a seleção está checando o dataset inteiro de novo e de novo
# não queremos isso
# vamos fazer assim:
selecao_1 = (data['ESTADO'] == "SAO PAULO") | (data['ESTADO'] == "RIO DE JANEIRO") # temos um dataframe só com valores booleanos
postos_sp_rj = data[selecao_1] # convertemos os valores booleanos pra um dataset onde só tem Rio e São Paulo
selecao_2 = postos_sp_rj['PRODUTO'] == "GASOLINA COMUM" # temos agora um dataframe só com valores booleanos de novo
gasolina_sp_rj = postos_sp_rj[selecao_2] # convertemos pra um dataset onde só tem Rio e SP e só tem produto de gasolina
selecao_3 = gasolina_sp_rj['PREÇO MÉDIO REVENDA'] > 2.0 # criamos um último dataframe só com valores booleanos
dataset_final = gasolina_sp_rj[selecao_3] # criamos um último dataset só com as informações que queremos

print(dataset_final) # eba

# só pra garantir:
print(dataset_final['ESTADO'].unique()) # vai printar só SAO PAULO e RIO DE JANEIRO, já que só tem esses
print(dataset_final['PRODUTO'].unique()) # vai printar só gasolina




# Aula 16: Filtragem (Parte 5 de 5)
# agora, vamos selecionar só as informações dos anos de 2008, 2010 e 2012
# alternativa #1:
selecao = (data['ANO'] == 2008) | (data['ANO'] == 2010) | (data['ANO'] == 2012)
print(data[selecao]) 

# se eu quisesse, além de selecionar somente as informações desses 3 anos, selecionar somente uma coluna, podemos dar um segundo arg
print(data[selecao]['ANO'])
# podemos confirmar, ainda, que os anos são somente 2008, 2010 e 2012 fazendo assim:
print(data[selecao]['ANO'].unique()) # printa 2008 2010 2012, mostrando que só tem esses anos

# alternativa #2:
# usamos .isin (is in, ou seja, está dentro) para checar se o ano está dentro da lista de valores de anos
lista_anos = [2008, 2010, 2012]
selecao = data['ANO'].isin(lista_anos) # retorna uma lista de booleanos que respondem com True caso esteja dentro da lista
print(data[selecao])

# alternativa #3
# usamos o query:
print(data.query('ANO in @lista_anos')) # olha como é feixa a sintaxe, usando @ pra citar o array lista_anos

### iterando com DataFrames ###
# podemos usar o "for-each DataFrame.iterrows()", mas ele é bem lento; só é indicado para iterar pequenos conjuntos de dados
# se tentássemos rodar com o data inteiro, demoraria aproximadamente 2 minutos pra rodar o trecho de código abaixo
# por isso, vamos fazer com só o topo do data, os primeiros 10 índices. data.head(10)
for index, row in data.head(10).iterrows():     # leia: para cada índice e coluna no data.head
    print(f'Índice: {index} ==> {row}')         # printa o índice e depois printa todas as colunas e seus valores
    
# poderíamos printar só uma coluna, caso estejamos interessados só em uma:
for index, row in data.head(10).iterrows():
    print(f"Índice: {index} => {row['ESTADO']}") # aqui vamos printar só a coluna estado para cada índice
    



# Aula 17: Limpeza de Dados (Parte 1 de 2)
# quando usamos data.info(), vemos que não há nenhum valor que seja NaN/Null
# mas isso não é bem verdadeiro
print(data.info())
# o Pandas automaticamente reconhece os tipos de dados de cada coluna
# porém tem alguns atributos que estão com seus tipos errados.
# Ex: "PREÇO MÉDIO DISTRIBUIÇÃO" deveria ser float64, e não object
# nesses casos, alguns registros tem uma string ao invés de um número

# os atributos "DATA INICIAL" e "DATA FINAL" deveriam ser do tipo datetime
# em outros casos, alguns atributos categóricos são objects, mas poderiam ser do tipo category, um tipo especial do pandas
# esse tipo é necessário pra se utilizar algumas funções específicas do pandas
# mas não converteremos para este tipo por ora

# vamos criar uma cópia do dataframe pra não alterar o original:
data_pre = data.copy()
# como os atributos de data do dataset já estão em um formato aceitável (YYYY-MM-DD), não precisamos converter nesse sentido
# podemos só converter direto
data_pre['DATA INICIAL'] = pd.to_datetime(data_pre['DATA INICIAL']) # o to_datetime retorna uma series com as datas convertidas certinha
data_pre['DATA FINAL'] = pd.to_datetime(data_pre['DATA FINAL'])

print(data_pre['DATA FINAL'])
print(data_pre['DATA INICIAL'])

# Dados Numéricos
# agora que o bicho pega
# temos alguns atributos que deveriam ser numéricos
# podemos usar o pandas.to_numeric, vamos ver logo logo
print(data_pre.info())
# analisando, vemos que temos algumas colunas que devemos transformar de object pra numérico
# como a margem media de revenda, preço médio distribuição, desvio padrão, preço mínimo, preço máximo e coeficiente de variação

# vamos fazer uma lista:
lista_alterar = ['MARGEM MÉDIA REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO', 'DESVIO PADRÃO DISTRIBUIÇÃO', 'PREÇO MÍNIMO DISTRIBUIÇÃO', 'PREÇO MÁXIMO DISTRIBUIÇÃO', 'COEF DE VARIAÇÃO DISTRIBUIÇÃO']
# vamos converter cada um dos atributos da lista pra numérico e alterar os valores originais
# o to_numeric, além de passar o que vai ser alterado, também deve-se passar o que fazer em caso de erro
# ex de erro: encontrar uma string que não representa um número
# existem 3 opções:
# errors='raise' => vai criar uma exceção e te cuspir no CMD
# errors='coerce' => os valores que tiver erro vão ser setados pra NaN (Not a Number)
# errors='ignore' => os valores que tiver erro vão continuar iguais

# vamos usar coerce
for atributo in lista_alterar:
    data_pre[atributo] = pd.to_numeric(data_pre[atributo], errors='coerce') 

print(data_pre.info()) # opa! agora os atributos que a gente alterou tem alguns valores nulos
# note que anteriormente estava 106823 non-null
# agora, está 103423 non-null
# ou seja, aproximadamente 3 mil e 400 atributos ficaram NaN
# vamos resolver isso




# Aula 18: Limpeza de Dados (Parte 2 de 2)
# vamos checar com mais cuidados nos dados originais e preprocessados

# vamos usar a função .isnull pra retornar uma series de booleanos com true(se for null) ou false
eh_null = data_pre['PREÇO MÉDIO DISTRIBUIÇÃO'].isnull()
print(data_pre[eh_null]) # hmmm... vamos checar o que que tinha nos dados originais
print(data[eh_null]) # opa! o preço médio de distribuição e etc tinham valores com tracinhos
# então apesar de não ter um 0 ou um valor nulo, a pessoa que fez o dataset colocou tracinho
# ou seja, na prática, apesar do data.info() retornar nenhum valor nulo, na prática não é verdade

# vamos tratar esses valores com NaN
# como vamos tratar o NaN vai depender do problema em questão
# inicialmente, poderíamos preencher os valores NaN com um valor padrão
# para isso, basta usar o método .fillna
# vamos, pra todos os valores nulos, eu vou colocar 0
data_pre_fill = data_pre.fillna(0) # ele retorna uma cópia do data frame 'data_pre' com todos os valores NaN de todas as colunas preenchidos com 0
# se eu quisesse alterar o próprio data frame, usaríamos o inplace='True'

print(data_pre_fill[eh_null]) # agora os valores que antes eram NaN são 0

# note que o dado original (data_pre) não alterou, já que passamos uma cópia

# outra coisa que podemos fazer é dar valores constantes diferentes pra cada coluna que tá com NaN
# usando fillna, podemos passar um dicionário com os valores de cada coluna que vamos colocar:
data_pre_fill = data_pre.fillna(value={
    'PREÇO MÉDIO DISTRIBUIÇÃO': 10,
    'DESVIO PADRÃO DISTRIBUIÇÃO': 20,
    'PREÇO MÍNIMO DISTRIBUIÇÃO': 30,
    'PREÇO MÁXIMO DISTRIBUIÇÃO': 'vazio'
})
print(data_pre_fill[eh_null]) # agora os valores que antes eram NaN foram alterados (com exceção do Coef de Variação Distribuição)

# por mais que a função fillna seja interessante e muito útil em diversos casos, no problema em questão queremos analisar precisamente,
# por exemplo, o "PREÇO MÉDIO DISTRIBUIÇÃO"
# nesse caso, não queremos ter valores sintéticos gerados pelo .fillna
# então vamos remover todos os valores NaN usando a função .dropna

data_pre.dropna(inplace=True) # remove, no próprio dataframe, todas as linhas de valores NaN em quaisquer colunas
print(data_pre.info) # agora só temos as linhas que não tem nenhum registro nulo
# por isso, agora só há apenas 103392 linhas, enquanto antes tinha 106822
# então limpamos o data frame, ou seja, deixamos ele mais enxuto

# essas são apenas algumas das técnicas de limpeza
# existem alguns outros pontos que deveríamos checar no dataset
# mas são técnicas mais avançadas, como a detecção de outliers, que não veremos aqui nesse curso

# vamos salvar o csv pré processado agora
data_pre.to_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019_preprocessadoFINAL.csv', index=False) # index = false pra n ter o unnamed: 0




# Aula 19: Estatísticas Descritivas

# vamos ver aqui como aplicar os conceitos ali de estatística e tals
# vamos primeiro ler o preprocessado
data_final = pd.read_csv('./py/análise de dados/dataset/GasPricesinBrazil_2004-2019_preprocessadoFINAL.csv')
print(data_final)

# usando .describe(), ele vai nos dar algumas estatísticas descritivas de cada coluna
# cada estatística é uma medida
# temos:
# count(contagem) => quantidade de linhas
# mean(média) => média duh
# std(desvio padrão) => o desvio padrão
# 25% => primeiro quartil
# 50% => segundo quartil (mediana)
# 75% => terceiro quartil
# max(máximo) => maior valor

print(data_final.describe())

# como o describe de um dataframe é outro dataframe, podemos filtrar apenas algumas colunas
print(data_final.describe()['PREÇO MÉDIO REVENDA'])

# note que tanto faz colocar o describe() antes ou depois da filtragem. Ou seja, os dois aqui funcionam da mesma forma:
print(data_final.describe()[['PREÇO MÉDIO REVENDA', 'PREÇO MÁXIMO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO']])
print(data_final[['PREÇO MÉDIO REVENDA', 'PREÇO MÁXIMO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO']].describe())
# tecnicamente, o segundo seria melhor, já que você está primeiro filtrando e daí o describe tem que iterar só pelo dataset filtrado
# o primeiro, primeiro o describe vê todas as 103 mil linhas e depois você filtra
# então o segundo seria mais otimizado
# mas os dois funcionam

# Acessando apenas algumas estatísticas:
# se quiséssemos acessar somente, a exemplo, a média, o mínimo e o máximo
# como queremos acessar a linha, a gente usa o .loc
# (usaríamos o iloc, mas nesse caso, o índice das linhas são strings (count, mean, std etc), não números (0, 1, 2, 3...))
print(data_final.describe().loc[['mean', 'min', 'max']])
# se quisermos filtrar não apenas pelas linhas, mas pela coluna:
print(data_final.describe().loc[['mean', 'min', 'max'], 'PREÇO MÉDIO REVENDA'])
print(data_final.describe().loc[['mean', 'min', 'max'], ['PREÇO MÉDIO REVENDA', 'PREÇO MÉDIO DISTRIBUIÇÃO']])

# isso é muito importante porque muitas vezes a gente quer só achar uma coisa só
# tipo "Ah, qual é o menor preço mínimo de revenda?"
print(data_final.describe().loc['min', 'PREÇO MÍNIMO REVENDA']) # pronto, 0.59
# "Qual é a média e desvio padrão dos preços mínimos de revenda?"
print(data_final.describe().loc[['mean', 'std'], 'PREÇO MÍNIMO REVENDA']) # pronto, 9.3 e 15.0
# "Quais são os estados considerados?"
print(data_final['ESTADO'].unique()) # perfeito
# (e se quisermos que fique bonitinho, podemos fazer assim:)
print(sorted(data_final['ESTADO'].unique()))

# por fim, podemos também usar a função .value_counts() para contar a frequência dos valores de cada variável
print(data_final['ESTADO'].value_counts()) # retorna em ordem decrescente uma series com as informações certinhas
# podemos também usar to_frame pra retornar um dataframe ao invés de uma series
print(data_final['ESTADO'].value_counts().to_frame)




# Aula 20: Apply e Map
# Uma alternativa ao for-loop, que vimos anteriormente e é lento, é usarmos funções próprias do pandam que aplicam uma dada função
# a todos os elementos de um DataFrame ou Series, retornando novos elementos "transformados"
# Apply: Funciona com *DataFrame* e com *Series*. É o método padrão, normalmente se usa ele
# Map: Funciona só com *Series*
# Applymap: Funciona só com *DataFrame*

df = pd.DataFrame({'A': [1, 2, 3, 4],
                   'B': [10, 20, 30, 40],
                   'C': [100, 200, 300, 400]},
                   index=['Linha 1', 'Linha 2', 'Linha 3', 'Linha 4'])

# o apply() é usado para aplicar uma função ao longo de um eixo de um DataFrame ou em valores de uma series
# "O que é um eixo?"
# quando dizemos eixo = 0, queremos dizer que vamos navegar pelas *linhas* de determinada coluna. Ou seja, navegaremos verticalmente
# quando dizemos eixo = 1, queremos dizer que vamos navegar pelas *colunas* de determinada linha. Ou seja, navegaremos horizontalmente

print(df)
# o DF está no formato:
#           A   B   C
#Linha 1    1   10  100
#Linha 2    2   20  200
#Linha 3    3   30  300
#Linha 4    4   40  400

# vamos definir uma função customizada:
def nossa_soma(linha):
    return linha.sum() # retorna a soma de todos os valores de uma linha

# agora, eu posso pegar o nosso dataframe df e falar
df.apply(nossa_soma, axis=1) # "pega as nossas linhas e soma elas aí, por favor"
# vamos ver oq printa:
print(df.apply(nossa_soma, axis=1)) 
# printa, corretamente, a soma da linha 1, depois a soma da linha 2, da 3 e da 4
print(df.apply(nossa_soma, axis=0))

# podemos, ainda, criar uma nova linha/coluna e colocar a soma lá
df.loc['Linha 5'] = df.apply(nossa_soma, axis=0)
df['SOMA (A, B, C)'] = df.apply(nossa_soma, axis=1)
print(df)
# ele printou:
#          A    B     C  SOMA (A, B, C)
#Linha 1   1   10   100             111
#Linha 2   2   20   200             222
#Linha 3   3   30   300             333
#Linha 4   4   40   400             444
#Linha 5  10  100  1000            1110

# também podemos usar funções temporárias, tbm chamadas de funções lambdas:
# suponhamos que queiramos fazer uma nova coluna com a média de A, B, C
# queremos ignorar a nova coluna "Soma (A, B, C)" e mexer só com as colunas A, B e C

# primeiro, vamos fazer uma filtragem aqui
# df[['A', 'B', 'C']]
# daí eu uso o apply com o trocinho de média
# df[['A', 'B', 'C']].apply(lambda series: series.mean())
# por fim, como eu queiro que seja a média das linhas, eu preciso colocar o eixo
print(df[['A', 'B', 'C']].apply(lambda series: series.mean(), axis=1))
# vai printar um series com a coluna com as médias
# daí basta colocar ali numa nova coluna
df['MÉDIA (A, B, C)'] = df[['A', 'B', 'C']].apply(lambda series: series.mean(), axis=1)
print(df)

# agora vamos supor que eu queira aplicar a lambda function pra cada elemento da coluna
# por exemplo, suponhamos que pra cada um dos elementos de C eu queira saber o dobro, e colocar as respostas numa coluna
df['C * 2'] = df['C']. apply(lambda x: 2*x)
# (obviamente poderíamos também fazer de um jeito mais fácil)
# tipo: df['A * 2'] = df['A'] * 2
# aquilo ali em cima é só um exemplo

# vamos ver o applymap(), que é usado pra aplicar uma função para cada elemento de um DataFrame

# exemplo: vamos fazer um novo dataframe com todos os elementos ao quadrado
# poderíamos usar uma função ao invés de uma lambda function, mas foda-se
print(df.applymap(lambda x: x ** 2)) # nota que ele retorna sempre uma cópia, nunca altera o dataframe original

# vamos usar o map() agora, que é usado para aplicar uma função para cada elemento de uma series
# suponha uma series de nomes:
nomes = pd.Series(['João', 'Maria', 'Alice', 'Pedro'])
# se printarmos, fica:
# 0     João
# 1    Maria
# 2    Alice
# 3    Pedro

# agora, vamos usar o map() pra retornar uma nova Series com todos os nomes com letras maiúsculas
# novamente, poderíamos usar uma função ao invés de uma lambda function, mas foda-se
print(nomes.map(lambda x: x.upper()))

# (poderíamos fazer isso de um jeito mais fácil, pois o Pandas já fornece uma série de métodos pra manipulação de strings)
# assim, poderíamos usar o código abaixo pra obter o mesmo resultado:
print(nomes.str.upper())




# Aula 21: Agrupamento (Parte 1 de 2)
# podemos, às vezes, querer agrupar diversas informações de um mesmo estado ou de uma mesma região
# a exemplo:
grupos = data_final.groupby('REGIÃO')
print(grupos.groups) # isso vai retornar para a gente um dicionário com todos os grupos e em quais índices estão elementos com aquele grupo
# podemos ver como um array ao invés de um dicionário:
print(grupos.indices)

# podemos usar o get_group pra pegar só um determinado grupo
print(grupos.get_group('CENTRO OESTE')) # vai retornar para a gente um DataFrame só com os do Centro Oeste

# podemos, ainda, usar umas funções para os grupos
# exemplo, podemos usar o describe para descrever algumas estatísticas descritivas para as observações de cada grupo
print(grupos.describe()) # dá um dataframe gigante, mas dá de boas
# podemos também pegar só a média, por exemplo
print(grupos.mean(numeric_only=True)) # precisa passar o numeric_only, senão dá erro pq ele tenta achar a média de datas
# poderíamos fazer algo mais diretão:
print(data_final.groupby('REGIÃO').min(numeric_only=True))




# Aula 22: Agrupamento (Parte 2 de 2)
# também podemos agrupar por mais de um atributo, ou seja, agrupar por mais de uma coluna

# vamos perguntar: qual é o preço médio de cada produto (combustível) para cada Região do Brasil?
# pra esse caso, precisamos fazer um agrupamento para cada região, daí fazer um segundo agrupamento para os diferentes produtos
# (etanol, gasolina, etc) e então por fim pegar só a média
# podemos fazer de um jeito mais simples:
grupos = data_final.groupby(['REGIÃO', 'PRODUTO']) # passamos uma lista de strings ao invés de uma string só
grupos['PREÇO MÉDIO REVENDA'].mean(numeric_only=True) # e pegamos a média dos grupos
print(grupos['PREÇO MÉDIO REVENDA'].mean(numeric_only=True)) # printamos isso

# também poderíamos fazer de uma vez só:
print(data_final.groupby(['REGIÃO', 'PRODUTO'])['PREÇO MÉDIO REVENDA'].mean(numeric_only=True))

# vamo checar como tá o grupos:
print(grupos['PREÇO MÉDIO REVENDA'].describe())

# enfim, também existe o .agg, que agrega(roda) uma série de funções para os elementos de um dataframe ou de grupos de um dataframe
# suponha o dataframe:
df = pd.DataFrame([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9],
                   [None, None, None]],
                  columns=['A', 'B', 'C'])

print(df)

# vamos usar o .agg para checar a soma dos valores e o mínimo de cada coluna
print(df.agg(["sum", "min"])) # retorna a soma e o menor valor dos dois, e ignora os NaN

# e quando eu passo um grupo?
grupos = data_final.groupby('REGIÃO')
# por região, apenas na coluna do preço médio de revenda,
grupos['PREÇO MÉDIO REVENDA'].agg(["min", "max"]) # me diga qual o valor máximo e mínimo
print(grupos['PREÇO MÉDIO REVENDA'].agg(["min", "max"]))




# Aula 23: Ordenação
# suponha o seguinte dataframe:
notas = pd.DataFrame({
    'nomes': ['João', 'Maria', 'José', 'Alice'],
    'Idade': [20, 21, 19, 20],
    'nota final': [5.0, 10.0, 6.0, 10.0]
})
print(notas)

# .sort_values(): ordena valores ao longo de um eixo
# utiliza-se o argumento "by=" pra dizer pelo o quê vamos ordenar
print(notas.sort_values(by='nota final'))
# por padrão, o método retorna uma cópia dos dados ordenados em ordem crescente. Podemos alterar isso pelo argumento "ascending=False"
print(notas.sort_values(by='nota final', ascending=False)) # ele cria uma cópia só com as linhas swapadas
# ele inclusive coloca os índices na ordem original. Se quisermos resetar os índices, adicionamos .reset_index(drop=True)
print(notas.sort_values(by='nota final', ascending=False).reset_index(drop=True))

# suponhamos que, se temos alunos com nota empatada, queiramos ordenar por ordem alfabética:
print(notas.sort_values(by=['nota final', 'nomes'], ascending=[False, True]))
# ele vai ordenar, primeiramente, pela coluna "nota_final" em ordem decrescente
# e então reordenar os registros empatados em ordem alfabética em ordem crescente (alfabética)
# note que o .sort_values retorna uma cópia, ou seja, o dataframe original não foi alterado
# colocariamos o inplace=True para que altere o próprio dataframe
notas.sort_values(by=['nota final', 'nomes'], ascending=[False, True], inplace=True)
# vamos resetar os índices:
notas.reset_index(drop=True, inplace=True)
# poderíamos, também, fazer tudo em uma linha só:
notas = notas.sort_values(by=['nota final', 'nomes'], ascending=[False, True]).reset_index(drop=True)
# (temos que tirar o inplace pq senão o reset_index não funciona)
print(notas)




# Aula 24: Exercícios
# vamos usar o dataset de preços de combustíveis no Brasil
# Exercício 1: Como há apenas medições de janeiro a junho do ano de 2019, vamos remover os dados desse ano, que tal?
selecao = data_final['ANO'] != 2019
data_sem2019 = data_final[selecao].reset_index(drop=True)
print(data_sem2019)

# ou:
data_sem2019 = data_final.query('ANO != 2019')
print(data_sem2019)

# Exercício 2: Qual a quantidade de registros de cada produto em cada região?
grupos = data_final.groupby('PRODUTO')
print(grupos['REGIÃO'].value_counts().to_frame())

# ou
print(data_final.groupby('PRODUTO')['REGIÃO'].value_counts().to_frame())

# Exercício 3: Como os preços da Gasolina Comum em São Paulo variaram em 2018?
sp = data_final.query('ESTADO == "SAO PAULO"')
sp_gasolina_comum = sp.query('PRODUTO == "GASOLINA COMUM"')
sp_gasolina_2018 = sp_gasolina_comum.query('ANO == 2018')
variacao_sp_gasolina2018 = sp_gasolina_2018['PREÇO MÉDIO REVENDA'].describe().to_frame()
print(variacao_sp_gasolina2018)

# ou
variacao_sp_gasolina2018 = data_final.query('ESTADO == "SAO PAULO" and PRODUTO == "GASOLINA COMUM" and ANO == 2018')['PREÇO MÉDIO REVENDA'].describe().to_frame()
print(variacao_sp_gasolina2018)
# (teoricamente, menos otimal, já que ele vai percorrer o dataset final inteiro várias vezes)

# Exercício 4: Como os preços da Gasolina Comum e o Etanol variaram em São Paulo em 2018?
# considerando os preços do Etanol e da Gasolina *JUNTOS*, temos essas estatísticas descritivas
sp = data_final.query('ESTADO == "SAO PAULO"')
sp_gasolina_comum = sp.query('PRODUTO == "GASOLINA COMUM" or PRODUTO == "ETANOL HIDRATADO"')
sp_gasolina_2018 = sp_gasolina_comum.query('ANO == 2018')
variacao_sp_gasolina2018 = sp_gasolina_2018['PREÇO MÉDIO REVENDA'].describe().to_frame()
print(variacao_sp_gasolina2018)

# ou
variacao_sp_gasolina2018 = data_final.query('ESTADO == "SAO PAULO" and (PRODUTO == "GASOLINA COMUM" or PRODUTO == "ETANOL HIDRATADO") and ANO == 2018')['PREÇO MÉDIO REVENDA'].describe().to_frame()
print(variacao_sp_gasolina2018)
