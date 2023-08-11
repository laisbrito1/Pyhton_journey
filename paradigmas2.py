# script funcao3.py
# captando os valores do campo Input
valores = input() 
# separando os valores pelo espaço em branco e 
# transformando-os em uma lista de inteiros
valores = [int(i) for i in valores.split()] #split adiciona valor na lista

def altera_lista(lista):
    nova_lista=list(lista) #alterarmos o valor do próprio parâmetro, criamos uma cópia dele 
    lista[2] = nova_lista[2] + 10
    return lista

def main():
    print("Nova lista", altera_lista(valores))
    print("Nova lista", altera_lista(valores))

if __name__ == "__main__":
    main()