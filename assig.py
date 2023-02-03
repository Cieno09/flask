# d = {'key1': 'aaa', 'key2': 'aaa', 'key3': 'bbb'}

# value = d['key1']
# print(value)

# num = 6


# for i in range(1, 13):
#    print(num, 'x', i, '=', num*i)

# #1. write a python program to print the factorial of a number....the number should be inputted by the user at the terminal
# n = int(input("Enter a number: "))
# f = 1

# if n < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif n== 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,n + 1):
#        f = f*i
#    print("The factorial of",n,"is",f)


test_dict = {'Gfg' : 1, 'for' : 2, 'CS' : 3}



# initializing value
val = 3

# Using naive method
# Search key from Value
for key in test_dict:
	if test_dict[key] == val:
		res = key

# printing result
print("The key corresponding to value : " + str(res))
