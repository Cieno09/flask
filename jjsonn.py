import json
filename ='jsaon.json'

with open (filename, 'r') as file:
    content =json.load (file)
    print (content)

data ={'shoe' : 4}
content.update(data)

with open (filename, 'w') as file:
    json.dump (content,file)


fig= input("what item") 
if fig in content:
    f=content[fig]
    print (f)



 
