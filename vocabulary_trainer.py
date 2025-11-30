import sqlite3
import random
from datetime import datetime


# know globaly
conn_vocab = sqlite3.connect("vocab_jap.db")
cur_vocab = conn_vocab.cursor()


def create_vocab_db():

    # create database if not there
    cur_vocab.execute(
        """
        CREATE TABLE IF NOT EXISTS Japanisch (
        id INTEGER PRIMARY KEY,
        word TEXT UNIQUE NOT NULL,
        translation TEXT NOT NULL
        )
        """
    )
    conn_vocab.commit()

def create_stats_db():
    # create user stats database
    # iterate through all vocab and add it if needed
    db_path="training_stats.db"
    conn_stats = sqlite3.connect(db_path)
    cur_stats = conn_stats.cursor()

    cur_stats.execute(
        """
        CREATE TABLE IF NOT EXISTS training_stats (
            vocab_id INTEGER PRIMARY KEY,
            last_trained TIMESTAMP,
            correct INTEGER DEFAULT 0,
            wrong INTEGER DEFAULT 0
        )
        """
    )
    conn_stats.commit() # TODO: do I need this here?

    # add new vocabulary
    cur_vocab.execute("SELECT id FROM Japanisch")
    vocab_ids = {row[0] for row in cur_vocab.fetchall()}

    cur_stats.execute("SELECT vocab_id FROM training_stats")
    stats_ids = {row[0] for row in cur_stats.fetchall()}

    missing_ids = vocab_ids - stats_ids

    for i in missing_ids:
        cur_stats.execute(
            """
            INSERT INTO training_stats
            (vocab_id, last_trained, correct, wrong)
            VALUES (?, NULL, 0, 0)
            """, (i,))

    conn_stats.commit()
    conn_stats.close()


def add_word(word, translation):
    try:
        cur_vocab.execute(
            """
            INSERT INTO Japanisch
            (word, translation) VALUES (?, ?)
            """,
            (word, translation)
        )
        conn_vocab.commit()
        print("added word")
    except sqlite3.IntegrityError:
        print("word already in database")


def get_all_vocab_pairs():
    cur_vocab.execute("SELECT word, translation, id FROM Japanisch")
    rows = cur_vocab.fetchall()

    return rows

def print_all_vocab():
    pairs = get_all_vocab_pairs()
    # print vocab database
    for word, translation in pairs:
        print(f"{word} \t  -> \t {translation}")


def update_stats(vocab_id, correct):
    db_path="training_stats.db"
    conn_stats = sqlite3.connect(db_path)
    cur_stats = conn_stats.cursor()

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

    cur_stats.execute(sql_string, (now, vocab_id))

    conn_stats.commit()
    conn_stats.close()


def get_last_learned(vocab_id):
    # return when a word was last reviewed
    db_path="training_stats.db"
    conn_stats = sqlite3.connect(db_path)
    cur_stats = conn_stats.cursor()

    now = datetime.now().isoformat(timespec='seconds')

    sql_string = """
    SELECT last_trained
    FROM training_stats
    WHERE vocab_id = ?;
    """

    cur_stats.execute(sql_string, (vocab_id,))
    res = cur_stats.fetchall()[0][0]
    # this is inefficent as this gets the last access time for each word individually

    conn_stats.commit()
    conn_stats.close()

    if res == None:
        return 365 * 24 * 60 * 60 # defualt one year - a bit arbitrary

    return (datetime.fromisoformat(now) -
            datetime.fromisoformat(res)).total_seconds()

def print_dbs():
    # for debug purposes
    db_path="training_stats.db"
    conn_stats = sqlite3.connect(db_path)
    cur_stats = conn_stats.cursor()
    cur_stats.execute("SELECT * FROM training_stats")
    rows = cur_stats.fetchall()
    print("Stats:")
    for row in rows:
        print(row)



if __name__ == "__main__":

    create_vocab_db()
    create_stats_db()

    print("Vocabulary Trainer")

    # add words to database

    while (input("Do you want to add a word? - press 'y' or 'n'") == 'y'):

        word = input("Add a word in japanese:")
        translation = input("What does it mean in German?:")

        add_word(word, translation)


    # test start
    print("let's start the test:")

    pairs = get_all_vocab_pairs()

    new_pairs = []
    for deu, jap, vocab_id in pairs:
        last = get_last_learned(vocab_id)
        new_pairs.append((deu, jap, vocab_id, last,))

    new_pairs +=  [(deu, jap, vocab_id, last) for (jap, deu, vocab_id, last) in new_pairs]

    for word, translation, vocab_id, _ in random.sample(new_pairs, 3):
        print()
        answer = input(f"{translation} :\n")
        if answer in word.split("/"):
            print("correct")
            update_stats(vocab_id, True)
        else:
            print(f"wrong - the correct answer is {word}")
            update_stats(vocab_id, False)
