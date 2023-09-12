import math 
from matplotlib import pyplot as plt
import sympy as sp
import numpy as np
from alive_progress import alive_bar
import time



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

def compute():
    print('Computing points:\n')
    fim = 2*math.pi
    with alive_bar((int((2*math.pi)/0.001)**2)) as bar:  # your expected total
        for i in np.arange(0,fim,0.001):
            lista_pontos.append([gama_x(i),gama_y(i)])
            bar() 
    print('Done\n')

compute()

lista_pontos_tuple = [tuple(row) for row in lista_pontos]


#index retorna so 1 ocorrencia, usar um metodo que retorna todas os index de ocorrencias nas listas e faz um slice na lista e checa se tem um ponto naquele intervalo pra tras ou pra frente, se sim achou uma auto interceção. OBS: as slices n podem incluir o proprio ponto.
def compute2():
    print('Computing auto intersecting points:\n')
    fim = 2*math.pi
    with alive_bar((int((2*math.pi)/0.001)**2)) as bar:  # your expected total
        array = np.array(lista_pontos_tuple)
        for i in lista_pontos_tuple:
            lista_pontos_tuple.remove(i)
            if i in lista_pontos_tuple and i not in coordenadas_autointerseção:
                coordenadas_autointerseção.append(i)
            bar() 
    print('Done\n')


auto_intersecao = len(coordenadas_autointerseção)

compute2()

t = sp.Symbol('t')
function_x = sp.sympify('8*cos(t) - 5*cos(4*t)')
function_y = sp.sympify('8*sin(t) - 5*sin(4*t)')

interval = np.arange(0, 2*math.pi, 0.001)

x_values = [function_x.subs(t, value) for value in interval]
y_values = [function_y.subs(t, value) for value in interval]


plt.figure(figsize=(10, 10))
plt.plot(x_values, y_values)

#for i in coordenadas_autointerseção_prontas:
    #plt.scatter(i[0], i[1], color="red")

plt.show()

            

#print('ACABOU')
print(coordenadas_autointerseção_prontas)
print(auto_intersecao)







