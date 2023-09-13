





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


print("Guess the Answer")




guess1 = input("Which bear lives at the North Pole? ")
check_guess(guess1, "polar bear")

guess2 = input("Which is the larget animal? ")
check_guess(guess2, "blue whale")

guess3= input("What is the name of the tallest tower in Kuwait?")
check_guess(guess3, "Al Hamra Tower")

guess4 = input("When did the First World War begin?")
check_guess(guess4,"1914")

guess5 = input("What was the first country to go into space?")
check_guess(guess5 ,"russia" )

guess6= input("How many teeth does a cat have?")
check_guess(guess6,"40")

guess7= input("How many hearts does an octopus have?")
check_guess(guess7,"3 hearts")

guess8 = input("The name of the largest gland?")
check_guess(guess8,"Liver")

guess9 = input("What is the smallest country in the world?")
check_guess(guess9,"Vatican")

guess10= input("What is the top programming initiative?")
check_guess(guess10,"Kuwait Codes")

print("Your Score is "+ str(score))

import turtle as t

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():



    t.fillcolor('red')

    t.begin_fill()

    t.lt(140)
    t.fd(113)

    curve()
    t.lt(120)

    curve()


    t.fd(112)


    t.end_fill()

heart()
t.done()

