def arrayMaxConsecutiveSum(inputArray, k):
    c = m = sum(inputArray[:k])
    
    for i in range(len(inputArray) - k):
        c = c + inputArray[i + k] - inputArray[i]
        m = max(c, m)
        
    return m



inputArray = [1, 3, 2, 4]
k = 3

print(arrayMaxConsecutiveSum(inputArray, k))