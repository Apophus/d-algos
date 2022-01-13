def extractEachKth(inputArray, k):

    
    if k ==1:
        inputArray.clear()
    
    no_of_elements = len(inputArray)//k


    for i in range(1,no_of_elements+1):
        inputArray.pop(k*i - i)
    return inputArray    

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k=3

print(extractEachKth(inputArray, k))