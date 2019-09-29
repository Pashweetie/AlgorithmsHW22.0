class Node:
  def __init__(self, cargo, children=None, isWord = False):
    self.isWord = isWord
    self.cargo = cargo
    self.children = [None]*26


storedWords= open('words.txt','r')

storedWords = storedWords.read().splitlines()
storedWords = [item.lower() for item in storedWords]
ord(storedWords[0][0]) # convert first letter to uni

root = Node(None)


def add_val(val, node):

  if len(val) > 1:
    if node.children[ord(val[0])-97] == None:
      node.children[ord(val[0])-97] = Node(val[0])

    node.children[ord(val[0])-97] = add_val(val[1:],node.children[ord(val[0])-97])
    return node

  elif len(val) == 1:
    if node.children[ord(val[0])-97] == None:
      node.children[ord(val[0])-97] = Node(val[0])

    node.children[ord(val[0])-97].isWord = True
    return node

def is_word(word, node) -> bool:
  if len(word)==1:
    return node.isWord
  else:
    if node.children[ord(word[0])-97] != None:
      return is_word(word[1:],node.children[ord(word[0])-97])
    else:
      return False

for word in storedWords:
  root = add_val(word,root)
    
print('Done with tree building')
testWord = 'sabotage'
print('Is '+testWord+' a word?: ')
print(is_word(testWord, root))


# def printTree(node, word):
#     if node.children == [None]*26:
#         print(node.cargo)
#     else:
#         for nodes in node.children:
#             if nodes != None:
#                 printTree(nodes,word+node.cargo)
# printTree(root," ")