
# This class will inizialite the list and will get a random word from the a list that we will include

import random

class Word:

     # ********************** Will initialize the list for the word ***********************
    def __init__(self):
        """
        This method will inizialied the list 
        """
        self.word = []
        self.list_words = []

    pass


    # ********************************** LIST OF WORDS ***********************************

    def list_of_words(self):

        """"
        This will have the list of a lot of word that the game randomnly will select and save in the
        word attribute it will not return any value just will contain the list
        """

        self.list_words = ["apple", "banana","cherry","mango", "orange","dog","goat", "pop","mouse","zebra","lion","beer","water", "love"  "hat","lamp", "book","umbrella", "cake", "bottle"]

    # ********************************** WILL ASSIGN A WORD  ***********************************

    def assign_word(self):

        """
        This Method will take our attribute word and will assign a random word from our list of words
        """

        # This will select ramdonly a word from the list of words and will assign it the attribute word
        self.word = random.sample(self.list_words,1)

    pass

    # ********************************** GET WORD ***********************************

    def get_word(self):
        """
        Get Word is the only methond that will return a value and is going to be the word that 
        randomly was chose and assign to the attribute word
        """
        
        return self.word







