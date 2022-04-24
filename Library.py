########## Libraries ##########
import os
import csv
from time import sleep
from xml.dom import InvalidAccessErr, InvalidCharacterErr
from utils import DuplicateEntry, EmptyEntry
from colorama import init, Fore as fg, Back as bg, Style as st
init(autoreset=True)

GAMECOLOR = st.BRIGHT + bg.BLACK + fg.GREEN
NULLCOLOR = st.BRIGHT + bg.BLACK + fg.BLUE
EMPTYCOLOR = st.BRIGHT + bg.BLACK + fg.RED
ARROW = chr(10236) + " "

sinp = lambda x: str(input(x))
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
                
        __repr__(self): 
            Returns:
                str: representing a Game's in csv format (FOR DEVELOPER ONLY)
        
    Class Methods:
        stog(cls, line): Secondary Constructor  
            Args:
                cls: class (automatically passed in)
                line (list): A list parsed by the imported CSV library
            Usage:
                Game.stog(list)
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
    
    def __repr__(self):
        return f"{self.title},{self.rating},{self.size},{self.price}"
    
    @classmethod
    def stog(cls, line):
        return cls(*line)

class Node:
    """
    Represents a single Node in a Linked List
    
    Attributes:
        Data (Game, optional): Game stored in the Node. Defaults to None.
        Next (Node, optional): Contains the next Node in the Linked List. Defaults to None.
        
    Instance Methods:
        __str__(self): 
            Usage:
                str(node1)
            Returns:
                str: Represents a Node's attributes
                
        getTitle(self):
            Usage:
                node1.getTitle()
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
                len(linkedlist1)
            Returns:
                int: Number of non-None Nodes in Linked List
                
        __str__(self): 
            Usage:
                str(linkedlist1)
            Returns:
                str: representing a Linked List 
                
        __delitem__(self, title): Deletes specified game in Linked List
            Args:
                title (str): Title of game to delete
            Usage:
                del linkedlist1[title] 
            Exceptions:
                InvalidAccessErr: When title is not present in Linked List
                
        emplace_back(self, game_): Constructs new Node, appends it to end of Linked List
            Args:
                game_ (Game): Game instance to add to Linked List
            Usage:
                linkedlist1.emplace_back(Game) 
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
        SIZE (int, optional): Number of linked Lists within arr. Defaults to 50
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
    def __init__(self, size=50):
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
    
    def __init__(self, size=50, mem="LibMem.csv"):
        self.dataBase = HashTable(size)   
        self.printable = [] # Stroes titles of Games in lexicographical order for printing
        self.MEMDIR = mem
        
        self.loadMemory(self.MEMDIR)
    
    # Resets entire game Library including LibMem.csv
    def reset(self):
        pass
    
    def search(self):
        """
        INSTRUCTIONS:
            (*) Prompt user for title using:
            
                    title_ = sinp("Enter title, or type 'back' to go back: ") 
            
                - If user input is "back", return, else search for game in self.dataBase using the title
                - "back" can be any combination of upper/lower-case letters
                - use a try-except to handle SPECIFIC exceptions when game not found (see HashTable class docstr for exceptions)
                    + Do NOT just check for 'Exception', there are specific exceptions for the class
                (**) What the user should see:
                
                        Please enter title, or type 'back' to go back: 
                        
            Searching:
                - If game with same title is found:
                    + Print formatted contents of the Game (repr(Game) will return a csv formatted string of Game):
                    + Now prompt user: "Enter 'back' to go back: "
                        Example: repr(foundGame) would return a string like: "CoD, 2.2, 10GB, $40"
                        (***) What the user should see:
                        
                                Title: CoD
                                Rating: 2.2
                                Size: 10GB
                                Price: $40
                                
                                Hit Enter to Return
                            
                    + Once user hits enter, go back to (**) screen
        """
        # Your Code here
        return
        
    def loadMemory(self, dir):
        pass
    
    # Writes newly added game to MEMDIR file 
    def writeMemory(self, game_):
        pass
        
    # imports games from a user-specified CSV
    def importGames(self):
        """
        INSTRUCTIONS:
            (*) Prompt user for filename using:
            
                    filename = sinp("Enter filename, or type 'back' to go back: ") 
                
                NOTE: If the user input for filename is 'back' (any combo of upper/lower-case letters), return
                    - Do NOT hard code in all combinations of "back"; use a str function to standardize input
                Read in a CSV line-by-line 
                    - For each line, split at ",", then pass the resulting list into the class method Game.stog() (returns Game instance)
                    - Add Game to self.dataBase using returnedGame.tile & returnedGame
                    - See HashTable's Docstring for how to add Games to self.dataBase (specifically __setitem__)
                    - You will need to be able to handle 'DuplicateEntry' & 'EmptyEntry' exceptions by using try-except blocks
                        + DO NOT USE 'EXCEPTION', IT MUST BE 'DuplicateEntry' exception
                        + If EmptyEntry, increment 'emty', an int of the number of failed lines due to empty lines that had commas
                        + If DuplicateEntry, increment 'dupe', an int of the number of failed lines due to duplicate games in file
                        + If no exception, increment a variable containging the number of successfully added games
                Print Results as shown below:
                
                                Import Complete
                            ----------------------
                            Successful Imports: 40
                            Duplicate Imports:  3
                            Empty Imports:      5
                            
                            Hit enter to continue: 
                    
                Once enter is pressed, loop back to (*)
        """
        # Your Code Here
        return
    
    # Adds game to library
    def addGame(self):
        """
        INSTRUCTIONS:
            (*) Prompt user for title, rating, size (in GB), & price (in $) using:
                    title_ = sinp("Enter title, or type 'back' to go back: ") 
                        NOTE: If the user input for title_ is 'back' (any combo of upper/lower-case letters), return, else continue prompts
                            - Do NOT hard code in all combinations of "back"; use a str function to standardize input
                    rating_ = sinp("Enter rating: ")
                    ...
            
            Put each in correct order in list of strings, then pass into Game.stog(list), which will return a Game instance
            Add to self.dataBase (HashTable) using title_ & returned Game instance
                - Look in the HashTable class Docstring to see how to add games to self.dataBase (__setitem__)
                - Use Try-Except block to handle DuplicateEntry excptions
            Print "Game successfully added" if no exceptions were thrown, sleep(2), then loop back to (*)
        """
        # Your code here
        return
    
    # Deletes a Game instance given a Title
    def delGame(self):
        """
        INSTRUCTIONS:
            (*) Prompt user for title using:
                    title_ = sinp("Enter title, or type 'back' to go back: ") 
            NOTE: If the user input for title_ is 'back' (any combo of upper/lower-case letters), return
                - Do NOT hard code in all combinations of "back"; use a str function to standardize input
            Else, delete a game from self.dataBase
                - Look in the HashTable class Docstring to see how to delete games from HashTable (__delitem__)
            Print "Game successfully deleted" if no exceptions are thrown
            Print "[ERROR]: Game not found" if an InvalidAccessErr is thrown
            Loop back to (*)
        """
        return
    
    # Dunder str(); Formats Library's HashTable (dataBase) to printable form
    def __str__(self):
        return str(self.dataBase)
    
    def printLib(self):
        """ 
        INSTRUCTIONS:
            (*) Print self cast as str
            On a newline, prompt for user for input any upper/lower-case combination of "back" 
                - (eg Back, back, BACK, BaCk, etc. are all accepted)
                - Use: 
                        response = sinp("Type 'back' to go back: ") 
                        
                - Do NOT hard code in all combinations of "back"; use a str function to standardize input
                - print "[ERROR] Invalid Response", use command sleep(3), then reprint stating from (*) above
                - Incorrect input handeling should be theoretically infinite until any version of back is entered
                
            What user should see (if Library is size 3, & only 1 game has been added):
                Empty List
                [CoD, 2.2, 10GB, $40]->[None]
                Empty List
                
                Type 'back' to go back: 
        """
        # your code here
        return 

    # Prompts user to make a selection; USE MATCH STATMENT (SWITCH)
    @staticmethod
    def promptMainMenu():
        print("########## Main Menu ##########")
        print("1) Search")
        print("2) Add Game")
        print("3) Delete Game")
        print("4) Print Library")
        print("5) Reset Library")
        print("6) Import Library")
        print("7) Save & Exit Program")
        print("###############################")
        
        sel = sinp("Make a Selection: ")
        if sel.isdigit() and 1 <= int(sel) <= 7:
            return int(sel)
        else:
            raise InvalidCharacterErr
    
    # Saves & Exits saftely (writes any unsaved added games)
    def saveAndExit(self):
        exit() ########## TEMP
        
########## Main ##########
if __name__ == "__main__":
    pass
    
    
    
    