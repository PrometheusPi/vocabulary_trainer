import sqlite3
import random
from datetime import datetime
import math


class VocabTrainer:
    def __init__(self, vocab_db_path = "vocab.db", stats_db_path="training_stats.db"):
        self.conn_vocab = sqlite3.connect(vocab_db_path)
        self.cur_vocab = self.conn_vocab.cursor()

        self.conn_stats = sqlite3.connect(stats_db_path)
        self.cur_stats = self.conn_stats.cursor()

        self.selected_language = None
        all_lang = self.get_all_languages()
        if len(all_lang) > 0:
            self.selected_language = all_lang[0]

        for lang in all_lang:
            self.create_stats_db(lang)

    def __del__(self):
        self.conn_vocab.close()
        self.conn_stats.close()

    def select_language(self, name):
        all_lang = self.get_all_languages()
        if name in all_lang:
            self.selected_language = name
        else:
            raise Exception(f"Your selection {name} is not in the language options: all_lang")

    def create_vocab_db(self, language):
        # create database if not there
        self.cur_vocab.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {language} (
            id INTEGER PRIMARY KEY,
            word TEXT UNIQUE NOT NULL,
            translation TEXT NOT NULL
            )
            """
        )
        self.conn_vocab.commit() # TODO: do I need this here?


    def create_stats_db(self, language):
        # create user stats database
        # iterate through all vocab and add it if needed
        self.cur_stats.execute(
            f"""
            CREATE TABLE IF NOT EXISTS {language} (
            vocab_id INTEGER,
            last_trained TIMESTAMP,
            correct INTEGER DEFAULT 0,
            wrong INTEGER DEFAULT 0,
            direction BOOL,
            PRIMARY KEY (vocab_id, direction)
            )
            """
        )
        self.conn_stats.commit() # TODO: do I need this here?

        # add new vocabulary
        self.cur_vocab.execute(f"SELECT id FROM {language}")
        vocab_ids = {row[0] for row in self.cur_vocab.fetchall()}

        self.cur_stats.execute(f"SELECT vocab_id FROM {language}")
        stats_ids = {row[0] for row in self.cur_stats.fetchall()}

        missing_ids = vocab_ids - stats_ids

        for i in missing_ids:
            self.cur_stats.execute(
                f"""
                INSERT INTO {language}
                (vocab_id, last_trained, correct, wrong, direction)
                VALUES (?, NULL, 0, 0, TRUE),
                       (?, NULL, 0, 0, FALSE)
                """, (i,i,))

            self.conn_stats.commit()


    def add_word(self, word, translation, language):
        try:
            self.cur_vocab.execute(
                f"""
                INSERT INTO {language}
                (word, translation) VALUES (?, ?)
                """,
                (word, translation)
            )
            self.conn_vocab.commit()
            print("added word")
            self.create_stats_db(language)
        except sqlite3.IntegrityError:
            print("word already in database")


    def get_all_languages(self):
        self.cur_vocab.execute("SELECT name FROM sqlite_master WHERE type='table';")
        language_tables = self.cur_vocab.fetchall()
        return [language_pair[0] for language_pair in language_tables]


    def get_all_vocab_pairs(self, language):
        self.cur_vocab.execute(f"SELECT word, translation, id FROM {language}")
        rows = self.cur_vocab.fetchall()

        return rows

    def print_all_vocab(self, language):
        pairs = self.get_all_vocab_pairs(language)
        # print vocab database
        for word, translation, _ in pairs:
            print(f"{word} \t  -> \t {translation}")


    def update_stats(self, vocab_id, direction, correct, language):
        now = datetime.now().isoformat(timespec='seconds')

        if correct:
            set_string = "correct = correct + 1"
        else:
            set_string = "wrong = wrong + 1"

        sql_string = f"""
        UPDATE {language}
        SET last_trained = ?,
        {set_string}
        WHERE vocab_id = ? AND direction = ?;
        """

        self.cur_stats.execute(sql_string, (now, vocab_id, direction))

        self.conn_stats.commit()



    def get_learning_info(self, vocab_id, direction, language):
        # return when a word was last reviewed
        now = datetime.now().isoformat(timespec='seconds')

        sql_string = f"""
        SELECT last_trained, correct, wrong
        FROM {language}
        WHERE vocab_id = ? AND direction = ?;
        """

        self.cur_stats.execute(sql_string, (vocab_id, direction, ))
        last_learned, correct, wrong= self.cur_stats.fetchall()[0]
        # this is inefficent as this gets the last access time for each word individually

        if last_learned == None:
            delta_time = 365 * 24 * 60 * 60 # default one year - a bit arbitrary
        else:
            delta_time = (datetime.fromisoformat(now) -
                          datetime.fromisoformat(last_learned)).total_seconds()

        if correct + wrong == 0:
            wrong_ratio = 1.0
        else:
            wrong_ratio = wrong / (correct + wrong)

        return (delta_time, wrong_ratio,)


    def convert_score_to_probability(self, score_list):
        # using a softmax approch
        weight = 1.0 / 60. / 60. / 24. / 7.
        exp_score = [math.exp((weight * s)**(r+0.05)) for s, r in score_list]
        norm = sum(exp_score)
        return [es / norm for es in exp_score]

    def print_stats(self):
        # for debug purposes
        for lang in self.get_all_languages():
            print(f"Stats {lang}:")
            self.cur_stats.execute(f"SELECT * FROM {lang}")
            rows = self.cur_stats.fetchall()
            print("Stats:")
            for row in rows:
                print(row)


    def get_vocab_pairs(self, n):
        """
        n ... int: number of vocab pairs
        """
        pairs = self.get_all_vocab_pairs(self.selected_language)

        new_pairs = []
        for word_lang_1, word_lang_2, vocab_id in pairs:
            # word_lang_1 -> word_lang_2
            last, wrong_ratio = self.get_learning_info(vocab_id, True, self.selected_language)
            new_pairs.append((word_lang_1, word_lang_2, vocab_id, last, wrong_ratio, True))
            # word_lang_2 -> word_lang_1
            last, wrong_ratio = self.get_learning_info(vocab_id, False, self.selected_language)
            new_pairs.append((word_lang_2, word_lang_1, vocab_id, last, wrong_ratio, False))

        score_list = [(d, r) for _, _, _, d, r, _ in new_pairs]

        probabilty = self.convert_score_to_probability(score_list)

        print("debug:", len(new_pairs), len(probabilty))
        print("debug:", new_pairs, probabilty)

        return random.choices(new_pairs, probabilty, k=n)
