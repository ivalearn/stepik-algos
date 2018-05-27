from sys import stdin
phones = [None] * (10**7+1)
next(stdin)
for req in stdin:
    req = req.split()
    cmd, num = req[0], int(req[1])
    if cmd == "add":
        phones[num] = req[2]
    elif cmd == "del":
        phones[num] = None
    else:
        print(phones[num] or "not found")