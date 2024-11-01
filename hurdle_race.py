# https://www.hackerrank.com/challenges/the-hurdle-race/problem


def hurdleRace(k, height):
    # Write your code here
    max_height = max(height)
    if k >= max_height:
        return 0
    if k < max_height:
        doses = max_height - k
        return doses
    
heights = [2,4,5,7,8,11]
k = 7

result = hurdleRace(k, heights)
print(result)