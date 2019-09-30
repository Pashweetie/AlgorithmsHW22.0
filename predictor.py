from pynput.keyboard import Key, Listener
import getpass
class Node:
  def __init__(self, cargo, children=None, isWord = False):
    self.isWord = isWord
    self.cargo = cargo
    self.children = [None]*26
keyvalue = ''
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
        # print(word)
        if len(resulting_words) <10:
          resulting_words.append(word)            
        counter = counter+1        
        for nodeys in node.children:            
            if nodeys != None and counter<10:
                traverse(nodeys,word+nodeys.cargo)
    else:
        for nodey in node.children:
            if nodey != None:                
                traverse(nodey,word+nodey.cargo)

def on_press(key):
    # print('{0} pressed'.format(
    #     key))
    global keyvalue
    # print('key entered: {0}'.format(key))
    if key == Key.backspace:
      keyvalue = keyvalue[:-1]
      print()
      print()
      print()
      print('your input: '+keyvalue)
      if keyvalue != '':    
        run_traverse(keyvalue)
    elif key.char.isalpha():      
      keyvalue = keyvalue + '{0}'.format(key.char)
      print()
      print()
      print()
      print('your input: '+keyvalue)
      if keyvalue != '':    
        run_traverse(keyvalue)
    else:
      print('invalid char')
    
def on_release(key):
    # print('{0} release'.format(
    #     key))
    
    if key == Key.esc:
        # Stop listener
        return False
def run_traverse(test):
  global root
  global counter
  global resulting_words
  baseNode=root
  # print('in key listener')
  counter = 0
  baseNode = find_word(test.lower(),baseNode)
  print('Suggestions: ')
  if baseNode!=None:        
      traverse(baseNode,test.lower())
  else:
      print('value does not return any suggestions')
  # print(resulting_words)
  for word in resulting_words:
      print(word)
  resulting_words = []

def main():
  global root
  global counter
  global keyvalue
  f= open('words.txt','r')
  # Collect events until released
  
  root = Node(None)
  fline = f.readlines()
  for line in fline:
    root = build(root, line.lower().rstrip())
  f.close()
  baseNode=root
  print('Done with tree building')  
  print('go ahead and input your word, esc to exit')
  # with Listener(
  #         on_press=on_press,
  #         on_release=on_release) as listener:
  #     listener.join()
  listener = Listener(
    on_press=on_press,
    on_release=on_release)
  listener.start()
  global resulting_words
  while(True):    
    test = getpass.getpass('')
    # print ('in main')
    # baseNode=root
    # resulting_words = []
    # counter = 0
    # baseNode = find_word(test.lower(),baseNode)
    # if baseNode!=None:        
    #     traverse(baseNode,test.lower())
    # else:
    #     print('value does not return any suggestions')
    # print()
    # print('your input: '+ keyvalue)
    # for word in resulting_words:
    #     print(word)
    # resulting_words = ''
if __name__ == "__main__":
  main()