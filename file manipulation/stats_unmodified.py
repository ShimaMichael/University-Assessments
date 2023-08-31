def stats () :
    # 'Top-level' function (main program)
    currentList = getNumList('statistics1.dat')   # Start with an empty list of numbers
                      # because the user hasn't entered a list yet
    # Main loop - repeatedly displays the menu,
    #             gets the user to choose an operation
    #             and carries out that operation
    while True :
        displayMenu ()
        choice = getMenuOption ()
        if choice == "0" :        # option 0 is 'quit the program'
            break
        else :
            currentList = executeMenuChoice (choice, currentList)
    print ("Thanks for using the program: goodbye")



def displayMenu () :
    print ("Menu options")
    print ("0 Quit the program")
    print ("1 Enter a new list of numbers")
    print ("2 Display the current list of numbers")
    print ("3 Get the mean of numbers in the current list")
    print ("4 Get the median of numbers in the current list")



def getMenuOption () :
    option = input ("Please choose a number between 1 and 4: ")
    print()
    return option



def executeMenuChoice (c,numbers) :
    # performs the operation specified by c on the list numbers
    if c == "1" :
        numbers = getNumList ()
    if c == "2" :
        displayNumList (numbers)
    if c == "3" :
        mean = calcMean (numbers)
        print ("The mean of the numbers in the list is",mean)
    if c == "4" :
        median = calcMedian (numbers)
        print ("The median of the numbers is",median)
    return numbers



def getNumList (filename) :
    # obtains a new list of numbers from the user
    numList = []
    with open(filename, 'r') as stat1:
        contents = stat1.read()
    if contents == '':
        return []
    else:
        stringlist = contents.split("\n")
        for string in stringlist:
            numList.append(string)
        return numList
  
 
 
def displayNumList (numList) :
    # shows the contents of numList on screen
    print ("The current list of numbers is")
    print (numList)
    print ()



def calcMean (numList) :
    # finds the arithmetic mean of the numbers numList
    total = sum (numList)
    count = len (numList)
    mean = total / count
    return mean



def calcMedian (numList) :
    # finds the median value in a list of numbers
    # the median is the 'middle-ranked' value in the list
    sList = sorted (numList)      # first get a sorted version of the list
    length = len (sList)
    mid = length // 2             # find the mid-point
    if length % 2 == 1 :
        # if the list has an odd number of elements
        # mid is the index of the middle value, so
        theMedian = sList [mid]
    else :
        # the list has an even number of elements, so
        # there are two middle values and the median
        # is the averaage of the two
        theMedian = (sList [mid-1] + sList [mid] ) / 2
    return theMedian

stats()
