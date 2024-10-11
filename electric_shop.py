# https://www.hackerrank.com/challenges/electronics-shop/problem


# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.
    # max amount 
    max_amount = -1
    
    for keyboard in keyboards:
        for drive in drives:
            if keyboard + drive <= b:
                max_amount = max(max_amount, keyboard+drive)
    
    return max_amount

keyboards = [40, 50, 60]  # Prices of keyboards
drives = [5, 8, 12]       # Prices of drives
budget = 60               # Available budge

c = getMoneySpent(keyboards, drives, budget)
print(c)