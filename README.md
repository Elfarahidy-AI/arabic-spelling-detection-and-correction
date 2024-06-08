# Arabic Spelling Detection and Correction

This project implements an Arabic spelling detection and correction system using a trie tree, bigram database, and unigram fallback. The system aims to identify misspelled Arabic words and provide the most probable correct word as a suggestion.
Features

- Detects unfamiliar words as potentially misspelled words using a trie tree.
- Utilizes a bigram database to determine the most probable correct word based on the context.
- Falls back to a unigram approach if the bigram fails to provide a suitable correction.
- Returns the most probable correct word as the suggested correction.

## Installation

#### Clone the repository:

    git clone git@github.com:Elfarahidy-AI/arabic-spelling-detection-and-correction.git
   
#### Install the required dependencies:

    pip install -r requirements.txt

#### Usage

    text = "هذا النص يحتوط على أخطال إملائية"

#### Output:

    هذا النص يحتوي على أخطاء إملائية


The project relies on the following data sources:

- Trie Tree: A trie tree is constructed using a corpus of Arabic words to efficiently detect unfamiliar words.
-  Bigram Database: A database of Arabic word bigrams is used to determine the most probable correct word based on the surrounding context.
- Unigram Database: A dictionary of frequencies of Arabic word unigrams stored in a pickle file is used as a fallback when the bigram approach fails to provide a suitable correction.
