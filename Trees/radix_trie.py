from trie import TrieNode, Trie

#helper function
def find_last_common_idx(word1, word2):
    idx = 0
    while(idx < len(word1)):
        if idx < len(word2) and word1[idx] == word2[idx]:
            idx += 1
        else:
            break
    return idx



class RadixTrie(Trie):
   
    ############################## INSERTION ##############################
    def __insert(self, start_node, word):
        while(word):
            ch = word[0]
            child = start_node.get_child(ch)
            if not child:
                new_node = TrieNode(word)
                new_node.is_word = True
                start_node.set_child(word[0], new_node)
                return
            else:
                child_data = child.get_data()
                # child has exactly the given word
                if child_data == word:
                    if not child.is_word:
                        child.is_word = True
                    return
                idx = find_last_common_idx(child_data, word)
                # child has part of the given word as a prefix
                if idx <= len(word) and idx != len(child_data):
                    # split child
                    new_node = TrieNode(child_data[:idx])
                    child.data = child_data[idx:]
                    new_node.set_child(child_data[idx], child)
                    # connect new_node to start_node
                    start_node.set_child(child_data[0], new_node)
                    child = new_node
                start_node = child
                word = word[idx:]
                if word == "":
                    start_node.is_word = True


    def insert(self, word):
        assert type(word) == str, "You can insert String objects only!!"
        assert len(word) > 0, "You can't insert any empty String!!"

        if self.root.children == {}:
            new_node = TrieNode(word)
            new_node.is_word = True
            self.root.set_child(word[0], new_node)
        else:
            start_node = self.root
            self.__insert(start_node, word)


    ############################## REMOVE ##############################
    def remove(self, word):
        assert type(word) == str, "You can remove String objects only!!"
        # search for the word
        start_node = self.root
        while(word):
            ch = word[0]
            child = start_node.get_child(ch)
            if not child:
                return
            else:
                child_data = child.get_data()
                if child_data == word[:len(child_data)]:
                    start_node = child
                    word = word[len(child_data):]
                else:
                    return
                
        # if word is found, clear it
        if start_node.is_word:
            start_node.is_word = False
        while(not start_node.is_word and start_node.has_no_children()):
            ch = start_node.get_data()[0]
            parent = start_node.get_parent()
            del parent.children[ch]
            start_node = parent


    ######################### AUTO-COMPLETION #########################
    def __get_candidates(self, start_node, prefix):
        output = []
        new_prefix = prefix.copy()
        new_prefix += start_node.get_data()
        if start_node.is_word:
            output.append("".join(new_prefix))
        # iterate over children
        for child in start_node.get_children():
            output.extend( self.__get_candidates(child, new_prefix) )
        return output
    
    def get_candidates(self, prefix=''):
        assert type(prefix) == str, "A character-sequence is expected!!"
        start_node = self.root
        # parse the prefix
        word = prefix
        while(word):
            ch = word[0]
            child = start_node.get_child(ch)
            if not child:
                return []
            else:
                child_data = child.get_data()
                if child_data == word[:len(child_data)]:
                    start_node = child
                    word = word[len(child_data):]
                else:
                    break
        # get candidates starting from given prefix
        candidates = []
        prefix = prefix[:len(word)]
        if start_node.is_word and word == prefix:
            candidates.append(prefix)
        for child in start_node.get_children():
            candidates.extend(self.__get_candidates(child, [prefix]))
        return candidates






if __name__ == "__main__":
    # # src: https://en.wikipedia.org/wiki/Radix_tree?oldformat=true
    # rt = RadixTrie()
    # rt.insert("romane")
    # rt.insert("romanus")
    # rt.insert("romulus")
    # rt.insert("rubens")
    # rt.insert("ruber")
    # rt.insert("rubicon")
    # rt.insert("rubicundus")
    # print(rt)
    # print('='*50)

    rt = RadixTrie()
    rt.insert("shear")
    rt.insert("she")
    rt.insert("shepard")
    rt.insert("shepard")
    rt.insert("she")
    rt.insert('s')
    print(rt)
    print(rt.find('s'))
    print(rt.find("shea"))
    print(rt.get_candidates("sh"))
    print('='*50)

    # rt = RadixTrie()
    # rt.insert("test")
    # rt.insert("toaster")
    # rt.insert("toasting")
    # rt.insert("slow")
    # rt.insert("slowly")
    # rt.insert("slowlier")
    # rt.insert("toast")
    # rt.insert("slower")
    # print(rt)
    # print(rt.find("slowlie"))
    # rt.remove("test")  # remove 'est' from tree
    # rt.remove("slow") # remove is_word
    # rt.remove("slowl") # do nothin'
    # print(rt)
    # print('='*50)
    
    # sanity checks
    rt = RadixTrie()
    print(rt.find(''))
    # print(rt.find(2)) #throws error


