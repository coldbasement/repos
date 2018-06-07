

def main():

    print("Please enter the amount of money you have. ")


    print()

    value = float(input("Enter Money:$ "))
    dollar = int(value)
    cent = round(float(value - dollar),2)
    cents = int(cent *100)
    print()
    '''
    print(dollar)
    print(cent)
    print(cents)
    '''
    print("You have {} dollars and {} cents".format(dollar,cents))






main()

  