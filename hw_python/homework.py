import random

def get_valid_difficulty_level():   
    #return 1,2,3 
    difficulty_level = int(input("Please choose difficulty level:\n"+
          "1.Easy 13 max attempts\n" + 
          "2.Medium 10 max attempts\n" + 
          "3.Hard 7 max attempts\n"))
    while (difficulty_level<1 or difficulty_level>3):
        difficulty_level = int(input("Invalid number, please choose a VALID difficulty level 1-3:\n"+
          "1.Easy 13 max attempts\n" + 
          "2.Medium 10 max attempts\n" + 
          "3.Hard 7 max attempts\n"))
    return difficulty_level

def is_number_valid(number):
    if (number < 1000 or 
        number > 9999):
      return False #e.g. 0912
    
    digits_array = [False] * 10
    
    while (number != 0):
        digit = number % 10        
                
        if (digits_array[digit] == True):
            return False
        
        number = number // 10
        digits_array[digit] = True
            
    return True

def calculate_amount_of_guesses(difficulty_level):
    my_array = [13,10,7]
    return my_array[difficulty_level - 1]
    # EASY_LEVEL_AMOUNT_OF_ROUNDS = 13
    # MEDIUM_LEVEL_AMOUNT_OF_ROUNDS = 10
    # HARD_LEVEL_AMOUNT_OF_ROUNDS = 7
    
    # if (difficulty_level == 1):
    #     return EASY_LEVEL_AMOUNT_OF_ROUNDS
    # elif (difficulty_level == 2):
    #     return MEDIUM_LEVEL_AMOUNT_OF_ROUNDS
    # else:
    #     return HARD_LEVEL_AMOUNT_OF_ROUNDS
    
def generate_computer_number ():
    computer_number = 0    
    while is_number_valid(computer_number) == False :
      computer_number = random.randint(1000, 9999)        
    
    return computer_number

def calculate_amount_of_exact_hits(computer_number, user_guess):
  # e.g. 1354 1352
   # e.g. 1534 1352
  counter = 0
  
  while (computer_number != 0):
    digit_computer = computer_number % 10
    digit_user = user_guess % 10
        
    computer_number = computer_number // 10
    user_guess = user_guess // 10
    
    if (digit_computer == digit_user):
      counter += 1
      
  return counter

def calculate_amount_of_near_miss(computer_number, user_guess):
  exact_hits = calculate_amount_of_exact_hits(computer_number, user_guess)
  
  counter = 0
  while (user_guess != 0):
    user_digit = user_guess % 10
    user_guess = user_guess // 10    
    
    temp = computer_number #1478
    while (temp > 0):
      computer_digit = temp % 10 #8
      temp = temp // 10          #147
      
      if (computer_digit == user_digit):
        counter += 1    
  
  return counter - exact_hits    
     
#####################################
    
difficulty_level = get_valid_difficulty_level()
amount_of_guesses = calculate_amount_of_guesses(difficulty_level)
computer_number = generate_computer_number()
is_user_won = False
round = 0
while (is_user_won == False and round < amount_of_guesses):
    user_guess = 0
    
    while(is_number_valid(user_guess) == False):
      user_guess = int(input("Enter new Guess..."))
      if (is_number_valid(user_guess) == False):
        print("That is an illegal guess...")
    
    if (user_guess == computer_number):
        print("Yay !! you won !! ")
        is_user_won = True
    else:
        amount_of_hits = calculate_amount_of_exact_hits(computer_number, user_guess)
        amount_of_near_miss = calculate_amount_of_near_miss(computer_number, user_guess)
        print(f"Hits: {amount_of_hits}; Near miss: {amount_of_near_miss}")
        
    round += 1
    
if (is_user_won == False):
    print(f"Oh.. you failed... the number was {computer_number}")