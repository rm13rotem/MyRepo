bad_words = ("fuck", "shit", "bugger", "tit", "ass")

def clean_language(sentence):
  words = sentence.split(' ')
  for word in words:
    if (word in bad_words):
      print("No swearing!")
      return
      
  print (sentence)

for index in range(3):
  line = input(">>")
  clean_language(line)