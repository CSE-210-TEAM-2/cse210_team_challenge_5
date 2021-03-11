from game.guess import Guess
from game.word import Word
from game.console import Draw

class Director:

     # ******************************************** Will inizialite the game ********************************************
    def __init__(self):

        """"Class Constructor: will inizialite a list and get the word to be guess"""

        self.keep_playing = True
        self.guess = Guess()
        self.draw = Draw()
        self.word = Word()


    # ******************************************** Start Game ********************************************
    def start_game(self):
        """Starts the game loop to control the sequence of play.


        """
        while self.keep_playing:
            self.get_inputs()
            self.do_outputs()
            self.do_updates()
           

    # ******************************************** Get imputs ********************************************
    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play.
            it will prompt to the user for the word to guess and will save it in a varible  
        """




    pass
        
        
    # ******************************************** do outputs ********************************************
    def do_outputs(self):
        """Outputs the important game information for each round of play. It will draw the paracuse 
        and the list of letter including if he had guess any or not.\
        """


        self.draw.parachuse_position()



    pass

    # ******************************************** Do updates ********************************************

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, it will compare the information if the user guess right or not 
        """


        print('Ready to play')

    


       
    




