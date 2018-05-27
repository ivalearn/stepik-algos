def main():
    input()
    arr = [int(val) for val in input().split()]
    win = int(input())
    imax = [0] * win
    omax = [0] * win
    res = []
    for i in range(win-1, len(arr)):
        j = i % win
        imax[j] = max(arr[i], imax[j-1]) if j else arr[i]
        if j < win-1:
            res.append(max(imax[j-win], omax[win-2-j]))
            continue
        omax[0] = arr[i]
        for k in range(win-1):
            omax[k+1] = max(arr[i-k-1], omax[k])
        res.append(omax[-1])
    print(*res)

main()