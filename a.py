# code for testing decorator chaining 
# filter, map, reduce, sorted

# Use if-else in Lambda Functions

# check if number is even or odd
result = lambda x : f"{x} is even" if x %2==0 else f"{x} is odd"

# print for numbers
print(result(12))
print(result(11))
# https://www.geeksforgeeks.org/using-apply-in-pandas-lambda-functions-with-multiple-if-statements/?ref=oin_asr2

my_dict = {i:i+7 for i in range(1, 10)}
print(my_dict)

import time

currenttime= time.localtime(time.time())
print(currenttime)