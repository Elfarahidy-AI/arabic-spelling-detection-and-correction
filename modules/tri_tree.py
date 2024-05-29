class Node:
    def __init__(self):
        self.children = {}
        # self.word = None
        self.is_end_of_word = False
        self.frequency = 0


class TrieTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = Node()
            node = node.children[char]
        node.is_end_of_word = True
        node.frequency += 1


    def spell_check(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]

        return node.is_end_of_word and node.frequency > 20
    

    def get_nearest_words( self,word, maxCost):
        
        # build first row
        currentRow = range( len(word) + 1 ) # " " + word

        results = []

        # recursively search each branch of the trie
        for letter in self.root.children:
            self.searchRecursive( self.root.children[letter], letter, word, currentRow, 
                results, maxCost , letter)

        return results


    """
    This function implements a dynamic programming approach to calculate the Levenshtein distance between the target word
    and words stored in the trie. It traverses the trie recursively, updating the costs in each row of the dynamic 
    programming matrix based on the edit operations required to transform the current word into the target word. Words 
    with a Levenshtein distance less than or equal to maxCost from the target word are appended to the results list along
    with their corresponding distances.
    """
    def searchRecursive(self, node, letter, word, previousRow, results, maxCost,currWordinTrie = ""):
        
        columns = len( word ) + 1
        currentRow = [ previousRow[0] + 1 ] # instertion first colums costs

        # Build one row for the letter, with a column for each letter in the target
        # word, plus one for the empty string at column 0
        for column in range( 1, columns ):

            insertCost = currentRow[column - 1] + 1
            deleteCost = previousRow[column] + 1

            if word[column - 1] != letter:
                replaceCost = previousRow[ column - 1 ] + 1
            else:                
                replaceCost = previousRow[ column - 1 ]

            currentRow.append( min( insertCost, deleteCost, replaceCost ) )

        # if the last entry in the row indicates the optimal cost is less than the
        # maximum cost, and there is a word in this trie node, then add it.
        if currentRow[-1] <= maxCost and node.is_end_of_word:
            results.append( (currWordinTrie, currentRow[-1] ) )

        # if any entries in the row are less than the maximum cost, then 
        # recursively search each branch of the trie # i can serach more since the minimum cost is less than maxCost
        if min( currentRow ) <= maxCost:
            for letter in node.children:
                self.searchRecursive( node.children[letter], letter, word, currentRow, 
                    results, maxCost , currWordinTrie + letter)