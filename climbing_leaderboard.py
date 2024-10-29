# https://www.hackerrank.com/challenges/climbing-the-leaderboard/problem

def climbing_leaderboard(ranked, player):
    ranks = []
    s = sorted(set(ranked), reverse=True)
    n = len(s)

    for score in player:
        while n > 0 and score >= s[n - 1]:
            n -= 1
        ranks.append(n+1)

    return ranks

ranked = [100,90,90,80]
player = [70,80,105]

ranks = climbing_leaderboard(ranked, player)
print(ranks)