class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
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
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def count_words_with_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0
            node = node.children[char]
        return self.sum_word_counts(node)

    def sum_word_counts(self, node):
        if node is None:
            return 0
        count = node.word_count if node.is_end_of_word else 0
        for child_node in node.children.values():
            count += self.sum_word_counts(child_node)
        return count

    def print_trie(self, node=None, word=""):
        if node is None:
            node = self.root

        if node.is_end_of_word:
            print(word)

        for char, child_node in node.children.items():
            self.print_trie(child_node, word + char)

    def suggest_words(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]

        suggestions = []
        self._get_words_from_node(node, prefix, suggestions)
        suggestions.sort()
        return suggestions

    def _get_words_from_node(self, node, prefix, suggestions):
        if node.is_end_of_word:
            suggestions.append(prefix)

        for char, child_node in node.children.items():
            self._get_words_from_node(child_node, prefix + char, suggestions)

trie = Trie()
insert_arr = ["apple","banana","cherry","dog","elephant","fox","grape","house","igloo","jacket", "avacado"]

# insert words to trie
for word in insert_arr:
    trie.insert(word)

# print trie
trie.print_trie()

# Search for some words in the Trie
print(trie.search("cherry")) # True
print(trie.search("cat")) # False


# Check if Trie contains words starting with certain prefixes
check_ele = ["a","f","e","i","b","x","p","k"]
for check in check_ele:
    print(trie.starts_with(check))


# count words with prefix
prefix_arr = ["a","ap","b","c","d","e","f","g","h","i","j","k","x"]
for pref in prefix_arr:
    print(trie.count_words_with_prefix(pref))

#  suggest words based on prefix
for suf_wor in prefix_arr:
    print(trie.suggest_words(suf_wor))