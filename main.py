import random

def guessing_system():
    num_of_rounds = int(input("Enter number of rounds you want to play: "))
    round = 1 
    attempts = 1 
    attempts_list = [] 
    user_point = 0 
    try:
        computer_target = random.randint(1, 100) 
        while True: 
            print(f"------Round {round}------") 
            print(f"======Attempt {attempts}======")
            user_guess = input("Enter your guess or Quit: ")
            if user_guess.lower() == "quit":
                print("You Quit The Game")
                break
            
            user_guess = int(user_guess)
            if user_guess == computer_target:
                print("Your guess is Correct, you got 10+ points")
                round+=1
                computer_target = random.randint(1, 100)
                user_point+=10
                attempts_list.append(attempts)
                attempts-=(attempts-1)
            elif user_guess < computer_target:
                print("You are guessing too small number..!!")
                attempts+=1
            else:
                print("You are guessing too big number..!!")
                attempts+=1
                
            if round > num_of_rounds:
                break
            else:
                continue
            
        for rounds,attm in enumerate(attempts_list, start=1):
            print("====================")
            print(f"Round {rounds}, {attm} Attempts")
        if sum(attempts_list) >= 10:
            print("--------------------------------")
            print(f"Your Total Score: {user_point}")
            print(f"You Noob Guesser...!!! you took {sum(attempts_list)} attempts")
            print("--------------------------------")
        elif sum(attempts_list) >= 5:
            print("--------------------------------")
            print(f"Your Total Score: {user_point}")
            print(f"You are Average Guesser in {sum(attempts_list)} attempts!!!")
            print("--------------------------------")
        elif sum(attempts_list) >= 1 and sum(attempts_list) <= 3:
            print("-------------------------------")
            print(f"Your Total Score: {user_point}") 
            print(f"Youuu are the Master Guesser in {sum(attempts_list)} attempts")
            print("--------------------------------")
        
        play_again = input("Play Again??Enter yes/no: ")
        if play_again.lower() != "yes":
            print("GAME OVER")       
        else:
            guessing_system()  
    except Exception as e:
        print(f"You are entering a invalid input {e}")
               
guessing_system()

        
