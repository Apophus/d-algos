def strip_comments(strng, markers):
    split_strng = strng.split('\n')
    #print(split_strng)
    res = []
    def marker_check(word):

        for index, char in enumerate(word):
            if char in markers:
                new_word = word[:index]
                # res.append(new_word.rstrip())
                return new_word

    for word in split_strng:
        if marker_check(word):
            res.append(word.rstrip())
            continue
    return '\n'.join(res)

strng = "\t@ oranges - lemons ?\n@ strawberries =\ncherries # watermelons apples\nbananas oranges lemons = '\n="

markers = ["'", '=', '?', '@', ',', '^', '.']

#'\n\ncherries # watermelons apples\nbananas oranges lemons\n'

print(strip_comments(strng, markers))
