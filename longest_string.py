def longest_string(arr):
  max_string = ""
  
  for index in range(len(arr)):
    if (len(arr[index]) > len(max_string)):
      max_string = arr[index]
      
  return max_string

my_array = ["moshe", "rotem", "Avraham", "Nasrallah"];
print (longest_string(my_array))