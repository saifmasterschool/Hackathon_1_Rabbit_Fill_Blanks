import wikipedia as wk

class WikipediaService:
    def __init__(self, language="simple"):
        wk.set_lang(language)

    def search_summary(self, query, sentences=2):
        try:
            return wk.summary(query, sentences=sentences)
        except wk.exceptions.DisambiguationError as e:
            print(f"Disambiguation Error: {e}")
            return None
        except wk.exceptions.PageError:
            print("Error: No Wikipedia page found for your input.")
            return None
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
