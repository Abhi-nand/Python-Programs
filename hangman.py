print("Let's play Mavel Hangman!")
import random
from bag import avengres
print('Hint:', avengres)
def play_hangman():
    word = random.choice(avengres).upper()
    guessed_words = []
    for character in word:
        guessed_words.append("_")
    attempts = 0
    attempts_left = 6

    def display_hangman(attempts_left):
        stages = [     # initial empty state
                    """
                       --------
                       |      |
                       |
                       |
                       |
                       |
                       -
                    """    ,
                    # head
                    """
                       --------
                       |      |
                       |      O
                       |
                       |
                       |
                       -
                    """,
                    # head and torso
                    """
                       --------
                       |      |
                       |      O
                       |      |
                       |      |
                       |
                       -
                    """,
                    # head, torso, and one arm
                    """
                       --------
                       |      |
                       |      O
                       |     \\|
                       |      |
                       |
                       -
                    """,
                    # head, torso, and both arms
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |
                       -
                    """,
                    # head, torso, both arms, and one leg
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     /
                       -
                    """,
                     # final state: head, torso, both arms, and both legs
                    """
                       --------
                       |      |
                       |      O
                       |     \\|/
                       |      |
                       |     / \\
                       -
                    """
                    ]
        return stages[attempts]
    print(display_hangman(attempts_left))
    print(guessed_words)
    print('\n\n')
    playGame = "Y"
    while playGame == "Y" and {attempts_left - attempts} != 0 :

        print(f"You have {attempts_left - attempts} attempts remaining")
        print(f"The current word is: {' '.join(guessed_words)}")
        letterGuessed = input("Please guess a letter: ").upper()
        if len(letterGuessed) > 1:
            print("Enter valid input")
        elif letterGuessed in guessed_words:
             print("You already guessed the letter",letterGuessed)
        elif letterGuessed in word:
            print(f"You guessed correctly! {letterGuessed} is in the word")
            for i in range(len(word)):
                character = word[i]
                if character == letterGuessed:
                    guessed_words[i] = word[i]
        elif letterGuessed not in word:
            print(f"You guessed wrong! {letterGuessed} is NOT in the word")
            attempts += 1
        print(display_hangman(attempts))
        print(guessed_words)
        print("\n")

        if "_" not in guessed_words:
            print("Congrats, you guessed the avengres! You win!")
            break

        elif attempts >= attempts_left:
            print("You lost, rest in peace!".upper())
            print("Sorry, you ran out of attempts. The word was " + word + ". Maybe next time!")
            break

def main():
    word = play_hangman()
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = play_hangman()
main()
