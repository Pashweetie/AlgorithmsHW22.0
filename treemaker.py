from node import Node
print ('hello world')
storedWords= open('words.txt','r')
# print(storedWords)
storedWords = storedWords.read().splitlines()
# print(storedWords)
print (ord(storedWords[0])%26)
root = Node(None)
node = Node(1)
node.children[5] = Node(5)
print('')

def addVal(val, node, root):
    print(val)
    if len(val) > 1:
        node.children[ord(val[0])%26] = Node(None)
        print(node.children[ord(val[0])%26].cargo)
        addVal(val[1:],node.children[ord(val[0])%26], root)
    elif len(val) == 1:
        node.isWord = True
        if val[0] == node.cargo:
            # print('repeated node', node)
            return root
        else:
            node.cargo = val[0]
            # print('created node', node)
            return root
def isWord(word, node) -> bool:
    if len(word)>1:
        # node.children[ord(word[0])%26] = Node(None)
        if node.children[ord(word[0])%26] != None:
            isWord(word[1:],node.children[ord(word[0])%26])
        else:
            return False  
    elif len(word)==1:
        if node.isWord == True:
            return True
        else:
            return False
for word in storedWords:
    root = addVal(word,root,root)
print('Done with tree building')
testWord = 'aa'
print('Is '+testWord+' a word?: ')
print(isWord(testWord, root))
# def printTree(node, word):
#     if node.children == [None]*26:
#         print(node.cargo)
#     else:
#         for nodes in node.children:
#             if nodes != None:
#                 printTree(nodes,word+node.cargo)
# printTree(root," ")

