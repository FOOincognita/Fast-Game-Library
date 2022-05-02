import utils
import unittest as uni
from io import StringIO
from unittest.mock import patch
from utils import DuplicateEntry, EmptyEntry
from xml.dom import InvalidAccessErr
from Library import Game, Node, LinkedList, HashTable, Library
from colorama import init, Fore as fg, Back as bg, Style as st
    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Style: DIM, NORMAL, BRIGHT, RESET_ALL
init(autoreset=True)

FAIL = st.BRIGHT + fg.RED + "[ FAIL ]"

NULLSTR = st.BRIGHT + bg.BLACK + fg.BLUE + "[None]" + st.RESET_ALL
ARROW = st.BRIGHT + fg.WHITE + chr(10236) + " "

sinp = lambda x: str(input(x)) 
gmestr = lambda x:  st.BRIGHT + bg.BLACK + fg.GREEN + str(x) + st.RESET_ALL + ARROW

fgc = lambda x,y: x + y 

class TestDataStructs(uni.TestCase):
    
    # Runs before each test
    def setUp(self):
        
        # test_Game objects
        self.testStrGame1 = Game("Game1", "5", "40GB", "$20")
        self.testStrGame2 = Game("", "", "", "")
        self.testStrGame3 = Game()
        
        self.testStogGame = Game.stog(["GameStog","10","80GB","$50"])
        
        # test_LL objects
        self.testLLstr1 = LinkedList()
        self.testLLstr2 = LinkedList()
        
        # test_HT objects
        self.testHT = HashTable(10)
        self.htTst = HashTable(1)
        
        # test_Lib object
        self.tLib = Library(3)
        
        
    
    # Tests Game::__str__() dunder method 
    def test_strGame(self):
        self.assertEqual(str(self.testStrGame1), "[Game1,5,40GB,$20]", FAIL)
        self.assertEqual(str(self.testStrGame2), "[,,,]", FAIL)
        self.assertEqual(str(self.testStrGame3), "[N/A,N/A,N/A,N/A]", FAIL)
        
    # Tests Game::stog() class method 
    def test_stogGame(self):
        self.assertEqual(str(self.testStogGame), "[GameStog,10,80GB,$50]", FAIL)
        
        
        
        
    # Tests LinkedList::__str__() dunder method 
    def test_LLStr(self):
        self.assertEqual(str(self.testLLstr1), NULLSTR, FAIL)
        
    # Tests LinkedList::emplace_back() method 
    def test_LLEmplace_Back(self):
        threw1 = False
        self.testLLstr1.emplace_back(self.testStrGame1)
        self.assertEqual(str(self.testLLstr1), gmestr("[Game1,5,40GB,$20]") + NULLSTR, FAIL)
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.assertEqual(str(self.testLLstr1), gmestr("[Game1,5,40GB,$20]") + gmestr("[,,,]") + NULLSTR, FAIL)
        self.testLLstr1.emplace_back(self.testStrGame3)
        self.assertEqual(str(self.testLLstr1), gmestr("[Game1,5,40GB,$20]") + gmestr("[,,,]") + gmestr("[N/A,N/A,N/A,N/A]") + NULLSTR, FAIL)
        
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
        self.assertEqual(len(self.testLLstr1), 0, FAIL) ######### 0
        self.assertEqual(str(self.testLLstr1), NULLSTR, FAIL)
        
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.testLLstr1.emplace_back(self.testStrGame3)
        del self.testLLstr1[self.testStrGame2.title]
        self.assertEqual(len(self.testLLstr1), 1, FAIL)
        self.assertEqual(str(self.testLLstr1), gmestr("[N/A,N/A,N/A,N/A]") + NULLSTR, FAIL)
        
        del self.testLLstr1[self.testStrGame3.title]
        self.assertEqual(len(self.testLLstr1), 0, FAIL)
        self.assertEqual(str(self.testLLstr1), NULLSTR, FAIL)
        
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
        
    # Tests LinkedList::__iter__() dunder method 
    def test_LLIter(self):
        testStr = ""
        self.testLLstr1.emplace_back(self.testStrGame1)
        self.testLLstr1.emplace_back(self.testStrGame2)
        self.testLLstr1.emplace_back(self.testStrGame3)
        for n in self.testLLstr1:
            testStr += str(n)
        self.assertEqual(testStr, "[Game1,5,40GB,$20][,,,][N/A,N/A,N/A,N/A]", FAIL)
        
        
        
    # Tests HashTable::hash() method 
    def test_HThash(self):
        hsh = self.testHT.hash("abcDtF")
        hshtest = self.testHT.hash("abcDtF")
        hshnetest = self.testHT.hash("abaesfaetF")
        self.assertTrue(hshtest == hsh, FAIL)
        self.assertTrue(hshnetest != hsh, FAIL)
        hshtest2 = self.testHT.hash("abcDtF")
        self.assertTrue(hshtest2 == hsh, FAIL)
    
    # Tests HashTable::__str__() dunder method with empty table
    def test_HTStr(self):
        testStr = ""
        
        for i in range(10):
            testStr += NULLSTR + "\n"
        self.assertEqual(str(self.testHT), testStr, FAIL)
    
    # Tests HashTable::__set/getitem__() dunder method 
    def test_HTSetItem(self):
        found1, except1, except2 = False, False, False
        self.testHT[self.testStrGame1.title] = self.testStrGame1
        for LL in self.testHT.arr:
            for node in LL:
                if "[Game1,5,40GB,$20]" == str(node):
                    found1 = True
        self.assertTrue(found1, FAIL)
        
        try: 
            self.testHT[self.testStrGame1.title] = self.testStrGame1
        except(DuplicateEntry): 
            except2 = True
        try: 
            self.testHT[self.testStrGame3.title] = self.testStrGame3
        except(EmptyEntry): 
            except1 = True
        
        self.assertTrue(except1, FAIL)
        self.assertTrue(except2, FAIL)
        
    # Tests HashTable::__del__() dunder method 
    def test_HTDelItem(self):
        raised = False
        try: del self.htTst["invalidtitle"]
        except(InvalidAccessErr): raised = True
        self.assertTrue(raised, FAIL)
        
        self.htTst[self.testStrGame1.title] = self.testStrGame1
        del self.htTst[self.testStrGame1.title]
        self.assertEqual(str(self.htTst), NULLSTR + "\n", FAIL)
        
    # Tests HashTable::__len__() dunder method 
    def test_HTDelItem(self):
        self.assertEqual(len(self.htTst), 0, FAIL)
        self.htTst[self.testStrGame1.title] = self.testStrGame1
        self.assertEqual(len(self.htTst), 1, FAIL)
        self.htTst[self.testStogGame.title] = self.testStogGame
        self.assertEqual(len(self.htTst), 2, FAIL)
        del self.htTst[self.testStrGame1.title]
        del self.htTst[self.testStogGame.title]
        self.assertEqual(len(self.htTst), 0, FAIL) 

if __name__ == "__main__":
    uni.main(verbosity=2)
    