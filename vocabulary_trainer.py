from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Label, Input
from textual.screen import ModalScreen

from lib import VocabTrainer

class TestVocabScreen(ModalScreen):
    def __init__(self, get_one):
        super().__init__()
        self.get_one = get_one
        self.translation = self.get_one[0][1]
        
    def compose(self) -> ComposeResult:
        yield Label(f"What is the translation of '{self.translation}'?", id="question")
        yield Input(placeholder="Your answer", id="answer-input")
        yield Button("Check", id="check-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "check-button":
            answer = self.query_one("#answer-input", Input).value
            self.dismiss((answer, self.get_one))

            
class AddWordScreen(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Add New Word Pair", id="title")
        yield Input(placeholder="Word", id="word-input")
        yield Input(placeholder="Translation", id="translation-input")
        yield Button("Save", id="save-button")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save-button":
            word = self.query_one("#word-input", Input).value
            translation = self.query_one("#translation-input", Input).value
            self.dismiss((word, translation))


class VocabularyTrainer(App):
    def __init__(self, vocab_trainer):
        super().__init__()
        self.vocab_trainer = vocab_trainer

    def compose(self) -> ComposeResult:
        yield Static("Vocabulary Trainer\nPress ctrl+q to exit\n\n", id="title")
        yield Button("Test Vocabulary", id="test_vocab")        
        yield Button("Add Word", id="add_word")
        yield Static("", id="result")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "test_vocab":
            get_one = self.vocab_trainer.get_vocab_pairs(1)
            self.push_screen(TestVocabScreen(get_one), self.on_test)
        elif event.button.id == "add_word":
            self.push_screen(AddWordScreen(), self.on_add_word)
            
    def on_test(self, result):
        answer, get_one = result
        word = get_one[0][0]
        vocab_id = get_one[0][2]
        if answer in word.split("/"):
            self.query_one("#result", Static).update("Correct!")
            self.vocab_trainer.update_stats(vocab_id, True)
        else:
            self.query_one("#result", Static).update(f"wrong - the correct answer is {word}")
            self.vocab_trainer.update_stats(vocab_id, False)
        
        

    def on_add_word(self, word_pair: tuple):
        word, translation = word_pair        
        self.vocab_trainer.add_word(word, translation)
    
if __name__ == "__main__":
    vocab_trainer = VocabTrainer()
    app = VocabularyTrainer(vocab_trainer)
    app.run()
