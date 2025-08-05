try:
    print("""
    ------------------
    Welcome to Hangman
    ------------------
    """)
    secret_word=input("Enter secret word: ")
    incorrect_guesses=0
    display_word=['_' for x in secret_word]
    while True:
        print(''.join(display_word))
        letter = input("Enter a letter: ")
        if letter.lower() in secret_word.lower():
            print("Correct guess!")
            new_word = [l if l.lower()==letter.lower() else '_' for l in secret_word]
            display_word = list(map(lambda letter,display_word_letter:letter if display_word_letter=='_' else display_word_letter,new_word,display_word))
        else:
            incorrect_guesses += 1
            print("Incorrect guess!.Remaining guesses",5 - incorrect_guesses)
        if ''.join(display_word)==secret_word:
            print("Word guessed correctly")
            break
        if incorrect_guesses==5:
            print("5 incorrect guessses. Game Over")
            break
except Exception as e:
    print(e)