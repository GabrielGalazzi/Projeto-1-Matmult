import math
import matplotlib
começo = 0
i = começo
fim = 2*math.pi
tolerancia = 1*10**(-30)
auto_intersecao = 0
coordenadas_autointerseção = []
pontos_interseção_x = []
pontos_interseção_y = []
lista_pontos = []
coordenadas_autointerseção_prontas =[]



def gama_x(t):

    x = 8*math.cos(math.radians(t)) - 5*math.cos(math.radians((4*t)))

    return x

def gama_y(t):

    y = 8*math.sin(math.radians(t)) - 5*math.sin(math.radians((4*t)))

    return y


while i < fim:
    lista_pontos.append([gama_x(i),gama_y(i)])

    i+= 0.001

for j in lista_pontos:
    for h in lista_pontos:
        if ((j == h and lista_pontos.index(j) != lista_pontos.index(h))) or (((((j[0] == h[0] + tolerancia and j[1] == h[1] + tolerancia) or (j[0] == h[0] - tolerancia and j[1] == h[1] - tolerancia))or (j[0] == h[0] - tolerancia and j[1] == h[1] + tolerancia) or (j[0] == h[0] + tolerancia and j[1] == h[1] - tolerancia)) and lista_pontos.index(j) != lista_pontos.index(h))):
            #print('BRUH')
            #ajeitar tolerancia (diminuir)
            #encrontrar um jeito de implantar ambas tolerancias (+- tolerancia) ao mesmo tempo (ver codigo de chava da prova de dessof 2021.2)
            coordenadas_autointerseção.append(j)

set = set(tuple(row) for row in lista_pontos) # por equanto não funciona pois perde-se a ordem dos pontos, mas em teoria isso deixa os pontos unicos na lista de coordenadas.
coordenadas_autointerseção_prontas = list(set)
auto_intersecao = len(coordenadas_autointerseção_prontas)
x_plot = lista_pontos[:,0]
y_plot = lista_pontos[:,1]
matplotlib.plot(x_plot,y_plot)
matplotlib.show()
            

#print('ACABOU')
#print(coordenadas_autointerseção_prontas)
#print(auto_intersecao)







