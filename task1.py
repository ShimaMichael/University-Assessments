##########
# TASK 1 #
##########

# Insert your Student Registration Number (SRN) between the
# quotation marks in the assignment statement below:

SRN = ""

# For example, if your SRN is 01234567 the assignment statement
# should read  SRN = "01234567"
#
# Please leave the next line unchanged
task = "task1"
# ----------------------------------------------------------------------------------------------------------------------------
# WHAT YOU HAVE TO DO
#
# Modify this script to provide correct implementations of the
# functions below, each of which currently contains a code stub
#
# When you have finished, submit the modified version of this script
#
# Do not change the names or parameters of any of these functions
# Make sure you read the function descriptions carefully
#
# You are not allowed to use any external modules
# in the solution of these problems (no imports)
# ----------------------------------------------------------------------------------------------------------------------------
#
# The script contains a test plan and code to test the functions
# and display the results of the tests
#
# To run the tests type  runtests()  at the command line in the
# Python shell
#
# ----------------------------------------------------------------------------------------------------------------------------

##########################
# Function 1 (2 marks)
##########################

def VennDiagram (Q,R,S) :
    first_set = S & Q - R 
# Parameters: three sets Q, R, S
# Returns:
#  A single set that combines sets Q, R and S in the manner
#  shown as a shaded area on the Venn diagram in the document
#  VennDiagram.pdf that you will find in the Zip archive
#  you downloaded from Canvas
#  The original sets Q, R and S are left unchanged

    return first_set    # code stub




##########################
# Function 2 (3 marks)
##########################

def dict_from (key_list,data_vals) :
    fuad = {}
    for items in range(len(key_list)):
        if items < len(data_vals):
            fuad[key_list[items]] = data_vals[items]
        else:
            fuad[key_list[items]] =  None
# Parameters: two lists key_list, data_vals that may be of
#  different lengths
#  key_list will contain a sequence of hashable values
#  (with no repeats) as it is going to supply the keys
#  for a dictionary
# Returns:
#  A dictionary in which the elements of key_list appear
#  as keys to the corresponding elements in data_vals
#
#  If the two lists are of the same length each key will
#  have a matching data item
#
#  If key_list is shorter than data_vals some data items
#  from data_vals will be lost. For example, if key_list
#  is [3,5] and data_vals is [1,4,6,7], the function
#  should return the dictionary {3:1, 5:4}
#
#  If key_list is longer than data_vals the unmatched keys
#  should point at the value None. For example, if key_list
#  is [3,5,8,9] and data_vals is [1,4], the function
#  should return the dictionary {3:1, 5:4, 8:None, 9:None}
#

    return fuad    # code stub




##########################
# Function 3 (3 marks)
##########################

def isPrime (n) :
# This function works correctly: DO NOT CHANGE IT
# It is for use in the definition
# of the function primes (below)
# Parameter: an integer, n
# Returns:
#  A Boolean value
#   True if n is a prime number
#   False otherwise
    if n <= 1 :
        return False
    else :
        for i in range(2,n) :
            if n % i == 0 :
                return False
        return True

def primes (intlist) :
    prime = []
    nonprime = []
    for item in intlist:
        if isPrime (item) == True:
            prime.append (item)
        else:
            nonprime.append(item)
    return {'primes': prime, 'nonprimes': nonprime} 
# Needs a function body to replace the code stub
# Parameter: a list of integers, intlist
# Returns:
#  A dictionary containing two entries
#  * The key 'primes' mapped to a set containing
#    the prime numbers in intlist, and no others
#    If there are no prime numbers in intlist the key
#    'primes' should map to an empty set
#  * The key 'nonprimes' mapped to a set containing
#    the non-prime numbers in intlist, and no others
#    If there are no non-prime numbers in intlist the key
#    'nonprimes' should map to an empty set
# YOU ARE REQUIRED TO USE the function isPrime (defined above)
# to determine whether or not the numbers in intlist are primes

      # code stub



##########################
# Function 4 (3 marks)
##########################

def encode (bit_str) :
    newcode = '+++'
    for item in bit_str:
        if item == '0':
            newcode += '+-+'
        else:
            newcode += '-+-'
    newcode += '---'
