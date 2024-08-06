class Solution:
    def carFleet(self, target, position, speed):
        stack = []
        pos_speed = [[p, s] for p, s in zip(position, speed)]
        
        for pos, sp in sorted(pos_speed)[::-1]:
            stack.append((target-pos)/sp)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
                
        return len(stack)
