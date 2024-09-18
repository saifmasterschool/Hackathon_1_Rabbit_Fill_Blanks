import string

class TextProcessor:

    def clean_text(self, text: str) -> str:
        """
        Remove punctuation from the input text.
        
        Args:
            text: The input string to clean.

        Returns:
            The cleaned text with punctuation removed.
        """
        # Remove all punctuation from the text using str.translate and return it
        return text.translate(str.maketrans('', '', string.punctuation))

    def make_case_insensitive(self, text: str) -> str:
        """
        Convert the input text to lowercase.
        
        Args:
            text: The input string to process.

        Returns:
            The text converted to lowercase.
        """
        # Convert the entire text to lowercase and return it
        return text.lower()

    def remove_every_5th_word(self, text: str) -> tuple[str, list[str]]:
        """
        Remove every 5th word from the text and replace it with underscores.
        
        Args:
            text: The input string from which every 5th word will be removed.

        Returns:
            A tuple containing:
                - The modified text with every 5th word replaced by underscores.
                - A list of words that were removed.
        """
        words = text.split()  # Split the text into a list of words
        removed_words = []  # To store the removed words

        # Iterate over the list of words, starting at the 5th word and then every 5th word after that
        for i in range(4, len(words), 5):
            removed_words.append(words[i])  # Add the removed word to the list
            words[i] = "_" * len(words[i])  # Replace the removed word with underscores of the same length
        
        # Join the modified list of words back into a string
        modified_text = " ".join(words)
        
        # Return the modified text and the list of removed words
        return modified_text, removed_words
