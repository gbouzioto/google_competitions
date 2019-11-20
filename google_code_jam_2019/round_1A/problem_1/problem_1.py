
import sys


def main():
    words = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()
            times = int(lines.pop(0))
            while len(lines) > 0:
                n = int(lines.pop(0))
                test_case = []
                for i in range(n):
                    test_case.append(lines.pop(0).rstrip())
                words.append(test_case)
    else:
        times = int(input())
        for i in range(times):
            n = int(input())
            test_case = []
            for _ in range(n):
                test_case.append(input())
            words.append(test_case)

    for index, test_case in enumerate(words, 1):
        count = 0
        rhymes = set()
        case = test_case.copy()
        while len(test_case) > 1:
            word = test_case.pop(0)
            for rest_word in test_case:
                possible_rhyme = ''
                for i in range(-1, -len(rest_word) - 1, -1):
                    if rest_word[i] == word[i]:
                        possible_rhyme += rest_word[i]
                        rhymes.add(''.join(reversed(possible_rhyme)))
                    else:
                        break
                rhymes.add(''.join(reversed(possible_rhyme)))
        if len(rhymes) == 1 and '' in rhymes:
            print('Case #{}: {}'.format(index, count))
            continue
        rhymes = list(rhymes)
        rhymes.sort(key=len, reverse=True)
        for rhyme in rhymes:
            already_matched = set()
            for i in range(len(case)):
                if case[i] in already_matched:
                    continue
                if case[i].endswith(rhyme):
                    already_matched.add(case[i])
            count += len(already_matched) // 2
        print('Case #{}: {}'.format(index, count))


if __name__ == '__main__':
    main()
