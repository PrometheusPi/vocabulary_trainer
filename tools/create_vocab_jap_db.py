import sys
sys.path.append('../lib/')

from vocabTrainer import VocabTrainer
from japanese_german import list_vocab_pairs_jap_deu
from italian_german import list_vocab_pairs_ital_deu


if __name__ == "__main__":
    vocab_trainer = VocabTrainer()


    vocab_trainer.create_vocab_db("Japanisch_Deutsch")
    for word, translation in list_vocab_pairs_jap_deu:
        vocab_trainer.add_word(word, translation, "Japanisch_Deutsch")
    print("Number of entries:", len(list_vocab_pairs_jap_deu))

    vocab_trainer.create_vocab_db("Italienisch_Deutsch")
    for word, translation in list_vocab_pairs_ital_deu:
        vocab_trainer.add_word(word, translation, "Italienisch_Deutsch")
    print("Number of entries:", len(list_vocab_pairs_ital_deu))

    print("Languages:")
    for lang in vocab_trainer.get_all_languages():
        print(lang, ":")

        print("Vocab list:")
        vocab_trainer.print_all_vocab(lang)
