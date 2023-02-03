'''Hiphop= {'JayZ' :'Niggas in paris',
          'Lil Wayne' : 'A milli'}
Soul= {'Alilcia Keys' : 'Girl on fire' , 
        'Beyonce'   : 'Halo'}
Music ={'   
#print( Music) 

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

xo= input('what is your class')
namez=input('what is your name')
if namez in school [xo] :
    print(school[xo][namez])
else:
    print ('null')'''

music= {'JayZ' :'Niggas in paris','Lil Wayne' : 'A milli','Alilcia Keys' : 'Girl on fire' ,     'Beyonce'   : 'Halo'}
txt= input('name of song')
for key in music:
        if music[key]==txt:
                res = key   
print(res)                     
