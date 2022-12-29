def reverse_words(text):
  #go for it
  split_txt = text.split(' ')
  result = []

  for word in split_txt:
    result.append(word[::-1])

  return ' '.join(result)