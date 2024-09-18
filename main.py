from game.game import Game
from services.wikipedia_service import WikipediaService
from game.text_processor import TextProcessor
from game.score_calculator import ScoreCalculator


def main():
    """
    The main function to initialize and start the game.
    """
    wikipedia_service = WikipediaService()
    text_processor = TextProcessor()
    score_calculator = ScoreCalculator()

    game = Game(wikipedia_service, text_processor, score_calculator)
    game.start()


if __name__ == "__main__":
    main()
