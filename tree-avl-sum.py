
class SumNode:
    def __init__(self, key=None):
        self.key = self.sum = key
        self._clear()
        
    def _clear(self):
        self.left = self.right = None
        self.parent = None
        self.height = 0

    @property
    def left_height(self):
        return self.left.height if self.left else -1

    @property
    def right_height(self):
        return self.right.height if self.right else -1

    @property
    def left_sum(self):
        return self.left.sum if self.left else 0

    @property
    def right_sum(self):
        return self.right.sum if self.right else 0

    # вспомогательная операция: обновление высоты и суммы элемента
    def _update_height(self):
        old_h = self.height
        old_s = self.sum
        self.height = 1 + max(self.left_height, self.right_height)
        self.sum = self.key + self.left_sum + self.right_sum
        return self.height != old_h or self.sum != old_s


class SumTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        node, found = self.find_node(key)
        return found

    def add(self, key):
        self.add_node(SumNode(key))

    def remove(self, key):
        node, found = self.find_node(key)
        if found:
            self.remove_node(node)

    def find_node(self, key):
        node = parent = self.root
        while node:
            parent = node
            if key > node.key:
                node = node.right
            elif key < node.key:
                node = node.left
            else:
                assert key == node.key
                return node, True
        if parent:
            assert not (parent.left and parent.right)
        return parent, False

    def add_node(self, node):
        if not node:
            return False
        if not self.root:
            self.root = node
            node.parent = None
            return True
        parent, found = self.find_node(node.key)
        if found:
            return False
        if parent.key > node.key:
            parent.left = node
        else:
            parent.right = node
        node.parent = parent
        self._rebalance(parent)
        return True

    def remove_node(self, node):
        if not node:
            return
        if node.left and node.right:
            # two children
            orig = node
            node = node.left
            while node.right:
                node = node.right
            node.key, orig.key = orig.key, node.key
            self.remove_node(node)
        else:
            # one child or no children
            parent = node.parent
            child = node.left or node.right
            self._replace_child(node, child)
            node._clear()
            self._rebalance(parent)
        return node

    # вспомогательная операция, которая заменяет ссылку на элемент
    # в его родителе; выделена, т.к. используется очень часто
    def _replace_child(self, old_node, new_node):
        parent = old_node.parent
        old_node.parent = None
        if parent is None:
            assert self.root == old_node
            self.root = new_node
            if new_node:
                new_node.parent = None
            return None
        if old_node == parent.left:
            parent.left = new_node
            if new_node:
                new_node.parent = parent
            return True
        elif old_node == parent.right:
            parent.right = new_node
            if new_node:
                new_node.parent = parent
            return False
        else:
            raise RuntimeError('tree broken')

    # перебалансировка элемента в точности как на лекции
    def _rebalance(self, node, force=False):
        while node:
            left_h = node.left_height
            right_h = node.right_height
            if right_h - left_h > 1:
                beta = node.right
                gamma = beta.left
                if beta.right_height > left_h:
                    # малое правое вращение
                    node.right = gamma
                    if gamma:
                        gamma.parent = node
                    beta.left = node
                    self._replace_child(node, beta)
                    node.parent = beta
                else:
                    # большое правое вращение
                    assert gamma is not None
                    node.right = gamma.left
                    if node.right:
                        node.right.parent = node
                    beta.left = gamma.right
                    if beta.left:
                        beta.left.parent = beta
                    gamma.right = beta
                    beta.parent = gamma
                    beta._update_height()
                    self._replace_child(node, gamma)
                    gamma.left = node
                    node.parent = gamma
                    node.height = -1  # force update
            elif left_h - right_h > 1:
                beta = node.left
                gamma = beta.right
                if beta.left_height > right_h:
                    # малое левое вращение
                    node.left = gamma
                    if gamma:
                        gamma.parent = node
                    beta.right = node
                    self._replace_child(node, beta)
                    node.parent = beta
                else:
                    # большое правое вращение
                    assert gamma is not None
                    node.left = gamma.right
                    if node.left:
                        node.left.parent = node
                    beta.right = gamma.left
                    if beta.right:
                        beta.right.parent = beta
                    gamma.left, beta.parent = beta, gamma
                    beta._update_height()
                    self._replace_child(node, gamma)
                    gamma.right = node
                    node.parent = gamma
                    node.height = -1  # force update
            if not (node._update_height() or force):
                break
            node = node.parent

    # этот метод считает сумму тех элементов, где ключ больше границы
    def _sum_above(self, key):
        node = self.root
        # сначала берём полную сумму
        summ = node.sum if node else 0
        while node:
            if node.key > key:
                # пропускаем элементы, которые больше границы
                node = node.left
                continue
            # у остальных элементов вычитаем их значение и сумму левого поддерева
            summ -= node.key + (node.left.sum if node.left else 0)
            # остановка, если наталкиваемся на точное совпадение ключа
            node = None if node.key == key else node.right
        return summ

    def sum_between(self, left, right):
        # проверка корректности интервала очень важна,
        # т.к. иначе разность будет некорректной
        if right > left:
            # вычитаем из более широкой суммы менее широкую
            return self._sum_above(left-1) - self._sum_above(right)
        elif right == left:
            # если границы равны, можно поступить оптимально
            # и вместо расчёта полных сумм просто проверить наличие совпадения
            return left * self.find(left)
        else:
            return 0


def main():
    from sys import stdin

    summ = 0
    tree = SumTree()

    def f(x):
        return (int(x) + summ) % 1000000001

    # число задач не нужно, просто читаем вход до конца
    next(stdin)

    for line in stdin:
        if line[0] == 's':
            op, left, right = line.split()
            left, right = f(left), f(right)
            summ = tree.sum_between(left, right)
            print(summ)
            continue

        op, val = line.split()
        val = f(val)
        if op == '?':
            print(['Not found','Found'][tree.find(val)])
        if op == '+':
            tree.add(val)
        elif op == '-':
            tree.remove(val)


if __name__ == '__main__':
    main()