# numbers2text.py
# Decodes my enoding program
# Efficient version using a list accumulator
#

def main():
    #get the sequence of numbers to decode
    inString = input("Please enter the Unicode-encouded message: ")
    #Loop through each string and build Unicode message
    chars = []

    #for each number in the input:
    #convert the number to the corresponding Unicode character add the
    # character to the end of the message
    for numStr in inString.split():
        codeNum = int(numStr) # convert digits to a number
        chars.append(chr(codeNum)) # accumlate new characters
        message = "".join(chars)
   
    # Print the message
    print("\nThe decoded message is:", message)
    
main()
