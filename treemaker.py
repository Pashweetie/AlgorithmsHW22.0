from node import Node
# print ('hello world')
storedWords= open('words.txt','r')
# print(storedWords)
storedWords = storedWords.read().splitlines()
storedWords = [item.lower() for item in storedWords]
# print(storedWords)
print (ord(storedWords[0])%26)
root = Node(None)
node = Node(1)
node.children[5] = Node(5)
print('')

def add_val(val, node):
    print('val: '+str(val)+' node cargo: '+str(node.cargo))
    if len(val) > 1:
        node.children[ord(val[0])%26] = Node(None)
        print('children: '+ str(node.children[ord(val[0])%26]))
        add_val(val[1:],node.children[ord(val[0])%26])
    elif len(val) == 1:
        node.isWord = True
        if val[0] == node.cargo:
            # print('repeated node', node)
            return node
        else:
            node.cargo = val[0]
            # print('created node', node)
            return node
def is_word(word, node) -> bool:
    if len(word)>1:
        # node.children[ord(word[0])%26] = Node(None)
        if node.children[ord(word[0])%26] != None:
            is_word(word[1:],node.children[ord(word[0])%26])
        else:
            return False  
    elif len(word)==1:
        if node.is_word == True:
            return True
        else:
            return False
for word in storedWords:
    root = add_val(word,root)
print('Done with tree building')
testWord = 'aa'
print('Is '+testWord+' a word?: ')
# print(is_word(testWord, root))


# def printTree(node, word):
#     if node.children == [None]*26:
#         print(node.cargo)
#     else:
#         for nodes in node.children:
#             if nodes != None:
#                 printTree(nodes,word+node.cargo)
# printTree(root," ")

