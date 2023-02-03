from read_rite import add_user,read_json,write_json,account



def register():
    new_name = input('what is your name')
    new_email = input('what is your email')
    new_password= input ('what is your password')
    add_user(new_email,new_name,new_password)

def login():
    email=input('what is your email')
    w= read_json(r"C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\bank-app\user.json")
    if email in w:
      password= input('password')
      if password == w[email]['password']:
            print (account)
      else:
            print('wrong password')    
    else:
        print ('wrong email')


def starter():
    first=input(' what do you want to do')
    if first == ('register'):
         register()
    elif first == 'login':
        account()
    else:
        "can only register and login"    


starter()  
