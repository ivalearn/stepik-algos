from collections import Counter, namedtuple
from heapq import heapify, heappush, heappop

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_encode(s):
    heap = []
    for ch, freq in Counter(s).items():
        heap.append((freq, len(heap), Leaf(ch)))

    heapify(heap)

    count = len(heap)
    while len(heap) > 1:
        freq1, _count1, left = heappop(heap)
        freq2, _count2, right = heappop(heap)
        node = Node(left, right)
        heappush(heap, (freq1 + freq2, count, node))
        count += 1

    code = {}
    if heap:
        [(_freq, _count, root)] = heap
        root.walk(code, "")

    return code

def main():
    s = input()
    code = huffman_encode(s)
    encoded = "".join(code[ch] for ch in s)
    print(len(code), len(encoded))
    for ch in sorted(code):
        print("{}: {}".format(ch, code[ch]))
    print(encoded)

def huffman_decode(code, encoded):
    result = ""
    while encoded:
        for ch, seq in code.items():
            if encoded.startswith(seq):
                result += ch
                encoded = encoded[len(seq):]
                break
    return result

def test(n_iter=1000):
    import random
    import string
    
    for i in range(n_iter):
        length = random.randint(0, 32)
        s = "".join(random.choice(string.ascii_letters) for _ in range(length))
        code = huffman_encode(s)
        encoded = "".join(code[ch] for ch in s)
        assert huffman_decode(code, encoded) == s

    print("OK")

#main()
test()