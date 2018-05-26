
def main():
    input()
    arr = [int(val) for val in input().split()]
    win1 = int(input()) - 1
    inp_val = arr[:win1]
    inp_max, out_max, res = [], [], []
    for val in arr[win1:]:
        inp_val.append(val)
        inp_max.append(max(val, inp_max[-1]) if inp_max else val)
        if out_max:
            res.append(max(inp_max[win1 - len(out_max)], out_max.pop()))
        else:
            out_max = [inp_val.pop()]
            while inp_val:
                out_max.append(max(inp_val.pop(), out_max[-1]))
            inp_max = []
            res.append(out_max.pop())
    print(*res)

main()