import math 
from matplotlib import pyplot as plt
import sympy as sp
import numpy as np
from alive_progress import alive_bar
import time


auto_intersecao = 0
coordenadas_autointerseção = []
pontos_interseção_x = []
pontos_interseção_y = []
lista_pontos = []

interval = np.arange(0, 2*math.pi, 0.001)
interval = interval.tolist()



x_values = []
y_values = []

t = sp.Symbol('t')
fx = '8*cos(t) - 5*cos(4*t)'
fy = '8*sin(t) - 5*sin(4*t)'

fxlinha = sp.diff(fx,t)
fylinha = sp.diff(fy,t)

fxlinhalinha = sp.diff(fxlinha,t)
fylinhalinha = sp.diff(fylinha,t)

print(fxlinhalinha)



def gama_x(t):

    x = 8*math.cos(math.radians(t)) - 5*math.cos(math.radians((4*t)))

    return x

def gama_y(t):

    y = 8*math.sin(math.radians(t)) - 5*math.sin(math.radians((4*t)))

    return y

def compute():
    print('Computing points:\n')
    fim = 2*math.pi
    with alive_bar(6284) as bar:  # your expected total
        for i in np.arange(0,fim,0.001):
            lista_pontos.append([gama_x(i),gama_y(i)])
            bar() 
    print('Done\n')

compute()

lista_pontos_tuple = [tuple(row) for row in lista_pontos]


#index retorna so 1 ocorrencia, usar um metodo que retorna todas os index de ocorrencias nas listas e faz um slice na lista e checa se tem um ponto naquele intervalo pra tras ou pra frente, se sim achou uma auto interceção. OBS: as slices n podem incluir o proprio ponto.
def compute2():
    print('Computing auto intersecting points:\n')
    with alive_bar(6284) as bar:  # your expected total
        array = np.array(lista_pontos_tuple)
        for i in range(len(interval)):
            
            

            d2x1 = fxlinha.subs(t, interval[i])
            d2y1 = fylinha.subs(t, interval[i])

            if i < len(interval)-1100:
                d2x2 = fxlinha.subs(t, interval[i+1100])
                d2y2 = fylinha.subs(t, interval[i+1100])
            else:
                d2x2 =0
                

            #fechar da simetria
            if d2x1 != 0 and d2x2 != 0:
                if abs((d2y1/d2x1)+(d2y2/d2x2)) <= 0.1 and abs((d2y1/d2x1)+(d2y2/d2x2))>= 0:
                    coordenadas_autointerseção.append([gama_x(i),gama_y(i)])
                    #print('foi 2')
            bar()
    print('Done\n')

compute2()

auto_intersecao = len(coordenadas_autointerseção)

print(coordenadas_autointerseção)
print(auto_intersecao)

function_x = sp.sympify('8*cos(t) - 5*cos(4*t)')
function_y = sp.sympify('8*sin(t) - 5*sin(4*t)')

def compute3():
    print('Ploting graphic:\n')
    with alive_bar(6284) as bar:  # your expected total
        for value in interval:

            x_values.append(function_x.subs(t, value))
            y_values.append(function_y.subs(t, value))

            bar()
    
    plt.plot(x_values, y_values)
    plt.show()
    print('Done\n')



def compute4():
    print('Ploting auto intersecting points:\n')
    fim = 2*math.pi
    plt.figure(figsize=(10, 10))
    with alive_bar(len(coordenadas_autointerseção)) as bar:  # your expected total
        for i in coordenadas_autointerseção:
            plt.scatter(i[0], i[1], color="red", s =15)
            bar()
    
    print('Done\n')

compute4()
compute3()
#plt.figure(figsize=(10, 10))
#plt.plot(x_values, y_values)


#plt.show()

            

#print('ACABOU')








