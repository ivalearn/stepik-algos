################################
# like exam, but recirsive

from collections import namedtuple

TupleNode = namedtuple('TupleNode', ['key', 'left', 'right'])

def validate_rec(tree, node=0):
    cur_val = cur_min = cur_max = tree[node].key
    left = tree[node].left
    if left >= 0:
        left_min, left_max = validate_rec(tree, left)
        assert cur_val > left_max
        cur_min = min(cur_min, left_min)
        cur_max = max(cur_max, left_max)
    right = tree[node].right
    if right >= 0:
        right_min, right_max = validate_rec(tree, right)
        assert cur_val < right_min
        cur_min = min(cur_min, right_min)
        cur_max = max(cur_max, right_max)
    return cur_min, cur_max

def main():
    num_nodes = int(input())
    tree = [TupleNode(*map(int, input().split()))
            for i in range(num_nodes)]
    try:
        if tree:
            validate_rec(tree)
        print('CORRECT')
    except AssertionError:
        print('INCORRECT')

if __name__ == '__main__':
    import sys
    sys.setrecursionlimit(65536)
    main()