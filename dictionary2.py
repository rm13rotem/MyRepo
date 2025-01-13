line_text = "hello he#llo. hello.. TEST. test how are        you ! one two THREE ARE"
def clean_string(my_string):
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'  ', ' ')
  my_string = str.replace(my_string,'.', '')
  my_string = str.replace(my_string,'!', '')
  my_string = str.replace(my_string,'#', '')
  return my_string

def return_map (my_string):
  words = clean_string(my_string).split(" ")
  print("original string is ",my_string)
  print ("after clean up words are ",words)
  result = {}
  
  for w in words:
    w = w.lower()
    if (w in result.keys()):
      result[w] += 1
    else :
      result[w] = 1
  
  if ('' in result.keys()):
    del result['']
    
  return result

print("grouped into words result is ",return_map(line_text))