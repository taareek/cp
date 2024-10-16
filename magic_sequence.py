def formingMagicSquare(s):
    # Write your code here
    s = sum(s, [])  # flaten s

    #  All possible magic squares of 3x3 order
    magic_squares = [
        [8, 1, 6, 3, 5, 7, 4, 9, 2],
        [6, 1, 8, 7, 5, 3, 2, 9, 4],
        [4, 9, 2, 3, 5, 7, 8, 1, 6],
        [2, 9, 4, 7, 5, 3, 6, 1, 8],
        [8, 3, 4, 1, 5, 9, 6, 7, 2],
        [4, 3, 8, 9, 5, 1, 2, 7, 6],
        [6, 7, 2, 1, 5, 9, 8, 3, 4],
        [2, 7, 6, 9, 5, 1, 4, 3, 8],
    ]

    costs = []  # this variable will contain all possible costs

    for magic_square in magic_squares:
        costs.append(sum([abs(magic_square[i] - s[i]) for i in range(9)]))

    return min(costs) 


def test_formingMagicSquare():
    s = [
        [4, 8, 2],
        [4, 5, 7],
        [6, 1, 6]
    ]
    assert formingMagicSquare(s) == 4, "Test Case 1 Failed!"
    print("Test Case 1 Passed!")

# Run the test
test_formingMagicSquare()
