import sys
sys.path.append('../lib/')

from vocabTrainer import VocabTrainer

list_vocab_pairs = []

list_vocab_pairs.append(("すし", "Sushi"))
list_vocab_pairs.append(("みず", "Wasser"))
list_vocab_pairs.append(("ください", "bitte"))
list_vocab_pairs.append(("ごはん", "Reis"))
list_vocab_pairs.append(("です", "da ist / es ist / ich bin"))
list_vocab_pairs.append(("いしゃ", "Arzt"))
list_vocab_pairs.append(("せんせい", "Lehrer"))
list_vocab_pairs.append(("やさしい", "einfach / nett"))
list_vocab_pairs.append(("べんごし", "Anwalt"))
list_vocab_pairs.append(("かっこいい", "cool"))
list_vocab_pairs.append(("ひと", "Person"))
list_vocab_pairs.append(("がくせい", "Schüler"))
list_vocab_pairs.append(("けん", "Ken / Ticket"))


if __name__ == "__main__":
    vocab_trainer = VocabTrainer()

    for word, translation in list_vocab_pairs:
        vocab_trainer.add_word(word, translation)

    print("Vocab list:")
    vocab_trainer.print_all_vocab()
