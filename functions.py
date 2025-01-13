import array

def is_sorted (arr):
    n = len(arr)
    
    for index in range (n-1):
      if (arr[index] > arr[index+1]):
        return False
    
    return True

def is_sorted2(some_array):
  
  if (some_array[0] > some_array[1]):
    return False
  if (some_array[1] <= some_array[2]):
    return True
  if (some_array[2] <= some_array[3]):
    return True
  
  return False

arr1 = array.array("i", [11,5,6,8,6,7,13,22,33])
arr2 = [1,5,6,8,9,11,13,22,33]; # python non-safe

print (is_sorted2(arr1)) #True 1<5
print (is_sorted2(arr2)) #True 1<5

if (is_sorted2(arr1)):
  print ("array is sorted")
else:
  print ("array is not sorted")