def lineEncoding(s):
    c = 1
    final = ""
    last = s[0]
    for i in range(1, len(s)):
        if last == s[i]:
            c += 1
        else:
            if c > 1:
                final += str(c) + last
            else:
                final += last
            last = s[i]
            c = 1
    return final + (str(c) if c > 1 else "") + last


print(lineEncoding('abbcabb'))

