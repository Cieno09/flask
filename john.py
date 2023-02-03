he = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
    'zero': '0',
    'plus':'.+',
    'minus':'-',
    'divide':'/',
    'multiply':'*',
}
 
te = "two four zero one"
 

print("The original string is : " + te)
 

res = ''.join(he[ele] for ele in te.split())
 

print("The string after performing replace : " + res)