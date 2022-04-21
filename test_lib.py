import utils
import unittest as uni
import Library as lib
from colorama import init, Fore as fg, Back as bg, Style as st
    # Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    # Style: DIM, NORMAL, BRIGHT, RESET_ALL
init(autoreset=True)

FAIL = st.BRIGHT + fg.RED + "[ FAIL ]"

fgc = lambda x,y: x + y 

class TestLibrary(uni.TestCase):
    
    # Runs once first
    @classmethod
    def setUp(cls):
        pass
    
    # Runs once last
    @classmethod
    def tearDown(cls):
        pass
    
    # Runs before each test
    def setUp(self):
        
        # test_strGame objects
        self.testGame1 = lib.game("Game1", "5", "40GB", "$20")
        self.testGame2 = lib.game("", "", "", "")
        self.testGame3 = lib.game()
        
    # Runs after each test
    def tearDown():
        pass
    
    # Tests game::__str__() method 
    def test_strGame(self):
        self.assertEqual(str(self.testGame1), "< Game1, 5, 40GB, $20 >", FAIL)
        self.assertEqual(str(self.testGame2), "< , , ,  >", FAIL)
        self.assertEqual(str(self.testGame3), "< N/A, N/A, N/A, N/A >", FAIL)
        
        
if __name__ == "__main__":
    uni.main(verbosity=2)
    