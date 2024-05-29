from pickle import dump, load

from modules.tri_tree import TrieTree
from modules.bigram import Bigram
from modules.unigram import Unigram
from db_drivers.bigram_driver import BigramDB
import gc



def save_trie_in_pickle(trie):
    with open("models/trie.pickle", "wb") as file:
        dump(trie, file)


def save_bigarm_in_pickle(ngram):
    with open("models/bigram.pickle", "wb") as file:
        dump(ngram, file)


def save_unigram_in_pickle(ngram):
    with open("models/unigram.pickle", "wb") as file:
        dump(ngram, file)


def load_trie_from_pickle():
    with open("models/trie.pickle", "rb") as file:
        return load(file)


def load_bigram_from_pickle():
    with open("models/bigram.pickle", "rb") as file:
        return load(file)


def load_unigram_from_pickle():
    with open("models/unigram.pickle", "rb") as file:
        return load(file)


def feed_data_to_trie(trie):
    for i in range(0, 19):
        if i == 9 or i == 13:
            continue
        filename = "datasets/cleaned/cleaned_text" + str(i) + ".txt"
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                words = line.split()
                for word in words:
                    trie.insert(word)
        print("file " + filename + " is done.")
    return trie

def train_bigram(bigram, db):
    for i in range(0, 19):
        if i == 9 or i == 13:
            continue
        filename = "datasets/cleaned/cleaned_text" + str(i) + ".txt"
        bigram.read_data(filename)
        bigram.handle_merging_wow_el3atf()
        bigram.build_bigram()
        
        db.store_bigram(bigram.bigram)  # Store the bigram dictionary in the database
        
        bigram.data_buffer.clear()
        bigram.bigram.clear()  # Clear the bigram dictionary after storing it
        gc.collect()
        print("file " + filename + " is done.")
    return bigram


def train_unigram(unigram):
    for i in range(0, 19):
        if i == 9 or i == 13:
            continue
        filename = "datasets/cleaned/cleaned_text" + str(i) + ".txt"
        unigram.read_data(filename)
        unigram.handle_merging_wow_el3atf()
        unigram.build_unigram()
        
        unigram.data_buffer.clear()
        gc.collect()
        print("file " + filename + " is done.")
    return unigram


def model_builder():
    trie = TrieTree()
    trie = feed_data_to_trie(trie )
    save_trie_in_pickle(trie)
    print("trie is saved in pickle file\n")

    print("now building the unigram model")
    unigram = Unigram()
    unigram = train_unigram(unigram)
    save_unigram_in_pickle(unigram)
    print("unigram is saved in pickle file\n")

    print("now building the bigram model")
    bigram = Bigram()
    db = BigramDB("models/bigram.db")  # Create an instance of BigramDB
    bigram = train_bigram(bigram, db)  # Pass the BigramDB instance to train_bigram
    print("bigram is stored in the database")



