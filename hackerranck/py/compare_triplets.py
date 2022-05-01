def compareTriplets(a, b):
    # Write your code here
    alice = 0 
    bob = 0
    for index, score in enumerate(a):
        if score > b[index]:
            alice += 1
        elif score < b[index]:
            bob += 1
        else:
            continue

    results = [alice, bob]

    return results



