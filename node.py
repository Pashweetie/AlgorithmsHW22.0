class Node:
    def __init__(self, cargo, children=None, isWord = False):
        self.isWord = isWord
        self.cargo = cargo
        self.children = [None]*26