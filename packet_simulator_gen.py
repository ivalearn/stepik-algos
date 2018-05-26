def buffer_sim(size, packets):
    ends = []
    for start, length in packets:
        time = ends[-1] if ends else start
        while ends and ends[0] <= start:
            del ends[0]
        result = -1
        if len(ends) < size:
            result = max(time, start)
            ends.append(result + length)
        yield result

if __name__ == "__main__":
    import sys
    input_gen = (map(int, line.split()) for line in sys.stdin)
    size, npackets = next(input_gen)
    print(*buffer_sim(size, input_gen), sep="\n")