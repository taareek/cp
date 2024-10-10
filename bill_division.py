# https://www.hackerrank.com/challenges/bon-appetit/problem

#
# Complete the 'bonAppetit' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY bill
#  2. INTEGER k
#  3. INTEGER b
#

def bonAppetit(bill, k, b):
    # Write your code here
    total_excluding_ana = sum(bill) - bill[k]
    
    ana_should_pay = total_excluding_ana // 2
    
    if ana_should_pay == b:
        print("Bon Appetit")
    else:
        owes = b - ana_should_pay
        print(owes)

bill = [3, 10, 2, 9]
k = 1  # Anna didn't eat the 2nd item (index 1)
b = 12  # Brian charged Anna 12
bonAppetit(bill, k, b)  # Output: 5 (Anna was overcharged by 5)
