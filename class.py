'''#name= input("what is your name")
#friend = input ("what is your friends name")

#print (f"Hello {name} your freinds name is {friend}" )


Fer=int(input("enter Ferh"))
Cel=(Fer-32)*5/9
print (f'Fact states that if Farechight{Fer} Celsius will be{Cel}')


weather=input('hows the weather')
if weather == 'rainy':
    print ('get wet ')
elif weather == 'Sunny':
    print("wear sunglasses")
else:
    print ('you can go out ')    



time=input('what is the time')
if time == '5:00':
    print ('wake up ')
elif time == '12:00':
    print("Lunch break")
elif time == '9:00':
    print("go to bed")
else:
    print ('do as you like  ')  
  



who_voting =input('who do yo wanna vote')
v2=input('what would you like to change')

V3 =input('what do you want to change to')
if v2 in who_voting:
    print(who_voting.replace(v2,v3))
else:    
     print (f"{v2}is not in your sentence")


a = 80 -100
b = 65 -79 
c = 50 -64
d = 40 - 49 
e = 35 -39 
f = 0 -34'''

score = float(input('enter your score'))
if score >=80 and  score <=100:
    print('A')
elif score <= 79 and score >=65:
    print ('B')  
elif score <= 64 and score >=50:
    print ('C') 
elif score <= 49 and score >=40:
    print('D')
elif score <= 39 and score >=35:
    print ('E')  
elif  score <=34 and score >=0:
    print ('F')    
else :
    print ('ERROR') 



    

