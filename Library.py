########## Libraries ##########
import os
import cursor # cursor.hide()
from time import sleep 
from xml.dom import InvalidAccessErr, InvalidCharacterErr
from utils import DuplicateEntry, EmptyEntry, InvalidSelection
from colorama import init, Fore as fg, Back as bg, Style as st
init(autoreset=True)

NULLSTR = st.BRIGHT + bg.BLACK + fg.BLUE + "[None]" + st.RESET_ALL
ARROW = st.BRIGHT + fg.WHITE + chr(10236) + " "
HIDECURSOR = '\033[?25l' # end=''
SHOWCURSOR = '\033[?25h' # end=''

sinp = lambda x: str(input(str(x)))
fgtxt = lambda x,y: st.BRIGHT + x + str(y) + st.RESET_ALL
gmestr = lambda x:  st.BRIGHT + bg.BLACK + fg.GREEN + str(x) + st.RESET_ALL + ARROW
rtxt = lambda x: fgtxt(fg.RED, x)
ytxt = lambda x: fgtxt(fg.YELLOW, x)
ctxt = lambda x: fgtxt(fg.CYAN, x)
gtxt = lambda x: fgtxt(fg.GREEN, x)
mtxt = lambda x: fgtxt(fg.MAGENTA, x)
wtxt = lambda x: fgtxt(fg.WHITE, x)

cPrint = lambda x: print(ctxt(x))
rPrint = lambda x: print(rtxt(x))
gPrint = lambda x: print(gtxt(x))
yPrint = lambda x: print(ytxt(x))
mPrint = lambda x: print(mtxt(x))
wPrint = lambda x: print(wtxt(x))

rsinp = lambda x: sinp(rtxt(x))
ysinp = lambda x: sinp(ytxt(x))
csinp = lambda x: sinp(ctxt(x))
gsinp = lambda x: sinp(gtxt(x))
msinp = lambda x: sinp(mtxt(x))
wsinp = lambda x: sinp(wtxt(x))

########## Global Constants ##########
T = True
F = False

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls||clear')

###################################################################### GAME CLASS ###################################################################### 
class Game:
    """ Each instance represents a single Game
    
    Attributes:
        title (str, optional): Game Title. Defaults to "N/A".
        rating (str, optional): Game Rating. Defaults to "N/A".
        size (str, optional): Game size (in GB). Defaults to "N/A".
        price (str, optional): Game Price (in $). Defaults to "N/A".
    """
    def __init__(self, title="N/A", rating="N/A", size="N/A", price="N/A"):
        self.title = title
        self.rating = rating
        self.size = size
        self.price = price
    
    def __str__(self):
        """ Formats Game instnace to str 
        Returns:
                str: representing a Game's attributes
        """
        return f"[{self.title}]"
    
    def __repr__(self):
        """ Formats Game instance to CSV style string
        Returns:
            str: representing a Game's in csv format (FOR DEVELOPER ONLY)
        Usage:
            gameString = repr(gameVariable) 
        """
        return f"{self.title},{self.rating},{self.size},{self.price}"
    
    @classmethod
    def stog(cls, line):
        """ Secondary Constructor  
        Args:
            cls: class (automatically passed in)
            line (list): A list parsed by the imported CSV library, or manually using split
        Usage:
            gameVariable = Game.stog(list)
        Returns:
                Game: instance initialized with data from CSV line
        """
        return cls(*line)


###################################################################### NODE CLASS ###################################################################### 

