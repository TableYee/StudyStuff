import sys

if __name__ == "__main__":
    k = int(sys.stdin.readline().strip())

    weights = list(map(int, sys.stdin.readline().strip().split()))

    weights.sort()

    max_num = sum(weights)

    candidates = [ weights[0] ]
    print(candidates)
    for i in range(1, k):
        cur_num = weights[i]
        temp = [ cur_num ]

        for e in candidates:
            print(cur_num, e)
            temp += [ cur_num + e, abs(cur_num-e) ]

        candidates += temp
        print(candidates)

    candidates = list(set(candidates))

    if 0 in candidates:
        candidates.remove(0)

    answer = max_num - len(candidates)

    print(answer)