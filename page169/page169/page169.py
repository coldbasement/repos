# Numeric value of a full name


def main():
    print("This program computes the numerica value of any name given")
    

    name = input("Please Enter a name: ")

    
    letters = "".join(name.split())
    total_value = 0
    for letter in letters:
        total_value = total_value + ord(letter.lower()) - ord('a') +1

    print("The Numeric value is:", total_value)
    print(name[-3])
main()
