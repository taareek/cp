def pageCount(n, p):
    # # counting flips 
    # forward_flips = 0
    # backward_flips = 0

    # # Calculate the number of flips needed from the front
    # for i in range(1, p // 2 + 1):  # number of flips(i)
    #     # check if we reach
    #     if p == i * 2 or p == i * 2 + 1: 
    #         forward_flips = i
    #         break

    # # Calculate the number of flips needed from the back
    # for i in range(0, (n // 2) + 1):  
    #      if p == n - (i * 2) or p == n - (i * 2 + 1):  # Check if we have reached page p
    #         backward_flips = i
    #         break

    # # Return the minimum number of flips
    # return min(forward_flips, backward_flips)

    # approach 2
    # Count flips from the front
    forward_flips = p // 2

    # Count flips from the back
    backward_flips = (n // 2) - (p // 2)

    # Return the minimum number of flips
    return min(forward_flips, backward_flips)




# Testing the function with the given case
print(pageCount(6, 2))  # Expected output: 1



n = 5
p = 4
print(pageCount(n, p))  
