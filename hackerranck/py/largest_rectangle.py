def largestRectangle(h):
    # Write your code here
    max_area = 0
    stack = []
    
    for curr_index, height in enumerate(h):
        start = curr_index
        
        while stack and stack[-1][1] > height:
            _index, _height = stack.pop()
            max_area = max(max_area, _height*(curr_index - _index))
            start = _index
        stack.append((start, height))
    for index, height in stack:
        max_area = max(max_area, height*(len(h)-index))
    return max_area
            