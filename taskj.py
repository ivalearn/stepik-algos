
import sys
from collections import Counter

def most_common(a):
    cnt = Counter(a)
    maxnum = max(cnt.values())
    vals = [val for val,num in cnt.items() if num==maxnum]
    return max(vals)

def test():
    assert most_common([3,3,3]) == 3
    assert most_common([4,1,4,3,3]) == 4
    assert most_common([10,6,10,10,10,10,8,8,10,9]) == 10
    print("ok")

def main():
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n
    print(most_common(a))

main()