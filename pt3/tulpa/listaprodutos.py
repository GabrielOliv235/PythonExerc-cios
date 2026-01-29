produtos =('Água', 2.00,
           'Coca-Cola', 5.00,
           'Água-de-Coco', 5.00,
           'Leite-de-Soja', 7.85,
           'Sprite', 5.00,
           'Suco-de-laranja',8.00)

print('='*30,'\n    LISTAGEM DE PRODUTOS')
print('='*30)

for item in range(0, len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}', end='')
    else:
        print(f'R${produtos[item]:>7.2f}')