from collections import Counter


def freq_seq(s, sep):
    count = Counter(s)
    res = []
    for letter in s:
        res.append(str(count[letter]))
    sequence = str(sep).join(res)
    return sequence

if __name__ == '__main__':
    s = 'hello world'
    sep = '-'
    print(freq_seq(s, sep))

