print( '{:=^40}'.format(' APP Delivery '))
preço = float(input ('Preço das compras: R$'))

print('''FORMAS DE PAGAMENTO
[1] á vista Dinheiro/Pix
[2] á vista Cartão
[3] 2x no Cartão
[4] 3x no Cartão ou mais''')

opção = int(input(' Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2;
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparç = int(input('Quantas parcelas?'))
    parcela = total / totparç
    print(' Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totparç, parcela))
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(preço, total))
