class Flashcard:
    def __init__(self, word, definition):
        self.word = word
        self.definition = definition
        
    def __str__(self):
        return f"{self.word}: {self.definition}"

    def to_dict(self):
        return {
            'word': self.word,
            'definition': self.definition
        }