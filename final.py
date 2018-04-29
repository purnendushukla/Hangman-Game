from random import choice
from nltk.corpus import brown
difficulty = raw_input("Set the difficulty to either easy, medium, or hard:")

difficulty = difficulty.lower()

while difficulty != "hard" and difficulty != "medium" and difficulty != "easy":
	difficulty = raw_input("Please enter 'easy', 'medium', or 'hard':")
	difficulty = difficulty.lower()

if difficulty == "easy":
	min_length = 6
	max_length = 7
elif difficulty == "medium": 
	min_length = 8
	max_length = 10
else:
	min_length = 5
	max_length = 5

word_list = brown.words()

answer = choice(word_list)
answer_length = len(answer)
while answer_length < min_length or answer_length > max_length or (not answer.isalpha()):
    answer = choice(word_list)
    answer_length = len(answer)
	

answer = answer.lower()

used = ["Used Letters: "]

attempt = ["Word: "]
attempt.extend(["__ "] * len(answer))

guess = 0
max_guesses = 8

board = []

def display_word(a):
    return a.append(attempt)

def display_used_letters(a):
    return a.append(used)

def make_initial_board(a):
    a.append([] * 20)
    display_word(a)
    a.append([] * 20)
    display_used_letters(a)
    return a

make_initial_board(board)

def print_board(a):
    guesses_left = max_guesses - guess
    for row in a:
        print "".join(row)
    print "Guesses left: " + str(guesses_left)


def take_input():
    global attempt
    global guess
    guessed_letter = raw_input("What is your letter?")
    guessed_letter = guessed_letter.lower()
            
    while len(guessed_letter) > 1 or guessed_letter + " " in used:
        if len(guessed_letter) > 1:
            guessed_letter = raw_input("You can only guess one letter:")
        else:
            guessed_letter = raw_input("You already guessed that! Try again:")
        guessed_letter = guessed_letter.lower()

    else:
        used.append(guessed_letter + " ")
        if guessed_letter in answer:
            index_list = []
            for i in range(0,len(answer)):
                if answer[i] == guessed_letter:
                    index_list.append(i)
            for i in index_list:
                j = i + 1
                attempt[j] = guessed_letter + " "          
        else:
                    
            guess += 1

            

def word_match():
    return not ("__ " in attempt)


while guess < max_guesses and (not word_match()):
    print_board(board)
    take_input()
else:
    if word_match():
        print "".join(answer)
        print "Congratulations! You won! The word was " + answer + "."
    else:
        print_board(board)
        print "You lost...the word was " + answer + ". Maybe try again?"