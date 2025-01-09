line_text = "welcome to Jamayca. have a nice day. how are you. date to dream"
word = "are"

def count_occurences(text_line, word):
  #1. split text line into words (tokens)
  tokens = line_text.split(" ")
  counter = 0
  #2. loop on array
  for index in range(len(tokens)):
    # 3. count appearences of word
    if (tokens[index] == word):
      counter += 1
  return counter

count = count_occurences(line_text, word)
print(f'the occurence of {word} is {count}')