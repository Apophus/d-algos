def knapsackLight(value1, weight1, value2, weight2, maxW):
    
    if (weight1 + weight2) > maxW and weight1 > maxW and weight2>maxW:
        return 0
    elif (weight2 + weight1) <= maxW:
        return value2+value1

    elif weight1 <= maxW and weight2 > maxW:
        return value1
    elif weight2 <= maxW and weight1 > maxW:
        return value2
    else:
        return max(value1, value2)