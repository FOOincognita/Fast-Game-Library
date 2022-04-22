########## Libraries ##########
import os
from utils import DuplicateEntry
from xml.dom import InvalidAccessErr

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
        return f"game({self.title},{self.rating},{self.size},{self.price})"
    
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

# LL used to manage collisions using chaining within hash table
# TODO: ADD __contains__(self, item), __iter__(self), __next__(self); 
class LinkedList:
    # Dunder Constructor
    def __init__(self):
        self.head = None
        
    # Dunder len(); returns number of non-None nodes in LL
    def __len__(self): 
        i = 0
        it = self.head
        while it:
            i += 1
            it = it.next
        return i
    
    # Dunder str(); Formats LL to str for print
    def __str__(self):
        s = ""
        it = self.head
        if not len(self): 
            return "Empty List"
        while it:
            s += str(it.data) + ("->None" if not it.next else "->")
            it = it.next
        return s
    
    # Dunder del; Removes specified Node; del LL[title]; throws InvalidAccessErr if non-existent
    def __delitem__(self, title):
        if not len(self): 
            raise InvalidAccessErr
        elif self.head.getTitle() == title:
            self.head = self.head.next
            return 
        else:
            it = self.head
            while it:
                if it.next is None: 
                    raise InvalidAccessErr
                if it.next.getTitle() == title:
                    if it.next.next:
                        it.next = it.next.next
                    else: 
                        it.next = None
                    return 
                it = it.next

    # Constructs Node, then appends it to back of list
    def emplace_back(self, game_):
        if not len(self):
            self.head = Node(game_)
            return
        it = self.head
        while it.next: 
            if game_.title in ([it.getTitle(), it.next.getTitle()] if it.next else [it.getTitle()]):
                raise DuplicateEntry
            it = it.next
        it.next = Node(game_)

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
    
    # Dunder set: HT[key] = game (SETTER)
    # TODO: TEST
    def __setitem__(self, title, game_):
        self.arr[self.hash(title)].emplace_back(game_)
        #TODO: EXCEPTION PASSTHROUGH WITHIN NESTED CALL?
        
    # Dunder get: HT[key] -return-> game (GETTER)
    # TODO: TEST
    def __getitem__(self, title_):
        it = self.arr[self.hash(title_)].head
        while it:
            if it.getTitle() == title_: 
                return it.data
            it = it.next
        raise InvalidAccessErr
            
    # Dunder del: del HT[key]; deletes game at index 
    # TODO: CHECK FOR CHAINED INVALIDACCESSERR THROWS IN TESTING
    def __delitem__(self, title_):
        del self.arr[self.hash(title_)][title_] # equivalent to del LL[title]
        
    def __str__(self):
        table = ""
        for ll in self.arr:
            table += str(ll) + "\n"
        return table
            
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
        
    def loadMemory(self):
        pass
    
    def writeMemory(self):
        pass
        
    def addGame(self, game_):
        pass
    
    def __str__(self):
        pass
    
    def __delitem__(self, title_):
        pass

    def promptMainMenu(self):
        pass
    
    def search():
        pass
    
    
        
########## Main ##########
