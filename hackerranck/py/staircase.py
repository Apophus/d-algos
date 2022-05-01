def staircase(n):
    # Write your code here
    char = '#'
    padding = ' '
    for i in range(1, n+1):
        # print(f'{char*i:{padding}>{n-i}}', f'-- {n-i} -- {i}')
        space = ' '*(n-i)
        reps = char * i 
        print(f"{space+reps}")

print(staircase(5))