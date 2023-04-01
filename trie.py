class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_the_word = False
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.word_count += 1
        node.is_end_of_the_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_the_word
    
    def start_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def suggested_words(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        suggestions = []
        self.get_words_from_node(node, prefix, suggestions)
        suggestions.sort()
        return suggestions
    
    def get_words_from_node(self, node, prefix, suggestions):
        if node.is_end_of_the_word:
            suggestions.append(prefix)
        
        for char, child in node.children.items():
            self.get_words_from_node(child, prefix+char, suggestions)
    
    def count_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self.sum_words_count(node)

    def sum_words_count(self, node):
        if node is None:
            return 0
        count = node.word_count if node.is_end_of_the_word else 0
        for child in node.children.values():
            count += self.sum_words_count(child)
        return count

    def print_trie(self, node=None, word = ""):
        if node == None:
            node = self.root

        if node.is_end_of_the_word:
            print(word)

        for char, child in node.children.items():
            self.print_trie(child, word+ char)


insert_arr = ["apple","banana","cherry","dog","elephant","fox","grape","house","igloo","jacket", "avacado","kivi"]

trie = Trie()

for word in insert_arr:
    trie.insert(word)

# trie.print_trie()

# print(trie.search("apple"))

# Check if Trie contains words starting with certain prefixes
check_ele = ["a","f","e","i","b","x","p","k"]

for check in check_ele:
    # print(trie.start_with(check))
    pass

# count words with prefix
prefix_arr = ["a","ap","b","c","d","e","f","g","h","i","j","k","x"]

for sug_word in prefix_arr:
    print(trie.suggested_words(sug_word), trie.count_words_with_prefix(sug_word))
