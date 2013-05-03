#!/bin/python

def position_of(element, grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == element:
                return i, j

def displayPathtoPrincess(n, grid):
    i_bot, j_bot = position_of('m', grid)
    i_princess, j_princess = position_of('p', grid)

    horiz_move = 'LEFT' if j_bot > j_princess else 'RIGHT'
    vert_move = 'UP' if i_bot > i_princess else 'DOWN'

    if i_bot != i_princess:
        print '\n'.join([vert_move] * abs(i_bot - i_princess))
    if j_bot != j_princess:
        print '\n'.join([horiz_move] * abs(j_bot - j_princess))


def main():
    m = input()

    grid = []
    for i in xrange(0, m):
        grid.append(raw_input().strip())

    displayPathtoPrincess(m,grid)

if __name__ == '__main__':
    main()
