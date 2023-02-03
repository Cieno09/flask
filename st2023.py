def add_staff():
    newstaff = input('Name of New Staff')
    dept = input ('Input Department') 
    if dept in employee.keys():
        v=employee[dept]
        v.append(newstaff)
        print (employee)   
    else:
        print('WE Dont Have That Department') 
    
   
    

def check_staff():
    

    name = input ('Enter Staff Name')
    if name in employee['cashier']:
        print (f'{name} is a cashier')
    elif name in employee['cleaner']:
        print (f'{name} is a cleaner')
    elif name in employee['accountant']:
        print (f'{name} is an accountant')
    else:
        print (f'{name}is a not staff here') 
    


def buy_items():
    shop ={'banana':{'price':3500,'qty': 3},
        'apple':{'price':2000, 'qty':1},
        'paw paw':{'price':1500,'qty':3},
        'orange':{'price':1000, 'qty':4} }

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

               


   

 




def verify(): 
    sos = {'ayo':'ay4ever',
    'trix':'sweet404',
    'fred':'freddred',
    'tony':'iron1',
    'stark':'man2',
    'yola':'9ja4live'
    }
    name =input('Enter Username')
    if name in sos:
        password = input('Enter Password')
        if password in sos[name]:
            print ('Valid')
        else:
            print('Invalid')    
    else:
        print('Wrong name')        


 


def admin():
    global employee 
    employee={'cashier': ['ayo','trix'],
    'cleaner':['fred','tony','stark'],
    'accountant':['yola']}
    task = input('What would you like to do')
    if task == 'check':
        check_staff()
    elif task == 'add':
        add_staff()
    else:
         print ('Admin Only Authorized To Add and Check')   


