import wikipedia as wk
import string

def display_title():
    print("*** Welcome to 'Word Guessing Game' ***")


def ask_user_for_text():
    return input('Enter a keyword or a topic to search on Wikipedia: ')


def clean_text(user_text_input):
    clean_text = user_text_input.translate(str.maketrans('', '', string.punctuation))
    return clean_text


def make_case_insensitive(text):
    return text.lower()


def search_user_input(user_input):
    wk.set_lang("simple")

    try:
        result = wk.summary(user_input, sentences=5)
        return result
    except wk.exceptions.DisambiguationError as e:
        print(f"Disambiguation Error: {e}")
        return "Please be more specific with your search."
    except wk.exceptions.PageError:
        print("Error: No Wikipedia page found for your input.")
        return "No page found."
    except Exception as e:
        print(f"An error occurred: {e}")
        return "An unexpected error occurred."


## TODO: fix adding blank space on the text
def remove_every_5_word(text):
    words = text.split()
    removed_words = []
    for i in range(4, len(words), 5):
        removed_words.append(words[i])
        words[i] = "______"
    modified_text = " ".join(words)
    return modified_text, removed_words

###TODO: Create  a method to take a user input for guessing the missing words
##TODO: Use while loop for user to take all required input
## TODO: Create a new method for checking ccounting correct answer

## TODO: Create a method displaying correct & incorrect  annswer. Show result in percentage(Gerald)
def main():
    display_title()
    user_text_input = ask_user_for_text()
    clean_user_input = clean_text(user_text_input)
    final_user_input = make_case_insensitive(clean_user_input)
    summary_result = make_case_insensitive(search_user_input(final_user_input))
    print(remove_every_5_word(summary_result))
    ## TODO: call a method for getting user input

if __name__ == "__main__":
    main()