# A function that mimics the encoding of bit-strings for transmission
# via a data link
# Parameter: a character string bit_str
#   bit_str contains a sequence of '0' and '1' characters each of
#   which represents a single bit in a bit-string.
#   For example
#   The character string '0010111' represents the bit-string 0010111
# Returns: a character string signal_str, representing high and low voltages
#   using '+' (plus) and '-' (minus) signs, derived from bit_str as follows
#   signal_str starts with the sequence '+++' (three plus signs) and ends
#   with the sequence '---' (three minus signs)
#   In between the start and end indicators the sequence of bits from
#   bit_string are encoded in signal_str as follows
#   every '0' from bit_str is encoded as '+-+'
#   every '1' from bit_str is encoded as '-+-'
# For example
# encode ('')    returns '+++---'
# encode ('0')   returns '++++-+---'
# encode ('1')   returns '+++-+----'
# encode ('00')  returns '++++-++-+---'
# encode ('001') returns '++++-++-+-+----'
# encode ('100') returns '+++-+-+-++-+---'
# encode ('110') returns '+++-+--+-+-+---'
# and so on, so that
# encode ('0010111') returns '++++-++-+-+-+-+-+--+--+----'

    return newcode    # code stub




##########################
# Function 5 (3 marks)
##########################

def decode (signal_str) :
    count = 3
    newcode = ''
    while count < len(signal_str)-3:
        if signal_str[count:count + 3] == '+-+':
            newcode += '0'
        else:
            newcode += '1'

        count += 3
    
# A function that extracts the original bit-string from the
# encoded version produced by encode (see function 4)
# so that after executing the following sequence of instructions
#   inbitstring = '0010'
#   signalstring = encode(inbitstring)
#   outbitstring = decode(signalstring)
# signalstring is  '++++-++-+-+-+-+---'  and outbitstring is  '0010'

    return newcode    # code stub




##########################
# Function 6 (3 marks)    USE RECURSION
##########################

def all_strings (my_list) :
    if not isinstance (my_list[0], str):
        return False
    elif len(my_list) == 1:
        return True
    else:
        return all_strings(my_list[1:len(my_list)])
# A function that determines whether or not all elements in a list
# are character strings (data type str)
# You are required to USE RECURSION when implementing this function

# Parameter: a non-empty list my_list
# Returns: a truth value
#   True when the elements of my_list are all character strings
#   False when one or more elements is/are not character strings

# Note that the function isinstance can be used to check whether
# a data item is a string.
#   isinstance(s,str)
# returns True if s is a character string and False if it is not
    
# code stub


##########################
# Function 7 (3 marks)    USE RECURSION
##########################

def in_order (numlist) :
    if len(numlist) <= 1:
        return True
    if numlist [0] <= numlist[1]:
        return in_order (numlist[1:])
    else:
        return False
# A function that determines whether or not the elements in a list
# of numbers are arranged in ascending order.
# You are required to USE RECURSION when implementing this function

# Parameter: a list of numbers, numlist
# Returns: a truth value
#   True when the numbers in numlist are in ascending order
#   False when they are not

# code stub



# ----------------------------------------------------------------------------------------------------------------------------
# Do not change any part of this script between here and
# the end of the file
# ----------------------------------------------------------------------------------------------------------------------------

###########################################################################

#                           TEST PLAN

############################################################################

test_plan = dict ()


fn = "VennDiagram"
test_plan [fn] = dict()
test_plan [fn] [1] = [[set(),set(),set()],set()]
test_plan [fn] [2] = [[{1},{2},{1,3,2}],{1}]
test_plan [fn] [3] = [[{1,2,3,4,5},{6,5,4,7,9},{1,5,6,2}],{1, 2}]
test_plan [fn] [4] = [[{8,9,7},{6,5,3},{5,4,7}],{7}]


fn = "dict_from"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[],[]],dict()]
test_plan [fn] [2] = [[[10],[-8]],{10:-8}]
test_plan [fn] [3] = [[[2,4,6],[18,20,22,8]],{2:18,4:20,6:22}]
test_plan [fn] [4] = [[[-5,9,7],[11,21]],{-5:11,9:21,7:None}]
test_plan [fn] [5] = [[[1,2,13,9],['a','b','m']],{1:'a',2:'b',13:'m',9:None}]


