import sys

WIN = {'R': 'P',
       'S': 'R',
       'P': 'S'}

NOT_LOSES = {'RP': 'P',
             'PR': 'P',
             'SR': 'R',
             'RS': 'R',
             'SP': 'S',
             'PS': 'S'}


def main():
    oppenents = []
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        with open(input_file) as f:
            lines = f.readlines()
            lines.pop(0)
            while len(lines) > 0:
                n = int(lines.pop(0))
                test_case = []
                for i in range(n):
                    test_case.append(lines.pop(0).rstrip())
                oppenents.append(test_case)
    else:
        times = int(input())
        for i in range(times):
            n = int(input())
            test_case = []
            for _ in range(n):
                test_case.append(input())
            oppenents.append(test_case)

    for index, test_case in enumerate(oppenents, 1):
        oppent_letters = {}
        impossible = False
        for opponent in test_case:
            for _index, letter in enumerate(opponent):
                if not oppent_letters.get(_index):
                    oppent_letters[_index] = set()
                oppent_letters[_index].add(letter)
        result = ''
        if len(oppent_letters[0]) == 3:
            impossible = True
        if not impossible:
            for key in oppent_letters.keys():
                letters = oppent_letters[key]
                if len(letters) == 1:
                    result += WIN[letters.pop()]
                    break
                elif len(letters) == 2:
                    if not oppent_letters.get(key + 1):
                        impossible = True
                        break
                    not_loses = NOT_LOSES[''.join(letters)]
                    result += not_loses
                    if len(oppent_letters[key + 1]) != 1 and not_loses in oppent_letters[key + 1]:
                        oppent_letters[key + 1].remove(not_loses)

        if impossible:
            print('Case #{}: IMPOSSIBLE'.format(index))
            continue
        print('Case #{}: {}'.format(index, result))


if __name__ == '__main__':
    main()
