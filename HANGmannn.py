import random
from words import words
def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word
def hangman():
    word = get_valid_word(words)
    turns = 10
    guessmade = ''
    valid_entries = set('abcdefghijklmnopqrstuvwxyz')
    
    while len(word)>0 :
        main_word = ""
        for letter in word:
             if letter in guessmade:
                 main_word = main_word +letter
             else:
                 main_word = main_word+ " _ "

        if main_word == word:
            print(main_word)
            print('YOU WON!!')
            break


        print('Guess the words ',main_word)
        guess = input()

        if guess in valid_entries:
            guessmade = guessmade + guess
        else:
            print('Enter valid character')
            guess = input()
        

        if guess not in word:
            turns = turns - 1

            if turns == 9:
                print(" 9 Turns Left")
                print("----------------")
            if turns == 8:
                print(" 8 Turns Left")
                print("----------------")
                print("       O        ")
            if turns == 7:
                print(" 7 Turns Left")
                print("----------------")
                print("       O        ")
                print("       |        ")
            if turns == 6:
                print(" 6 Turns Left")
                print("----------------")
                print("       O        ")
                print("       |        ")
                print("      /         ")
            if turns == 5:
                print(" 5 Turns Left")
                print("----------------")
                print("       O        ")
                print("       |        ")
                print("      / \       ")
            if turns == 4:
                print(" 4 Turns Left")
                print("----------------")
                print("      \O        ")
                print("       |        ")
                print("      / \       ")
            if turns == 3:
                print(" 3 Turns Left")
                print("----------------")
                print("      \O/       ")
                print("       |        ")
                print("      / \       ")
            if turns == 2:
                print(" 2 Turns Left")
                print("----------------")
                print("      \O/  |    ")
                print("       |        ")
                print("      / \       ")
            if turns == 1:
                print(" 1 Turns Left")
                print("----------------")
                print("      \O/__|    ")
                print("       |        ")
                print("      / \       ")
            if turns == 0:
                print("YOU LOSE!!!!!")
                print("----------------")
                print("       O __|    ")
                print("      /|\       ")
                print("      / \       ")
                print('Actuall word is  ', word)
                break
            
name = input("ENTER  YOUR NAME -> ")
print(f"Welcome {name} !")
print("---------------------------")
print("Try to guess the word within 10 ATTEMPTS")
hangman()