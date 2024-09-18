from colorama import Fore, Style


class ScoreCalculator:
    def check_answers(self, removed_words, guessed_words):
        """
        Check the user's guessed words against the actual removed words and display the result.

        Args:
            removed_words: List of words removed from the summary.
            guessed_words: List of words guessed by the user.
        """
        correct_guesses = 0  # To count the number of correct guesses
        total_guesses = len(removed_words)  # Total number of removed words

        # Loop through each removed and guessed word pair, comparing them
        for idx, (removed_word, guessed_word) in enumerate(zip(removed_words, guessed_words), start=1):
            # Compare the words in a case-insensitive way
            if removed_word.lower() == guessed_word.lower():
                correct_guesses += 1  # Increment if the guess is correct
                # Print a message indicating the guess was correct
                print(f"{Fore.LIGHTGREEN_EX}Word {idx}: Correct! (You guessed: {guessed_word})")
            else:
                # Print a message indicating the guess was incorrect and show the correct word
                print(f"{Fore.RED}Word {idx}: Incorrect. The correct word was '{removed_word}' (You guessed: {guessed_word})")

        # Calculate the user's score as a percentage
        score_percentage = (correct_guesses / total_guesses) * 100

        # Display the final score and number of correct guesses
        print(f"\n{Fore.YELLOW}You guessed {correct_guesses} out of {total_guesses} words correctly.")
        print(f"Your score: {score_percentage:.2f}% {Style.RESET_ALL}")
