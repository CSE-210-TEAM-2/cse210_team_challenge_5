
# This class will draw the parachuse and will make the update in the draw 
# Will see if the person is still alive or not and if not will draw it 
# Everytime that the user guess wrong will cut a line from the list 


#class Draw:
#
#    # ********************** Will initialize the list ***********************
#    def __init__(self):
#        """
#        This method will inizialied the list to draw the parachuse 
#        """
#        self.parachuse = []
#
#    pass
#
#    # ********************************** DRAW PARACHUSE ***********************************
#
#    def draw_parachuse(self):
#
#        """
#        This will draw the parachuse. It is a list and in each stop will be a line 
#        of the parachise to make it easier if the user get it worng
#        """
#
#        self.parachuse.append('___')
#        self.parachuse.append('/___\/')
#        self.parachuse.append('\   /')
#        self.parachuse.append('\ /')
#        self.parachuse.append('0')
#        self.parachuse.append('/|\/')
#        self.parachuse.append('/ \/')
#        self.parachuse.append('')
#        self.parachuse.append('^^^^^^^')
#
#
#
#    # ********************************** WRONG ***********************************
#
#    def cut_line(self):
#        """
#        This will update the  parachuse list if the user guessed wrong and will update it
#        cutting one line of the parachuse
#        """
#
#
# This class will draw the parachuse and will make the update in the draw 
# Will see if the person is still alive or not and if not will draw it 

# Everytime that the user guess wrong will cut a line from the list 
class Draw:


    def __init__(self):
    # ********************** Will initialize the list ***********************
        This method will inizialied the list to draw the parachute 
        """
        self.parachute = []
        """
    pass

    # ********************************** DRAW PARACHUSE ***********************************

    def draw_parachute(self):

        """

        of the parachise to make it easier if the user get it worng
        This will draw the parachute. It is a list and in each stop will be a line 

        """
        
        self.parachute.append()
        self.print(" ___")
        self.print("/___\\")
        self.print("\   /")
        self.print(" \ /")
    # ********************************** WRONG ***********************************
#    def remove_line(self):
#
#        
#        """
#        This will update the  parachuse list if the user guessed wrong and will update it
#        """
#
#        s_zero = self.print(" ___\n/___\\\n\   / \n \ /")
#
#        s_one = self.print(" ___\n/___\\\n    / \n   /")
#
#        s_two = self.print(" ___\n ___\\\n    /\n   /")
#        
#        s_three = self.print(" \n ___\\\n    /\n   /")
#        
#        s_four = self.print("\n___\n   /\n  /")
#        
#        s_five = self.print("\n\n    /\n   /")
#
#        strike_list = [s_one,s_two,s_three,s_four,s_five,s_six]
#strike_list[i] += 1
#        i = 0
#        for i in range(5):
#            strike_list[i] += 1


#strike_list[3]
        
#print(" ___\n/___\\\n\   / \n \ /")

#print(" ___\n/___\\\n    / \n   /")

print(" ___\n ___\\\n    /\n   /")



def show_board(wrong_guesses,correct_guesses, secret_word):
    print(strike_list[len(wrong_guesses)])
    print()

    print('Wrong guesses:', end=' ')
    for letter in wrong_guesses:
        print(letter, end='')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_guesses:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end='')
    print()


#def get_guess(already_guessed):
#    while True:
#        print('Go ahead. Guess a letter.')
#        guess = input()
#        guess = guess.lower()
#        if len(guess) != 1:
#            print('Please enter a single letter.')
#        elif guess in already_guessed:
#            print('You already gueesed that letter. Now for a different one.')
#        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
#            print('No weird keys please.')
#        else:
#            return guess

#if wrong:
#    remove_line(strike)
#
#
#    guesse
#
#
#    guesses = 
#
#    while guesses > 0:
#        dead = 0
#
#        for guess in guesses:
#            if guess in letters:
#                print(letter)
#            else:
#                strike_list[letter] += 1
#                print(strike_list[letter])
#                attempts -= 1