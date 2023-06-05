print (' Welcome to Mefix Puzzle Game\n This Game will task your Mind')
secret_word = "password"
clue = "_" * len(secret_word)  # Initialize the clue with underscores
guesses = 0

while True:
    print(f"Clue: {clue}")  # Display the clue to the user
    guess = input("Guess the secret word: ")

    guesses += 1

    if guess == secret_word:
        print(f"Congratulations! You guessed the secret word in {guesses} guesses.")
        print('Hope you Enjoyed the Puzzle')
        break

      # Update the clue with correctly guessed letters
    for i in range(len(secret_word)):
        if guess[i:i+1] == secret_word[i:i+1]:
            clue = clue[:i] + guess[i:i+1].upper() + clue[i+1:]
        elif guess[i:i+1] in secret_word:
            clue = clue[:i] + guess[i:i+1].lower() + clue[i+1:]