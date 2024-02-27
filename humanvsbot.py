import random
def get_operator(x,y, operator):
   if operator == 1:
      return x + y
   elif operator == 2:
      return x - y
   elif operator == 3:
      return x * y
   elif operator == 4:
      if y != 0:
          return x / y
      else:
        return "invalid"
   elif operator == 5:
      return random.randrange(1,4)
      
def choose_operator():
    print("Select operator:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Random mixture")
    player_operator_choice = int(input("Please choose your operator: "))
    if player_operator_choice in (1, 2, 3, 4, 5):
        return player_operator_choice
    else:
        print("Invalid operator choice.")
        return choose_operator()


def opponent(x, y):
    if random.randint(1, 4) == 1:
        return random.randint(1, 100)
    else:
        return x * y

def get_difficulty_level():
    while True:
        difficulty = int(input("Select difficulty level (1 for single-digit, 2 for two digits): "))
        if difficulty in (1, 2):
            return int(difficulty)
        else:
            print("Invalid input. Please enter 1 or 2 for difficulty level.")

player_correct = 0
opponent_point = 0
difficulty = get_difficulty_level()

while True:
    if difficulty == 1:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
    elif difficulty == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)




    operator = choose_operator()

    print(f"How much is {x} {'+' if operator == 1 else '-' if operator == 2 else '*' if operator == 3 else '/'} {y}: ?")
    
    result = get_operator(x,y,operator)

    player_input = input()
    if player_input.isdigit():
        player_input = int(player_input)
    else:
        print("Invalid input. Please enter a number.")
        continue

    if player_input == result:
        
        player_correct += 1

    component_result = opponent(x, y)
    print("The answer of the computer is:", component_result)

    if component_result == result:
        opponent_point += 1

    print("Do you want to continue?")
    player_choice = input("Enter 'y' or 'n': ")
    
    if player_choice == 'n' or player_choice == 'N':
        print("Thank you!")
        print("Player's points:", player_correct)
        print("Computer's points:", opponent_point)

        if player_correct > opponent_point:
            print("Player wins")
        elif player_correct < opponent_point:
            print("Computer wins")
        else:
            print("Draw")
        break