def nonDivisibleSubset(k, s):
    # Write your code here
    remainders = [0]*k
    
    for i in s:
        remainders[i%k] += 1
        
    count = min(remainders[0],1)
    for i in range(1, k//2+1):
        if i ==k-i:
            count+=1
        else:
            count += max(remainders[i], remainders[k-i])
            
    return count