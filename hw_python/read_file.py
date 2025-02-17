import os

path = os.environ['path']
paths = path.split(';')

def write_file(file_name):
    # Open the file in read mode
    with open(file_name, "w") as file:
        # Read all lines of the file
        content = file.read()
        return content
        
content = read_file("example.txt")
print(content)
text_lines_array = content.split("\n")
print(len(text_lines_array))

words = {}
for line in text_lines_array:
  words_in_line = line.split(" ")
  for word in words_in_line:
    if (word in words.keys()):
      words[word] += 1
    else :
      words[word] = 1

for w in words.keys() : 
  if (words[w]> 1):
    print (w, "appears more than once")
    
    
for w in words.keys() : 
  print (w, "appears ", words[w])
    
    