
# This function will take the word from the class word and will compare with the user guess
# if it Guess it will return it as it failed 
#  if it Guess it will call the methon  word from word and will update the word and add the word in the place it has to be 

from game.word import Word

class Guess:    


    # ********************************** INIZIALITED ***********************************
    def __init__(self):
        """
        This method will inizialied the two list the one for the gues and the one with the word
        """
        self.word = Word()
        self.random_word = []
        self.user_word = 

    # ********************************** GUESS WORD ***********************************
    def guess_word(self):
        """
        This will prompt to the user to the letter that he want to guess
        """

        user_word = input ("Guess a letter from [a-z] : ")

    pass

    # ********************************** ASSIGN RANDOM WORD ***********************************

    def assign_random_word(self):
        """
        This Method will assign the random world from the class word to the attribute random_world
        """

        self.random_word = self.word.get_word()

    # ********************************** USER PROGRESS ***********************************

    def user_progress(self):
        """
        This Method will return the progress that the user have made so far
        """

    pass

    




