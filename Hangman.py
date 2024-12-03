import random


words = ("apple", "banana", "cherry", "orange", "coconut", "pineapple")

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
    pass

def display_hint(hint):
    pass

def display_answer(answer):
    pass

def main():
    pass


if __name__ == "__main__":
    main()
