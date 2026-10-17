from textual.app import App, ComposeResult
from textual.widgets import Button, Static, Label, Input, DataTable
from textual.screen import ModalScreen
import random

from lib import VocabTrainer

class TestVocabScreen(ModalScreen):
    def __init__(self, vocab_trainer):
        super().__init__()
        self.vocab_trainer = vocab_trainer
        self.get_one = self.vocab_trainer.get_vocab_pairs(1)
        self.word = self.get_one[0][0]

    def compose(self) -> ComposeResult:
        yield Label(f"What is the translation of '{self.word.strip()}'?", id="question")
        yield Input(placeholder="Your answer", id="answer-input")
        yield Button("Check", id="action-button")
        yield Button("Exit", id="exit-button")
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
                self.vocab_trainer.update_stats(vocab_id, direction, True, self.vocab_trainer.selected_language)
            else:
                self.query_one("#result",
                               Static).update(f"wrong - the correct answer for {word} is {translation} (you wrote: {answer})")
                self.vocab_trainer.update_stats(vocab_id, direction, False, self.vocab_trainer.selected_language)
            event.button.label = "Next"
        elif event.button.id == "action-button" and event.button.label == "Next":
            self.dismiss()
        elif event.button.id == "exit-button":
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
    def __init__(self, vocab_pairs, lang):
        super().__init__()
        self.vocab_pairs = vocab_pairs
        self.languages = lang.split("_")

    def compose(self) -> ComposeResult:
        yield Label("list of all vocabulary", id="title")
        yield DataTable()
        yield Button("Exit", id="exit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)

        table.add_column(self.languages[0])
        table.add_column(self.languages[1])

        for pair in self.vocab_pairs:
            table.add_row(pair[0], pair[1])


class LearnScreen(ModalScreen):
    def __init__(self, vocab_pairs, lang):
        super().__init__()
        self.vocab_pairs = vocab_pairs
        self.languages = lang.split("_")
        self.show_index = 0
        self.show_count = len(vocab_pairs)

    def compose(self) -> ComposeResult:
        yield Label("learn vocabulary", id="title")
        yield DataTable()
        yield Button("Learn Next", id="next")
        yield Button("Start Testing", id="start_test")
        yield Button("Exit", id="exit")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "next":
            table = self.query_one(DataTable)
            old_pair = self.vocab_pairs[self.show_index]
            self.show_index = (self.show_index + 1) % self.show_count
            pair = self.vocab_pairs[self.show_index]
            table.clear()
            table.add_row(pair[0], pair[1])
        else:
            self.dismiss()

    def on_mount(self) -> None:
        table = self.query_one(DataTable)

        table.add_column(self.languages[0])
        table.add_column(self.languages[1])

        pair = self.vocab_pairs[0]
        table.add_row(pair[0], pair[1])

class LearningSessionScreen(ModalScreen):
    """
    Two-staged learning session for never-before trained words

    stage 1: browse each word pair for laerning, mark it as laerned or for repetition
    stage 2: quiz all paits in both directions until all are answered correctly
    """

    def __init__(self, vocab_trainer, vocab_pairs, language):
        super().__init__()
        self.vocab_trainer = vocab_trainer
        self.language = language
        self.languages_pair = language.split("_")

        self.vocab_pairs = list(vocab_pairs) # full list - keep untouched
        self.browse_queue = list(vocab_pairs) # for stage 1
        self.quiz_items = [] # for stage 2
        self.session_results = []

    def compose(self) -> ComposeResult:
        # always (top)
        yield Label("", id="title")
        yield Static("", id="card")

        # stage 1:
        yield Button("Show again later", id="again")
        yield Button("Got it!", id="got-it")

        #stage 2:
        yield Input(placeholder="your answer", id="answer-input")
        yield Button("check", id="check")

        # always (bottom)
        yield Button("exit", id="exit")
        yield Static("", id="result")

    def on_mount(self) -> None:
        # start stage 1, hide stage 2
        self.query_one("#answer-input", Input).disply = False
        self.query_one("#check", Button).display = False
        self.show_browse_item()

    def show_browse_item(self) -> None:
        """
        stage 1: learn 10 new vocabulary pairs
        """
        word, translation, _ = self.browse_queue[0]
        self.query_one("#title", Label).update(
            f"Stage 1: {len(self.browse_queue)} word left to learn")
        self.query_one("#card", Static).update(
            f"{word.strip()}  ->  {traslaltion.strip()}")

    def start_quiz(self) -> None:
        """
        stage 2: test what you just learned
        """
        # hide stage 1 interface
        self.query_one("#again", Button).display = False
        self.query_one("#got-it", Button).display = False
        # reveal stage 2 interface
        self.query_one("#answer-input", Input).display = True
        self.query_one("#check", Button).display = True
        

class SelectLanguagesScreen(ModalScreen):
    def __init__(self, list_lang):
        super().__init__()
        self.list_lang = list_lang

    def compose(self) -> ComposeResult:
        yield Label("list of all languages", id="title")
        for lang in self.list_lang:
            yield Button(lang, id=lang)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        self.dismiss(event.button.id)


class VocabularyTrainer(App):
    def __init__(self, vocab_trainer):
        super().__init__()
        self.vocab_trainer = vocab_trainer

        self.list_of_languages = self.vocab_trainer.get_all_languages()
        if len(self.list_of_languages) > 0:
            self.selected_language = self.list_of_languages[0]
        else:
            self.selected_language = None

        self.daily_streak = 0
        #self.query_one("#streak", Static).update(f"Streak of 0 days")

    def create_title_string(self):
        return f"Vocabulary Trainer: {self.selected_language}\nPress ctrl+q to exit\n\n"

    def compose(self) -> ComposeResult:
        self.header = Static(self.create_title_string(), id="title")
        yield self.header
        yield Button("Test all Vocabulary", id="test_vocab")
        yield Button("Show vocabulary", id="list")
        yield Button("Add Word", id="add_word")
        yield Button("Learn", id="learn")
        yield Button("Change Language", id="change_language")
        yield Button("Close App", id="quit")
        yield Static("", id="daily")


    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "test_vocab":
            self.push_screen(TestVocabScreen(self.vocab_trainer), self.on_test)
            self.daily_streak += 1
            self.query_one("#daily", Static).update(f"Trained {self.daily_streak} vocabs today.")
        elif event.button.id == "list":
            vocab_pairs = self.vocab_trainer.get_all_vocab_pairs(self.selected_language)
            self.push_screen(ListScreen(vocab_pairs, self.selected_language), self.on_list)
        elif event.button.id == "add_word":
            self.push_screen(AddWordScreen(), self.on_add_word)
        elif event.button.id == "learn":
            vocab_pairs = self.vocab_trainer.get_all_vocab_pairs(self.selected_language)[:10]
            self.push_screen(LearnScreen(vocab_pairs, self.selected_language), self.on_learn)
        elif event.button.id == "change_language":
            all_lang = self.vocab_trainer.get_all_languages()
            self.push_screen(SelectLanguagesScreen(all_lang), self.on_change_lang)
        elif event.button.id == "quit":
            self.exit()

    def on_test(self, result):
        pass

    def on_list(self, result):
        pass

    def on_add_word(self, word_pair: tuple):
        word, translation = word_pair
        self.vocab_trainer.add_word(word, translation)

    def on_learn(self, result):
        pass

    def on_change_lang(self, selected_lang):
        self.selected_language = selected_lang
        self.vocab_trainer.select_language(self.selected_language)
        self.header.update(self.create_title_string())

if __name__ == "__main__":
    vocab_trainer = VocabTrainer()
    app = VocabularyTrainer(vocab_trainer)
    app.run()
