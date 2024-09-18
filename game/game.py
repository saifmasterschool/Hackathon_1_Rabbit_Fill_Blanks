import time
import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()


class Game:
    def __init__(self, wikipedia_service, text_processor, score_calculator):
        """
        Initialize the Game class with services for Wikipedia, text processing, and score calculation.
        
        Args:
            wikipedia_service: Handles fetching Wikipedia summaries.
            text_processor: Cleans and processes text.
            score_calculator: Evaluates user guesses and calculates scores.
        """
        self.wikipedia_service = wikipedia_service
        self.text_processor = text_processor
        self.score_calculator = score_calculator

    def start(self):
        """
        Start the game by displaying the title, taking user input, fetching a Wikipedia summary, 
        modifying the summary, and then asking the user to guess the removed words.
        """
        self.display_title()  # Display the welcome message.
        user_input = self.ask_user_for_text()  # Ask the user for a topic.
        clean_input = self.text_processor.clean_text(user_input)  # Clean the user's input.
        final_input = self.text_processor.make_case_insensitive(clean_input)  # Make input case insensitive.

        # Fetch Wikipedia summary based on the cleaned input.
        summary_result = self.wikipedia_service.search_summary(final_input)

        if summary_result:
            # Process the summary by making it case-insensitive and removing every 5th word.
            summary_result = self.text_processor.make_case_insensitive(summary_result)
            modified_text, removed_words = self.text_processor.remove_every_5th_word(summary_result)
            
            # Display the modified summary with blanks.
            self.display_summary_with_blanks(modified_text)
            
            # Get the user's guesses for the missing words.
            guessed_words = self.get_user_guesses(removed_words)
            
            # Check and score the user's answers.
            self.score_calculator.check_answers(removed_words, guessed_words)
        else:
            print("Please provide a valid input to continue the game.")

    def display_title(self):
        """Display the welcome title of the game with blinking and growing effect."""
        self.blinking_and_growing_text(
            f"{Fore.MAGENTA}  **    W E L C O M E    TO    G A M E    **", times=2, speed=0.5)
        print()

    def blinking_and_growing_text(self, text, times=5, speed=0.5):
        """
        Create a blinking text effect by printing and clearing the text multiple times.
        
        Args:
            text: The text to be displayed with the effect.
            times: Number of times to blink the text.
            speed: Speed of the blinking effect (in seconds).
        """
        for i in range(times):
            # Blinking effect: show the text.
            sys.stdout.write('\r' + text)
            sys.stdout.flush()
            time.sleep(speed)
            
            # Blinking effect: hide the text temporarily.
            sys.stdout.write('\r' + ' ' * len(text))
            sys.stdout.flush()
            time.sleep(speed)
            
            # Show the text again after blinking.
            sys.stdout.write('\r' + text)
            sys.stdout.flush()
        print()

    def ask_user_for_text(self):
        """Prompt the user to enter a keyword or topic to search on Wikipedia."""
        return input(f"{Fore.CYAN}Enter a keyword or a topic to search on Wikipedia: {Style.RESET_ALL}")

    def display_summary_with_blanks(self, text):
        """
        Display the Wikipedia summary with blank spaces where every 5th word has been removed.
        
        Args:
            text: The modified summary text with blanks.
        """
        print("\nHere is the summary with blanks: ")
        print()

        # Break the text into lines, 60 characters per line, for better readability.
        for i in range(0, len(text), 60):
            print(text[i:i+60])

        print()

    def get_user_guesses(self, removed_words):
        """
        Ask the user to guess the words that were removed from the summary.
        
        Args:
            removed_words: List of words that were removed from the summary.
        
        Returns:
            guessed_words: List of words guessed by the user.
        """
        guessed_words = []

        # Loop through each removed word and prompt the user to guess it.
        for idx in range(len(removed_words)):
            guess = input(f"Guess the missing word number {idx + 1}: ")
            guessed_words.append(guess)

        print()

        return guessed_words
    