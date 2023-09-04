import math
começo = 0
i = começo
fim = 4*math.pi
auto_intersecao = 0
coordenadas_autointerseção = []
pontos_interseção_x = []
pontos_interseção_y = []
lista_pontos = []
coordenadas_autointerseção_prontas =[]



def gama_x(t):

    x = 5*math.cos(math.radians(t)) - 4*math.cos(math.radians((5*t)/2))

    return x

def gama_y(t):

    y = 5*math.sin(math.radians(t)) - 4*math.sin(math.radians((5*t)/2))

    return y


while i < fim:
    lista_pontos.append([gama_x(i),gama_y(i)])

    i+= 0.001

for j in lista_pontos:
    for h in lista_pontos:
        if j == h and lista_pontos.index(j) != lista_pontos.index(h):
            print('BRUH')
            coordenadas_autointerseção.append(j)

set = set(tuple(row) for row in lista_pontos)
coordenadas_autointerseção_prontas = list(set)
auto_intersecao = len(coordenadas_autointerseção_prontas)
            

print('ACABOU')
#print(coordenadas_autointerseção_prontas)
print(auto_intersecao)







