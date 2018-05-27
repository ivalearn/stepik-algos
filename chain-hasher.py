from sys import stdin

hash_size = int(next(stdin))
n_reqs = int(next(stdin))
table = [[] for _ in range(hash_size)]
for line in stdin:
    cmd, word = line.split()
    if cmd == "check":
        ind = int(word)
    else:
        ind, mul = 0, 1
        for ch in word:
            ind = (ind + ord(ch) * mul) % 1000000007
            mul *= 263
        ind %= hash_size
    if cmd == "add":
        if word not in table[ind]:
            table[ind].insert(0, word)
    elif cmd == "del":
        if word in table[ind]:
            table[ind].remove(word)
    elif cmd == "find":
        print(["no", "yes"][word in table[ind]])
    elif cmd == "check":
        print(*table[ind])