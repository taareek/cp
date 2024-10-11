#  https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    # Write your code here
    vally_count = 0
    altitude = 0
    
    for step in path:
        if step == 'U':
            altitude += 1
        if step == 'D':
            altitude -= 1
        if (altitude == 0 and step =='U'):
            vally_count += 1
    
    return vally_count

steps = 14
path = 'UUDDDDUUUDDUUU'
a = countingValleys(steps, path)
print(a)
