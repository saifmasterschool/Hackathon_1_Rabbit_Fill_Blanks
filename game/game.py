import sys

import colorama
from colorama import Fore, Back, Style
colorama.init()
import time

class Game:
    def __init__(self, wikipedia_service, text_processor, score_calculator):
        self.wikipedia_service = wikipedia_service
        self.text_processor = text_processor
        self.score_calculator = score_calculator

    def start(self):
        self.display_title()
        user_input = self.ask_user_for_text()
        clean_input = self.text_processor.clean_text(user_input)
        final_input = self.text_processor.make_case_insensitive(clean_input)

        summary_result = self.wikipedia_service.search_summary(final_input)

        if summary_result:
            summary_result = self.text_processor.make_case_insensitive(summary_result)
            modified_text, removed_words = self.text_processor.remove_every_5th_word(summary_result)
            self.display_summary_with_blanks(modified_text)
            guessed_words = self.get_user_guesses(removed_words)
            self.score_calculator.check_answers(removed_words, guessed_words)
        else:
            print("Please provide a valid input to continue the game.")

    def display_title(self):
        """Displaying the welcome message"""
        self.blinking_and_growing_text(f"{Fore.RED}  **    W E L C O M E    TO    G A M E    **", times=2, speed=0.5)

    def blinking_and_growing_text(self, text, times=5, speed=0.5):
        for i in range(times):
            # Blinking efekt: show text
            sys.stdout.write('\r' + text)
            sys.stdout.flush()
            time.sleep(speed)
            # Blinking efekt: hide the text temporarily
            sys.stdout.write('\r' + ' ' * len(text))
            sys.stdout.flush()
            time.sleep(speed)
            # again show text after blinkling
            sys.stdout.write('\r' + text)
            sys.stdout.flush()
        print()

    def ask_user_for_text(self):
        """Ask for user input for choosing the summary from the wikipedia"""
        return  input(f"{Fore.BLACK}Enter a keyword or a topic to search on Wikipedia:")

    def display_summary_with_blanks(self, text):
        """Display the summary with blank space"""
        print("\nHere is the summary with blanks:")
        print(text)

    def get_user_guesses(self, removed_words):
        """Collect guesses from the user for each removed word."""
        guessed_words = []

        for idx in range(len(removed_words)):
            guess = input(f"Guess the missing word number {idx + 1}: ")
            guessed_words.append(guess)

        return guessed_words

