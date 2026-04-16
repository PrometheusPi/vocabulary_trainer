import sys
sys.path.append('../lib/')

from vocabTrainer import VocabTrainer

list_vocab_pairs = [
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


if __name__ == "__main__":
    vocab_trainer = VocabTrainer()

    for word, translation in list_vocab_pairs:
        vocab_trainer.add_word(word, translation)

    print("Languages:")
    for lang in vocab_trainer.get_all_languages():
        print(lang)

    print("Vocab list:")
    vocab_trainer.print_all_vocab()
