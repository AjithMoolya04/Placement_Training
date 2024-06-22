#random number generation and guess the number
import random
def generate_random_number(low,high):
    return random.randint(low,high)
def check_guess(secret_number,guess):
    if guess < secret_number:
        return "Too low"
    elif guess >secret_number:
        return "Too high"
    else :
        return "correct"
def main():
    low=1
    high=100
    secret_number=generate_random_number(low,high)
    print("welcome to the number guessing game")
    print("Guess the number between {} and {}".format(low,high))
    
    guesses=0
    while True:
        guess=int(input("enter your guess: "))
        result=check_guess(secret_number,guess)
        print(result)
        guesses+=1
        if result=="Correct":
            print("You guessed the number in {} guesse.".format(guesses))
if __name__=="__main__":
    main()