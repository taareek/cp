# https://www.hackerrank.com/challenges/sock-merchant/problem


def sockMerchant(n, ar):
    sock_count = {}
    count_pairs = 0

    # Count occurrences of each sock
    for sock in ar:
        if sock in sock_count:
            sock_count[sock] += 1
        else:
            sock_count[sock] = 1

        # Whenever a pair is found, increment count_pairs and reset sock count
        if sock_count[sock] % 2 == 0:
            count_pairs += 1
            
    return count_pairs

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
print(sockMerchant(n, ar)) 
