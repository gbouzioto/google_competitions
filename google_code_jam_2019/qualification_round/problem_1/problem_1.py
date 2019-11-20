"""
Last updated: Apr 6 2019, 11:09

Problem
Someone just won the Code Jam lottery, and we owe them N jamcoins!
However, when we tried to print out an oversized check, we encountered a problem.
The value of N, which is an integer, includes at least one digit that is a 4...
and the 4 key on the keyboard of our oversized check printer is broken.

Fortunately, we have a workaround: we will send our winner two checks for positive
integer amounts A and B, such that neither A nor B contains any digit that is a 4,
and A + B = N. Please help us find any pair of values A and B that satisfy these conditions.

Input
The first line of the input.txt gives the number of test cases, T. T test cases follow;
each consists of one line with an integer N.

Output
For each test case, output one line containing Case #x: A B,
where x is the test case number (starting from 1), and A and B are positive
integers as described above.

It is guaranteed that at least one solution exists. If there are multiple solutions,
you may output any one of them. (See "What if a test case has multiple correct solutions?"
in the Competing section of the FAQ. This information about multiple solutions will not be
explicitly stated in the remainder of the 2019 contest.)

Limits
1 ≤ T ≤ 100.
Time limit: 10 seconds per test set.
Memory limit: 1GB.
At least one of the digits of N is a 4.



Sample

Input   Output

3
4       Case #1: 2 2
940     Case #2: 852 88
4444    Case #3: 667 3777

"""
import re
import sys


def main():

    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            numbers = list(map(int, f.readlines()))[1:]
    else:
        times = int(input())
        numbers = [int(input()) for _ in range(times)]

    p = re.compile("4")
    for index, number in enumerate(numbers, 1):
        subtractor_list = ['0'] * len(str(number))
        for match in re.finditer(p, str(number)):
            subtractor_list[match.start()] = '1'
        subtractor = int(''.join(subtractor_list))

        print('Case #{}: {} {}'.format(index, number - subtractor, subtractor))


if __name__ == '__main__':
    main()
