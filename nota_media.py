n1 = float(input('Digite primeira nota: '))
n2 = float(input('Digite segunda nota:'))
media = (n1 + n2) / 2
print('Sua média foi de : {:.1f}'.format(media))
if media >=7 :
    print('Você foi aprovado ')
else :
    print("estude mais")