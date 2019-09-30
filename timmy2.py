class Node:
  def __init__(self, cargo, children=None, isWord = False):
    self.isWord = isWord
    self.cargo = cargo
    self.children = [None]*26

storedWords= open('words.txt','r')

storedWords = storedWords.read().splitlines()
storedWords = [item.lower() for item in storedWords]

root = Node(None)

def build(node, val):
  index = ord(val[0])-97
  if node.children[index] == None:
      node.children[index] = Node(val[0])
  if len(val) == 1:
    node.children[index].isWord = True
    return node 
  else:
    node.children[index] = build(node.children[index], val[1:])
    return node

def is_word(word, node) -> bool:
  child = node.children[ord(word[0])-97]
  if len(word)==1:
    if child == None:
      return False
    return child.isWord
  else:
    if node.children[ord(word[1])-97] != None:
      return is_word(word[1:],node.children[ord(word[0])-97])
    else:
      return False
def find_word(word, node):
    if len(word)==1:
        if
for word in storedWords:
  root = build(root, word)



print('Done with tree building')
testWord = 'convuluted'
print('Is '+testWord+' a word?: ')
print(is_word(testWord, root))

while(True):
  test = input("Enter a word: ")
  print(is_word(test.lower(), root))