########## Libraries ##########
import os 

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')

########## Classes ##########

# Serves as a object representing a single game
class game:
    # Dunder Constructor
    def __init__(self, title="N/A", rating="N/A", size="N/A", price="N/A"):
        self.title = title
        self.rating = rating
        self.size = size
        self.price = price
    
    # Dunder str(); Formats game instance to str
    # TODO: TEST
    def __str__(self):
        return "game( {}, {}, {}, {} )\n".format(self.title, self.rating, self.size, self.price)
    
    # Class Method (secondary constructor); returns new game instance from single CSV line; stog -> String to Game (C++ convention)
    # TODO: TEST SPLAT OPERATOR 
    @classmethod
    def stog(cls, line):
        return cls(*line.strip().split(","))

# Serves as each node in Linked List
class Node:
    # Dunder Constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# LL used to manage collisions using chaining within hash table
# TODO: ADD __contains__(self, item), __iter__(self), __next__(self); 
class LinkedList:
    # Dunder Constructor
    def __init__(self):
        self.head = None
        
    # Dunder str(); Formats LL to str for print
    # TODO: TEST
    def __str__(self):
        s = ""
        it = self.head
        if not self.head: 
            return "Empty List"
        while it:
            s += str(it.data) + ("->None" if not it.next else "->")
            it = it.next
        return s
        
    # Dunder len(); returns number of non-None nodes in LL
    # TODO: TEST
    def __len__(self): 
        i = 0
        it = self.head
        while it:
            i += 1
            it = it.next
        return i
    
    # Dunder del; Removes specified Node; del LL[title]
    #TODO: DOESN'T HANDLE NON-EXISTANT DELETE REQUESTS
    def __delitem__(self, title):
        if len(self) < 2: # This doesn't check if the specified item is correct
            self.head = None
            return 
        elif self.head.data.title == title: ## TODO: OVERLOAD EQUALITY OPERATOR FOR GAME CLASS
            self.head = self.head.next
            return 
        else:
            it = self.head
            while it:
                if not it.next: return 
                if it.next.data.title == title:
                    if it.next.next:
                        it.next = it.next.next
                    else: 
                        it.next = None
                    return 
                it = it.next  
        
    # Constructs Node, then appends it to back of list
    def emplace_back(self, data):
        if not self.head:
            self.head = Node(data)
            return
        it = self.head
        while it.next: 
            it = it.next
        it.next = Node(data)

# Serves as a Hash Table to be used within class library
# TODO: TEST
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
        #TODO: CHECK FOR DUPLICATES
        
    # Dunder get: HT[key] -return-> game (GETTER)
    # TODO: TEST
    def __getitem__(self, title_):
        it = self.arr[self.hash(title_)].head
        while it:
            if it.data.title == title_: ############ TODO:  OVERLOAD EQUALITY OPERATOR!!!!!!!
                return it.data
            it = it.next
        return None # returns None if game not found
            
    # Dunder del: del HT[key]; deletes game at index 
    # TODO: FIX & TEST
    def __delitem__(self, title_):
        del self.arr[self.hash(title_)][title_] # equivalent to del LL[title]

# Serves as the highest abstract data type (class), which contains the game database 
class library:
    
    numBooks = 0
    
    def __init__(self, size=100):
        self.ht = HashTable(size)    
        
        library.numBooks += 1
        
########## Main ##########