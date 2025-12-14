from lib.vocabTrainer import vocab_trainer

if __name__ == "__main__":

    my_vocab_trainer = vocab_trainer()

    print("Vocabulary Trainer")

    # add words to database
    while (input("Do you want to add a word? - press 'y' or 'n'") == 'y'):

        word = input("Add a word in japanese:")
        translation = input("What does it mean in German?:")

        my_vocab_trainer.add_word(word, translation)


    # test start
    print("let's start the test:")
    
    for word, translation, vocab_id, _ in my_vocab_trainer.get_vocab_pairs(3):
        print()
        answer = input(f"{translation} :\n")
        if answer in word.split("/"):
            print("correct")
            my_vocab_trainer.update_stats(vocab_id, True)
        else:
            print(f"wrong - the correct answer is {word}")
            my_vocab_trainer.update_stats(vocab_id, False)
