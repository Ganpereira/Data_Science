
import csv
import matplotlib.pyplot as plt



# Vamos ler os dados como uma lista (OK)
print("Lendo o documento...")
with open("chicago.csv", "r") as file_read:
    reader = csv.reader(file_read)
    data_list = list(reader)
print("Ok!")

# Vamos verificar quantas linhas nós temos (OK 1.551.506)
print("Número de linhas:")
print(len(data_list))



# Imprimindo a primeira linha de data_list para verificar se funcionou. (OK)
print("Linha 0: ")
print(data_list[0])
# É o cabeçalho dos dados, para que possamos identificar as colunas.


# Imprimindo a segunda linha de data_list, ela deveria conter alguns dados (OK)
print("Linha 1: ")
print(data_list[1])


input("Aperte Enter para continuar...")
# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop para identificar os dados.
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")

''' O iterador linha percorre a tabela data_list e efetua a busca dentro do range
entre a primeira linha, após o cabeçalho até a linha 21'''

for linha in data_list[1:21]:
    print(linha)


# Vamos mudar o data_list para remover o cabeçalho dele.
data_list = data_list[1:]

# Nós podemos acessar as features pelo índice
# Por exemplo: sample[6] para imprimir gênero, ou sample[-2]

input("Aperte Enter para continuar...")


# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas

print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")



for linha in data_list[1:21]:
    print(linha[6])


# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros

input("Aperte Enter para continuar...")
# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) de uma lista em outra lista, na mesma ordem



def column_to_list(data, index):
    ''' Itera uma determinada lista e indexa uma coluna em uma outra lista.

    INPUT:
    data: representa os dados buscados
    index: representa os dados aplicados de acordo com o indice

    OUTPUT:
    Uma lista com os valores adicionados
    '''
    column_list = []
    for lista in data:
        column_list.append(lista[index])



    # Dica: Você pode usar um for para iterar sobre as amostras, pegar a feature pelo seu índice, e dar append para uma lista
    return column_list



# Vamos checar com os gêneros se isso está funcionando (apenas para os primeiros 20)
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, -2)[1:21])
print(len(column_to_list(data_list, -2)))
print('VALIDAR ESTE ITEM COM O MONITOR')
# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, -2)) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, -2)) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, -2)[0] == "" and column_to_list(data_list, -2)[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------




input("Aperte Enter para continuar...")
# Agora sabemos como acessar as features, vamos contar quantos Male (Masculinos) e Female (Femininos) o dataset tem
# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
vazio = 0

for i in data_list:
    if i[-2] == "Male":
        male += 1
    elif i[-2] == "Female":
        female += 1
    else:
        vazio += 1

print(vazio)
print(male)
print(female)


# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------




# Ótimo! Nós podemos pegar as linhas(samples) iterando com um for, e as colunas(features) por índices.
# Mas ainda é difícil pegar uma coluna em uma lista. Exemplo: Lista com todos os gêneros



input("Aperte Enter para continuar...")
# Por que nós não criamos uma função para isso?
# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista.
# Isso deveria retornar uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)


def count_gender(data_list):
    ''' Conta quantas vezes o genero se repete'''
    male = 0
    female = 0
    for i in data_list:
        if i[-2] == 'Male':
            male += 1
        elif i[-2] == 'Female':
            female += 1

    return [male, female]


print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"



input("Aperte Enter para continuar...")
# Agora que nós podemos contar os usuários, qual gênero é mais prevalente?
# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Male", "Female", ou "Equal" como resposta.



def most_popular_gender(data_list):
    ''' Retorna qual o genero mais popular'''

    answer = ""
    c_gender = count_gender(data_list)
    if c_gender[0] > c_gender[1]:
        answer = 'Male'
    elif c_gender[0] < c_gender[1]:
        answer = 'Female'
    elif c_gender[0] == c_gender[1]:
        answer = 'Equal'

    return answer


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))


#Se tudo está rodando como esperado, verifique este gráfico!
gender_list = column_to_list(data_list, -2)
types = ["Male", "Female"]
quantity = count_gender(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantity)
plt.ylabel('Quantidade')
plt.xlabel('Gênero')
plt.xticks(y_pos, types)
plt.title('Quantidade por Gênero')
plt.show(block=True)


 #------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Male", "TAREFA 6: Resultado de retorno incorreto!"



input("Aperte Enter para continuar...")
# TAREFA 7
# TODO: Crie um gráfico similar para user_types. Tenha certeza que a legenda está correta.
print("\nTAREFA 7: Verifique o gráfico!")



def count_user_type(data_list):
    ''' Conta a quantidade de tipos de usuário. '''
    customer = 0
    subscriber = 0
    for i in data_list:
        if i[-3] == 'Customer':
            customer += 1
        elif i[-3] == 'Subscriber':
            subscriber += 1

    return [customer, subscriber]

# Se tudo está rodando como esperado, verifique este gráfico!
user_list = column_to_list(data_list, -3)
types = ["Customer", "Subscriber"]
quantidade = count_user_type(data_list)
y_pos = list(range(len(types)))
plt.bar(y_pos, quantidade)
plt.ylabel('Quantidade')
plt.xlabel('Tipo')
plt.xticks(y_pos, types)
plt.title('Quantidade por Tipo de Usuário')
plt.show(block=True)



input("Aperte Enter para continuar...")
# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Isso está ocorrendo devido a soma dos generos masculinos e femininos não estarem iguais ao total, pois no .csv data_list constam 316867 itens vazios."
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------


input("Aperte Enter para continuar...")
# Vamos trabalhar com trip_duration (duração da viagem) agora. Não conseguimos tirar alguns valores dele.
# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas para isso, como max() e min().
trip_duration_list = column_to_list(data_list, 2)
min_trip = 0
max_trip = 0
mean_trip = 0
median_trip = 0

for trip_duration in trip_duration_list:

	trip_duration = int(trip_duration)
	duracao = trip_duration

	if min_trip == 0:
		min_trip = trip_duration
	if max_trip == 0:
		max_trip = trip_duration
	if trip_duration < min_trip:
		min_trip = trip_duration
	if trip_duration > max_trip:
		max_trip = trip_duration


'''utilizei a logica aplicada para geração da media deste exercicio
consultando em: https://bit.ly/2LT3aDk '''

trip_duration_list = column_to_list(data_list, 2)
trip_duration_list = [int(time) for time in trip_duration_list]
def calcular_total(lista):
    amount = 0
    for value in lista:
        amount += value
    return amount

trip_total_duration = calcular_total(trip_duration_list)
mean_trip = round(trip_total_duration/len(trip_duration_list))

itens = len(trip_duration_list)
sorted_list = sorted(trip_duration_list, key = int)

#if itens / 2 == 0:
#    median_trip = sorted_list[round((itens / 2))]
#else:
#    median_trip = sorted_list[int(itens / 2)]

if itens % 2 == 0:
    median_trip = (float(sorted_list[(itens // 2)]) + float(sorted_list[itens//2 -1])) / 2
else:
    median_trip = float(sorted_list[int(itens // 2)])

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# --------------------------------------------------


input("Aperte Enter para continuar...")
# TAREFA 10
# Gênero é fácil porque nós temos apenas algumas opções. E quanto a start_stations? Quantas opções ele tem?
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
start_stations = set(column_to_list(data_list, 3))

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(start_stations))
print(start_stations)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(start_stations) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------


input("Aperte Enter para continuar...")
# TAREFA 11
# Volte e tenha certeza que você documentou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
