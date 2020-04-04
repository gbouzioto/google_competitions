"""
Problem
tl;dr: Given a string of digits S, insert a minimum number of opening and closing parentheses into it such that the
resulting string is balanced and each digit d is inside exactly d pairs of matching parentheses.

Let the nesting of two parentheses within a string be the substring that occurs strictly between them. An opening
parenthesis and a closing parenthesis that is further to its right are said to match if their nesting is empty, or if
 every parenthesis in their nesting matches with another parenthesis in their nesting. The nesting depth of a position
 p is the number of pairs of matching parentheses m such that p is included in the nesting of m.

For example, in the following strings, all digits match their nesting depth: 0((2)1), (((3))1(2)), ((((4)))),
((2))((2))(1). The first three strings have minimum length among those that have the same digits in the same order,
 but the last one does not since ((22)1) also has the digits 221 and is shorter.

Given a string of digits S, find another string S', comprised of parentheses and digits, such that:
all parentheses in S' match some other parenthesis,
removing any and all parentheses from S' results in S,
each digit in S' is equal to its nesting depth, and
S' is of minimum length.

Input
The first line of the input gives the number of test cases, T. T lines follow. Each line represents a test case and
contains only the string S.

Output
For each test case, output one line containing Case #x: y, where x is the test case number (starting from 1) and y
is the string S' defined above.

Limits
Time limit: 20 seconds per test set.
Memory limit: 1GB.
1 ≤ T ≤ 100.
1 ≤ length of S ≤ 100.

Test set 1 (Visible Verdict)
Each character in S is either 0 or 1.

Test set 2 (Visible Verdict)
Each character in S is a decimal digit between 0 and 9, inclusive.

Sample

Input

Output

4
0000
101
111000
1


Case #1: 0000
Case #2: (1)0(1)
Case #3: (111)000
Case #4: (1)
"""

import sys


def main():
    strings = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()
            test_cases = int(lines[0].rstrip())
            for i in range(1, test_cases + 1):
                strings.append(lines[i].rstrip())
    else:
        test_cases = int(input())
        for i in range(1, test_cases + 1):
            strings.append(input().rstrip())
    for index, string in enumerate(strings, 1):
        int_string = list(map(int, string))
        first_par = '(' * int_string[0] + string[0]
        result = [first_par]
        for i in range(1, len(int_string)):
            num = int_string[i]
            prev_num = int_string[i-1]
            if num > prev_num:
                par_diff = '(' * (int_string[i] - int_string[i-1]) + string[i]
                result.append(par_diff)
            elif num < prev_num:
                par_diff = ')' * (int_string[i-1] - int_string[i]) + string[i]
                result.append(par_diff)
            else:
                result.append(string[i])
        last_par = ')' * int_string[-1]
        result.append(last_par)
        final_res = ''.join(result)
        print('Case #{}: {}'.format(index, final_res))


if __name__ == '__main__':
    main()