shop={'mango':2,
'paw paw' : 3,
'apple' :2,
'banana':5,
}
# amount=0
# while True :
#     add = input("add item")
#     if add =='end':
#         break
#     else:
#         if add in shop:
#             price =shop[add]
#             # print(price)
#             amount = amount + price
#         else:
#             print(f'{add} is not in the shop')
# print (amount)            


amount =0
while True:
    add = input('add item')
    if add == 'end':
        break
    else:
        if add in shop:     
            price=shop[add]
            if shop[add] > 1:    
                amount= price -1
                shop[add]=amount
                print (amount)
            else:
                print('E DON FINISH')                   
        else:
            print(f'{add} not in shop list')
 
    

                

           

