import json
import datetime

date = str(datetime.datetime.now())

with open (r"bank\random.txt", 'r') as content:
    a = content.readlines()
    print(a)

with open (r"bank\second.txt", 'r') as content:
    a = content.readlines()
    print(a)

def add(a,b):
    print(a+b)

add(50,40)

def readfile(x):
    with open (x, "r") as content:
        a = content.readlines()
        print (a)

readfile(r"bank\third.txt")

readfile(r"bank\first.txt")

#readfile(r"bank\users.json")



# with open (r"bank\users.json", "r") as new:
#     b = json.load(new)
#     print(b)

with open (r"bank\users.json", "w") as writer:
    json.dump({"name":"peace"}, writer)

def write_json(i, j):
    with open (i, "w") as writer:
        json.dump(j, writer)



def read_json(y):
    with open (y, "r") as new:
        b = json.load(new)
        return(b)

#z = read_json(r"bank-app\users.json")
#print (z)

# new_entry = {"trial@gmail.com": {"id": "2023-01-19 10:19:48.874343", "name": "new trial", "password": "try123"}}

# z.update(new_entry)

# print(z)

# write_json(r"bank-app\users.json", z)

def add_user(email, name, password):
    z = read_json(r"bank-app\users.json")
    new_entry = {email: {"id": date, "name": name, "password": password}}
    z.update(new_entry)
    write_json(r"bank-app\users.json", z)
    print("Write Successful")

add_user("john@gmail.com", "john francis", "54t")