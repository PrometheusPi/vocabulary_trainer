import sqlite3
import random
from datetime import datetime
import math


class VocabTrainer:
    def __init__(self, vocab_db_path = "vocab_jap.db", stats_db_path="training_stats.db"):
        self.conn_vocab = sqlite3.connect(vocab_db_path)
        self.cur_vocab = self.conn_vocab.cursor()
        self.create_vocab_db()


        self.conn_stats = sqlite3.connect(stats_db_path)
        self.cur_stats = self.conn_stats.cursor()
        self.create_stats_db()

    def __del__(self):
        self.conn_vocab.close()
        self.conn_stats.close()

    def create_vocab_db(self):
        # create database if not there
        self.cur_vocab.execute(
            """
            CREATE TABLE IF NOT EXISTS Japanisch (
            id INTEGER PRIMARY KEY,
            word TEXT UNIQUE NOT NULL,
            translation TEXT NOT NULL
            )
            """
        )
        self.conn_vocab.commit() # TODO: do I need this here?


    def create_stats_db(self):
        # create user stats database
        # iterate through all vocab and add it if needed
        self.cur_stats.execute(
            """
            CREATE TABLE IF NOT EXISTS training_stats (
            vocab_id INTEGER PRIMARY KEY,
            last_trained TIMESTAMP,
            correct INTEGER DEFAULT 0,
            wrong INTEGER DEFAULT 0
            )
            """
        )
        self.conn_stats.commit() # TODO: do I need this here?

        # add new vocabulary
        self.cur_vocab.execute("SELECT id FROM Japanisch")
        vocab_ids = {row[0] for row in self.cur_vocab.fetchall()}

        self.cur_stats.execute("SELECT vocab_id FROM training_stats")
        stats_ids = {row[0] for row in self.cur_stats.fetchall()}

        missing_ids = vocab_ids - stats_ids

        for i in missing_ids:
            self.cur_stats.execute(
                """
                INSERT INTO training_stats
                (vocab_id, last_trained, correct, wrong)
                VALUES (?, NULL, 0, 0)
                """, (i,))

            self.conn_stats.commit()


    def add_word(self, word, translation):
        try:
            self.cur_vocab.execute(
                """
                INSERT INTO Japanisch
                (word, translation) VALUES (?, ?)
                """,
                (word, translation)
            )
            self.conn_vocab.commit()
            print("added word")
            self.create_stats_db()
        except sqlite3.IntegrityError:
            print("word already in database")


    def get_all_vocab_pairs(self):
        self.cur_vocab.execute("SELECT word, translation, id FROM Japanisch")
        rows = self.cur_vocab.fetchall()

        return rows

    def print_all_vocab(self):
        pairs = self.get_all_vocab_pairs()
        # print vocab database
        for word, translation in pairs:
            print(f"{word} \t  -> \t {translation}")


    def update_stats(self, vocab_id, correct):
        now = datetime.now().isoformat(timespec='seconds')

        if correct:
            set_string = "correct = correct + 1"
        else:
            set_string = "wrong = wrong + 1"

        sql_string = """
        UPDATE training_stats
        SET last_trained = ?,
        {}
        WHERE vocab_id = ?;
        """.format(set_string)

        self.cur_stats.execute(sql_string, (now, vocab_id))

        self.conn_stats.commit()



    def get_last_learned(self, vocab_id):
        # return when a word was last reviewed
        now = datetime.now().isoformat(timespec='seconds')

        sql_string = """
        SELECT last_trained
        FROM training_stats
        WHERE vocab_id = ?;
        """

        self.cur_stats.execute(sql_string, (vocab_id,))
        res = self.cur_stats.fetchall()[0][0]
        # this is inefficent as this gets the last access time for each word individually


        if res == None:
            return 365 * 24 * 60 * 60 # defualt one year - a bit arbitrary

        return (datetime.fromisoformat(now) -
                datetime.fromisoformat(res)).total_seconds()


    def convert_score_to_probability(self, score_list):
        # using a softmax approch
        weight = 1.0 / 60. / 60. / 24. / 7.
        exp_score = [math.exp(weight * s) for s in score_list]
        norm = sum(exp_score)
        return [es / norm for es in exp_score]

    def print_stats(self):
        # for debug purposes
        self.cur_stats.execute("SELECT * FROM training_stats")
        rows = self.cur_stats.fetchall()
        print("Stats:")
        for row in rows:
            print(row)


    def get_vocab_pairs(self, n):
        """
        n ... int: number of vocab pairs
        """
        pairs = self.get_all_vocab_pairs()

        new_pairs = []
        for deu, jap, vocab_id in pairs:
            last = self.get_last_learned(vocab_id)
            new_pairs.append((deu, jap, vocab_id, last,))

        new_pairs +=  [(deu, jap, vocab_id, last) for (jap, deu, vocab_id, last) in new_pairs]

        score_list = [s for _, _, _, s in new_pairs]

        probabilty = self.convert_score_to_probability(score_list)

        return random.choices(new_pairs, probabilty, k=n)
