# max stack
from sys import stdin
stack, maxes = [], []
num = int(stdin.readline())
for lineno in range(num):
    line = stdin.readline()
    if line.startswith("push"):
        x = int(line[5:])
        stack.append(x)
        maxes.append(max(x, maxes[-1]) if maxes else x)
    elif line.startswith("pop"):
        stack.pop()
        maxes.pop()
    elif line.startswith("max"):
        print(maxes[-1])