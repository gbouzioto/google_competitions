import os
from collections import namedtuple
from itertools import combinations
from sys import argv

path = os.path.dirname(os.path.realpath(__file__))
DEPTH = 30
Photo = namedtuple('Photo', ['index', 'type', 'tags'])


def read_file(fin):
    with open(fin, 'r') as f:
        f.readline()
        V, H = [], []
        for i, line in enumerate(f.readlines()):
            line = line.strip().split()
            tags = line[2:]
            if line[0] == 'V':
                V.append(Photo(str(i), line[0], set(tags)))
            else:
                H.append(Photo(str(i), line[0], set(tags)))
        return V, H


def write_file(testcase, solution):
    with open(testcase[:-4].replace('inputs', 'outputs') + ".out", 'w') as f:
        f.write("{}\n".format(len(solution)))
        for slide in solution:
            f.write("{}\n".format(slide))


def combine_photos(p1, p2):
    if p1.type == p2.type == 'V':
        return Photo("{} {}".format(p1.index, p2.index), 'V',
                     p1.tags.union(p2.tags))


def calc_score(p1, p2):
    return min(len(p1.tags.intersection(p2.tags)),
               len(p1.tags.difference(p2.tags)),
               len(p2.tags.difference(p1.tags)))


def find_next_photo(photo, photos):
    return max(photos, key=lambda p: calc_score(p, photo))


def solve(testcase):
    V, H = read_file(testcase)
    sol = []

    V.sort(key=lambda x: len(x.tags))
    H.sort(key=lambda x: len(x.tags))

    if H:
        curr_photo = H.pop(0)
    else:
        curr_photo = combine_photos(V.pop(0), V.pop(0))
    sol.append(curr_photo.index)

    while len(V) > 1 or len(H) > 0:
        Vs = combinations(V[:DEPTH], 2)
        curr_photo = find_next_photo(
            curr_photo, H[:DEPTH] + map(lambda x: combine_photos(*x), Vs))
        if curr_photo.type == 'H':
            H.remove(curr_photo)
        else:
            for p in V[:DEPTH]:
                if p.index in curr_photo.index:
                    V.remove(p)
        sol.append(curr_photo.index)

    return sol


def main():
    testcases = os.listdir(os.path.join(path, 'inputs'))
    if len(argv) > 1:
        case = argv[1]
        if case not in testcases:
            print("No testcase name %s, running all testcases") % case
        else:
            testcases = [case]
    testcases = list(map(lambda x: os.path.join('inputs', x), testcases))

    for testcase in testcases:
        sol = solve(testcase)
        write_file(testcase, sol)


if __name__ == '__main__':
    main()
