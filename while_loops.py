def star_game():
    print("Enter the number of stars to get a star show")
    star_count =  int(input("Enter max number of stars: "))
    i=1
    while i<= star_count:
        print("*" * i)
        i +=1
    print("Enjoy your day!")

def guess_game():
    print("Guess the secret number in 3 attempts")
    secret_number = 9
    attempt = 0
    max_attempt = 3
    while attempt < max_attempt:
        user_input = int(input("Guess: "))
        attempt += 1
        if user_input == secret_number:
            print("Congratulations! You found the secret!")
            break
        else:
            if attempt == max_attempt:
                print("Please try later!")
            else:
                print("Try again!")



guess_game()