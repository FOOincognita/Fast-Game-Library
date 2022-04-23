########## Libraries ##########
import os
from utils import DuplicateEntry, EmptyEntry
from xml.dom import InvalidAccessErr
from colorama import init, Fore as fg, Back as bg, Style as st
init(autoreset=True)

GAMECOLOR = st.BRIGHT + bg.BLACK + fg.GREEN

NULLCOLOR = st.BRIGHT + bg.BLACK + fg.BLUE

EMPTYCOLOR = st.BRIGHT + bg.BLACK + fg.RED

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')

########## Classes ##########

# Serves as a object representing a single game
class Game:
    # Dunder Constructor
    def __init__(self, title="N/A", rating="N/A", size="N/A", price="N/A"):
        self.title = title
        self.rating = rating
        self.size = size
        self.price = price
    
    # Dunder str(); Formats game instance to str
    def __str__(self):
        return f"[{self.title},{self.rating},{self.size},{self.price}]"
    
    # Class Method (secondary constructor); returns new game instance from CSV format line; stog -> String to Game (C++ convention)
    @classmethod
    def stog(cls, line):
        return cls(*line.strip().split(","))



# Serves as each node in Linked List
class Node:
    # Dunder Constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def getTitle(self):
        return self.data.title
    
    def __str__(self):
        return str(self.data)

# LL used to manage collisions using chaining within hash table
class LinkedList:
    # Dunder Constructor
    def __init__(self):
        self.head = None
        
    # Dunder iter(); Allows LLs to be iterable in for loops
    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
            
    def __contains__(self, title):
        for node in self:
            if node.getTitle() == title:
                return True
        return False
        
    # Dunder len(); returns number of non-None nodes in LL
    def __len__(self): 
        i = 0
        for node in self:
            i += 1
        return i
    
    # Dunder str(); Formats LL to str for print
    def __str__(self):
        s = ""
        if not len(self): 
            return EMPTYCOLOR + "Empty List" + st.RESET_ALL
        for node in self:
            s += GAMECOLOR + str(node.data) + st.RESET_ALL + (chr(10236) + " " + NULLCOLOR + "[None]" + st.RESET_ALL if not node.next else chr(10236) + " ") 
        return s
    
    # Dunder del; Removes specified Node; del LL[title]; throws InvalidAccessErr if non-existent
    def __delitem__(self, title):
        if not len(self) or title not in self: 
            raise InvalidAccessErr
        elif self.head.getTitle() == title:
            self.head = self.head.next
            return 
        else:
            for node in self:
                if node.next is None: 
                    raise InvalidAccessErr
                if node.next.getTitle() == title:
                    if node.next.next:
                        node.next = node.next.next
                    else: 
                        node.next = None
                    return 

    # Constructs Node, then appends it to back of list
    def emplace_back(self, game_):
        if not len(self):
            self.head = Node(game_)
            return
        if game_.title in self:
            raise DuplicateEntry
        for node in self: 
            if node.next is None:
                node.next = Node(game_)
                return

# Serves as a Hash Table to be used within class library
class HashTable:
    # Dunder Constructor
    def __init__(self, size=100):
        self.SIZE = size
        self.arr = [LinkedList() for _ in range(self.SIZE)] 
        
    # Generates hashed index based on the summation of ASCII values in key; AKA Hash Function
    def hash(self, title):
        hsh = 0
        for c in title:
            hsh += ord(c)
        return hsh%self.SIZE
    
    # Dunder set: HT[key] = Game; throws EmptyEntry & DuplicateEntry
    def __setitem__(self, title_, game_):
        if not len(title_) or title_ == "N/A":
            raise EmptyEntry
        if title_ in self.arr[self.hash(title_)]:
            raise DuplicateEntry
        else:
            self.arr[self.hash(title_)].emplace_back(game_)
        
    # Dunder get: HT[key] -return-> Game; Throws InvalidAccessErr
    def __getitem__(self, title_):
        for node in self.arr[self.hash(title_)]:
            if node.getTitle() == title_: 
                return node
        raise InvalidAccessErr
            
    # Dunder del: del HT[key]; deletes game with matching title; Throws InvalidAccessErr 
    def __delitem__(self, title_):
        del self.arr[self.hash(title_)][title_] 
        
    # Dunder str(); Formats HashTable as string
    def __str__(self):
        table = ""
        for ll in self.arr:
            table += str(ll) + "\n"
        return table
            
    # Dunder len(); Returns int number of games in Hash Table
    def __len__(self): 
        i = 0
        for ll in self.arr:
            i += len(ll)
        return i
        
    

# Serves as the highest abstract data type (class), which contains the game database 
class Library:
    
    numGames = 0
    
    def __init__(self, size=100):
        self.dataBase = HashTable(size)   
        self.printable = [] 
        self.MEMDIR = "LibMem.txt"
        
    # Loads in "LibMem.txt" at program start
    def loadMemory(self):
        pass
    
    # Writes all data to "LibMem.txt" at exit
    def writeMemory(self):
        pass
        
    # [TEMPORARY METHOD]: Adds game to library
    def addGame(self, game_):
        pass
    
    # Dunder str(); Formats Library's HashTable (dataBase) to printable form
    def __str__(self):
        pass
    
    # Dunder del; Deletes a Game instance given a Title
    def __delitem__(self, title_):
        pass

    # Prompts user to make a selection; USE MATCH STATMENT (SWITCH)
    def promptMainMenu(self):
        pass
    
    # Saves & Exits saftely (writes to LibMem)
    def saveAndExit():
        pass
    
    
        
########## Main ##########
if __name__ == "__main__":
    pass
    
    