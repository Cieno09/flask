# #loops for loops while loops




# van = ['rice','beans','moi moi']
# car= ['34','78','43']

# for v in van:


# for c in van:
#     van.append(c) 
#     print (van)


# for c in car:   
#     van.append(c)
# print (van)    


# for v in van:
#     print (v)

# for t in range (0,11,2):
#     print (t)


# print ('Done')  



cars= ['bentley','benz','rolls roys','range rover', 'lexus']

# for car in cars:
#     print (car)
#     if car == 'rolls royes':
#         break


# for car in cars: 
#     print(car) 
#     if car == 'range rover':
#     continue
    
brand=input ('brand of car')
if brand in cars :

    for car in cars :
        if car == brand:
            continue
        print (car)
else:
    print ('not a luxury car ')

