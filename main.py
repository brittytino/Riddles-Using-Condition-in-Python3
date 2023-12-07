def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry Wrong Answer, try again")
            attempt = attempt + 1
    if attempt == 3:
        print("The Correct answer is ",answer )
    
score = 0
print("Guess the Riddle")
guess1 = input("What word is always pronounced wrong? ")
check_guess(guess1, "wrong")
guess2 = input("The leaves are on the fruit, The fruits is on the leaves. What is it? ")
check_guess(guess2, "pineapple")
guess3 = input("What fruit has its seeds on the outside? ")
check_guess(guess3, "strawberry")
guess4 = input("You answer me, although I never ask you questions. What am I? ")
check_guess(guess4, "telephone")
guess5 = input("I am wet when drying. What am I? ")
check_guess(guess5, "towel")
print("Your Score is "+ str(score))
