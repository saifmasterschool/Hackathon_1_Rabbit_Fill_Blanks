import string

class TextProcessor:

    def clean_text(self, text: str)-> str:
        """
        Remove punctuation from the input text and  returns The cleaned text with punctuation removed.
        """
        return text.translate(str.maketrans('', '', string.punctuation))

    def make_case_insensitive(self, text: str)-> str:
        """
         Convert the input text to lowercase and return the text in lowercase.
        """
        return text.lower()

    def remove_every_5th_word(self, text: str)-> tuple[str, list[str]]:
        """
           Remove every 5th word from the text and replace it with underscores.
        """
        words = text.split()
        removed_words = []
        for i in range(4, len(words), 5):
            removed_words.append(words[i])
            words[i] = "______"
        modified_text = " ".join(words)
        return modified_text, removed_words