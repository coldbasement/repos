#text2numbers.py
#  A Program to convert a textual message into a sequence of numbers
 # utilizing the underlying Unicode encoding.

def main():
 #Introduction 

 #get the message to encode
 message = input("Please enter the message to encode: ")

 print("\nHere are the Unicode codes: ")

 # for each character in the message:
 # print the letter number of the character
 for ch in message:
     print(ord(ch), end =" ")

 print() # blank line before prompt


main()
