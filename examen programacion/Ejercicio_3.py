from random import randint
lista=[]
for i in range(77):
  w=randint(1, 999)
  lista.append(w)

print(lista)

lista.sort()
print(lista)

print('Máximo:',max(lista))
print('Mímino:',min(lista))


for lista in range(100,999, 2):
    print(lista)