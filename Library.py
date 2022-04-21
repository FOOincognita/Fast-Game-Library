########## Libraries ##########
import os 

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# shortens x is None to empty(x)
def empty(x):
    return x is None

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')

########## Classes ##########

# Serves as a object representing a single game
class game:
    # Constructor
    def __init__(self, title="N/A", rating="N/A", size="N/A", price="N/A"):
        self.title = title
        self.rating = rating
        self.size = size
        self.price = price
        
    # Returns true when instance is all N/A
    # TODO: Should I remove?
    def nullEntry(self):
        return self.title == "N/A"
    
    # Allows the str()/print() method to be used directly on the game instance
    # TODO: TEST
    def __str__(self):
        return "< {}, {}, {}, {} >".format(self.title, self.rating, self.size, self.price)
    
    # Parses CSV line (str); returns new game instance; stog -> String to Game (C++ convention)
    @classmethod
    def stog(cls, line):
        return cls()

# Serves as each node in Linked List; used for collisions in Hash table
class Node:
    # Constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

# Serves as main class for Linked List data structure
class LinkedList:
    # Constructor
    def __init__(self):
        self.head = None
    
    # Constructs Node, then appends it to list
    def emplace_back(self, data):
        if empty(self.head):
            self.head = Node(data)
            return
        it = self.head
        while it.next: 
            it = it.next
        it.next = Node(data)
        
    # Allows a LinkedList() object to be used in str()/print()
    #TODO: TEST
    def __str__(self):
        if empty(self.head): return "Empty List"
        it = self.head
        s = ""
        while it:
            s += str(it.data) + ("->None" if empty(it.next) else "->")
            it = it.next
        return s
        
    # Allows the use of len() to return integer length of the Linked list, which is the number of nodes
    # TODO: TEST
    def __len__(self): 
        i = 0
        if empty(self.head): return i
        it = self.head
        while it:
            i += 1
            it = it.next
        return i
    
    # Removes specified Node
    #TODO: DOESN'T HANDLE NON-EXISTANT DELETE REQUESTS
    def __delitem__(self, data_):
        if len(self) < 2: # This doesn't check if the specified item is correct
            self.head = None
            return 
        elif self.head.data == data_: ## TODO: OVERLOAD EQUALITY OPERATOR FOR GAME CLASS
            self.head = self.head.next
            return 
        else:
            it = self.head
            while it:
                if empty(it.next): return 
                if it.next.data == data_:
                    if it.next.next:
                        it.next = it.next.next
                    else: 
                        it.next = None
                    return 
                it = it.next  
        

# Serves as a Hash Table to be used within class library
# TODO: TEST
class HashTable:
    # Constructor
    def __init__(self, size=100):
        self.size = size
        self.arr = [LinkedList() for _ in range(self.size)] 
        
    # Generates hashed index based on the summation of ASCII values in key; AKA Hash Function
    def hash(self, title):
        hsh = 0
        for c in title:
            hsh += ord(c)
        return hsh%self.size
    
    # [] operator overload: HT[key] = game (SETTER)
    # TODO: TEST
    def __setitem__(self, title, game_):
        hsh = self.hash(title)
        if not empty(self.arr[hsh].head):
            self.arr[hsh].emplace_back(game_)
        else:
            self.arr[hsh].head.data = game_
        
    # [] operator overload: HT[key] -return-> game (GETTER)
    # TODO: TEST
    def __getitem__(self, title_):
        n = len(self.arr[self.hash(title_)])
        it = self.arr[self.hash(title_)].head
        if not n: return None
        elif n == 1 and it.data.title == title_: ############ TODO:  OVERLOAD EQUALITY OPERATOR!!!!!!!
            return it.data
        else:
            while it:
                if (it.data.title == title_):
                    return it.data
                it = it.next
            return None # returns None if game not found
            
    # del operator overload: del HT[key]; deletes value at index 
    # TODO: FIX & TEST
    def __delitem__(self, title):
        self.arr[self.hash(title)] = None

# Serves as the highest abstract data type (class), which contains the game database 
class library:
    numBooks = 0
    
    def __init__(self, size=100):
        self.ht = HashTable(size)    
        
        library.numBooks += 1
        
########## Main ##########