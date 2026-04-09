import sys
sys.path.append('../lib/')

from vocabTrainer import VocabTrainer

list_vocab_pairs = []

list_vocab_pairs.append(("すし", "Sushi"))
list_vocab_pairs.append(("みず", "Wasser"))


if __name__ == "__main__":
    vocab_trainer = VocabTrainer()

    for word, translation in list_vocab_pairs:
        vocab_trainer.add_word(word, translation)

    print("Vocab list:")
    vocab_trainer.print_all_vocab()
