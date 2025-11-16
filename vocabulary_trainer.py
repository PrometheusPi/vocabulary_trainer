import sqlite3



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


if __name__ == "__main__":

    create_db()
    
    print("Vocabulary Trainer")

    while (input("Do you want to add a word? - press 'y' or 'n'") == 'y'):
    
        word = input("Add a word in japanese:")
        translation = input("What does it mean in German?:")

        add_word(word, translation)
    
    # print vocab database

    cur.execute("SELECT word, translation FROM Japanisch")
    rows = cur.fetchall()

    for word, translation in rows:
        print(f"{word} \t  -> \t {translation}")
