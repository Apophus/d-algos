def contains_alphabet(word):
    for _ in word:
        if _.isalpha(): return True
    return False

def top_3_words(text):
    if not text:
        return []
    
    word_count = {}
    word = ''
    left  = 0
    
    for char in text.lower():
        if char.isalpha() or char == "'":
            word += char
            left += 1
        elif left == 0:
            pass
        else:
            if not contains_alphabet(word):
                word = ''
                continue
            else:
                word_count[word] = word_count.get(word, 0) + 1
                
            word = ''
            left = 0
    word_count = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    if not word_count: return []
    elif len(word_count) == 1: return [word_count[0][0]]
    elif len(word_count) == 2: return [word_count[0][0],word_count[1][0]]
    elif len(word_count) >=3:  
        return [word_count[0][0],word_count[1][0], word_count[2][0]]
    

if __name__ == '__main__':
    text = 'a a a  b  c c  d d d d  e e e e e'
    res = top_3_words(text)
    print(res)