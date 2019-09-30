class Node:
  def __init__(self, cargo, children=None, isWord = False):
    self.isWord = isWord
    self.cargo = cargo
    self.children = [None]*26
counter = 0
resulting_words = []
root = Node(None)
def build(node, val):
  index = ord(val[0])%97
  if node.children[index] == None:
    node.children[index] = Node(val[0])
  if len(val) == 1:
    node.children[index].isWord = True
  else:
    node.children[index] = build(node.children[index], val[1:])
  return node

def is_word(val, node):
  index = ord(val[0])%97
  if node.children[index] == None:
    return False 
  elif len(val) == 1:
    return node.children[index].isWord
  else:
    return is_word(val[1:], node.children[index])

def find_word(val, node):
    index = ord(val[0])%97
    if node.children[index] == None:
        print('failed to find node matching user input')
        return None
    elif len(val) == 1:
        # print(node.children[index])
        return node.children[index]
    else: 
        return find_word(val[1:], node.children[index])
def traverse(node,word):
    global counter
    global resulting_words
    if  node.isWord == True:        
        print('word: '+word)
        resulting_words.append(word)            
        counter = counter+1        
        for nodeys in node.children:            
            if nodeys != None and counter<10:
                traverse(nodeys,word+nodeys.cargo)
    else:
        for nodey in node.children:
            if nodey != None:                
                traverse(nodey,word+nodey.cargo)

def main():
  global root
  global counter
  f= open('words.txt','r')
  root = Node(None)
  fline = f.readlines()
  for line in fline:
    root = build(root, line.lower().rstrip())
  f.close()
  baseNode=root
  print('Done with tree building')
  global resulting_words
  while(True):
    test = input("Enter a word: ")
    baseNode=root
    resulting_words = []
    counter = 0
    baseNode = find_word(test.lower(),baseNode)
    if baseNode!=None:        
        traverse(baseNode,test.lower())
    else:
        print('value does not return any suggestions')
    for word in resulting_words:
        print(word)
    resulting_words = ''
if __name__ == "__main__":
  main()