class Node:
    """ Represents a single Node in a Linked List
    
    Attributes:
        Data (Game, optional): Game stored in the Node. Defaults to None.
        Next (Node, optional): Contains the next Node in the Linked List. Defaults to None.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
        
    @property
    def title(self):
        """ Gets the title of a game within a Node's data attribute
        Usage:
            nodeInstanceVariable.title 
        Returns:
            str: title of the Game stored in the Node
        """
        return self.data.title
    
    def __str__(self):
        """ Formats a Node to a string
        Usage:
            str(node1)
        Returns:
            str: Represents a Node's attributes
        """
        return str(self.data)
    
    
###################################################################### LINKEDLIST CLASS ###################################################################### 

class LinkedList:
    """ Linked List used in Hash Table to implement chaining method for handling collisions 
    
    Attributes:
        head (Node): Contains the first Node in a Linked List. Always initialized to None.
    """
    def __init__(self):
        self.head = None
        
    def __iter__(self):
        """ Allows Linked List to be iterable (e.g. in for loops)
        yields:
            iterator: Next Node in list (Node.next), if any
        """
        curr = self.head
        while curr:
            yield curr
            curr = curr.next
            
    def __contains__(self, title_):
        """ Checks if game is in Linked List by title
        Args:
            title (str): Title of game
        Usage:
            if title in LinkedListInstance: Do something
        Returns:
            Bool: True if a Game obj with the passed in title is present in the linked list
        """
        for node in self:
            if node.title == title_:
                return True
        return False
        
    def __len__(self): 
        """ Length of Linked List
        Usage:
            len(linkedlistInstance)
        Returns:
            int: Number of non-None Nodes in Linked List
        """
        i = 0
        for _ in self:
            i += 1
        return i
    
    def __str__(self):
        """ Returns string representing Linked List
        Usage:
            str(linkedlistInstance)
        Returns:
            str: representing a Linked List 
        """
        s = ""
        if not len(self): 
            return NULLSTR #<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< CHANGE TO NULLSTR ###################################################################
        for node in self:
            s += gmestr(node.data) + (NULLSTR if not node.next else "") 
        return s
    
    def __delitem__(self, title):
        """ Deletes specified game in Linked List
        Args:
            title (str): Title of game to delete
        Usage:
            del linkedlistInstance[title] 
        Raises:
            InvalidAccessErr: When title is not present in Linked List
        """
        if not len(self) or title not in self: 
            raise InvalidAccessErr
        elif self.head.title == title:
            self.head = self.head.next
            return 
        else:
            for node in self:
                if node.next is None: 
                    raise InvalidAccessErr
                if node.next.title == title:
                    if node.next.next:
                        node.next = node.next.next
                    else: 
                        node.next = None
                    return 

    def emplace_back(self, game_):
        """ Constructs new Node, appends it to end of Linked List
        Args:
            game_ (Game): Game instance to add to Linked List
        Usage:
            linkedlistInstance.emplace_back(Game) 
        Exceptions:
            DuplicateEntry: When Game with same title already exists in Linked List
        """
        if not len(self):
            self.head = Node(game_)
            return
        if game_.title in self:
            raise DuplicateEntry
        for node in self: 
            if node.next is None:
                node.next = Node(game_)
                return


###################################################################### HASHTABLE CLASS ###################################################################### 

class HashTable:
    """ Hash Table data structure which contains all Games in Library. Uses Linked Lists for chaining to handle collisions
    
    Attributes:
        SIZE (int, optional): Number of linked Lists within arr. Defaults to 50
        arr (list): list containing LinkedLists
    """
    def __init__(self, size=50):
        self.SIZE = size
        self.arr = [LinkedList() for _ in range(self.SIZE)] 
        
    def hash(self, title_):
        """ Generates hashed index for self.arr placement based on the summation of ASCII values in key; AKA Hash Function
        Args:
            title_ (str): title of Game instance
        Usage:
            hashValue = self.hash(title_) 
        Returns:
            int: hashed integer in interval [0,self.SIZE]
        """
        hsh = 0
        for c in title_:
            hsh += ord(c)
        return hsh%self.SIZE
    
    def __setitem__(self, title_, game_):
        """ Inserts Game object into HashTable
        Args:
            title_ (str): Title of game
            game_ (str): Game instance
        Usage:
            HashTableInstance[title_] = game_
        Exceptions:
            EmptyEntry: When a Game instnace has title "N/A" or ""
            DuplicateEntry: When a Game with same title is already in HashTable
        """
        if not len(title_) or title_ == "N/A":
            raise EmptyEntry
        if title_ in self.arr[self.hash(title_)]:
            raise DuplicateEntry
        else:
            self.arr[self.hash(title_)].emplace_back(game_)
        
    def __getitem__(self, title_):
        """ Gets Game at hashed index if it exists
        Args:
            title_ (str): title of Game instance
        Usage:
            gameInstance = HashTableInstance[title_]
        Returns:
            Game: Game instance with specified title (if one exists in HashTable instance)
        Raises:
            InvalidAccessErr: When a Game with passed title is not in Hash Table
        """
        for node in self.arr[self.hash(title_)]:
            if node.title == title_: 
                return node.data
        raise InvalidAccessErr
            
    def __delitem__(self, title_):
        """ Deletes specified game in Hash Table (by title)
        Args:
            title_ (str): Title of Game to delete
        Usage:
            del HashTableInstance[title_] 
        Raises:
            InvalidAccessErr: When title is not present in Linked List
        """
        del self.arr[self.hash(title_)][title_] 
        
    def __str__(self):
        """ Formats hash table to str (shows contents & links)
        Usage:
            str(self) or str(HashTableInstance)
        Returns:
            str: representing a Hash Table
        """
        table = ""
        for ll in self.arr:
            table += str(ll) + "\n"
        return table
            
    def __len__(self): 
        """ Gets Number of Games in Hash Table
        Usage:
            length = len(HashTableVariable) or length = len(self)
        Returns:
            int: Number of Games in HashTable
        """
        i = 0
        for ll in self.arr:
            i += len(ll)
        return i
    
    
###################################################################### LIBRARY CLASS ###################################################################### 
    
# Serves as the highest abstract data type (class), which contains the game database (Hash Table)
class Library:
    """ Represents the Game library; wrapper for data structures
    
    Attributes:
        size (int, optional): size of the dataBase. Defaults to 50
        dataBase (HashTable): Hash Table which contains all stored Games
        MEMDIR (str): Directory of persistent memory file
    """
    def __init__(self, size=50):
        self.size = size
        self.dataBase = HashTable(size)   
        self.MEMDIR = "LibMem.csv"
        
        self.loadMemory()
    
    # Resets entire game Library including LibMem.csv
    def resetLib(self):
        """ Prompts user Y/N if they want to erase all Game permanently """
        while T:
            clear()
            rPrint("\n[WARNING]: Resetting the library will delete all games in memory forever!\n")
            sleep(1)
            selYN = ysinp("\nAre you sure you want to delete all games [Y/N]?\n").strip().upper()
            if len(selYN) == 1 and selYN.isalpha() and selYN in ["Y","N"]:
                match selYN:
                    case "N": return
                    case "Y": 
                        open(self.MEMDIR, 'w').close() 
                        self.dataBase = HashTable(self.size)
                        gPrint("\nLibrary Successfully Reset!\n")
                        ysinp("Press Enter to Continue")
                        return
            else:
                clear()
                rPrint("\n[ERROR]: INVALID SELECTION\nPLEASE SELECT 'Y', OR 'N'")
                sleep(4)
    
    # Prints instructions
    @staticmethod
    def instructions():
        """ Prints Instructions """
        clear()
        wPrint("#"*22 + " Instructions " + "#"*22)
        print(mtxt("This library uses a HashTable to store & reterieve games\n& their data in constant time (Instantly)."), end="")
        mPrint(" Lists, which\nare normally used to store indexable data, take linear\ntime (proportional to number of games stored).\n")
        print(mtxt("In this library, you can search, add games, delete games,\ncombine the existing library with a file containing\nentries,"), end="")
        mPrint("print the library, reset the library, then save\n& exit whenever you're done.\n")
        mPrint("Whenever you exit, your games will be saved in memory,\nmeaning they'll still be in the libary for next time.\n")
        mPrint("User instructions for this software are always on screen.")
        wPrint("#"*57)
        ysinp("\nPress Enter to Return")
        return
    
    
    # Searches for single game by user inputted title
    def search(self):    
        while(True):
            title_=sinp("Enter Title, or Type 'back' to Go Back:")
            if (title_.lower() =="back"): return
            try: gamev = self.dataBase[title_]
            except InvalidAccessErr:
                rPrint("\n[Error]: Game not Found\n")
                sleep(3) 
            else:
                a = repr(gamev).strip(",")
                print("Title:  ",a[0])
                print("Rating:  ",a[1])
                print("Size:  ",a[2])
                print("Price:  ",a[3])
                sinp("\n Hit Enter to Continue")
        
        
        
        
        
        
        
        
    # Loads in persistent memory stored in self.MEMDIR (LibMem.csv, or any other csv containing Game entries)
    # TODO: IMPLEMNET
    def loadMemory(self):
        """
        Read in a CSV or txt file line-by-line (Library's attribute self.MEMDIR contains the filename of the peristsent memory, AKA, the csv/txt file)
            - For each line, split into a list of 4 strings for each piece of data ([title, rating, size, price]) then pass the 
                    resulting list into Game.stog(list goes here), which will return a Game instance (See Game class Docstring for more info)
                + Be sure to strip each line of newline characters & extra spaces (do not remove necessary spaces in the title)
            - Add Game to self.dataBase (You can use GameVar.title to access the title of the game)
                + See HashTable's Docstring for how to add Games to self.dataBase (specifically __setitem__)
                NOTE: You will need to be able to handle 'DuplicateEntry' & 'EmptyEntry' exceptions by using a try-except-else block (see #resources channel)
                + DO NOT USE 'Exception', IT MUST BE 'DuplicateEntry' exception, or 'EmptyEntry' exception
            - If EmptyEntry or Duplicate entry is raised, ignore the line
            - If no exception, add the game to self.dataBase (see __setitem__ in HashTable's docstring)
        When the end of the file is reached, return
        """
        
        # Your Code Here
        
        return
    
    # Writes newly added game(s) to MEMDIR file upon save & exit call
    # TODO: IMPLEMENT
    def writeMemory(self, game_):
        pass
        
        
        
        
        
        
        
        
    # imports games from a user-specified CSV
    def importGames(self):
        while T:
            filename = sinp("Enter filename, or type 'back' to go back: ") 
            if str.lower(filename) == "back": return
            else:
                openfile = open(filename,'r')
                filedata = openfile.read()
                lista = filedata.split('\n')
                listb = [string.split(',') for string in lista]
                openfile.close()
                
                d, e, p = 0, 0, 0
                for row in listb:
                    try:
                        gameinfo = Game.stog(row)
                        self.dataBase[gameinfo.title] = gameinfo
                    except DuplicateEntry: d+=1
                    except EmptyEntry: e+=1                
                    else: p+=1
                      
                print("    Import Completed    ")
                print("----------------------")
                print("Successful Imports: {}".format(p))
                print("Duplicate Imports:  {}".format(d))
                print("Empty Imports:      {}".format(e))
                print()
                ysinp("Press Enter to Continue")
                return

    
    
    
    
    
    
    
    
    
    
    
    
    
    # Adds game to library
    def addGame(self):
        """
        INSTRUCTIONS:
            (*) Prompt user for title using (see sinp at very top of file):
            
                    title_ = sinp("Enter title, or type 'back' to go back: ") 
                    
                NOTE: 
                    - If user enters 'back' (any combo of upper/lower-case letters), return
                        + Do NOT hard code in all combinations of "back"; use a str function to standardize input
                    - Else prompt for rating, size (in GB), & price (in $)
                        + Add "GB" if missing from user inputted size string
                        + Add "$" if missing from user inputted price string
                        What user should see:
                        
                        Enter Rating: 
                        ...
            
            Put each in correct order in list of strings, then pass into Game.stog(list) (returns a Game instance)
                - See Game's Docstring for stog usage
            Use Try-Except-Except-Else-finally block to handle DuplicateEntry exceptions for next steps
                - Do NOT check for 'Exception'; you must only check for DuplicateEntry exceptions
            Try to add Game to self.dataBase (HashTable) using title_ & the Game instance returned by Game.stog()
                - Look in the HashTable class Docstring to see how to add games to self.dataBase (HashTable's __setitem__ will be useful)
                - Print "\nGame successfully added\n" if no exceptions were raised
                - If DuplicateEntry is raised, print "\n[ERROR]: Duplicate Game!\n"
                - If EmptyEntry is raised, print "\n[ERROR]: Empty Entry!\n"
            Finally, sleep(3)
            Loop back to (*); This means most, if not all, of your code will be in a While True loop, which only stops upon return
        """
        
        
        # Your code here
        
        
        
        return
    
    
    
    
    
    
    
    
    
    
    
    # Deletes a Game instance given a Title
    def delGame(self):
        """
        INSTRUCTIONS:
            (*) Prompt user for title using (see sinp at very top of file):
            
                    title_ = sinp("Enter Title of Game, or 'back' to Return to Main Menu: ") 
                    
            If the user input for title_ is any combo of upper/lower-case letters of "back", return
                - "back", "Back", "BaCk", & all other combinations should be accepted as equal to "back"
                - Do NOT hard code in all combinations of "back"; use a str function to standardize string input
            Else, using a try-except-else-finally block:
            
                Try to delete game from self.dataBase using title_
                    - Look in the HashTable class Docstring to see how to delete games using a title
                        + __delitem__ documentation will be useful, especially the "usage" portion
                            
                If InvalidAccessErr raised, Print "\n[ERROR]: Game not found\n"
                    - Do NOT check for the exception called 'Exception'; you MUST only check for 'InvalidAccessErr'
                        
                Else, Print "\nGame successfully deleted\n"   
                
                Finally, sleep(3)
                      
            Loop back to (*); This means most, if not all, of your code will be in a while True loop
        """
        
        
        # Your code here
        
        
        return 
    
    
    
    
    
    
    
    
    
    
    
    # Dunder str(); Formats Library's HashTable (dataBase) to printable form
    def __str__(self):
        """ Casts Library Instance to string
        Returns:
            str: a string representing the underlying HashTable Instnace
        """
        return str(self.dataBase)
    
    
    
    
    
    
    # Prints library to terminal
    def printLib(self):
        """ 
        INSTRUCTIONS:
            (*) Print Library as a string (the function right above you will allow self to be cast as a string)
                + do NOT use str(self.dataBase)
            Print a newline, then prompt user for input using (see sinp at very top of file):
             
                    sinp("Press Enter to go back: ") 
                
            What user should see if the Library has a size of 3, & contains 1 game; game may appear in a different order):
            
                    [None]
                    [Call of Duty]->[None]
                    [None]
                
                    Press Enter to go back

            Once they hit enter, return 
        """
        
        
        # your code here
        
        
        return







    # Prompts user to make a selection; USE MATCH STATMENT (SWITCH)
    @staticmethod
    def promptMainMenu():
        """ Prompts main menu; grabs user input with error checking
        Raises:
            InvalidSelection: When user inputs anything other than an int in [1,8]
        Returns:
            int: user input (menu selection)
        """
        sel = ""
        while not sel:
            clear()
            wPrint("#"*10 + " Main Menu " + "#"*10)
            cPrint("1) Search")
            cPrint("2) Add Game")
            cPrint("3) Delete Game")
            cPrint("4) Instructions")
            cPrint("5) Print Library")
            cPrint("6) Reset Library")
            cPrint("7) Import Library")
            cPrint("8) Save & Exit Program")
            wPrint("#"*30)
            sel = ysinp("Please Make a Selection: ")
            
        if sel.isdigit() and 1 <= int(sel) <= 8:
            return int(sel)
        else:
            raise InvalidSelection(sel)
    
    # Saves & Exits saftely (writes any unsaved added games)
    # TODO: IMPLEMENT FULL FUNCTIONALITY
    def saveAndExit(self):
        while T:
            clear()
            selYN = rsinp("\nAre you sure you want to exit [Y/N]?\n").strip().upper()
            if len(selYN) == 1 and selYN.isalpha() and selYN in ["Y","N"]:
                match selYN:
                    case "N": return
                    case "Y": exit()
            else:
                clear()
                rPrint("\n[ERROR]: INVALID SELECTION\nPLEASE SELECT 'Y', OR 'N'")
                sleep(4)
        
###################################################################### MAIN ###################################################################### 
if __name__ == "__main__":
    pass

# Function Signup Sheet: https://docs.google.com/spreadsheets/d/1FHZYT3ugd7z8yNfNrpPMC92HNbMRgKagbsxZSr7g1Bs/edit?usp=sharing

