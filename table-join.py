import sys

def main():
    input()
    sizes = list(map(int, input().split()))
    links = list(range(len(sizes)))
    szmax = max(sizes)
    def root(t):
        r = t
        while r != links[r]:
            r = links[r]
        if r not in (t, links[t]):
            while t != r:
                t, links[t] = links[t], r
        return r
    for line in sys.stdin:
        d, s = line.split()
        d = root(int(d)-1)
        s = root(int(s)-1)
        if s != d:
            sizes[d] += sizes[s]
            sizes[s] = 0
            links[s] = d
            szmax = max(szmax, sizes[d])
        print(szmax)

main()