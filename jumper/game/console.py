
# This class will draw the parachuse and will make the update in the draw 
# Will see if the person is still alive or not and if not will draw it 
# Everytime that the user guess wrong will cut a line from the list 


class Draw:

   # ********************** Will initialize the list ***********************
   def __init__(self):
       """
       This method will inizialied the list to draw the parachuse 
       """
       self.parachuse = []
       self.position = 0

   pass

   # ********************************** DRAW PARACHUSE ***********************************

   def draw_parachuse(self):

       """
       This will draw the parachuse. It is a list and in each stop will be a line 
       of the parachise to make it easier if the user get it worng
       """

       self.parachuse.append('___')
       self.parachuse.append('/___\/')
       self.parachuse.append('\   /')
       self.parachuse.append('\ /')
       self.parachuse.append('0')
       self.parachuse.append('/|\/')
       self.parachuse.append('/ \/')
       self.parachuse.append('')
       self.parachuse.append('^^^^^^^')



   # ********************************** WRONG ***********************************

    def parachuse_position(self):
       """
       This will update the  parachuse list if the user guessed wrong and will update it
       cutting one line of the parachuse
       """

        for self.position in self.parachuse:
            print(self.parachuse(self.position))


    pass

