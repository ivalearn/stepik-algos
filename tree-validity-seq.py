#########
# exam

from collections import namedtuple


def validate_seq():
    node, stack, oldval = 0, [], None
    while tree and node >= 0 or stack:
        if node >= 0:
            stack.append(node)
            node = tree[node].left
            continue
        node = stack.pop()
        curval = tree[node].key
        node = tree[node].right
        if oldval is not None and curval <= oldval:
            return False
        oldval = curval
    return True


num_nodes = int(input())
TupleNode = namedtuple('TupleNode', ['key', 'left', 'right'])
tree = [TupleNode(*map(int, input().split())) for _ in range(num_nodes)]
print(['INCORRECT', 'CORRECT'][validate_seq()])