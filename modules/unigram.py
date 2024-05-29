


class Unigram():

    def __init__(self):
        self.data_buffer = []
        self.unigram = {}


    def read_data(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    words = line.split()
                    for word in words:
                        self.data_buffer.append(word)
    

    """
    handling the words that has a 'و' before it to merge them together
    """
    def handle_merging_wow_el3atf(self):
        merged_buffer = []
        i = 0
        while i < len(self.data_buffer):
            if self.data_buffer[i] == 'و' and i + 1 < len(self.data_buffer):
                merged_buffer.append('و' + self.data_buffer[i+1])
                i += 2
            else:
                merged_buffer.append(self.data_buffer[i])
                i += 1
        self.data_buffer = merged_buffer



    """
    build a unigram model for the backoff after the bigram
    """    
    def build_unigram(self):
        for i in range(0, len(self.data_buffer)):
            if self.data_buffer[i] not in self.unigram:
                self.unigram[self.data_buffer[i]] = 1
            else:
                self.unigram[self.data_buffer[i]] += 1



    """
    handle wow el3atf in the text before predicting
    """
    def handle_wow_el3atf_in_predict(self, text):
        words = text.split()
        i = 0
        while i < len(words):
            if words[i] == 'و' and i + 1 < len(words):
                words[i] = 'و' + words[i+1]
                words.pop(i+1)
            i += 1
        return words
    
    """
    the prediction function for the unigram model
    """    
    def predict(self, potential_words):
        max_prob = 0
        predicted_word = ""
        for word in potential_words:
            if word in self.unigram.keys():
                freq = self.unigram[word]
                if freq > max_prob:
                    max_prob = freq
                    predicted_word = word
        return predicted_word

