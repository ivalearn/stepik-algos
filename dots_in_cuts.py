
def main():
    from sys import stdin
    reader = (list(map(int, line.split())) for line in stdin)
    n_cuts, n_dots = next(reader)
    cuts = [next(reader) for _ in range(n_cuts)]
    dots = next(reader)
    assert len(dots) == n_dots
    print(*dots_in_cuts(dots, cuts))


def test():
    from random import randint
    from time import perf_counter as timer
    from sys import stderr

    assert dots_in_cuts([], [(1,5),(7,9)]) == []
    assert dots_in_cuts([5], []) == [0]
    assert dots_in_cuts([3], [(1,6),(5,3),(1,6)]) == [2]
    result1 = dots_in_cuts([1,6,11], [(8,9),(0,5)])
    assert result1 == [1,0,0], "got {}".format(result1)
    result2 = dots_in_cuts([1,6,11], [(0,5),(7,10)])
    assert result2 == [1,0,0], "got {}".format(result2)

    xmax = 10**6
    xmin = -xmax
    nmax = 10**4
    tmax = 10
    niter = 1000

    maxtime = maxiter = 0
    for t in range(niter):
        dots = [randint(xmin, xmax) for _ in range(randint(0, nmax))]
        cuts = [(min(a,b), max(a,b))
                for a,b in ((randint(xmin,xmax), randint(xmin, xmax))
                            for _ in range(randint(0, nmax)))]
        t1 = timer()
        real_result = dots_in_cuts(dots, cuts)
        t2 = timer()
        naive_result = [sum(c[0]<=d<=c[1] for c in cuts) for d in dots]
        assert real_result == naive_result
        assert t2-t1 < tmax
        maxtime = max(maxtime, t2-t1)
        maxiter = max(maxiter, (t2-t1) / (len(dots) * len(cuts) + 1))
        stderr.write(".")
        stderr.flush()

    print("ok {:.3f}ms {:.3f}us".format(maxtime*1e3, maxiter*1e6))


def dots_in_cuts(dots, cuts):
    from itertools import groupby

    if not cuts:
        return [0] * len(dots)
    if not dots:
        return []

    cl, cr, cn = zip(*((c[0], c[1], sum(1 for _ in g))
                       for c, g in groupby(sorted(cuts))
                       if c[0] <= c[1]))
    n = len(cn)-1

    counts = []
    for d in dots:
        if d < cl[0]:
            counts.append(0)
            continue
        cnt = 0

        l, r = 0, n
        while l < r:
            break
            m = (l + r + 1) // 2
            if cl[m] > d:
                r = m-1
            else:
                l = m

        for i in range(n, -1, -1):
            if cl[i] <= d:
                break

        #assert i == l, "{}<>{} : {} {}".format(l, i, d, cl)

        for j in range(i+1):
            if d <= cr[j]:
                cnt += cn[j]

        counts.append(cnt)

    return counts

#main()
test()