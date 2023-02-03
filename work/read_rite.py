
import json



def read_json(y):
    with open (y, "r") as new:
        b = json.load(new)
        return(b)   




def account(email, password):
   
    w= read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json")
    u=read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\account.json")
    if email in w:
      
      if password == w[email]['password']:
            id= w[email]['id']
            accountnumber=u[id]["account_no"]
            accountype=u[id]["account_type"]
            accountbalance= u[id]["account_balance"]
            return accountbalance,accountype,accountnumber
    
      else:
            print('wrong password')    
    else:
        print ('wrong email')
    
