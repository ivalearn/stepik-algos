
def max_non_inc_seq(A, n=None):
    if n is None:
        n = len(A)
    D = [1] * n
    P = [-1] * n
    a_best = i_best = d_best = 0

    for i in range(n):
        a = A[i]
        if a <= a_best:
            p, d = i_best, d_best+1
        else:
            p, d = -1, 0
            for j in range(i):
                if a <= A[j] and D[j] > d:
                    p, d = j, D[j]
            d += 1
        P[i], D[i] = p, d
        if d > d_best:
            i_best, a_best, d_best = i, a, d

    out = [0] * d_best
    i = i_best
    for j in range(d_best-1, 0, -1):
        out[j], i = i+1, P[i]
    out[0] = i+1
    return d_best, out


def main():
    from sys import stdin
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d, seq = max_non_inc_seq(a, n)
    print(d)
    print(*seq)


def test(niter=60, nmax=10**5, xmax=10**9, tmax=2, rseed=123):
    from random import randint, shuffle, seed
    from time import perf_counter as timer
    from sys import stderr
    seed(rseed)

    assert max_non_inc_seq([1]) == (1, [1])
    assert max_non_inc_seq([5,3,4,4,2]) == (4, [1,3,4,5])

    t1 = timer()
    maxd, out = max_non_inc_seq([xmax-i for i in range(nmax)])
    t2 = timer()
    assert t2-t1 < tmax

    for t in range(niter):
        a = list(range(1, randint(2, nmax)))
        shuffle(a)
        t1 = timer()
        maxd, out = max_non_inc_seq(a)
        t2 = timer()
        assert t2-t1 < tmax, "got {:.1f} sec".format(t2-t1)
        stderr.write(".")

    stderr.flush()
    print("OK")
    
#max_non_inc_seq([5,3,4,4,2], 5)
#main()
test(niter=1, tmax=8)