


ID= input('do you have a vaild ID').lower()
if ID == ('yes'):
    gender =input('Gender')
    if gender== ('male'):
        age= int(input('your age'))
        if age >=30 and age <= 60:
            print ('approved')
        else:
            print ('denied overage/underage')
    elif gender ==('female') :
        age= int(input('your age'))
        if age >=25 and age <= 40:
            print ('approved')
        else:
            print (' denied overage/underage')
    else :
        print ('invalid Gender')        
        
else:
    print ('Denied NoId ')

