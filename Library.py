########## Libraries ##########
import os
from utils import DuplicateEntry, EmptyEntry
from xml.dom import InvalidAccessErr
from colorama import init, Fore as fg, Back as bg, Style as st
init(autoreset=True)

GAMECOLOR = st.BRIGHT + bg.BLACK + fg.GREEN
NULLCOLOR = st.BRIGHT + bg.BLACK + fg.BLUE
EMPTYCOLOR = st.BRIGHT + bg.BLACK + fg.RED
ARROW = chr(10236) + " "

gmestr = lambda x:  GAMECOLOR + str(x) + st.RESET_ALL
nullstr = lambda x: ARROW + NULLCOLOR + str(x) + st.RESET_ALL

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')

########## Classes ##########
class Game:
    """
    Each instance represents a single Game 

    Attributes:
        title (str, optional): Game Title. Defaults to "N/A".
        rating (str, optional): Game Rating. Defaults to "N/A".
        size (str, optional): Game size (in GB). Defaults to "N/A".
        price (str, optional): Game Price (in $). Defaults to "N/A".
        
    Instance Methods:
        __str__(self): 
            Returns:
                str: representing a Game's attributes
        
    Class Methods:
        stog(cls, line): Secondary Constructor  
            Args:
                cls: class (automatically passed in)
                line (str): A str holding a CSV line from a file
            Usage:
                Game1.stog(str)
            Returns:
                Game: instance initialized with data from CSV line
    """
    def __init__(self, title="N/A", rating="N/A", size="N/A", price="N/A"):
        self.title = title
        self.rating = rating
        self.size = size
        self.price = price
    
    def __str__(self):
        return f"[{self.title},{self.rating},{self.size},{self.price}]"
    
    @classmethod
    def stog(cls, line):
        return cls(*line.strip().split(","))

class Node:
    """
    Represents a single Node in a Linked List
    
    Attributes:
        Data (Game, optional): Game stored in the Node. Defaults to None.
        Next (Node, optional): Contains the next Node in the Linked List. Defaults to None.
        
    Instance Methods:
        __str__(self): 
            Usage:
                str(Node1)
            Returns:
                str: Represents a Node's attributes
                
        getTitle(self):
            Usage:
                Node1.getTitle()
            Returns:
                str: title of the Game stored in the Node
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    def getTitle(self):
        return self.data.title
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    """
    Linked List used in Hash Table to implement chaining method for handling collisions 
    
    Attributes:
        head (Node): Contains the first Node in a Linked List. Always initialized to None.
        
    Instance Methods:
        __iter__(self): Allows Linked List to be iterable (in for loops)
            yields:
                class iterator
        
        __contains__(self, title): Checks if game is in Linked List by title
            Args:
                title (str): Title of game
            Usage:
                if title in LinkedList1
            Returns:
                Bool: True if a Game obj with the passed in title is present in the linked list
                
        __len__(self): Length of Linked List
            Usage:
                len(LinkedList1)
            Returns:
                int: Number of non-None Nodes in Linked List
                
        __str__(self): 
            Usage:
                str(LinkedList1)
            Returns:
                str: representing a Linked List 
                
        __delitem__(self, title): Deletes specified game in Linked List
            Args:
                title (str): Title of game to delete
            Usage:
                del LinkedList[title] 
            Exceptions:
                InvalidAccessErr: When title is not present in Linked List
                
        emplace_back(self, game_): Constructs new Node, appends it to end of Linked List
            Args:
                game_ (Game): Game instance to add to Linked List
            Usage:
                LinkedList1.emplace_back(Game) 
            Exceptions:
                DuplicateEntry: When Game with same title already exists in Linked List
    """
    def __init__(self):
        self.head = None
        
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
        
    def __len__(self): 
        i = 0
        for node in self:
            i += 1
        return i
    
    def __str__(self):
        s = ""
        if not len(self): 
            return EMPTYCOLOR + "Empty List" + st.RESET_ALL
        for node in self:
            s += gmestr(node.data) + (nullstr("[None]") if not node.next else ARROW) 
        return s
    
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

class HashTable:
    """
    Hash Table which contains all Games in Library. Uses chaining to handle collisions
    
    Attributes:
        SIZE (int, optional): Number of linked Lists within arr. Defaults to 100
        arr (list): list containing LinkedLists
        
    Instance Methods:
        hash(self, title): Generates hashed index based on the summation of ASCII values in key; AKA Hash Function
            Args:
                title (str): title of Game instance
            Usage:
                HashTable1.hash(title)
            Returns:
                int: hashed integer in interval [0,SIZE]
        
        __setitem__(self, title_, game_): Inserts Game object into HashTable
            Args:
                title_ (str): Title of game
                game_ (str): Game instance
            Usage:
                HashTable1[title] = Game
            Exceptions:
                EmptyEntry: When a Game instnace has title "N/A" or ""
                DuplicateEntry: When a Game with same title is already in HashTable
                
        __getitem__(self, title_): Length of Linked List
            Usage:
                HashTable1[title]
            Returns:
                Game: Game instnace with specified title
            Exceptions:
                InvalidAccessErr: When a Game with passed title is not in Hash Table
                
        __str__(self): Formats table to str
            Usage:
                str(HashTable1)
            Returns:
                str: representing a Hash Table
                
        __delitem__(self, title_): Deletes specified game in Hash Table
            Args:
                title_ (str): Title of Game to delete
            Usage:
                del HashTable1[title] 
            Exceptions:
                InvalidAccessErr: When title is not present in Linked List
                
        __len__(self): Gets Number of Games in Hash Table
            Usage:
                len(HashTable1)
            Returns:
                int: Number of Games in HashTable
    """
    def __init__(self, size=100):
        self.SIZE = size
        self.arr = [LinkedList() for _ in range(self.SIZE)] 
        
    def hash(self, title):
        hsh = 0
        for c in title:
            hsh += ord(c)
        return hsh%self.SIZE
    
    def __setitem__(self, title_, game_):
        if not len(title_) or title_ == "N/A":
            raise EmptyEntry
        if title_ in self.arr[self.hash(title_)]:
            raise DuplicateEntry
        else:
            self.arr[self.hash(title_)].emplace_back(game_)
        
    def __getitem__(self, title_):
        for node in self.arr[self.hash(title_)]:
            if node.getTitle() == title_: 
                return node.data
        raise InvalidAccessErr
            
    def __delitem__(self, title_):
        del self.arr[self.hash(title_)][title_] 
        
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
        
        self.loadMemory()
        
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
        # 1-liner: return dataBase as a string
        pass
    
    # Dunder del; Deletes a Game instance given a Title
    def __delitem__(self, title_):
        # 1-liner: delete a game from database the same way you'd delete an element from dictionary
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
    
    
    
    