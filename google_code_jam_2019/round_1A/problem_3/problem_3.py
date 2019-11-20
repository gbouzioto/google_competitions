import sys

if len(sys.argv) > 1:
    input_file = sys.argv[1]
    with open(input_file) as f:
        numbers = list(map(int, f.readlines()))[1:]
else:
    times = int(input())
    numbers = [int(input()) for _ in range(times)]
