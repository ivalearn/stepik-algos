from sys import stdin
read = lambda: map(int, stdin.readline().split())

n, m = read()
axis = []

for i in range(n):
    l, r = read()
    axis.append((l, -1, i))
    axis.append((r, 1, -i))

for i, d in enumerate(read()):
    axis.append((d, 0, i))

axis.sort()
hits = [0] * m
depth = 0

for x, dec, i in axis:
    depth -= dec
    if not dec:
        hits[i] = depth

print(*hits)