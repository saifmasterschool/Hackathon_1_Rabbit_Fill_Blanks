class ScoreCalculator:
    def check_answers(self, removed_words, guessed_words):
        correct_guesses = 0
        total_guesses = len(removed_words)

        for idx, (removed_word, guessed_word) in enumerate(zip(removed_words, guessed_words), start=1):
            if removed_word.lower() == guessed_word.lower():
                correct_guesses += 1
                print(f"Word {idx}: Correct! (You guessed: {guessed_word})")
            else:
                print(f"Word {idx}: Incorrect. The correct word was '{removed_word}' (You guessed: {guessed_word})")

        score_percentage = (correct_guesses / total_guesses) * 100
        print(f"\nYou guessed {correct_guesses} out of {total_guesses} words correctly.")
        print(f"Your score: {score_percentage:.2f}%")
