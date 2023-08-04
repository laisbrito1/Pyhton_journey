




print ('Informe a Classe do seu personagem:'
       '(1)Druida',
       '(2)Mago',
       '(3)Paladino',
       '(4)Ranger',
       '(5)Bardo')

playertype=input('Digite o número do seu personagem: ')

if playertype =='1':
    playertype='Druida'
elif playertype =='2':
    playertype ='Mago' 
elif playertype == '3':
    playertype="Paladino"
elif playertype == '4':
    playertype ="Ranger"
elif playertype == '5':
    playertype = "Bardo"
else:
    print ('Erro, esse número não corresponde a um personagem')

print (' Seu personagem é', playertype)


print ('Agora invoque sua Habilidade')
manainvocar=int(input('Insira de mana da Habilidade'))
manaplayer = 100

if manaplayer > manainvocar:
    manaplayer= manaplayer - manainvocar
    print ("Você invocou a Habilidade")
else:
    print("você não tem mana suficiente")

print (' Sua mana atual é:', manaplayer)