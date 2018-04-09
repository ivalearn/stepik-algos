# knapsack practicum
# https://stepik.org/lesson/13244/step/3
import sys
import heapq

def fractional_knapsack(capacity, values_and_weights):
    order = [(-v / w, w) for v, w in values_and_weights]
    heapq.heapify(order)

    acc = 0
    while order and capacity:
        v_per_w, w = heapq.heappop(order)
        can_take = min(w, capacity)
        acc -= v_per_w * can_take
        capacity -= can_take

    return acc

def main():
    reader = (tuple(map(int, line.split())) for line in sys.stdin)
    n, capacity = next(reader)
    values_and_weights = list(reader)
    assert len(values_and_weights) == n
    opt_value = fractional_knapsack(capacity, values_and_weights)
    print("{:.3f}".format(opt_value))

def test():
    assert fractional_knapsack(0, [(60,20)]) == 0
    assert fractional_knapsack(25, [(60,20)]) == 60.0
    assert fractional_knapsack(25, [(60,20), (0,100)]) == 60.0
    assert fractional_knapsack(25, [(60, 20), (50, 50)]) == 65.0
    assert fractional_knapsack(50, [(60,20),(100,50),(120,30)]) == 180.0

    from random import randint
    from timing import timed
    for attempt in range(100):
        n = randint(1, 1000)
        m = 2 * 10**6
        capacity = randint(0, m)
        values_and_weights = []
        for _ in range(n):
            v = randint(0, m)
            w = randint(1, m)
            values_and_weights.append((v,w))
        t = timed(fractional_knapsack, (capacity, values_and_weights))
        assert t < 1
    print("OK")

main()
#test()