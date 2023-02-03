school ={'ss1':
        {'Ngolo':'Maths',
        'Jane':'English',
        'Rose':'Civic'},
       'ss2':
        {'Mike':'Argic',
       'Peter':'Biology',
        'Jane':'Maths' },
        'ss3':
        {'Vina':'Biology',
        'Peace':'Art',
        'Favour':'Geography'}}

name =input('name of name')
for i in school:
    a = school[i].keys()
    if name in a:
        print (i)
    
