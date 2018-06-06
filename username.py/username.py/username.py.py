#username.py
# Simple string processing program to generate usernames

def main():
    print("This program generates computer usernames.\n")
   
    # get the user's first and Last name

    first = input("Please eneter your first name (all lowercase): ")
    last = input("Please eneter your last name (all lowercase): ")

    #concatenate first initial with 7 chars of the last name
    uname = first[0] + last[:7]

    #output the username
    print("Your username is:", uname)

main()
