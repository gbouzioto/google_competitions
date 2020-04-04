"""
Problem
Vestigium means "trace" in Latin. In this problem we work with Latin squares and matrix traces.

The trace of a square matrix is the sum of the values on the main diagonal
(which runs from the upper left to the lower right).

An N-by-N square matrix is a Latin square if each cell contains one of N different values, and no value is repeated
within a row or a column. In this problem, we will deal only with "natural Latin squares" in which the N values are
the integers between 1 and N.

Given a matrix that contains only integers between 1 and N, we want to compute its trace and check whether it is a
natural Latin square. To give some additional information, instead of simply telling us whether the matrix is a natural
Latin square or not, please compute the number of rows and the number of columns that contain repeated values.

Input
The first line of the input gives the number of test cases, T. T test cases follow. Each starts with a line containing
a single integer N: the size of the matrix to explore. Then, N lines follow. The i-th of these lines contains N integers
 Mi,1, Mi,2 ..., Mi,N. Mi,j is the integer in the i-th row and j-th column of the matrix.

Output
For each test case, output one line containing Case #x: k r c, where x is the test case number (starting from 1), k is
the trace of the matrix, r is the number of rows of the matrix that contain repeated elements, and c is the number of
columns of the matrix that contain repeated elements.

Limits
Test set 1 (Visible Verdict)
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
2 ≤ N ≤ 100.
1 ≤ Mi,j ≤ N, for all i, j.

Sample

Input

Output

3
4
1 2 3 4
2 1 4 3
3 4 1 2
4 3 2 1
4
2 2 2 2
2 3 2 3
2 2 2 3
2 2 2 2
3
2 1 3
1 3 2
1 2 3
"""
import sys


def main():
    matrix_array = []

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()
            test_cases = int(lines[0].rstrip())
            del lines[0]
            i = 0
            while test_cases != 0:
                array_size = int(lines[i].rstrip())
                array = []
                for j in range(i + 1, array_size + i + 1):
                    row = [int(i) for i in lines[j].split(" ")]
                    array.append(row)
                matrix_array.append(array)
                i += array_size + 1
                test_cases -= 1
    else:
        test_cases = int(input())
        i = 0
        while test_cases != 0:
            array_size = int(input().rstrip())
            array = []
            for j in range(i + 1, array_size + i + 1):
                row = list(map(int, input().split(" ")))
                array.append(row)
            matrix_array.append(array)
            i += array_size + 1
            test_cases -= 1

    for index, matrix in enumerate(matrix_array, 1):
        size = len(matrix)
        trace = 0
        elements = set()
        duplicate_rows = 0
        duplicate_columns = 0

        for i in range(size):
            for j in range(size):
                if i == j:
                    trace += matrix[i][j]

        for i in range(size):
            for j in range(size):
                elem = matrix[i][j]
                if elem in elements:
                    duplicate_rows += 1
                    break
                elements.add(elem)
            elements.clear()
        elements.clear()

        for i in range(size):
            for j in range(size):
                elem = matrix[j][i]
                if elem in elements:
                    duplicate_columns += 1
                    break
                elements.add(elem)
            elements.clear()
        print('Case #{}: {} {} {}'.format(index, trace, duplicate_rows, duplicate_columns))


if __name__ == '__main__':
    main()
