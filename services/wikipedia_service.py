import wikipedia as wk

class WikipediaService:
    def __init__(self, language="simple"):
        """
        Initialize the WikipediaService class and set the language for Wikipedia searches.

        Args:
            language: The language to use for Wikipedia queries (default is "simple" for Simple English).
        """
        # Set the language for Wikipedia searches.
        wk.set_lang(language)

    def search_summary(self, query, sentences=2):
        """
        Search for a summary of a given topic on Wikipedia.

        Args:
            query: The topic or keyword to search for on Wikipedia.
            sentences: The number of sentences to return from the summary (default is 2).

        Returns:
            The Wikipedia summary of the query if successful, otherwise None.
        """
        try:
            # Try to fetch a summary from Wikipedia for the given query.
            return wk.summary(query, sentences=sentences)
        except wk.exceptions.DisambiguationError as e:
            # Handle disambiguation error, which occurs when there are multiple pages for the query.
            print(f"Disambiguation Error: {e}")
            return None
        except wk.exceptions.PageError:
            # Handle page error, which occurs when no Wikipedia page is found for the query.
            print("Error: No Wikipedia page found for your input.")
            return None
        except Exception as e:
            # Handle any other exception that may occur during the search.
            print(f"An error occurred: {e}")
            return None
