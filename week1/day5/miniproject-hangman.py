import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

display_word = ['_' if char != ' ' else ' ' for char in word]


def show_word():
    print("\nWord: " + " ".join(display_word))


def guess_letter():
    return input("Guess a letter: ").lower()


def update_word(guess):
    found = False

    for i, letter in enumerate(word):
        if letter == guess:
            display_word[i] = guess
            found = True

    return found


def check_win():
    return "_" not in display_word


def play():
    global wrong_guesses

    print("🎮 Welcome to Hangman!")

    while True:
        show_word()
        guess = guess_letter()

        if guess in guessed_letters:
            print("You already tried this letter.")
            continue

        guessed_letters.append(guess)

        if update_word(guess):
            print("Good job!")
        else:
            wrong_guesses += 1
            print(f"Wrong! Attempts: {wrong_guesses}/6")

        if check_win():
            print("\nYou win! 🎉")
            print("The word was:", word)
            break

        if wrong_guesses >= max_wrong:
            print("\nYou lost 💀")
            print("The word was:", word)
            break


play()