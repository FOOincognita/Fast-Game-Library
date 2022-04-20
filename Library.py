########## Libraries ##########
import os 

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# shortens x is None to empty(x)
def empty(x):
    return x is None

########## Classes ##########

# Serves as a object representing a single game
class game:
    # Constructor
    def __init__(self, title="N/A", rating="N/A", size="N/A", price="N/A"):
        self.title = title
        self.rating = rating
        self.size = size
        self.price = price
        
    # Returns true when the calling game object is a null entry (used to denote a failed get/search)
    def nullEntry(self):
        return self.title == "N/A"
    
    # Allows the str() or print() method to be used directly on the game object
    def __str__(self):
        return "{}, {}, {}, {}".format(self.title, self.rating, self.size, self.price)

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
        if self.head is None:
            self.head = Node(data)
            return
        it = self.head
        while it.next: 
            it = it.next
        it.next = Node(data)
        
    # FOR TESTING ONLY; prints list of nodes with STL datatypes ONLY (str, int, etc.)
    def printL(self):
        if self.head is None:
            print("Empty List")
            return
        it = self.head
        s = ""
        while it:
            s += str(it.data) + ("->None" if it.next is None else "->")
            it = it.next
        print(s)
        
    # Returns len(LL)
    def len(self): 
        i = 0
        it = self.head
        while it:
            i += 1
            it = it.next
        return i
    
    # Removes specified Node
    def __delitem__(self, data):
        if self.head is None:
            return 
        elif self.len() == 1:
            self.head = None
            return 
        elif self.head.data == data:
            self.head = self.head.next
            return 
        it = self.head
        while it:
            if it.next is None: 
                return 
            if it.next.data == data:
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
        
    # Generates hashed index based on the summation of ASCII values in key 
    def hash(self, title):
        hsh = 0
        for c in title:
            hsh += ord(c)
        return hsh%self.size
    
    # [] operator overload: HT[key] = game 
    # TODO: TEST
    def __setitem__(self, title, game_):
        hsh = self.hash(title)
        if (self.arr[hsh].head.data):
            self.arr[hsh].emplace_back(game_)
        else:
            self.arr[hsh].head.data = game_
        
    # [] operator overload: HT[key] -return-> game 
    # TODO: TEST
    def __getitem__(self, title):
        hsh = self.hash(title)
        n = self.arr[hsh].len()
        if (not n):
            return game()
        elif (n == 1): 
            return self.arr[hsh].head.data
        else:
            it = self.arr[hsh].head
            while it:
                if (it.data.title == title):
                    return it.data
                it = it.next
            return game() # returns blank game if game not found
            
    # del operator overload: del HT[key]; deletes value at index 
    # TODO: FIX & TEST
    def __delitem__(self, title):
        self.arr[self.hash(title)] = None

# Serves as the highest abstract data type (class), which contains the game database 
class library:
    def __init__(self, size=100):
        self.ht = HashTable(size)    
        
########## Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')
    
########## Main ##########