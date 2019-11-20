"""
Problem
You have just entered the world's easiest maze. You start in the northwest cell of an N by N grid of unit cells, and you must reach the southeast cell. You have only two types of moves available: a unit move to the east, and a unit move to the south. You can move into any cell, but you may not make a move that would cause you to leave the grid.

You are excited to be the first in the world to solve the maze, but then you see footprints. Your rival, Labyrinth Lydia, has already solved the maze before you, using the same rules described above!

As an original thinker, you do not want to reuse any of Lydia's moves. Specifically, if her path includes a unit move from some cell A to some adjacent cell B, your path cannot also include a move from A to B. (However, in that case, it is OK for your path to visit A or visit B, as long as you do not go from A to B.) Please find such a path.

In the following picture, Lydia's path is indicated in blue, and one possible valid path for you is indicated in orange:

Input
The first line of the input gives the number of test cases, T. T test cases follow; each case consists of two lines. The first line contains one integer N, giving the dimensions of the maze, as described above. The second line contains a string P of 2N - 2 characters, each of which is either uppercase E (for east) or uppercase S (for south), representing Lydia's valid path through the maze.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y is a string of 2N - 2 characters each of which is either uppercase E (for east) or uppercase S (for south), representing your valid path through the maze that does not conflict with Lydia's path, as described above. It is guaranteed that at least one answer exists.

Limits
1 ≤ T ≤ 100.
Time limit: 15 seconds per test set.
Memory limit: 1GB.
P contains exactly N - 1 E characters and exactly N - 1 S characters.

Input Output

2
2
SE          Case #1: ES
5
EESSSESE    Case #2: SEEESSES
"""

import sys


def main():
    lydia_path_dimensions = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()[1:]
            for i in range(0, len(lines), 2):
                lydia_path_dimensions.append((int(lines[i]), lines[i+1].rstrip()))
    else:
        times = int(input())
        for i in range(times):
            lydia_path_dimensions.append((int(input()), input()))
    mapping = {'E': 'S', 'S': 'E'}
    for index, lydia_path_dimension in enumerate(lydia_path_dimensions, 1):
        symmetric_path = [mapping[c] for c in lydia_path_dimension[1]]
        print('Case #{}: {}'.format(index, "".join(symmetric_path)))


if __name__ == '__main__':
    main()