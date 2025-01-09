# General algorythm - maintain two pointers 
# for the sum of sub_series - total1 and total2
#
# Alignment - 
# in case of positive new number - add to them both
# in case of negative members - diverge the summation
# Disalignment - 
# add new number only to total2, until it goes below zero

# if at any point total2 exceeds total1 - drop total1, 
# and bring him to total2.

#TDD example - -9, -1, 0, 1, 2, 3, -1, -1, 4. 
# Max sub-series - 1,2,3,-1,-1,4 ==> sum = 8
# starting at 1 (index = 3), and collecting 6 elements

total1 = int (input("enter number"))
total2 = total1

start_index1 = 0
start_index2 = 0

count1 = 1
count2 = 1

for index in range(10):
  #print(index)
  number = int(input("enter number: "))
   
  if (total1 <= 0 and number >= total1):
    total1 = number
    total2 = number
    
    count1 = 1
    count2 = 1
    
    start_index1 = index
    start_index2 = index
    # total was -9 and now we got -4.   
     
  elif (number >= 0 and total1 == total2):
    # here total1 and total2 are positive
    total1 = total1 + number
    total2 = total2 + number
    
    count1 += 1
    count2 += 1
    # for example 1,3,4,2,1, ... -- keep collecting them.    
  else :
    total2 += number
    count2 += 1
    # for example 1,2, 3, -1, -1, 1,2, 3
    # total = 6, total2 = 6 and now (-1) they split
    
  if (total2 < 0):
    total2 = 0
    count2 = 0
    start_index2 = index + 1 
    # 1,2,3 , -1, *-7*, -8, 1,2, 3,4
    
  if (total2 > total1 & total1 > 0):
    total1 = total2
    start_index1 = start_index2
    count1 = count2
    
  print ("debug : number - ", number)
  print("total - ", total1, "from index = ", start_index1, " taking #", count1)
  print("total2 - ", total2, "from index = ", start_index2, " taking #", count2)

print ("sum of biggest series (of non negatives) is ", total1)