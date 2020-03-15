from itertools import groupby
def solution(A):

    splitted = [''.join(g) for _, g in groupby(A)]
    moves = 0
    for segment in splitted:
        moves += int(len(segment) / 3)

    return moves
