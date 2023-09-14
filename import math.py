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