from sys import stdin

n_vars, n_eqs, n_neqs = map(int, next(stdin).split())
link = list(range(n_vars+1))
rank = [0] * (n_vars + 1)

def find(t):
    r = t
    while r != link[r]:
        r = link[r]
    if r not in (t, link[t]):
        while t != r:
            t, link[t] = link[t], r
    return r

# equalitites
for i in range(n_eqs):
    a, b = next(stdin).split()
    a, b = find(int(a)), find(int(b))
    if a == b:
        continue
    if rank[a] > rank[b]:
        a, b = b, a
    link[a] = b
    if rank[a] == rank[b]:
        rank[b] += 1

# inequalities
for line in iter(stdin):
    a, b = line.split()
    if find(int(a)) == find(int(b)):
        print(0)
        break
else:
    print(1)