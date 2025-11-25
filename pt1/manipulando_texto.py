from random import choice
texto = 'Bom dia'

print(texto[::])
print('INÍCIO : FIM : PULA LETRAS:')

mussum = """Mussum Ipsum, cacilds vidis litro abertis. Praesent 
malesuada urna nisi, quis volutpat erat hendrerit non. Nam 
vulputate dapibus. Atirei o pau no gatis, per gatis num 
morreus. Casamentiss faiz malandris se pirulitá. Em pé sem 
cair, deitado sem dormir, sentado sem cochilar e fazendo pose."""
print('Usando o .count() para aontagem de letras o : ',mussum.count('o'))
print('Convertendo frase com o .upper() para maiúsculo',mussum.upper())
print('Utilizando o len() para saber o tamanho da frase : ',len(mussum))
print('len() mais utilização do .strip para remoção de espaços antes e depois', len(mussum.strip()))
print('utilizando o .raplace (palavra,palavra que ira entrar no lugar) para substituir palavras: ', mussum.replace('Mussum', 'Lero'))
print('Verifica de existe palavra desejada dentro do texto: ex (palavra in mussum) :', 'Mussum' in mussum)
print('Mostrar posição da palavra desejada dentro da frase: ex (mussum.find(cochilar): ', mussum.find('cochilar'))

print('Transformando a frase em lista : mussum.split()')
mussum1 = """Em pé sem 
cair, deitado sem dormir, sentado sem cochilar e fazendo pose."""
dividido = mussum1.split()
print(dividido)
print('escolhendo palavra aleatoria com .choice : ')
print(choice(dividido))


text1 = "hello, world!"
capitalized_text1 = text1.capitalize()
print(capitalized_text1)  # Output: Hello, world!



n1 = str(input('Digite um numero de 0 a 9999: ' ))
print('Numero digita foi : {}'.format(n1))
print('unidade :{}'.format(n1[3:4:]))
print('dezena :{}'.format(n1[2:3:]))

print('centena :{}'.format(n1[1:2:]))
print('milhar :{}'.format(n1[:1:]))

