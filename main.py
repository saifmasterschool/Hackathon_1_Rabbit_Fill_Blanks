import wikipedia as wk
import string
import random


def display_title():
    print("*** Welcome to 'Word Guessing Game' ***")


def ask_user_for_text():
    return input("Enter a keyword or a topic to search on Wikipedia: ")


def clean_text(user_text_input):
    clean_text = user_text_input.translate(str.maketrans("", "", string.punctuation))
    return clean_text


def make_case_insensitive(text):
    return text.lower()


def search_user_input(user_input):
    wk.set_lang("simple")

    try:
        result = wk.summary(user_input, sentences=2)
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


def remove_every_5_word(text):
    words = text.split()
    removed_words = []
    for i in range(4, len(words), 5):
        removed_words.append(words[i])
        words[i] = "______"
    modified_text = " ".join(words)
    return modified_text, removed_words


def guess_missing_words(removed_words, all_words):
    guessed_words = []

    for word in removed_words:
        # Generate three choices: the correct word + 2 random incorrect words
        choices = [word] + random.sample([w for w in all_words if w != word], 2)
        random.shuffle(choices)

        # Display choices and prompt the player to guess
        print(f"Guess the missing word: {choices}")

        # Input validation loop to ensure correct input (1, 2, or 3)
        while True:
            guess = input(f"Choose the correct word (1, 2, or 3): ")
            if guess in ["1", "2", "3"]:
                chosen_word = choices[int(guess) - 1]
                guessed_words.append(chosen_word)
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")

    return guessed_words


def display_text_with_blanks(text):
    print(text[0])


# New function to display the results
def display_results(removed_words, guessed_words):
    correct_count = 0
    for i in range(len(removed_words)):
        if removed_words[i].lower() == guessed_words[i].lower():
            print(f"Correct! The missing word was '{removed_words[i]}'.")
            correct_count += 1
        else:
            print(
                f"Incorrect. The correct word was '{removed_words[i]}', but you guessed '{guessed_words[i]}'."
            )

    total_words = len(removed_words)
    correct_percentage = (correct_count / total_words) * 100
    print(f"\nYou got {correct_count} out of {total_words} correct.")
    print(f"Your score: {correct_percentage:.2f}% correct.")


def main():
    display_title()
    user_text_input = ask_user_for_text()
    clean_user_input = clean_text(user_text_input)
    final_user_input = make_case_insensitive(clean_user_input)
    summary_result = make_case_insensitive(search_user_input(final_user_input))

    # Split the summary result into words (used to generate incorrect choices)
    all_words = summary_result.split()

    result = remove_every_5_word(summary_result)
    display_text_with_blanks(result)
    removed_words = result[1]

    # Pass both 'removed_words' and 'all_words' to 'guess_missing_words'
    guessed_words = guess_missing_words(removed_words, all_words)
    display_results(removed_words, guessed_words)


if __name__ == "__main__":
    main()
