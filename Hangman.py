from words import words
import random


hangman_art = {0: ("  ┌┌────┐  ",
                   "  ││       ",
                   "  ││       ",
                   "──┘└──     "),
               1: ("  ┌┌────┐  ",
                   "  ││    ●  ",
                   "  ││       ",
                   "──┘└──     "),
               2: ("  ┌┌────┐  ",
                   "  ││    ●  ",
                   "  ││    │  ",
                   "──┘└──     "),
               3: ("  ┌┌────┐  ",
                   "  ││    ●  ",
                   "  ││   /│  ",
                   "──┘└──     "),
               4: ("  ┌┌────┐  ",
                   "  ││    ●  ",
                   "  ││   /│\\",
                   "──┘└──     "),
               5: ("  ┌┌────┐  ",
                   "  ││    ●  ",
                   "  ││   /│\\",
                   "──┘└── /   "),
               6: ("  ┌┌────┐  ",
                   "  ││    ●  ",
                   "  ││   /│\\",
                   "──┘└── / \\")}

def display_man(wrong_guesses):
    for line in hangman_art[wrong_guesses]:
        print(line)


def display_hint(hint):
    print(" ".join(hint))

def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        print("\n")
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input.")
            continue

        if guess in guessed_letters:
            print("**********************")
            print(f"{guess} is already guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1

        if "_" not in hint:
            print("Congrats! You guessed the word!")
            is_running = False
        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            print("\nYou lose!")
            print(f"{answer.capitalize()} was the correct answer!")
            is_running = False

if __name__ == "__main__":
    main()
