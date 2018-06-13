#########
# exam

from collections import namedtuple
Node = namedtuple('Node', ['key', 'left', 'right'])

num = int(input())
tree = [Node(*map(int, input().split())) for _ in range(num)]

node = 0 if tree else -1
stack = []
lval = rval = None
valid = True

while node != -1 or stack:
    if node != -1:
        stack.append((node, lval, rval))
        key = tree[node].key
        valid = ((lval is None or lval <= key) and
                 (rval is None or key < rval))
        if not valid:
            break
        rval = key if rval is None else min(rval, key)
        node = tree[node].left
        continue
    node, lval, rval = stack.pop()
    key = tree[node].key
    lval = key if lval is None else max(lval, key)
    node = tree[node].right

print(['INCORRECT','CORRECT'][valid])