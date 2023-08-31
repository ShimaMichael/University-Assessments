##########
# TASK 2 #
##########

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = ""

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"
#
# Please leave the next line unchanged
task = "task2"
# ----------------------------------------------------------------------------------------------------------------------------
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of each
# method below that currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# DO NOT CHANGE the names or parameters of any of these methods
# DO NOT CHANGE the names of the four fields
# Make sure you read the method descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a class definition and a program that can
# be used to test its behaviour
#
# To run the program type  play_game()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

class peg_game () :
    # A class of objects that capture the state of a game that involves
    # inserting pegs into holes in a board until all holes are full
    # The winner is the person who inserts the last peg(s)
    # Each peg_game, P, has four fields:
    #  P.holes    the total number of holes
    #             P.holes is a positive int
    #  P.pegs     the current number of pegs in holes
    #             P.pegs is a non-negative int
    #  P.maxplay  the absolute maximum number of pegs that a
    #             player is allowed to add in one move
    #             P.maxplay is a positive int
    #  P.next     the identity of the next player to play
    #             P.next is either 1 or 2

    def __init__ (self,holes,maxplay) :
        # Creates a new peg_game object, using the parameters
        # holes and maxplay, and initialises the identity of the
        # player whose turn it is to play next to player 1
        # This method already works correctly
        self.holes    = holes  # remains constant throughout the game
        self.pegs     = 0
        self.maxplay  = maxplay
        self.player   = 1


# Method 1: 1 mark
    def all_holes_full (self) :
        # Returns True if all holes are full
        # returns False otherwise
        full = self.pegs == self.holes
        return full    # code stub


# Method 2: 1 mark   
    def next_player_ID (self) :
        # Returns the identity of the player whose turn
        # it is to play next (either 1 or 2)
        if self.player == 2:
            return 2
        if self.player == 1:
            return 1
        return None   # code stub


# Method 3: 1 mark
    def previous_player_ID (self) :
        # Returns the identity of the player who played
        # the last turn (either 1 or 2)
        if self.player == 2:
            return 1
        return 2   # code stub


# Method 4: 3 marks
    def max_pegs_this_turn (self) :
        # Returns the limit on the number of pegs that
        # can be inserted on the next turn. This will depend
        # on maxplay and on how many holes are empty
        noholes = self.holes - self.pegs
        left = min (self.holes, noholes)
        return left   # code stub


# Method 5: 1 mark
    def empty_holes (self) :
        # Returns the number of empty holes on the board
        # When this number is reached the game is over
        noholes = self.holes - self.pegs
        return noholes   # code stub


# Method 6: 3 marks
    def add_pegs (self,pegs_to_add) :
        # Adds the number of pegs specified by the parameter
        # pegs_to_add and switches to the next player
        self.pegs += pegs_to_add
        self.player = 3 - self.player
        # code stub (currently does nothing)


    def __str__ (self) :
        # Returns a string-based representation of the playing board
        # in a peg_game object so that it can be displayed using Python's
        # built-in print function
        # This method already works correctly
        game_as_string = "Total holes in board = " + str(self.holes) + "\n"
        game_as_string += "Currently " + str(self.pegs) + " holes are full:\n"
        game_as_string += ("!" * self.pegs) + ("." * (self.holes-self.pegs))
        return game_as_string


# ----------------------------------------------------------------------------------------------------------------------------
# DO NOT CHANGE any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------
# GAME PLAY


def play_game() :
    # Sets up and runs a peg game
    # Once you have got the peg_game class working you should
    # test it by setting up games with different numbers of holes
    # in the board and a different number of pegs that can be
    # added on each turn
    # For example    game = peg_game(10,3)
    print ("Welcome to the peg game")
    hole_count = int(input("What is the total number of holes in the playing board? "))
    maxpegs = int(input("What is the maximum number of pegs that can be inserted on each turn? "))
    game = peg_game(hole_count,maxpegs)
    print ("Players take it in turns to insert pegs into holes")
    print ("until all " + str(game.empty_holes()) + " holes are full\n")
    print ("You may insert between 1 and " + str(game.max_pegs_this_turn()) + " pegs")
    print ("The player who fills up the board is the winner\n")
    playing = True
    while playing :
        print (game,"\n")
        next_player = game.next_player_ID()
        print ("It's player",next_player,"to play next")
        while True :
            prompt = "There are currently " + str(game.empty_holes()) + " empty holes. "
            prompt += "How many pegs do you want to insert?\n"
            prompt += "(maximum possible on this turn is " + str(game.max_pegs_this_turn()) + "): "
            n = int(input(prompt))
            if n >= 1 and n <= game.max_pegs_this_turn() :
                print ()
                break
        game.add_pegs(n)
        if game.all_holes_full() :
            print ("Congratulations player",game.previous_player_ID(),"you win")
            playing = False
    print ("Thank you for playing")
