shop ={'banana':{'price':350,'qty': 3},
        'apple':{'price':200, 'qty':1},
        'paw paw':{'price':150,'qty':3},
        'orange':{'price':100, 'qty':4} }


amount =0
quantity=0
while True:
        add=input('add')
        if add == 'end':
                break
        else:
                if add in shop:
                        quant=shop[add]['qty']
                        if quant>0:
                                quantity=quant-1
                                shop[add]['qty'] =quantity
                                print(f'{quantity} left')
                                price=shop[add]['price']
                                amount=amount + price
                                print(f'total amount is {amount}')
                        else:
                                print(f'{add} has finish')
                else:
                        print(f'{add} NOT IN THE STORE')                

               



                       
                     
        