#!/usr/bin/env python3
""" Nqueens"""
import sys


def nqueen_solution(n , board, answer):
        """
        recresive function 
        which will go throw rows
        """
        def possible_place(row,col):
            """
            """
            for i in range(row):
                if board[i] == col or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
                    return False
            return True


        def queen_position(row):
            """
            """
            if row == n:
                answer.append(board[:])
            else:
                for col in range(n):
                    if possible_place(row, col):
                        board[row] = col
                        queen_position(row + 1)

        queen_position(0)

        print(answer)


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

    board = [-1] * n
    answer = []
    nqueen_solution(n, board, answer)
