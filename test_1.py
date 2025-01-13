import array
array1 = array.array("i", [1,1 ,11,3,1])
array2 = array.array("i", [1,21,11,3,1])

def count_in_array(arr, item):
  # alternative form - array1 = [1,1,11,3,1]
  #item = int(input("which number is being counted?"))
  counter = 0
  for current_index in len(arr):
    if (arr[current_index] == item) : 
      counter +=1
 
## Question 1:
def is_sorted_array(arr):
  for index in range(len(arr) - 1):
    if (arr[index + 1] <= arr[index]):
      return False    
  return True

array1item = [1]
print (is_sorted_array(array1item))
def is_sorted(arr):
  if (is_sorted_array(arr, True) or is_sorted_array(arr, False)):
    return True
  else:
    return False
  
##Check question 1 : 
a1 = [1,2,44,55]
print (a1)
print ("is a1 ascending sorted ? ", is_sorted_array(a1, True))
print ("is a1 descending sorted ? ", is_sorted_array(a1, False))
print ("is a1 sorted ? ", is_sorted(a1))


a1 = [1,333,44,55]
print (a1)
print ("is a2 ascending sorted ? ", is_sorted_array(a1, True))
print ("is a2 descending sorted ? ", is_sorted_array(a1, False))
print ("is a2 sorted ? ", is_sorted(a1))

## Question 2:
def second_highest(arr):
  
  if (arr[0] >= arr[1]):
    max_item = arr[0]
    second_item = arr[1]
  else : 
    max_item = arr[1]
    second_item = arr[0]
  #arr = [1,88,55, 222, 344]
  
  for index in range(3):
    if (arr[index +2] >= max_item):
      second_item = max_item
      max_item = arr[index + 2]
    elif (arr[index + 2] >= second_item):
      second_item = arr[index+2]
  
  return second_item

#check question 2 : 
a3 = [1,88,55, 22, 34]
print(a3)
print ("second highest of a3 is ", second_highest(a3))


#Question 3
def reverse_number(my_number):
  reversed_result = 0
  
  while(my_number > 0):
    digit = my_number % 10
    reversed_result = (reversed_result * 10) + digit
    my_number = my_number // 10
    
  return reversed_result

my_num = 123423

print(f'my number is {my_num}. reversed is {reverse_number(my_num)}')   


#Question 4 
def weak_union(arr1, arr2):
  my_set = set()
  for item in arr1:
    my_set.add(item)
  for item2 in arr2:
    my_set.add(item2)
    
  return my_set

#check question 4
arr1 = [1,2,3,3,4,4,3,2]
arr2 = [1,2,3,8,4,4,3,2]

print (arr1, arr2, weak_union(arr1, arr2))

# question 5
def count_words_in_line(line):
  words_in_line = line.split(" ")
  words = {}
  for word in words_in_line:
      if (word in words.keys()):
        words[word] += 1
      else :
        words[word] = 1
        
  return words

#check question 5
line = "Mary had a little lamb its fleas were white as snow white as snow white as snow"

print (line)
print(count_words_in_line(line))

## Bonus : 
def is_permutation(num1, num2):
  arr1 = array.array("i",[])
  arr2 = array.array("i",[])
  
  while(num1 > 0):
    digit = num1 % 10
    arr1.append(digit)
    digit = num2 % 10
    arr2.append(digit)
    num1 = num1 // 10
    num2 = num2 // 10
  
  count1 = {}
  count2 = {}
  for index in range(len(arr1)):
      current1 = arr1[index]
      current2 = arr2[index]
      if (current1 in count1.keys()):
        count1[current1] += 1
      else :
        count1[current1] = 1
      
      if (current2 in count2.keys()):
        count2[current2] += 1
      else :
        count2[current2] = 1
        
  if (len(count1.keys()) != len (count2.keys())):
    return False
  else : 
    for key in count1.keys():
      if (not(key in count2.keys()) or 
          count1[key] != count2[key]):
        return False
  
  return True

#Check Bonus : 
num1 = 1231
num2 = 3221

print (num1, num2)
print (is_permutation(num1, num2))

num1 = 123
num2 = 321

print (num1, num2)
print (is_permutation(num1, num2))
      