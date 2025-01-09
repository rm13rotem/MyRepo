array1 = [1,2,3,4,2]
array2 = [1,1,2,1,1]
array3 = [-1,-2,-3,-4,-2]


def is_balanced (arr):
  sum_bottom = arr[0]
  sum_top = arr[-1]
  i = 0
  j = -1
  while (i<len(arr) + j):
    if (sum_bottom == sum_top and i == len(arr) + j - 1):
      return True
    elif (sum_bottom > sum_top and arr[j-1] > 0):
      j = j-1
      sum_top += arr[j]
    elif (sum_bottom < sum_top and arr[j-1] < 0):
      j = j-1
      sum_top += arr[j]
    elif (sum_bottom > sum_top and arr[i+1] > 0):
      i = i+1
      sum_bottom += arr[i]
    else:
      i = i+1
      sum_bottom += arr[i]
    
    print ("sum1 =", sum_bottom," i=",i, " sum2 = ", sum_top, " j = ",j)
  return False

print ("array 1 is balance = ", is_balanced(array1))
print ("array 2 is balance = ", is_balanced(array2))
print ("array 3 is balance = ", is_balanced(array3))

def is_array_balanced(array):
  total_sum = sum(array)
  left_sum = 0
  if total_sum%2==1:
   return False

  for num in array:
    left_sum += num
    if left_sum == total_sum / 2:
       return True
  return False

array = []
array_length = int(input("How long do you want the array? "))
for i in range(array_length):
    num = int(input("Please enter a number for the array: "))
    array.append(num)
if is_array_balanced(array):
   print("The array is balanced")
else:
   print("The array is not balanced")