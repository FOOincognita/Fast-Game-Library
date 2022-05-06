########## Libraries ##########
import os
from time import sleep 
from xml.dom import InvalidAccessErr, InvalidCharacterErr
from utils import DuplicateEntry, EmptyEntry, ExitNoSave, InvalidSelection, SaveExit
from colorama import init, Fore as fg, Back as bg, Style as st
init(autoreset=True)

NULLSTR = st.BRIGHT + bg.BLACK + fg.BLUE + "[None]" + st.RESET_ALL
ARROW = st.BRIGHT + fg.WHITE + chr(10236) + " "
ARROW_WSL = st.BRIGHT + fg.WHITE + bg.BLACK + "->" + st.RESET_ALL
HIDECURSOR = '\033[?25l' # end=''
SHOWCURSOR = '\033[?25h' # end=''

sinp = lambda x: str(input(str(x)))
fgtxt = lambda x,y: st.BRIGHT + x + str(y) + st.RESET_ALL
gmestr = lambda x:  st.BRIGHT + bg.BLACK + fg.GREEN + str(x) + st.RESET_ALL + ARROW_WSL ################# CHNAGE TO ARROW WHEN USING VSCODE'S TERMINAL, LEAVE AS IS FOR WSL2
rtxt = lambda x: fgtxt(fg.RED, x)
btxt = lambda x: fgtxt(fg.BLUE, x)
ytxt = lambda x: fgtxt(fg.YELLOW, x)
ctxt = lambda x: fgtxt(fg.CYAN, x)
gtxt = lambda x: fgtxt(fg.GREEN, x)
mtxt = lambda x: fgtxt(fg.MAGENTA, x)
wtxt = lambda x: fgtxt(fg.WHITE, x)

cPrint = lambda x: print(ctxt(x))
rPrint = lambda x: print(rtxt(x))
bPrint = lambda x: print(btxt(x))
gPrint = lambda x: print(gtxt(x))
yPrint = lambda x: print(ytxt(x))
mPrint = lambda x: print(mtxt(x))
wPrint = lambda x: print(wtxt(x))

rsinp = lambda x: sinp(rtxt(x))
bsinp = lambda x: sinp(btxt(x))
ysinp = lambda x: sinp(ytxt(x))
csinp = lambda x: sinp(ctxt(x))
gsinp = lambda x: sinp(gtxt(x))
msinp = lambda x: sinp(mtxt(x))
wsinp = lambda x: sinp(wtxt(x))

########## Global Constants ##########
T = True
F = False
LOW = ["of", "the"]

########## Global Functions ##########

