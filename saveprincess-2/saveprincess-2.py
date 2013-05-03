#!/bin/python

def position_of(element, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == element:
                return i, j

def next_move(n, x, y, grid):
    i_bot, j_bot = position_of('m', grid)
    i_princess, j_princess = position_of('p', grid)

    i_diff, j_diff = abs(i_bot - i_princess), abs(j_bot - j_princess)

    if i_diff > j_diff:
        return 'UP' if i_bot > i_princess else 'DOWN'
    elif j_diff > 0:
        return 'LEFT' if j_bot > j_princess else 'RIGHT'

    return None

def main():
    n = input()
    x,y = [int(i) for i in raw_input().strip().split()]
    grid = []
    for i in xrange(0, n):
        grid.append(raw_input())

    print next_move(n, x, y, grid)

if __name__ == '__main__':
    main()
