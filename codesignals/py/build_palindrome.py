def buildPalindrome(st):
    string_list = list(st)
    i = 0
    while string_list != string_list[::-1]:
        string_list.insert(len(st),st[i])
        i += 1
    return "".join(string_list)

print(buildPalindrome('ababab')) # abababa
print(buildPalindrome('abc')) # abcba
print(buildPalindrome('abcb')) # abcbcba
print(buildPalindrome('abcabc')) # abcabcbacba
print(buildPalindrome('cbdbedffcg')) # cbdbedffcgcffdebdbc