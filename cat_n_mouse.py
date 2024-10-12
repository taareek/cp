# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem

# Complete the catAndMouse function below.
def catAndMouse(x, y, z):
    if abs(z-x) < abs(z-y):
        result = "Cat A"
    if abs(z-y) < abs(z-x):
        result = "Cat B"
    if abs(z-x) == abs(z-y):
        result = "Mouse C"
    
    return result

q = int(input())

for q_itr in range(q):
    xyz = input().split()
    x = int(xyz[0])
    y = int(xyz[1])
    z = int(xyz[2])
    result = catAndMouse(x, y, z)
    print(result + '\n')