
class Solution:
    def validPalindrome(self, s):
        
        left, right = 0, (len(s)-1)
        
        while left <= right:
            print(left, right)
            if s[left] != s[right]:
                left_str = s[:left] + s[left+1:]
                right_str = s[:right] + s[right+1:]
            
                return left_str==left_str[::-1] or right_str==right_str[::-1]
            left+=1
            right-=1
            
        return True                

if __name__ == "__main__":
    s = "abca"
    sol = Solution()
    print(sol.validPalindrome(s))