# numbers2text.py
# Decodes my enoding program
#
#

def main():
    #get the sequence of numbers to decode
    inString = input("Please enter the Unicode-encouded message: ")
    #message = ""
    message = ""

    #for each number in the input:
    #convert the number to the corresponding Unicode character add the
    # character to the end of the message
    for numStr in inString.split():
        codeNum = int(numStr) # convert digits to a number
        message = message + chr(codeNum) # concatentate character to message

   
    # Print the message
    print("\nThe decoded message is:", message)
    
main()