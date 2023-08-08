#encontrar o menor numero

def encontrar_minimo(lista):
    mininimo = lista[0] #inicialmente, a posição 1 é considerada
    for elem in lista:
        if (elem < mininimo) :
            mininimo=elem
    return mininimo
    
listanumeros= [23,54,19,40,23,5,]
minimo = encontrar_minimo(listanumeros)
print("O menor número da lista é:[{}]".format(minimo))



def par(n):
    r=(n%2==0)
    return r

def somar(lista):
    soma=0
    for num in lista:
        if (par(num)):
            soma=soma+num
    return soma
soma=somar(listanumeros)
print(f'a soma dos elementos pares é:,{soma}')



def fatorial(n):
    if((n==0)or(n==1)):
        return 1
    return n*fatorial(n-1)
numero = 5
print (f'O fatorial do numero {numero} é {fatorial(numero)}')