# Clears terminal screen on Win, Mac, & Linux
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def formName(name):
    """ Formats name (First, Middle, & Last) to have capital first letter, lowercase remaining 
    Returns:
        str: Correctly formatted title
    """
    form = ""
    for n in name.strip().split(" "):
        if not len(n): return name
        form += n if n.isupper() else (n.lower() if n.casefold() in LOW else n[0].upper() + n[1:].lower())
        form += " "
    return form[:-1]

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
            return NULLSTR 
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
            if node.title.casefold() == title_.casefold(): 
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
    
    
class Library:
    """ Represents the Game library; wrapper for data structures; highest abstract class
    
    Attributes:
        size (int, optional): size of the dataBase. Defaults to 50
        dataBase (HashTable[Game]): Hash Table which contains all stored Games
        MEMDIR (str): Directory of persistent memory file
        titles (list[str]): contains all titles of entered games; used for lexicographical sorting for printLib()
        modified (bool): True when a game(s) has been imported, added, deleted; False when dataBase hasn't been modified
    """
    def __init__(self, size=50, mem="LibMem.csv"):
        self.size = size
        self.dataBase = HashTable(size)   
        self.MEMDIR = mem
        self.titles = []
        
        self.modified = False
        
        self.loadMemory()
        
    def exportLibrary(self):
        """ Creates a backup of the current library named using user-input """
        while T:
            clear()
            response = ysinp("\n\nType 'back', or enter a filename for your exported library: ")
            if (response.casefold() == "back"): return
            else:
                if response[-4:] != ".csv": response += ".csv"
                if os.path.exists(response):
                    clear()
                    rPrint(f"\n\n[WARNING]: A file named {response} already exists")
                    selYN = ysinp("\nWould you like to overwrite this file with this export [Y/N]?").strip().upper()
                    if len(selYN) == 1 and selYN.isalpha() and selYN in ["Y","N"]:
                        if selYN == "N": continue
                    else:
                        clear()
                        rPrint("\n[ERROR]: INVALID SELECTION\nPLEASE SELECT 'Y', OR 'N'")
                        sleep(4)
                        continue
                
                with open(response, 'w') as f:
                    for ll in self.dataBase.arr:
                        if len(ll):
                            for node in ll:
                                if node.data is not None:
                                    f.write(f"{repr(node.data)}\n")
                clear()
                gPrint("\n\nExport Complete!")
                ysinp("\nHit Enter to Continue")
                                
    
    def __len__(self):
        """ Enables use of len(Library)
        Returns:
            int: Number of Games in Library's HashTable (dataBase)
        """
        return len(self.dataBase)
    
    def resetLib(self):
        """ Prompts user Y/N if they want to erase all Games permanently from HashTable & specified persistent memory CSV """
        while T:
            clear()
            rPrint("\n[WARNING]: Resetting the library will delete all games in memory forever!\n")
            sleep(1)
            selYN = ysinp("\nAre you sure you want to delete all games [Y/N]?\n").strip().upper()
            if len(selYN) == 1 and selYN.isalpha() and selYN in ["Y","N"]:
                match selYN:
                    case "N": return
                    case "Y": 
                        self.titles = []
                        open(self.MEMDIR, 'w').close() 
                        self.dataBase = HashTable(self.size)
                        gPrint("\nLibrary Successfully Reset!\n")
                        ysinp("Press Enter to Continue")
                        return
            else:
                clear()
                rPrint("\n[ERROR]: INVALID SELECTION\nPLEASE SELECT 'Y', OR 'N'")
                sleep(4)
    
    @staticmethod
    def instructions():
        """ Prints Instructions """
        clear()
        wPrint("#"*22 + " Instructions " + "#"*22)
        print(mtxt("This library uses a HashTable to store & reterieve games\n& their data in constant time (Instantly)."), end="")
        mPrint(" Lists, which\nare normally used to store indexable data, take linear\ntime (proportional to number of games stored).\n")
        print(mtxt("In this library, you can search, add games, delete games,\ncombine the existing library with a file containing\nentries,"), end="")
        mPrint(" print the library/database, reset the library,\nthen save & exit whenever you're done.\n")
        mPrint("Whenever you exit, your games will be saved in memory,\nmeaning they'll still be in the library for next time.\n")
        mPrint("User instructions for this software are always on screen.")
        wPrint("#"*57)
        ysinp("\nPress Enter to Return")
        return
    
    
    def search(self):    
        """ Searches for single game by user inputted title, prints matching game's attributes """
        while(True):
            clear()
            title_ = ysinp("\n\n\nEnter Title, or Type 'back' to Go Back:").strip()
            if (title_.casefold() == "back"): return
            try: gamev = self.dataBase[formName(title_)]
            except InvalidAccessErr:
                clear()
                rPrint("\n\n[Error]: Game not Found")
                sleep(3) 
            else:
                clear()
                rep = repr(gamev)
                a = rep.split(",")
                spc = " "*6
                bar = "_"*(len(a[0])+12)
                print("\n\n\n")
                wPrint(f"{spc}{a[0]}{spc}")
                wPrint(f"{bar}\n")
                cPrint("Rating:".ljust(10) + f"{a[1]}")
                cPrint("Size:".ljust(10) + f"{a[2]}")
                cPrint("Price:".ljust(10) + f"{a[3]}")
                ysinp("\n\nHit Enter to Continue")
        
    def importGames(self):
        """ Imports games from a user-specified CSV into self.dataBase (a HashTable) """
        while T:
            clear()
            filename_ = ysinp("\n\nEnter filename, or type 'back' to go back: ") 
            if filename_.casefold() == "back": return
            else:
                try:
                    with open(filename_, 'r') as f:
                        filedata = f.read()
                        lista = filedata.split('\n')
                        listb = [string.split(',') for string in lista]
                except FileNotFoundError: 
                    clear()
                    rPrint(f"\n\n[ERROR]: {filename_} not found")
                    sleep(5)
                else:
                    d, e, p = 0, 0, 0
                    for row in listb:
                        try:
                            gameinfo = Game.stog(row)
                            gameinfo.title = formName(gameinfo.title)
                            self.dataBase[gameinfo.title] = gameinfo
                        except DuplicateEntry: d+=1
                        except EmptyEntry: e+=1                
                        else: 
                            self.modified = T
                            self.titles.append(gameinfo.title)
                            p+=1
                    clear()
                    print("\n\n\n")
                    print("    Import Completed    ")
                    print("------------------------")
                    gPrint("Successful Imports:".ljust(22) + f"{p}")
                    rPrint("Duplicate Imports:".ljust(22) + f"{d}")
                    rPrint("Empty Imports:".ljust(22) + f"{e}\n\n")
                    print("------------------------")
                    ysinp("Press Enter to Continue")
                    return
        
    @staticmethod
    def promptMainMenu():
        """ Prompts main menu; grabs user input with error checking
        Raises:
            InvalidSelection: When user inputs anything other than an int in [1,11]
        Returns:
            int: user input in interval [1,11] (menu selection)
        """
        sel = ""
        while not sel:
            clear()
            wPrint("#"*10 + " Main Menu " + "#"*10)
            cPrint("  1)  Search")
            cPrint("  2)  Add Game")
            cPrint("  3)  Delete Game")
            cPrint("  4)  Instructions")
            cPrint("  5)  Print Library")
            cPrint("  6)  Print Database")
            cPrint("  7)  Delete Library")
            cPrint("  8)  Import Library")
            cPrint("  9)  Export Library")
            cPrint("  10) Save & Exit Program")
            cPrint("  11) Exit Without Saving")
            wPrint("#"*30)
            sel = ysinp("Please Make a Selection: ").strip()
            
        if sel.isdigit() and 1 <= int(sel) <= 11:
            return int(sel)
        else:
            raise InvalidSelection(sel)
    
    def saveAndExit(self):
        """ Saves & Exits saftely (writes any unsaved added games)
        Raises:
            SaveExit: to indicate a save & exit safe exit in GameLib.py
        """
        while T:
            clear()
            selYN = rsinp("\nAre you sure you want to exit [Y/N]?\n").strip().upper()
            if len(selYN) == 1 and selYN.isalpha() and selYN in ["Y","N"]:
                match selYN:
                    case "N": return
                    case "Y": 
                        if self.modified:
                            open(self.MEMDIR, 'w').close() 
                            with open(self.MEMDIR, 'w') as f:
                                for ll in self.dataBase.arr:
                                    if len(ll):
                                        for node in ll:
                                            if node.data is not None:
                                                f.write(f"{repr(node.data)}\n")
                        raise SaveExit
            else:
                clear()
                rPrint("\n[ERROR]: INVALID SELECTION\nPLEASE SELECT 'Y', OR 'N'")
                sleep(4)
                
    def exitNoSave(self):
        """ Exits program without saving changes
        Raises:
            ExitNoSave: Flag to exit program without saving chnages safe exit in GameLib.py
        """
        while T:
            clear()
            selYN = rsinp("Exiting without saving will delete all games added after startup\nAre you sure you want to exit without saving [Y/N]?\n").strip().upper()
            if len(selYN) == 1 and selYN.isalpha() and selYN in ["Y","N"]:
                match selYN:
                    case "N": return
                    case "Y": raise ExitNoSave
            else:
                clear()
                rPrint("\n[ERROR]: INVALID SELECTION\nPLEASE SELECT 'Y', OR 'N'")
                sleep(4)
                
    def __str__(self):
        """ Formats Library's HashTable (dataBase) to printable form
        Returns:
            str: a string representing the underlying HashTable Instnace
        """
        return str(self.dataBase)
        
    def loadMemory(self):
        """ Loads in data saved at the path held by self.MEMDIR upon startup only """
        with open(self.MEMDIR, 'r') as f:
            for line in f:
                gme = line.strip().split(',') 
                try: 
                    gme[0] = formName(gme[0])
                    self.dataBase[gme[0]] = Game.stog(gme)           
                except DuplicateEntry: continue
                except EmptyEntry: continue
                else: self.titles.append(gme[0])
        return
    
    def addGame(self):
        """ Adds game to Library's dataBase attribute (HashTable) using user-inputted data """
        while T:
            clear()
            title_ = formName(ysinp("\n\nEnter title, or type 'back' to go back: ").strip())
            if title_.lower() == "back": return
            else:
                msg = ""
                rating_ = ysinp("Enter rating: ").strip() 
                size_ = ysinp("Enter size (GB): ").strip()
                price_ = ysinp("Enter Price ($): ").strip()
                
                if len(rating_) > 3: rating_ = rating_[:3]
                if size_[-2:].upper() != "GB": size_ += "GB"
                if price_[0] != '$': price_ = "$" + price_
                
                try: self.dataBase[title_] = Game.stog([title_, rating_, size_, price_])
                except DuplicateEntry: msg = rtxt("\n[ERROR]: Duplicate Game Entry!\n")
                except EmptyEntry: msg = rtxt("\n[ERROR]: Blank Game Entry!\n")
                else: 
                    self.modified = T
                    self.titles.append(title_)
                    msg = gtxt("\nGame Successfully Added to Library!\n")
                finally:
                    clear()
                    print(msg)
                    sleep(4)
                    
    def delGame(self):
        """ Deletes a Game instance given a Title """
        while True:
            clear()
            title_ = formName(ysinp("Enter Title of Game, or 'back' to Return to Main Menu: ").strip())
            if title_.lower() == "back": return
            else:
                try: del self.dataBase[title_]
                except InvalidAccessErr: 
                    clear()
                    rPrint("\n\n[ERROR]: Game not found\n")
                else: 
                    clear()
                    self.modified = T
                    self.titles.remove(title_)
                    gPrint("\n\nGame successfully deleted!\n" )
                finally: ysinp("\nHit Enter to Continue")
    
    
    def printLib(self):
        """ Prints library in a user friendly way """
        clear()
        self.titles.sort(key=lambda x: x[0])
        print("\n")
        mPrint(f"\nGame Entries: {len(self)}\n")
        for entry in self.titles:
            cPrint(entry)
        print("\n")
        ysinp("Press Enter to Return to Main Menu")
            
    def printdataBase(self):
        """ Prints Library's database (HashTable) to terminal as a linked list """
        clear()
        mPrint(f"\nGame Entries: {len(self)}\n")
        print(self)
        ysinp("Press Enter to go back: ") 
        return

if __name__ == "__main__": pass
    # You can write code under here to test module. Else, run from GameLib.py