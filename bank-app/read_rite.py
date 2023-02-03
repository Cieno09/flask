import datetime
import json

date = str(datetime.datetime.now())
#print (type(date))

users = {"p@gmail.com":{"id":date, "name": "prisca", "password":"123"}}
accounts = {date:{"account_no":"01235674", "account_name":"prisca matthews", "account_type":"savings", "account_balance":6500}}



def write(content,filenames):
    with open (filenames, 'w') as file:
        json.dump(content,file)
      
#write(users,(r'C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json')
     
def read(filename):
    with open (filename, 'r') as file:
        data = json.load(file)
        return (data)

#c = read(r'C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\account.json')




def write(content,filenames):
    with open (filenames, 'w') as file:
        json.dump(content,file)


def write_json(i, j):
    with open (i, "w") as writer:
        json.dump(j, writer)

def read_json(y):
    with open (y, "r") as new:
        b = json.load(new)
        return(b)   



#z = read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json")
#print (z)

# new_entry = {"trial@gmail.com": {"id": "2023-01-19 10:19:48.874343", "name": "new trial", "password": "try123"}}

# z.update(new_entry)

# print(z)

# write_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json", z)


def add_user(email, name, password):
    z = read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json")
    new_entry = {email: {"id": date, "name": name, "password": password}}
    z.update(new_entry)
    write_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json", z)
    print("Write Successful")


#add_user("john@gmail.com", "john francis", "54t")

def account():
    email=input('what is your email')
    w= read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json")
    u=read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\account.json")
    if email in w:
      password= input('password')
      if password == w[email]['password']:
            id= w[email]['id']
            accountnumber=u[id]["account_no"]
            accountname=u[id]["account_name"]
            accountype=u[id]["account_type"]
            accountbalance= u[id]["account_balance"]
            print(f"The name of is account is {accountname} your account number is {accountnumber}, while the account typr is {accountype}, and the remaining balance is {accountbalance} " )
    
      else:
            print('wrong password')    
    else:
        print ('wrong email')
    


def add_account(account_num,account_name, account_type, account_balance):
    s=read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\account.json")
    new_acct={date:{"account_no":account_num, "account_name": account_name, "account_type": account_type,"account_balance": account_balance}}
    s.update(new_acct)
    write_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\account.json")
    print ('Success')