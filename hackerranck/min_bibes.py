def minimumBribes(q):
    # Write your code here
    swaps = 0

    Q = [P-1 for P in q]

    for index, pos in enumerate(Q):

        if pos - index > 2:
            print("Too chaotic")

            return

        for j in range(max(pos-1, 0), index):
            if Q[j] > pos:
                swaps +=1

    print(swaps)

q = [2, 1, 5, 3, 4]

print(minimumBribes(q))
