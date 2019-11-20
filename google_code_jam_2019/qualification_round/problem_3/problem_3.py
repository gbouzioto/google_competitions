"""
Problem
On the Code Jam team, we enjoy sending each other pangrams, which are phrases that use each
letter of the English alphabet at least once. One common example of a pangram is
"the quick brown fox jumps over the lazy dog". Sometimes our pangrams contain confidential
information — for example, CJ QUIZ: KNOW BEVY OF DP FLUX ALGORITHMS — so we need to keep
them secure.

We looked through a cryptography textbook for a few minutes, and we learned that it is
very hard to factor products of two large prime numbers, so we devised an encryption scheme
based on that fact. First, we made some preparations:

We chose 26 different prime numbers, none of which is larger than some integer N.
We sorted those primes in increasing order. Then, we assigned the smallest prime to the
letter A, the second smallest prime to the letter B, and so on.
Everyone on the team memorized this list.

Now, whenever we want to send a pangram as a message, we first remove all spacing to form a
plaintext message. Then we write down the product of the prime for the first letter of the
plaintext and the prime for the second letter of the plaintext. Then we write down the product
of the primes for the second and third plaintext letters, and so on, ending with the product
of the primes for the next-to-last and last plaintext letters. This new list of values is our
ciphertext. The number of values is one smaller than the number of characters in the plaintext
message.

For example, suppose that N = 103 and we chose to use the first 26 odd prime numbers,
because we worry that it is too easy to factor even numbers. Then A = 3, B = 5, C = 7,
D = 11, and so on, up to Z = 103. Also suppose that we want to encrypt the CJ QUIZ...
pangram above, so our plaintext is CJQUIZKNOWBEVYOFDPFLUXALGORITHMS. Then the first value in
our ciphertext is 7 (the prime for C) times 31 (the prime for J) = 217; the next value is 1891,
and so on, ending with 3053.

We will give you a ciphertext message and the value of N that we used. We will not tell you
which primes we used, or how to decrypt the ciphertext. Do you think you can recover the plaintext
anyway?

Input
The first line of the input gives the number of test cases, T. T test cases follow;
each test case consists of two lines. The first line contains two integers: N, as
described above, and L, the length of the list of values in the ciphertext.
The second line contains L integers: the list of values in the ciphertext.

Output
For each test case, output one line containing Case #x: y, where x is the test case number
(starting from 1) and y is a string of L + 1 uppercase English alphabet letters: the plaintext.

Limits
1 ≤ T ≤ 100.
Time limit: 20 seconds per test set.
Memory limit: 1 GB.
25 ≤ L ≤ 100.
The plaintext contains each English alphabet letter at least once.

Sample
Input
2
103 31
217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053
10000 25
3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543

Output

Case #1: CJQUIZKNOWBEVYOFDPFLUXALGORITHMS
Case #2: SUBDERMATOGLYPHICFJKNQVWXZ
"""

import sys
from collections import namedtuple

TestSet = namedtuple('TestSet', ['largest_n', 'length', 'message_list'])

ALPHABET_MATCH = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H',
                  9: 'I', 10: 'J', 11: 'K', 12: 'L', 13: 'M', 14: 'N', 15: 'O', 16: 'P',
                  17: 'Q', 18: 'R', 19: 'S', 20: 'T', 21: 'U', 22: 'V', 23: 'W', 24: 'X',
                  25: 'Y', 26: 'Z'}


def sieve_of_eratosthenes(number):
    # sieve of eratosthenes algorithm for finding primes
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for _ in range(number + 1)]
    p = 2
    while p * p <= number:

        # If prime[p] is not changed, then it is a prime
        if prime[p] is True:

            # Update all multiples of p
            for i in range(p * p, number + 1, p):
                prime[i] = False
        p += 1

    return [p for p in range(2, number + 1) if prime[p] is True]


def main():
    test_sets = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()[1:]
            for i in range(0, len(lines), 2):
                n, length = map(int, lines[i].split())
                message = [int(number) for number in lines[i + 1].split()]
                test_sets.append(TestSet(n, length, message))
    else:
        times = int(input())
        for i in range(times):
            n, length = map(int, input().split())
            message = [int(number) for number in input().split()]
            test_sets.append(TestSet(n, length, message))

    for index, test_set in enumerate(test_sets, 1):
        # contains the alphabet of primes
        alphabet = {}
        possible_primes = sieve_of_eratosthenes(test_set.largest_n)
        counter = 1

        for prime in possible_primes:
            for message_num in test_set.message_list:
                if message_num % prime == 0:
                    alphabet[prime] = ALPHABET_MATCH[counter]
                    counter += 1
                    break
            if counter > 26:
                break

        result_list = []
        previous_prime = 0
        first_number = test_set.message_list[0]
        for prime in alphabet.keys():
            if first_number % prime == 0:
                if previous_prime == 0:
                    pair = (min(prime, first_number // prime),
                            max(prime, first_number // prime))
                    letter_pair = alphabet[pair[0]] + alphabet[pair[1]]
                    result_list.append(letter_pair)
                    previous_prime = pair[1]
                    break
        for number in test_set.message_list[1:]:
            if number > previous_prime:
                previous_prime = number // previous_prime
            else:
                previous_prime = previous_prime // number

            result_list.append(alphabet[previous_prime])
        print('Case #{}: {}'.format(index, (''.join(result_list))))


if __name__ == '__main__':
    main()
