cart = ['Cars','House','Clothes','shoes']

while True :
    add = input("add item  ")
    if add =='end':
        break
    else:
        if add in cart :
            print (f'{add} already exist')
        else:
               
            cart.append(add) 
print (cart)



while True :
    add = input("add item  ")
    if add =='end':
        break
    if add in cart :
        print (f' {add} already exist')
        continue
    cart.append(add)
print (cart)

u=shop['apple']['qty']
print(u)