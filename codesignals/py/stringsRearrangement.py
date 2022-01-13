from itertools import permutations as p
def stringsRearrangement(inputArray):

    def differs_by_one(str_1, str2):
        return(sum(a!=b for a,b in zip(str_1,str2))) == 1

    def good_arrangement(arr):
        return all(differs_by_one(arr[i], arr[i+1]) for i in range(len(arr)-1))
    
    return any(map(good_arrangement, p(inputArray)))

    
