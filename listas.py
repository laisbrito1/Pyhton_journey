pokedex=['charmander', 'squirtle', 'bubasaur', 'mew']

#o comprimento do array
len(pokedex)


pos=3
print   (f"{pokedex[pos]} eu escolho você")

print (pokedex[1:3])


#criar lista vazia
card_deck=[]

#adicionar coisas na lista com append
card_deck.append('Pikachu')
print(card_deck)

#estruturas de repetição evitam a repetição do mesmo codigo varias  vezes


#usamos for para retetir um código por um numero finito de vezes
for pokemon in pokedex:

   print   (f"{pokemon} está na pokedex")
else: print ("Esses são todos seus pokemons")

#usamos While para repetir um código enquanto uma função for verdadeira

print ("Vamos inserir mais pokemons!")

inserir= '1'
novodeck=[]
while inserir == '1':
   novo_pokemon = input("Qual o pokemon que quer inserir?")
   novodeck.append(novo_pokemon)
   inserir = input('Deseja inserir ao deck? Digite "1" para SIM e "2" para NÃO')
print(f"seu Novo deck tem', {len(novodeck)},'cards")