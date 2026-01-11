from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Label, Input, DataTable
from textual.screen import ModalScreen
import random

from lib import VocabTrainer

class TestVocabScreen(ModalScreen):
    def __init__(self, get_one, vocab_trainer):
        super().__init__()
        self.get_one = get_one
        self.word = self.get_one[0][0]
        self.vocab_trainer = vocab_trainer

    def compose(self) -> ComposeResult:
        yield Label(f"What is the translation of '{random.choice(self.word.split('/'))}'?", id="question")
        yield Input(placeholder="Your answer", id="answer-input")
        yield Button("Check", id="action-button")
        yield Static("", id="result")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "action-button" and event.button.label == "Check":
            answer = self.query_one("#answer-input", Input).value

            word = self.get_one[0][0]
            translation = self.get_one[0][1]
            vocab_id = self.get_one[0][2]
            direction = self.get_one[0][5]
            if answer.strip() in [trans.strip() for trans in translation.split("/")]:
                self.query_one("#result", Static).update(f"Correct! {word} is {translation}")
                self.vocab_trainer.update_stats(vocab_id, direction, True)
            else:
                self.query_one("#result",
                               Static).update(f"wrong - the correct answer for {word} is {translation} (you wrote: {answer})")
                self.vocab_trainer.update_stats(vocab_id, direction, False)
            event.button.label = "Next"
        elif event.button.id == "action-button" and event.button.label == "Next":
            self.dismiss()


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


class ListScreen(ModalScreen):
    def __init__(self, vocab_pairs):
        super().__init__()
        self.vocab_pairs = vocab_pairs

    def compose(self) -> ComposeResult:
        yield Label("list of all vocabulary", id="title")
        yield DataTable()
        yield Button("Exit", id="exit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)
        table.add_column("Japanisch")
        table.add_column("Deutsch")

        for pair in self.vocab_pairs:
            table.add_row(pair[0], pair[1])


class VocabularyTrainer(App):
    def __init__(self, vocab_trainer):
        super().__init__()
        self.vocab_trainer = vocab_trainer

    def compose(self) -> ComposeResult:
        yield Static("Vocabulary Trainer\nPress ctrl+q to exit\n\n", id="title")
        yield Button("Test Vocabulary", id="test_vocab")
        yield Button("Show vocabulary", id="list")
        yield Button("Add Word", id="add_word")
        yield Button("Close App", id="quit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "test_vocab":
            get_one = self.vocab_trainer.get_vocab_pairs(1)
            self.push_screen(TestVocabScreen(get_one, self.vocab_trainer), self.on_test)
        elif event.button.id == "list":
            vocab_pairs = self.vocab_trainer.get_all_vocab_pairs()
            self.push_screen(ListScreen(vocab_pairs), self.on_list)
        elif event.button.id == "add_word":
            self.push_screen(AddWordScreen(), self.on_add_word)
        elif event.button.id == "quit":
            self.exit()

    def on_test(self, result):
        pass

    def on_list(self, result):
        pass


    def on_add_word(self, word_pair: tuple):
        word, translation = word_pair
        self.vocab_trainer.add_word(word, translation)

if __name__ == "__main__":
    vocab_trainer = VocabTrainer()
    app = VocabularyTrainer(vocab_trainer)
    app.run()
