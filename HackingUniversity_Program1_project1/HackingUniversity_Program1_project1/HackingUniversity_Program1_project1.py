

def main():
    user_name = input("What is your name?")
    user_age = int(input("What is your age?"))
    user_pets = int(input("How many pets do you have?"))
    user_GPA = float(input("what is your GPA?"))

    print() #print a blank line

    print("{0} is {1} years old. They have a {3}GPA, probably because they have {2} pets.".format(user_name, user_age, user_pets, user_GPA))

main()  
    