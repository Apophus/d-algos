import heapq

def cookies(k, A):
    # Write your code here
    heapq.heapify(A)
    
    if A[0] >= k: return 0
    operations = 0
    
    while len(A) >=2:
        least = heapq.heappop(A)
        second_least = heapq.heappop(A)
        heapq.heappush(A, least+(2*second_least))
        operations +=1
        new_least = heapq.heappop(A)
        if new_least >= k:
            return operations
        heapq.heappush(A, new_least)
    
    return -1
if __name__ == '__main__':
    A = [1, 2, 3, 9, 10, 12] 
    res = cookies(7, A)
    print(res)