import sqlite3
import random


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
    cur_vocab.execute("SELECT word, translation FROM Japanisch")
    rows = cur_vocab.fetchall()

    return rows

def print_all_vocab():
    pairs = get_all_vocab_pairs()
    # print vocab database
    for word, translation in pairs:
        print(f"{word} \t  -> \t {translation}")




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
    pairs +=  [(deu, jap) for (jap, deu) in pairs]

    for word, translation in random.sample(pairs, 3):
        print()
        answer = input(f"{translation} :\n")
        if answer == word:
            print("correct")
        else:
            print(f"wrong - the correct answer is {word}")

