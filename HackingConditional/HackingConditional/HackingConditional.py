
def main():

    age = int(input("How old are you?"))
    if(age<=18 and age > 0):
        print("Starting early! Good for you!")
    elif(age >= 80 and age < 105):
        print("Never too late to learn!")
    elif(age >18 and age <80):
        print("Ah, a good age to learn")
    else:
        print ("That seems link an invalid age.")
        quit()

    print("Thank you for downloading this book")


main()
