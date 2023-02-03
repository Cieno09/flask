school ={'ss1':
        {'Ngolo':'Maths',
        'Jane':'English',
        'Rose':'Civic'},
       'ss2':
        {'Mike':'Agric',
       'Peter':'Biology',
        'Jane':'Maths' },
        'ss3':
        {'Vina':'Biology',
        'Peace':'Art',
        'Favour':'Geography'}}


sub=input('name of sub')
for clas,i in school.items():
    for j in i :
    
            if sub ==i[j]:
                
                    print (clas,j)
    

    
         