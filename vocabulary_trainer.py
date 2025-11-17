import sqlite3
import random


# know globaly
conn = sqlite3.connect("vocab_jap.db")
cur = conn.cursor()


def create_db():

    # create database if not there
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS Japanisch (
        id INTEGER PRIMARY KEY,
        word TEXT UNIQUE NOT NULL,
        translation TEXT NOT NULL
        )
        """
    )
    conn.commit()



def add_word(word, translation):
    try:
        cur.execute(
            """
            INSERT INTO Japanisch
            (word, translation) VALUES (?, ?)
            """,
            (word, translation)
        )
        conn.commit()
        print("added word")
    except sqlite3.IntegrityError:
        print("word already in database")


def get_all_vocab_pairs():
    cur.execute("SELECT word, translation FROM Japanisch")
    rows = cur.fetchall()

    return rows

def print_all_vocab():
    pairs = get_all_vocab_pairs()
    # print vocab database
    for word, translation in pairs:
        print(f"{word} \t  -> \t {translation}")




if __name__ == "__main__":

    create_db()

    print("Vocabulary Trainer")

    # add words to database

    while (input("Do you want to add a word? - press 'y' or 'n'") == 'y'):

        word = input("Add a word in japanese:")
        translation = input("What does it mean in German?:")

        add_word(word, translation)


    # test start
    print("let's start the test:")

    pairs = get_all_vocab_pairs()


    for word, translation in random.sample(pairs, 3):
        print()
        answer = input(f"{translation} :\n")
        if answer == word:
            print("correct")
        else:
            print(f"wrong - the correct answer is {word}")
