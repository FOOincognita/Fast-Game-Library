from utils import DuplicateEntry
from xml.dom import InvalidAccessErr
from kiwisolver import DuplicateEditVariable
import utils
import unittest as uni
from Library import Game, Node, LinkedList, HashTable, Library
from colorama import init, Fore as fg, Back as bg, Style as st
    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Style: DIM, NORMAL, BRIGHT, RESET_ALL
init(autoreset=True)

FAIL = st.BRIGHT + fg.RED + "[ FAIL ]"

fgc = lambda x,y: x + y 

class TestLibrary(uni.TestCase):
    
    # Runs before each test
    def setUp(self):
        
        # test_Game objects
        self.testStrGame1 = Game("Game1", "5", "40GB", "$20")
        self.testStrGame2 = Game("", "", "", "")
        self.testStrGame3 = Game()
        
        self.testStogGame = Game.stog("GameStog,10,80GB,$50\n")
        
        # test_LL objects
        self.testLLstr1 = LinkedList()
        self.testLLstr2 = LinkedList()
        
        # test_HT object
        self.testHT = HashTable()


    
    # Tests Game::__str__() dunder method 
    def test_strGame(self):
        self.assertEqual(str(self.testStrGame1), "game(Game1,5,40GB,$20)", FAIL)
        self.assertEqual(str(self.testStrGame2), "game(,,,)", FAIL)
        self.assertEqual(str(self.testStrGame3), "game(N/A,N/A,N/A,N/A)", FAIL)
        
    # Tests Game::stog() class method 
    def test_stogGame(self):
        self.assertEqual(str(self.testStogGame), "game(GameStog,10,80GB,$50)", FAIL)
        
        
        
        
    # Tests LinkedList::__str__() dunder method 
    def test_LLStr(self):
        self.assertEqual(str(self.testLLstr1), "Empty List", FAIL)
        
    # Tests LinkedList::emplace_back() method 
    def test_LLEmplace_Back(self):
        threw1 = False
        self.testLLstr1.emplace_back(self.testStrGame1)
        self.assertEqual(str(self.testLLstr1), "game(Game1,5,40GB,$20)->None", FAIL)
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.assertEqual(str(self.testLLstr1), "game(Game1,5,40GB,$20)->game(,,,)->None", FAIL)
        self.testLLstr1.emplace_back(self.testStrGame3)
        self.assertEqual(str(self.testLLstr1), "game(Game1,5,40GB,$20)->game(,,,)->game(N/A,N/A,N/A,N/A)->None", FAIL)
        
        try:
            self.testLLstr1.emplace_back(self.testStrGame1)
        except(DuplicateEntry):
            threw1 = True
        self.assertTrue(threw1, FAIL)
        
        
    # Tests LinkedList::__len__() dunder method 
    def test_LLLen(self):
        self.assertEqual(len(self.testLLstr1), 0, FAIL)
        self.testLLstr1.emplace_back(self.testStrGame1)
        self.assertEqual(len(self.testLLstr1), 1, FAIL)
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.testLLstr1.emplace_back(self.testStrGame3)
        self.assertEqual(len(self.testLLstr1), 3, FAIL)
        
    # Tests LinkedList::__delitem__() dunder method 
    def test_LLDelItem(self):
        threw1, threw2 = False, False
        
        self.testLLstr1.emplace_back(self.testStrGame1)
        del self.testLLstr1[self.testStrGame1.title]
        self.assertEqual(len(self.testLLstr1), 0, FAIL)
        self.assertEqual(str(self.testLLstr1), "Empty List", FAIL)
        
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.testLLstr1.emplace_back(self.testStrGame3)
        del self.testLLstr1[self.testStrGame2.title]
        self.assertEqual(len(self.testLLstr1), 1, FAIL)
        self.assertEqual(str(self.testLLstr1), "game(N/A,N/A,N/A,N/A)->None", FAIL)
        
        del self.testLLstr1[self.testStrGame3.title]
        self.assertEqual(len(self.testLLstr1), 0, FAIL)
        self.assertEqual(str(self.testLLstr1), "Empty List", FAIL)
        
        try:
            del self.testLLstr1[self.testStrGame2.title]
        except(InvalidAccessErr):
            threw1 = True
        self.assertTrue(threw1, FAIL)
        
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.testLLstr1.emplace_back(self.testStrGame3)
        try:
            del self.testLLstr1[self.testStrGame1.title]
        except(InvalidAccessErr):
            threw2 = True
        self.assertTrue(threw2, FAIL)
            
        
        
        
        
        
if __name__ == "__main__":
    uni.main(verbosity=2)
    