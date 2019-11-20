import random
import string


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


def generate_random_word(alphabet, letters=25):
    random_word = []
    random_word_str = []
    reverse_alphabet = {v: k for k, v in alphabet.items()}
    print(reverse_alphabet)
    c_count = 1
    primes = [alphabet[letter] for letter in string.ascii_uppercase]
    random_word.append(primes[0] * primes[1])
    random_word_str.append('AB')
    for index in range(1, len(primes) - 1):
        random_word.append(primes[index] * primes[index + 1])
        random_word_str.append(string.ascii_uppercase[index + 1])
        c_count += 1
    remaining_letters = letters - c_count
    if remaining_letters <= 0:
        return random_word, random_word_str
    random.shuffle(primes)
    previous_prime = alphabet['Z']
    while remaining_letters > 0:
        random_int = random.randint(0, len(primes) - 1)
        random_word_str.append(reverse_alphabet[primes[random_int]])
        random_word.append(previous_prime * primes[random_int])
        previous_prime = primes[random_int]
        remaining_letters -= 1
    return random_word, random_word_str


def main():
    primes = sieve_of_eratosthenes(10000)
    random_p = random.sample(primes, 26)
    random_p.sort()
    print(random_p)
    alphabet_map = {}
    eng_alpha_str = string.ascii_uppercase
    assert len(eng_alpha_str) == 26
    for i in range(26):
        alphabet_map[eng_alpha_str[i]] = random_p[i]
    print(alphabet_map)
    word, word_str = generate_random_word(alphabet_map, 100000)
    print(' '.join(str(num) for num in word))
    print(''.join(c for c in word_str))
    print(len(word), len(''.join(c for c in word_str)))


if __name__ == '__main__':
    main()
