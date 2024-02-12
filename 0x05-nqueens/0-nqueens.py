#!/usr/bin/python3
""" Nqueens"""
import sys


def queens(n):
    """
    return total positions of quens in dashboard
    """
    col = []
    posdig = []
    negdig = []
    result = []

    def position_of_queen(row):
        """
        q place in each row
        """
        if row == n:
            result.append([[i, col[i]] for i in range(n)])
            return
        for c in range(n):
            if (c not in col and (row + c) not in posdig
                and (row - c) not in negdig):
                col.append(c)
                negdig.append(row - c)
                posdig.append(row + c)

                position_of_queen(row + 1)
                col.pop()
                posdig.pop()
                negdig.pop()

    position_of_queen(0)
    for i in result:
        print(i)


if __name__ == ('__main__'):
    if len(sys.argv) != 2:
        print('Usage: nqueens N')
        sys.exit(1)

    try:
        n = int(sys.argv[1])
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if n < 4:
        print('N must be at least 4')
        sys.exit(1)

    queens(n)
