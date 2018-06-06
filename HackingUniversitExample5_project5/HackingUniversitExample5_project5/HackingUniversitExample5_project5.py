

def cm_to_inch(cm):

    inch = cm * 0.39

    return inch

def inch_to_cm(inch):

    cm=inch*2.54

    return cm

print("Inch/cm converter")

print("1: Convert cm to inch")

print("2: Convert inch to cm")

choice = int(input("Enter a menu option: "))

while (choice!= 1 and choice != 2):

    print("Invalid, try again.")

    choice = int(input("Enter a menu option: "))

if(choice == 1):

    user_input = int(input("Enter cm: "))


    print("{} cm is {} inches.".format(user_input, cm_to_inch(user_input)))

if(choice == 2):

    user_input = int(input("Enter inches: "))


    print("{} inches is {} is {} cm.".format(user_input, inch_to_cm(user_input)))

print("Thank you for using the program.")



