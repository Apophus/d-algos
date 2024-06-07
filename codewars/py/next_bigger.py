def next_bigger(n):
    res = -1
    
    if n < 10:
        return 
    
    def keep_deviding(n):
        divisor = 1
    
        while n > 10*divisor:
            divisor *= 10
        
        quotient, remainder = divmod(n,divisor)
        res = (quotient*divisor)+res if res else quotient       
        if remainder < 100:
            first, last = remainder //  10, remainder%10
            if  first > last:
                last, first = first, last
                res += first *10
                res += last
            return
        keep_deviding(remainder)
    keep_deviding(n)  
    return res
        
