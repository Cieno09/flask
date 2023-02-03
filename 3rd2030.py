from st2023 import *

def supermarket():

    supmat =['Admin','staff','visitor']
    W= input ('Who Are You') 
    if W == supmat[0]:
        admin()
    elif W == supmat[1]:
        verify()
    elif W == supmat[2]:
        buy_items()  
    else:
        print('Not Working Here')     

            

        
         
supermarket()    