
def main():

    print("Pythin Quiz")

    answered = 0
    correct = 0

    print()
    print("What version of python are we using?")
    print("A:1, B:2, C:3")
    user_answer = input("Enter A, B, or C:")

    answered +=1

    print()
    
    if(user_answer == "C"or user_answer =="c"):
        correct+=1
        print("Correct")
    else:
        print("Incorrect")
    print()

    print("How many 'else' statements can be in a decision tree?")
    print("A: 1, B: Infiniate, C: None")
    user_answer = input("Enter A, B, or C:")

    answered +=1
    print()

    if(user_answer =="A" or user_answer =="a"):

        correct +=1
        print("Correct")
    
    else:
        print("Incorrect")
    
    print()

    print("What does '=' do in Python?")

    print("A: Compare, B: Assigned, C: Both")
    user_answer = input("Enter A, B, or C:")
    
    answered +=1
    print()

    if(user_answer == "B" or user_answer == "b"):
        
        correct +=1
        print("Correct")

    else:

        print("Incorrect")
    
    print()

    print("You got {} out of {} correct.".format(correct, answered))

    if(correct ==3):

        print("Congradualtions! Good score.")
    
    elif(correct ==2):

        print("Good work, but study hard!")

    else:
        print("Go back and read over the section again, I'm sure you'll get it.")

main()

    