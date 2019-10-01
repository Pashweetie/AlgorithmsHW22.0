from pynput.keyboard import Key, Listener
import getpass
#Justin Treece made dis


#!*!*!*!*!*!*! IMPORTANT RUNNING INFO!*!*!*!*!*!*!*
#unless you install the pynput with the command:
#pip install pynput
#or
#pip3 install pynput
#There WILL  be errors with this program probably saying something along the lines of 
#cannot find pynput.keyboard
#in order to run this command you must have an updated pip
#command to update pip is: python -m pip install --upgrade pip
#or
#python3 -m pip install --upgrade pip
#both the library command and the upgrade pip require admin level permissions (wouldnt work on a school computer unless you're admin)
#additionally this was made in python 3.7!!! could be cross compatible with 2 but unlikely
#make sure that if you're using python3 and not python 2 run it with python3 not sure if python will work

#run command python3/python predictor.py
#must have words.txt in the same directory

#The program definetly works to your specifications so if you have any problems running it let me know, I can probably solve then and if not
#I can always record a video or screenshare my application working

#pynput is my library for the keyboard interrupts, getpass is so when you type into
#the "input" field your deletions and insertions wont affect whats printed out directly after
class Node:
  def __init__(self, cargo, children=None, isWord = False):
    self.isWord = isWord
    self.cargo = cargo
    self.children = [None]*26
keyvalue = ''
counter = 0
resulting_words = []
root = Node(None)
#builds the tree, characters are put 0-25 based on how far they are on the alphabet
#for example a is index 0 z is index 25
def build(node, val):
  index = ord(val[0])%97
  if node.children[index] == None:
    node.children[index] = Node(val[0])
  if len(val) == 1:
    node.children[index].isWord = True
  else:
    node.children[index] = build(node.children[index], val[1:])
  return node
#used this method to check and make sure that my tree was fully functioning. Just confirms
# whether a word is a word or not. Ended up using
#a similar method to find words in traverse
def is_word(val, node):
  index = ord(val[0])%97
  if node.children[index] == None:
    return False 
  elif len(val) == 1:
    return node.children[index].isWord
  else:
    return is_word(val[1:], node.children[index])
#simply returns a node for the eventual input that a user will put in to be set
#as my base node to search from
def find_word(val, node):
    index = ord(val[0])%97
    if node.children[index] == None:
        print('failed to find node matching user input')
        return None
    elif len(val) == 1:
        return node.children[index]
    else: 
        return find_word(val[1:], node.children[index])
#traverse finds nodes until counter is seen to hit 10. Ended up actually being forced to check the words
#length in order to certify that it actually hit exactly ten. This made
#the output much nicer and more uniform in the commandline
def traverse(node,word):
    global counter
    global resulting_words
    if  node.isWord == True:
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
#key press interrupts necessary for the conintuously updated word suggesstions
#relatively easy to break, a couple special characters especially control break
#the loop
def on_press(key):
    global keyvalue
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
    if key == Key.esc:
        return False
def run_traverse(test):
  #wanted to avoid globals but with recursion I was worried and confused about how some of these would be modified. Global
  #variables definetly make it easier
  global root
  global counter
  global resulting_words
  baseNode=root
  counter = 0
  baseNode = find_word(test.lower(),baseNode)
  print('Suggestions: ')
  #nested traverse within this function to make the code a tad bit cleaner
  if baseNode!=None:        
      traverse(baseNode,test.lower())
  else:#error check so that if your entry is blank or if your entry simply isnt found it will gracefully deal with it
      print('value does not return any suggestions')
      #prints the word suggestions
  for word in resulting_words:
      print(word)
  resulting_words = []

#without a main method python gets confused and wont run the file
def main():
  global root
  global counter
  global keyvalue
  f= open('words.txt','r')  
  root = Node(None)
  fline = f.readlines()
  for line in fline:
    root = build(root, line.lower().rstrip())
  f.close()
  baseNode=root
  print('Done with tree building')  
  print('go ahead and input your word, esc to exit')
  #this listener listens for keystrokes and interrupts when necessary. I had a blocking version before and found this
  #this is much better
  listener = Listener(
    on_press=on_press,
    on_release=on_release)
  listener.start()
  global resulting_words
  while(True):    
    #gives a interrupt to pause until the user updates the input field which is invisible by design (before i wrote
    #this with a input which shows what you're typing in. This had some very strange and wild effects on printed values
    #genuinely I could have found a bug with python
    test = getpass.getpass('')
#this is another part to make the file always run
if __name__ == "__main__":
  main()