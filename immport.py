import math
import time
import datetime
import shutil


num= int(input('enter digit'))
result = math.sqrt(num)
print(f'the square root of {num} is {result}')



n =math.radians
results2= math.sin(math.pi/2)
print (results2)


print(math.factorial(4))
time.sleep(5)
print(math.factorial(5))


print (datetime.datetime.now())


source=r'C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\claas7.py'
destination=r'C:\Users\marki\OneDrive\Documents\Sports Interactive\PYTHON\lesson\tales.py'

shutil.copy(source,destination)
print('Copied Successfully')