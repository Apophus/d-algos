#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    # Write your code here
    max_day = 0
    stack = []
    
    for plant in p:
        day = 0
        while stack and stack[-1][0]>=plant:
            day = max(day, stack.pop()[1])
            
        if stack:
            day += 1
        else:
            day = 0
            
        max_day = max(max_day, day)
        stack.append([plant, day])

    return max_day    
