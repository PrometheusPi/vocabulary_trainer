import sys
sys.path.append('../lib/')

from vocabTrainer import VocabTrainer

list_vocab_pairs_jap = [
    ("すし", "Sushi"),
    ("みず", "Wasser"),
    ("ください", "bitte"),
    ("ごはん", "Reis"),
    ("です", "da ist / es ist / ich bin"),
    ("いしゃ", "Arzt"),
    ("せんせい", "Lehrer"),
    ("やさしい", "einfach / nett"),
    ("べんごし", "Anwalt"),
    ("かっこいい", "cool"),
    ("ひと", "Person"),
    ("がくせい", "Schüler"),
    ("けん", "Ken / Ticket"),
    ("こんにちは", "hallo / hi"),
    ("どうぞよろしく", "schön dich kennenzulernen"),
    ("はな", "Blume"),
    ("なおみ", "Naomi"),
    ("さん", "Herr / Frau"),
    ("こんばんは", "guten Abend / heute Abend"),
    ("はい", "ja"),
    ("いいえ", "nein"),
    ("にほんじん", "Japaner"),
    ("カナダ", "Kanada"),
    ("アメリカじん", "Amerikaner"),
    ]

list_vocab_pairs_ital = [
    ("l'uomo", "der Mann"),
    ("i uomini", "die Männer"),
    ("la donna", "die Frau"),
    ("il signor", "der Herr"),
    ("la signora", "die Frau")
    ]

if __name__ == "__main__":
    vocab_trainer = VocabTrainer()


    vocab_trainer.create_vocab_db("Japanisch_Deutsch")
    for word, translation in list_vocab_pairs_jap:
        vocab_trainer.add_word(word, translation, "Japanisch_Deutsch")

    vocab_trainer.create_vocab_db("Italienisch_Deutsch")        
    for word, translation in list_vocab_pairs_ital:
        vocab_trainer.add_word(word, translation, "Italienisch_Deutsch")

        
    print("Languages:")
    for lang in vocab_trainer.get_all_languages():
        print(lang, ":")

        print("Vocab list:")
        vocab_trainer.print_all_vocab(lang)