fn = "primes"
test_plan [fn] = dict()
test_plan [fn] [1] = [[list()],{'primes': set(),'nonprimes': set()}]
test_plan [fn] [2] = [[[1,3,5,6,8]],{'primes': {3, 5}, 'nonprimes': {8, 1, 6}}]
test_plan [fn] [3] = [[[4,6,8]],{'primes': set(), 'nonprimes': {8, 4, 6}}]
test_plan [fn] [4] = [[[5,7,11,13]],{'primes': {13, 11, 5, 7}, 'nonprimes': set()}]


fn = "encode"
test_plan [fn] = dict()
test_plan [fn] [1] = [[''],'+++---']
test_plan [fn] [2] = [['1'],'+++-+----']
test_plan [fn] [3] = [['01'],'++++-+-+----']
test_plan [fn] [4] = [['0011'],'++++-++-+-+--+----']
test_plan [fn] [5] = [['11100110'],'+++-+--+--+-+-++-+-+--+-+-+---']


fn = "decode"
test_plan [fn] = dict()
test_plan [fn] [1] = [['+++---'],'']
test_plan [fn] [2] = [['+++-+----'],'1']
test_plan [fn] [3] = [['++++-+-+----'],'01']
test_plan [fn] [4] = [['++++-++-+-+--+----'],'0011']
test_plan [fn] [5] = [['+++-+--+--+-+-++-+-+--+-+-+---'],'11100110']


fn = "all_strings"
test_plan [fn] = dict()
test_plan [fn] [1] = [[['a']],True]
test_plan [fn] [2] = [[[1,'a']],False]
test_plan [fn] [3] = [[['0','fred']],True]
test_plan [fn] [4] = [[['bill',36.5]],False]
test_plan [fn] [5] = [[['x','y','z']],True]


fn = "in_order"
test_plan [fn] = dict()
test_plan [fn] [1] = [[[2]],True]
test_plan [fn] [2] = [[[1,3,5,7]],True]
test_plan [fn] [3] = [[[0,1]],True]
test_plan [fn] [4] = [[[1,2,4,-1]],False]
test_plan [fn] [5] = [[[-9,-8]],True]


###########################################################################

#                           TEST DRIVER

############################################################################

def tester (ms) :
    results = dict()
    totalmark = 0
    for funcname in ms :
        results[funcname] = dict()
        totalfunc = 0
        tests = ms[funcname].copy()
        for case in tests :
            test      = tests [case]
            args      = test[0]
            arg0      = args[0]
            if isinstance (arg0,str) :
                arg0 = "'" + arg0 + "'"
            else :
                arg0 = str(args[0])
            strargs = "(" + arg0
            for arg in args[1:] :
                if isinstance (arg,str) :
                    arg = "'" + arg + "'"
                else :
                    arg = str(arg)
                strargs = strargs + "," + arg
            strargs   = strargs + ")"
            target    = test[1]
            if isinstance (target,str) :
                strtarget = "'" + target + "'"
            else :
                strtarget = str(target)
            try :
                call = funcname + strargs
                actual = eval(call)
                if isinstance (actual,str) :
                    stractual = "'" + actual + "'"
                else :
                    stractual = str(actual)

            except NameError :
                result = "Name error"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except RecursionError :
                result = "Recursion error (too many recursive calls)"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue
            except :
                result = funcname + " crashed"
                results[funcname][case] = [strargs,strtarget,"no result",result]
                continue

            if type(actual) != type(target) :
                result = "wrong type returned"
                
            else :
                if target == actual :
                    result = "pass"
                else :
                    result = "FAIL"

            results[funcname][case] = [strargs,strtarget,stractual,result]

    return results



def DisplayTestResults (results) :    
    display = "Test results\n"
    display += "Each function listed in the order tested\n\n"
    
    for fn in results :
        display += "\nTesting " + fn + "\n=========================="
        testres = results[fn]
        for test in testres :
            t = testres[test]
            #display += "\nTest " + str(test)
            display += "\nParameters:    " + t[0]
            display += "\nShould return: " + t[1]
            display += "\nActual return: " + t[2]
            display += "\nTest result:   " + t[3]
            display += "\n"
        display += "\n"
    return display




def run_tests () :
    global test_plan
    
    results = tester(test_plan)
    message = DisplayTestResults (results)
    print (message)

