import random

aceitarparticipar = input("Gostaria de tentar advinhar o número? s/n:  ")
x = random.randint (1,10) 

while aceitarparticipar == 's':

  if aceitarparticipar == 's':
    valorchute = int(input('Qual número chutar? '))
  else:
    print ('deixa para uma proxima então')


  while valorchute != x:
    
    if valorchute < x:
        print ('chutou baixou')
    elif valorchute > x:
        print ('chutou alto')

    valorchute = int(input('tente novamente: '))
      
  print ('parabéns acertou') 

  aceitarparticipar = input('desejar continuar? S/N ')
  x = random.randint (1,10)