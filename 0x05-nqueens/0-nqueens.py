#!/usr/bin/python3
""" Nqueens"""
import sys


def queens(n):
    """
    return total positions of queens in dashboard
    """
    colums = []  # q in cloumns
    posdig = []  # row + col
    negdig = []  # row - col
    result = []

    def position_of_queen(row):
        """
        main indicate position in each column
        queen positions colums arr where index = rows
        """
        if row == n:  # base case recursion (end of dashboard)
            # print(colums)
            result.append([[i, colums[i]] for i in range(n)])
            return
        for col in range(n):
            if (col not in colums and (row + col) not in posdig
               and (row - col) not in negdig):
                colums.append(col)
                negdig.append(row - col)
                posdig.append(row + col)

                position_of_queen(row + 1)  # loop over rows
                colums.pop()
                posdig.pop()
                negdig.pop()

    position_of_queen(0)
    # print(result)
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
