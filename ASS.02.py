

Teamlist= {'Jordan':'Sql',
    'Conor':'Excel',
    'Mike':'java', 
    'Coleman':'Azure',
    'Onana':'java',
    'Gordon':'c++',
    'alex': ['phyton', 'React']}
     
player=input('what player')
if player in Teamlist:
    course=input('what cousre')
    if course ==Teamlist[player]:
        print('successfull')
    else :
        print('unsussessful')    
else:
    print('not a player')    





'''player1 =input('what player')
if player1 in Teamlist:
    course = Teamlist[player1]
    print(f'{player1} offers {course}')
else:
    print(f'{player1}is not a player')  



add= input('additional course')
x=Teamlist['alex']
x.append(add)
print (x)'''
